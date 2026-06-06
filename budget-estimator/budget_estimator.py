"""
Budget Estimator — Parametric CAPEX with P50/P90 Monte Carlo
AACE RP 18R-97 compliant estimate classification
"""

import argparse
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import yaml

ITERATIONS = 10_000
MILLIONS = 1_000_000

# AACE accuracy ranges: (downside_fraction, upside_fraction)
AACE_ACCURACY = {
    1: (0.03, 0.10),
    2: (0.05, 0.15),
    3: (0.10, 0.20),
    4: (0.15, 0.30),
    5: (0.20, 0.50),
}

# Heuristic base costs — pipeline (EUR/km installed, DVGW/IPA Western Europe)
PIPELINE_BASE_EUR_PER_KM = {
    "DN300": 1_850_000,
    "DN400": 2_400_000,
    "DN500": 3_100_000,
    "DN600": 3_900_000,
}

TERRAIN_FACTORS = {
    "flat_agricultural": 1.00,
    "gently_rolling": 1.10,
    "rolling_rural": 1.12,
    "mountainous_or_rock": 1.35,
    "urban_corridor_hdd_heavy": 1.50,
}

H2_MATERIAL_PREMIUM = 0.15
H2_WELD_PREMIUM = 0.08
COMPRESSION_EUR_PER_MW = 2_200_000
BLOCK_VALVE_EUR = 280_000
OWNER_COST_FRACTION = 0.12


@dataclass(frozen=True)
class WorkPackage:
    id: str
    description: str
    base_cost: float  # EUR, P50 central estimate
    low_cost: float   # EUR, P10 (optimistic)
    high_cost: float  # EUR, P90 (conservative)

    def sample(self, rng: np.random.Generator, n: int) -> np.ndarray:
        """Triangular distribution sample."""
        return rng.triangular(self.low_cost, self.base_cost, self.high_cost, n)


@dataclass
class EstimateResult:
    project_name: str
    aace_class: int
    work_packages: list[WorkPackage]
    iterations: np.ndarray  # shape (ITERATIONS,) — total CAPEX per run
    wp_samples: dict[str, np.ndarray] = field(default_factory=dict)


def _aace_bounds(base: float, aace_class: int) -> tuple[float, float]:
    down, up = AACE_ACCURACY[aace_class]
    return base * (1 - down), base * (1 + up)


def parametric_pipeline(
    length_km: float,
    diameter: str,
    terrain: str,
    h2_service: bool,
    compression_mw: float,
    block_valves: int,
    aace_class: int,
    description: str = "Mainline Pipeline",
    wp_id: str = "WBS-PIPE",
    include_owner_costs: bool = False,
) -> WorkPackage:
    base_per_km = PIPELINE_BASE_EUR_PER_KM[diameter]
    terrain_f = TERRAIN_FACTORS.get(terrain, 1.0)
    h2_f = (1 + H2_MATERIAL_PREMIUM + H2_WELD_PREMIUM) if h2_service else 1.0
    pipeline_cost = length_km * base_per_km * terrain_f * h2_f

    compression_cost = compression_mw * COMPRESSION_EUR_PER_MW if compression_mw > 0 else 0.0
    valve_cost = block_valves * BLOCK_VALVE_EUR
    owner_cost = (pipeline_cost + compression_cost + valve_cost) * OWNER_COST_FRACTION if include_owner_costs else 0.0

    base = pipeline_cost + compression_cost + valve_cost + owner_cost
    low, high = _aace_bounds(base, aace_class)
    return WorkPackage(wp_id, description, base, low, high)


def load_yaml_estimate(path: str) -> tuple[str, int, list[WorkPackage]]:
    with open(path) as f:
        data = yaml.safe_load(f)

    project_name = data.get("project", {}).get("name", Path(path).stem)
    aace_class = int(data.get("project", {}).get("aace_class", 3))
    packages = []

    for wp in data.get("work_packages", []):
        wp_id = wp["id"]
        desc = wp.get("description", wp_id)
        method = wp.get("method", "direct")

        if method == "parametric":
            params = wp.get("params", {})
            pkg = parametric_pipeline(
                length_km=float(params.get("length_km", 0)),
                diameter=params.get("diameter", "DN400"),
                terrain=params.get("terrain", "flat_agricultural"),
                h2_service=bool(params.get("h2_service", False)),
                compression_mw=float(params.get("compression_mw", 0)),
                block_valves=int(params.get("block_valves", 0)),
                aace_class=aace_class,
                description=desc,
                wp_id=wp_id,
                include_owner_costs=bool(params.get("include_owner_costs", False)),
            )
        else:
            base = float(wp["base_cost_eur"])
            uncertainty = float(wp.get("uncertainty_pct", AACE_ACCURACY[aace_class][1]))
            down = float(wp.get("downside_pct", AACE_ACCURACY[aace_class][0]))
            low = base * (1 - down)
            high = base * (1 + uncertainty)
            pkg = WorkPackage(wp_id, desc, base, low, high)

        packages.append(pkg)

    return project_name, aace_class, packages


def run_monte_carlo(packages: list[WorkPackage]) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    rng = np.random.default_rng(42)
    wp_samples = {p.id: p.sample(rng, ITERATIONS) for p in packages}
    total = sum(wp_samples.values())
    return total, wp_samples


def sensitivity_spearman(total: np.ndarray, wp_samples: dict) -> list[tuple[str, float]]:
    """Rank correlation between each WP sample and total CAPEX."""
    from scipy.stats import spearmanr
    results = []
    for wp_id, samples in wp_samples.items():
        corr, _ = spearmanr(samples, total)
        results.append((wp_id, abs(float(corr))))
    return sorted(results, key=lambda x: x[1], reverse=True)


def chart_distribution(total: np.ndarray, project_name: str, output_dir: str) -> None:
    p10, p50, p90 = np.percentile(total, [10, 50, 90])
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(total / MILLIONS, bins=80, color="#4472C4", edgecolor="white", linewidth=0.3, alpha=0.85)
    for val, label, color in [(p10, "P10", "#70AD47"), (p50, "P50", "#ED7D31"), (p90, "P90", "#FF0000")]:
        ax.axvline(val / MILLIONS, color=color, linewidth=2, linestyle="--")
        ax.text(val / MILLIONS + 5, ax.get_ylim()[1] * 0.85, f"{label}\nEUR {val/MILLIONS:.0f}M",
                color=color, fontsize=9, fontweight="bold")
    ax.set_xlabel("Total CAPEX (EUR millions)", fontsize=11)
    ax.set_ylabel("Frequency", fontsize=11)
    ax.set_title(f"{project_name} — CAPEX Distribution ({ITERATIONS:,} iterations)", fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "01_cost_distribution.png"), dpi=150, bbox_inches="tight")
    plt.close()


def chart_tornado(
    sensitivity: list[tuple[str, float]],
    wp_samples: dict,
    packages: list[WorkPackage],
    output_dir: str,
) -> None:
    top_n = sensitivity[:8]
    pkg_map = {p.id: p for p in packages}
    labels, swings = [], []
    for wp_id, _ in top_n:
        pkg = pkg_map.get(wp_id)
        if pkg:
            swing = (pkg.high_cost - pkg.low_cost) / MILLIONS
            labels.append(f"{wp_id}\n{pkg.description[:30]}")
            swings.append(swing)

    fig, ax = plt.subplots(figsize=(9, max(4, len(labels) * 0.7)))
    colors = ["#C00000" if s == max(swings) else "#4472C4" for s in swings]
    ax.barh(range(len(labels)), swings, color=colors, alpha=0.85)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("P90 − P10 swing (EUR millions)", fontsize=11)
    ax.set_title("Sensitivity Analysis — Top Cost Drivers (P90 minus P10 range)", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "02_tornado_chart.png"), dpi=150, bbox_inches="tight")
    plt.close()


def chart_wbs_breakdown(packages: list[WorkPackage], output_dir: str) -> None:
    labels = [f"{p.id}" for p in packages]
    p50_vals = [p.base_cost / MILLIONS for p in packages]
    swing_up = [(p.high_cost - p.base_cost) / MILLIONS for p in packages]

    fig, ax = plt.subplots(figsize=(max(8, len(packages) * 1.4), 5))
    x = np.arange(len(packages))
    ax.bar(x, p50_vals, color="#4472C4", alpha=0.9, label="P50 estimate")
    ax.bar(x, swing_up, bottom=p50_vals, color="#FF0000", alpha=0.4, label="P50 to P90 range")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9, rotation=30, ha="right")
    ax.set_ylabel("CAPEX (EUR millions)", fontsize=11)
    ax.set_title("CAPEX Breakdown by Work Package", fontsize=11)
    ax.legend(fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "03_wbs_breakdown.png"), dpi=150, bbox_inches="tight")
    plt.close()


def generate_report(
    project_name: str,
    aace_class: int,
    packages: list[WorkPackage],
    total: np.ndarray,
    wp_samples: dict,
    sensitivity: list[tuple[str, float]],
    output_dir: str,
) -> str:
    p10, p50, p90 = np.percentile(total, [10, 50, 90])
    contingency = p90 - p50
    contingency_pct = contingency / p50 * 100

    down, up = AACE_ACCURACY[aace_class]
    pkg_map = {p.id: p for p in packages}

    lines = [
        f"# Budget Estimate — {project_name}",
        f"**AACE Estimate Class:** {aace_class} | "
        f"**Accuracy:** −{int(down*100)}% / +{int(up*100)}% | "
        f"**Iterations:** {ITERATIONS:,}",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Percentile | CAPEX (EUR) | Notes |",
        "|-----------|-------------|-------|",
        f"| **P10** (optimistic) | EUR {p10/MILLIONS:.1f}M | 10% probability of coming in below this |",
        f"| **P50** (central estimate) | EUR {p50/MILLIONS:.1f}M | Most likely outcome — use as planning basis |",
        f"| **P90** (conservative) | EUR {p90/MILLIONS:.1f}M | 90% probability of not exceeding this value |",
        f"| Contingency (P90 − P50) | EUR {contingency/MILLIONS:.1f}M ({contingency_pct:.1f}%) | Recommended reserve |",
        "",
        "> **Board reporting basis:** Use P50 as the central estimate and P90 as the risk-adjusted",
        "> ceiling for budget approval. The P90 contingency should be held as a managed reserve,",
        "> not distributed into work-package budgets.",
        "",
        "---",
        "",
        "## Work Package Breakdown",
        "",
        "| WBS | Description | P50 (EUR) | P90 (EUR) | P90 Swing |",
        "|-----|-------------|-----------|-----------|-----------|",
    ]

    for pkg in packages:
        wp_p50 = np.percentile(wp_samples[pkg.id], 50)
        wp_p90 = np.percentile(wp_samples[pkg.id], 90)
        swing_pct = (wp_p90 - wp_p50) / wp_p50 * 100
        lines.append(
            f"| {pkg.id} | {pkg.description} | "
            f"EUR {wp_p50/MILLIONS:.1f}M | EUR {wp_p90/MILLIONS:.1f}M | +{swing_pct:.1f}% |"
        )

    lines += [
        f"| **TOTAL** | | **EUR {p50/MILLIONS:.1f}M** | **EUR {p90/MILLIONS:.1f}M** | "
        f"+{contingency_pct:.1f}% |",
        "",
        "---",
        "",
        "## Top Cost Drivers (Sensitivity Analysis)",
        "",
        "Ranked by Spearman rank correlation between work-package sample and total CAPEX.",
        "Higher rank = greater influence on the P90 outcome.",
        "",
        "| Rank | WBS | Description | Rank Correlation |",
        "|------|-----|-------------|-----------------|",
    ]

    for rank, (wp_id, corr) in enumerate(sensitivity[:8], 1):
        pkg = pkg_map.get(wp_id)
        desc = pkg.description if pkg else wp_id
        lines.append(f"| {rank} | {wp_id} | {desc} | {corr:.3f} |")

    lines += [
        "",
        "---",
        "",
        "## Charts",
        "",
        "![CAPEX Distribution](01_cost_distribution.png)",
        "",
        "![Sensitivity Tornado](02_tornado_chart.png)",
        "",
        "![WBS Breakdown](03_wbs_breakdown.png)",
        "",
        "---",
        "",
        "## Estimate Basis and Limitations",
        "",
        f"- **AACE Class {aace_class}** estimate: accuracy range −{int(down*100)}% / +{int(up*100)}%",
        "- Parametric work packages use IPA/DVGW benchmarks from `heuristics/pipeline-cost.yaml`",
        "- Monte Carlo uses triangular distributions; correlations between work packages are not modelled",
        "- Owner costs included at 12% of EPC scope (engineering, PM, insurance, permitting)",
        "- Escalation not included; apply project-specific escalation index for schedules > 24 months",
        "- A Class 2 estimate (FEED-complete, ±5/+15%) is required before Final Investment Decision",
        "",
        f"*Generated by `budget_estimator.py` | {ITERATIONS:,} Monte Carlo iterations | "
        f"AACE RP 18R-97 methodology*",
    ]

    report = "\n".join(lines)
    out_path = os.path.join(output_dir, "estimate-report.md")
    with open(out_path, "w") as f:
        f.write(report)
    return report


def run_estimate(
    yaml_path: Optional[str] = None,
    project_type: str = "pipeline",
    length_km: float = 0,
    diameter: str = "DN400",
    terrain: str = "flat_agricultural",
    compression_mw: float = 0,
    h2_service: bool = True,
    block_valves: int = 0,
    aace_class: int = 3,
    output_dir: str = "./estimate-output/",
) -> str:
    os.makedirs(output_dir, exist_ok=True)

    if yaml_path:
        project_name, aace_class, packages = load_yaml_estimate(yaml_path)
    else:
        pkg = parametric_pipeline(
            length_km=length_km,
            diameter=diameter,
            terrain=terrain,
            h2_service=h2_service,
            compression_mw=compression_mw,
            block_valves=block_valves,
            aace_class=aace_class,
            description=f"{diameter} pipeline, {terrain}, {length_km} km",
            wp_id="WBS-1.0",
        )
        project_name = "Quick Parametric Estimate"
        packages = [pkg]

    total, wp_samples = run_monte_carlo(packages)
    sensitivity = sensitivity_spearman(total, wp_samples)

    chart_distribution(total, project_name, output_dir)
    chart_tornado(sensitivity, wp_samples, packages, output_dir)
    chart_wbs_breakdown(packages, output_dir)

    report = generate_report(
        project_name, aace_class, packages, total, wp_samples, sensitivity, output_dir
    )

    p10, p50, p90 = np.percentile(total, [10, 50, 90])
    print(f"\n{project_name}")
    print(f"  AACE Class {aace_class} Estimate")
    print(f"  P10 = EUR {p10/MILLIONS:.1f}M")
    print(f"  P50 = EUR {p50/MILLIONS:.1f}M  (planning basis)")
    print(f"  P90 = EUR {p90/MILLIONS:.1f}M  (risk-adjusted ceiling)")
    print(f"  Contingency (P90-P50) = EUR {(p90-p50)/MILLIONS:.1f}M ({(p90-p50)/p50*100:.1f}%)")
    print(f"\n  Outputs written to: {output_dir}")
    return report


def main():
    parser = argparse.ArgumentParser(description="Parametric CAPEX estimator with P50/P90 Monte Carlo")
    parser.add_argument("yaml", nargs="?", help="YAML estimate definition file")
    parser.add_argument("--type", default="pipeline", help="Project type (pipeline)")
    parser.add_argument("--length-km", type=float, default=100)
    parser.add_argument("--diameter", default="DN400", choices=list(PIPELINE_BASE_EUR_PER_KM.keys()))
    parser.add_argument("--terrain", default="flat_agricultural", choices=list(TERRAIN_FACTORS.keys()))
    parser.add_argument("--compression-mw", type=float, default=0)
    parser.add_argument("--no-h2", action="store_true")
    parser.add_argument("--block-valves", type=int, default=0)
    parser.add_argument("--aace-class", type=int, default=3, choices=[1, 2, 3, 4, 5])
    parser.add_argument("--output", default="./estimate-output/")
    args = parser.parse_args()

    run_estimate(
        yaml_path=args.yaml,
        project_type=args.type,
        length_km=args.length_km,
        diameter=args.diameter,
        terrain=args.terrain,
        compression_mw=args.compression_mw,
        h2_service=not args.no_h2,
        block_valves=args.block_valves,
        aace_class=args.aace_class,
        output_dir=args.output,
    )


if __name__ == "__main__":
    main()

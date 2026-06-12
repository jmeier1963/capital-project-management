---
name: budget-estimator
description: >
  Parametric CAPEX estimation for large capital projects with P50/P90
  probabilistic values via 10,000-iteration Monte Carlo simulation. Produces an
  AACE-classified estimate report, work-package breakdown, sensitivity (tornado)
  chart, and cost distribution histogram. Activates on: "estimate CAPEX",
  "budget estimate", "cost estimate", "P50", "P90", "probabilistic estimate",
  "Monte Carlo estimate", "what will this project cost", "how much will it
  cost", "generate an estimate", or when the user provides a YAML file
  containing a `work_packages:` key. Also use to close a SYS-06 gap
  (risk-adjusted estimate) raised by a systems-thinking audit.
metadata:
  version: 1.1.0
  dependencies: python>=3.9, numpy, scipy, matplotlib, pyyaml, pandas
  standard: AACE RP 18R-97 (cost estimate classification), AACE RP 41R-08 (contingency via simulation)
  domain: capital project management / pre-FID estimating
---

# Budget Estimator Skill — Probabilistic CAPEX (P50/P90)

## Purpose

Generate parametric CAPEX estimates for large capital projects with P50 and P90
probabilistic values via Monte Carlo simulation (10,000 iterations). Produces an
AACE-classified estimate, work-package breakdown, sensitivity (tornado) chart,
and cost distribution histogram. Designed for the pre-FID window: after concept
screening but before the engineering definition required for a bottom-up takeoff.

## When to Use This Skill

Activate automatically whenever the user:
- Asks to "estimate CAPEX", "budget estimate", "cost estimate"
- Mentions "P50", "P90", "probabilistic estimate", "Monte Carlo estimate"
- Asks "what will this project cost" or "how much will it cost"
- Provides a YAML file with a `work_packages:` key
- Asks to "generate an estimate for [project type]"
- Needs to close a **SYS-06 (risk-adjusted estimate)** gap flagged by the
  `systems-thinking` skill

## ⚠️ CRITICAL BEHAVIOUR REQUIREMENTS ⚠️

**DO NOT ask what the user wants to do with the estimate input.**
**DO NOT list analysis options and wait for a choice.**
**IMMEDIATELY run the full estimate and present ALL results.**

If required parameters are missing (e.g. no AACE class, no work packages),
ask for the minimum missing information in ONE question, then run.

### Execution Steps (always in this order)

1. **Identify the input** — a YAML estimate file from the user's message or the
   project directory, or CLI parameters for a quick parametric estimate. If the
   AACE class is not stated, ask once; do not silently assume a class.

2. **Run the estimator**:
   ```bash
   python ~/.claude/skills/budget-estimator/budget_estimator.py <estimate.yaml> --output /tmp/estimate-output/
   ```

3. **Display the markdown report** in full — do not summarise or truncate it.

4. **Show all three charts** — cost distribution, tornado, WBS breakdown,
   each inline with a caption.

5. **Interpret the results** — add a 3–5 sentence plain-language interpretation
   covering:
   - The P50 (planning basis) and P90 (risk-adjusted ceiling) and what they mean
   - The contingency implied by P90 − P50, as a value and a percentage
   - The top 2–3 cost drivers from the tornado chart and where additional
     engineering definition would most reduce uncertainty
   - Whether the distribution is heavily right-skewed (large upside risk)

6. **Benchmark and validate**:
   - If `project-brief.md` contains an approved FID CAPEX, compare P50 and P90
     against it and state the variance explicitly
   - Cite the source and version of every heuristic applied (from
     `heuristics/*.yaml`); if the project falls outside a heuristic's valid
     range (diameter, region, terrain), flag this prominently — do not apply
     the benchmark silently
   - Confirm the estimate class is appropriate for the project phase (see
     stage-gate table below); flag a mismatch as non-compliant

7. **Suggest next steps** — one concise bullet list of ≤5 items (e.g. tighten
   definition on the top tornado driver, commission a reference class forecast,
   re-run at Class 2 after detailed design).

## Entry Point

`budget_estimator.py`

## Input Formats

### YAML estimate file (recommended)

A YAML file describing the project and work packages. See `examples/` for
templates. Pass the path as the first argument:

```
python budget_estimator.py examples/my-project-estimate.yaml
```

### CLI quick-estimate (pipeline)

For a rapid parametric estimate without a YAML file:

```
python budget_estimator.py \
  --type pipeline \
  --length-km 500 \
  --diameter DN400 \
  --terrain rolling_rural \
  --compression-mw 80 \
  --aace-class 3 \
  --output /tmp/my-estimate/
```

## Output

| File | Description |
|------|-------------|
| `estimate-report.md` | Full markdown report: P10/P50/P90, work-package table, AACE class, recommended contingency |
| `01_cost_distribution.png` | Histogram of 10,000 Monte Carlo iterations with P10/P50/P90 markers |
| `02_tornado_chart.png` | Sensitivity chart — top 8 inputs ranked by contribution to P90–P50 spread |
| `03_wbs_breakdown.png` | Stacked bar chart of P50 CAPEX by work package |

## Methodology Notes

- Monte Carlo uses **triangular distributions** for each cost element: low = P10
  input range, base = central estimate, high = P90 input range
- Accuracy ranges per AACE class are applied automatically if not overridden:
  Class 5 = −20%/+50%; Class 4 = −15%/+30%; Class 3 = −10%/+20%;
  Class 2 = −5%/+15%; Class 1 = −3%/+10%
- P50 = the 50th percentile of the simulation total CAPEX distribution
- P90 = the 90th percentile (90% probability of not exceeding this value)
- Sensitivity analysis uses rank correlation (Spearman) between each input
  variable and the total CAPEX across all iterations
- Contingency is reported separately as P90 − P50

## When to Use Which Estimate Class

| Phase | AACE Class | Accuracy | Use for |
|-------|-----------|---------|---------|
| Concept screening | 5 | −20/+50% | Go/no-go decision |
| Pre-FEED | 4 | −15/+30% | Budget setting |
| FEED completion | 3 | −10/+20% | FID preparation |
| Detailed design | 2 | −5/+15% | Contract award basis |
| Actuals | 1 | −3/+10% | Claims, final account |

## Integration with the Skill Suite

This skill is the operational answer to **SYS-06** in the `systems-thinking`
audit. It also anchors the execution-phase feedback loop:

- **Upstream (`systems-thinking`)** — when an audit rates SYS-06 PARTIAL or
  ABSENT, produce a P50/P90 estimate at the phase-appropriate AACE class as the
  remediation artifact
- **Gate review (`gate-readiness`)** — the estimate report is required gate
  evidence; the gate-readiness skill checks its existence, AACE class, and age
- **Downstream (`evm`)** — the P50 becomes the planning basis the EVM skill
  later benchmarks EAC forecasts against; keep `estimate-report.md` in the
  project directory so the EVM skill can find it
- **Close-out (`lessons-learned`)** — final actuals are compared against this
  estimate per work package to calibrate the `heuristics/*.yaml` benchmarks for
  the next project

## Example Usage

```
User: "Estimate the CAPEX for the pipeline described in estimate.yaml"
```
→ Run estimator, display full report, show all charts, interpret, benchmark
against FID CAPEX if available.

```
User: "What would a 300 km DN500 hydrogen pipeline in mountainous terrain cost?"
```
→ Confirm AACE class (likely 5 if conceptual), run the CLI quick-estimate,
present P50/P90 with the accuracy caveats of the chosen class.

```
User: "The systems-thinking audit flagged SYS-06 — fix it"
```
→ Build a YAML work-package definition from the project brief, run the
estimator, and present the risk-adjusted estimate as the SYS-06 remediation.

## Files

- `budget_estimator.py` — Parametric engine with Monte Carlo simulation
- `requirements.txt` — Python dependencies
- `examples/h2-pipeline-estimate.yaml` — AACE Class 3 worked example

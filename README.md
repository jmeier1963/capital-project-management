# Large Capital Project Management — Claude Code Scaffolding

A **Claude Code skill and project scaffolding system** for large capital projects
(LCPs) such as hydrogen pipelines, offshore platforms, refineries, and
infrastructure programmes. Combines structured data schemas, domain heuristics,
specialist agents, a fully working **Earned Value Management (EVM) skill**, a
**parametric Budget Estimator skill** that produces P50/P90 CAPEX forecasts via
Monte Carlo simulation, and a **Systems Thinking audit skill** that stress-tests
project definitions against fifteen research-derived heuristics before FID or
stage-gate review.

![Overview of the AI-augmented large capital project management skill suite](overview_projectmanagement.png)

The full rationale, architecture, evaluation results, and investment case are
documented in the integrated concept paper:
[`concept-paper/large_capital_project_management.md`](concept-paper/large_capital_project_management.md)
([PDF](concept-paper/large_capital_project_management.pdf)).

---

## Contents

```
.
├── evm/                         # EVM skill — install into Claude Code
│   ├── SKILL.md                 #   Behavioral instructions for Claude
│   ├── evm_calculator.py        #   Core Python engine (713 lines)
│   ├── requirements.txt         #   pandas, matplotlib, numpy
│   └── examples/
│
├── budget-estimator/            # Budget estimator skill — P50/P90 Monte Carlo
│   ├── SKILL.md                 #   Behavioral instructions for Claude
│   ├── budget_estimator.py      #   Parametric CAPEX engine with Monte Carlo
│   ├── requirements.txt         #   numpy, scipy, matplotlib, pyyaml, pandas
│   └── examples/
│       └── h2-pipeline-estimate.yaml   # H2-PIPE-DE-001 AACE Class 3 estimate
│       ├── h2-pipeline-snapshot.csv      # Single-period test data
│       └── h2-pipeline-timephased.csv    # Five-period trend test data
│
├── scaffolding/                 # Project-level Claude configuration templates
│   ├── CLAUDE.md                #   Domain rules, judgment rules, output standards
│   ├── .claude/rules/
│   │   ├── roles.md             #   Role taxonomy and addressing rules
│   │   ├── heuristics.md        #   Rules for applying heuristics
│   ├── agents/
│   │   ├── schedule-analyzer.md #   Schedule health and recovery agent
│   │   ├── contract-reviewer.md #   Contract extraction and CO assessment agent
│   │   └── risk-assessor.md     #   Risk register EMV and escalation agent
│   ├── heuristics/
│   │   ├── pipeline-cost.yaml   #   EUR/km installed cost by diameter and terrain
│   │   └── productivity-norms.yaml  # Labour productivity by discipline
│   ├── schemas/
│   │   ├── project-brief.schema.json
│   │   ├── contract.schema.json
│   │   └── risk-register.schema.json
│   └── templates/
│       └── project-brief.md     #   Blank project brief template
│
├── systems-thinking/            # Systems thinking audit skill
│   ├── SKILL.md                 #   Audit workflow + output template
│   ├── references/
│   │   └── sys-rules.md         #   Full criteria for all 15 SYS rules
│   ├── evals/
│   │   └── evals.json           #   3 test scenarios with assertions
│   └── systems-thinking.skill   #   Packaged .skill file for direct installation
│
├── concept-paper/               # Academic-practitioner paper
│   ├── large_capital_project_management.md/.pdf   # Integrated concept paper
│   ├── pandoc-pdf-header.tex    #   LaTeX preamble for the PDF build
│   └── references/
│       ├── large_capital_project_management_execution_skill.md/.pdf
│       ├── large_capital_project_management_systems-thinking_skill.md/.pdf
│       └── systems-thinking-research-report-en.md
│
└── examples/
    └── H2-PIPE-DE-001/          # GreenArtery — 500 km H2 pipeline, Germany
        ├── project-brief.md
        └── 03-cost/
            ├── evm-snapshot-2026-05.csv
            └── evm-timephased.csv
```

---

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| [Claude Code](https://claude.ai/code) | Latest | CLI or IDE extension |
| Python | ≥ 3.9 | For the EVM calculator |
| pip | Any | To install Python dependencies |

---

## Installation

### 1 — Install the EVM skill into Claude Code

Copy the `evm/` directory into your Claude Code skills folder:

```bash
# macOS / Linux
cp -r evm/ ~/.claude/skills/evm/

# Windows (PowerShell)
Copy-Item -Recurse evm\ $env:USERPROFILE\.claude\skills\evm\
```

Install Python dependencies:

```bash
pip install -r ~/.claude/skills/evm/requirements.txt
```

That's it. Claude Code will discover the skill automatically on next launch
(it scans `~/.claude/skills/` for `SKILL.md` files).

### 2 — Set up a new project using the scaffolding

Create your project directory and copy the scaffolding templates:

```bash
mkdir -p my-project/{00-foundation,01-contracts,02-schedule,03-cost,04-resources,05-risk,06-engineering}
cp scaffolding/CLAUDE.md my-project/CLAUDE.md
cp -r scaffolding/.claude/ my-project/.claude/
cp -r scaffolding/heuristics/ my-project/heuristics/
cp -r scaffolding/schemas/ my-project/schemas/
cp scaffolding/templates/project-brief.md my-project/project-brief.md
```

Edit `my-project/CLAUDE.md` to adjust any project-specific judgment rules,
then open the project in Claude Code:

```bash
claude my-project/
```

---

## Using the EVM Skill

### Automatic activation

The skill activates automatically when you mention any of these in Claude Code:

- `"run EVM"`, `"earned value"`, `"CPI/SPI"`, `"EAC forecast"`
- `"analyse project costs"`, `"cost performance report"`
- When you provide a CSV file with columns `bac`, `bcws_cum`, `bcwp_cum`, `acwp_cum`

### Manual invocation

In Claude Code, type:

```
Analyse the EVM data in examples/H2-PIPE-DE-001/03-cost/evm-snapshot-2026-05.csv
```

or reference the skill directly:

```
/evm examples/H2-PIPE-DE-001/03-cost/evm-timephased.csv
```

### Run the calculator directly from the terminal

```bash
# Snapshot (single period)
python evm/evm_calculator.py examples/H2-PIPE-DE-001/03-cost/evm-snapshot-2026-05.csv

# Time-phased (multi-period — generates S-curve and trend charts)
python evm/evm_calculator.py examples/H2-PIPE-DE-001/03-cost/evm-timephased.csv --output /tmp/evm-report/
```

### Import as a Python module

```python
from evm.evm_calculator import run_evm_analysis

report = run_evm_analysis(
    csv_path="examples/H2-PIPE-DE-001/03-cost/evm-timephased.csv",
    output_dir="/tmp/my-report/"
)
print(report)
```

---

## EVM Input CSV Format

### Snapshot (one row per WBS element)

```csv
wbs_code,wbs_description,bac,bcws_cum,bcwp_cum,acwp_cum,period
WBS-1.1,Mainline Construction N,485000000,58200000,43650000,48000000,2026-05
WBS-1.2,Mainline Construction S,493000000,52000000,50000000,49500000,2026-05
WBS-2.0,Compression Stations,340000000,45000000,38000000,41500000,2026-05
```

### Time-phased (multiple rows per WBS, one per period)

```csv
wbs_code,wbs_description,bac,period,bcws_cum,bcwp_cum,acwp_cum
WBS-1.1,Mainline Construction N,485000000,2026-01,5000000,4500000,4800000
WBS-1.1,Mainline Construction N,485000000,2026-02,12500000,9800000,10500000
WBS-1.1,Mainline Construction N,485000000,2026-03,24000000,18200000,19800000
```

> All BCWS/BCWP/ACWP values must be **cumulative** (not period-only increments).
> The script auto-detects snapshot vs. time-phased format.

**Required columns:**

| Column | Type | Description |
|--------|------|-------------|
| `wbs_code` | string | WBS identifier |
| `wbs_description` | string | Human-readable name |
| `bac` | float | Budget at Completion (project currency) |
| `bcws_cum` | float | Cumulative Planned Value (BCWS) |
| `bcwp_cum` | float | Cumulative Earned Value (BCWP) |
| `acwp_cum` | float | Cumulative Actual Cost (ACWP) |
| `period` | string | *(optional for snapshot)* e.g. `2026-05` |

---

## EVM Outputs

| File | Description |
|------|-------------|
| `evm-report.md` | Full markdown report: executive summary, WBS table, 3 EAC methods, escalation flags |
| `01_s_curve.png` | Cumulative BCWS/BCWP/ACWP S-curve *(time-phased only)* |
| `02_indices_trend.png` | CPI & SPI trend with GREEN/AMBER/RED bands *(time-phased only)* |
| `03_wbs_variance.png` | Cost Variance by WBS package (RAG-coloured horizontal bars) |
| `04_eac_comparison.png` | BAC vs three EAC methods per package |
| `05_cpi_spi_quadrant.png` | Four-quadrant performance map, bubble size ∝ BAC |

### Metrics computed

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| CV | BCWP − ACWP | Cost Variance (+ve = under budget) |
| SV | BCWP − BCWS | Schedule Variance (+ve = ahead) |
| CPI | BCWP / ACWP | Cost efficiency (>1 = under budget) |
| SPI | BCWP / BCWS | Schedule efficiency (>1 = ahead) |
| EAC (CPI) | BAC / CPI | Forecast assuming current efficiency |
| EAC (Composite) | ACWP + (BAC−BCWP) / (CPI×SPI) | **Recommended for LCPs** |
| EAC (Planned) | ACWP + (BAC−BCWP) | Optimistic — full recovery assumed |
| ETC | EAC − ACWP | Remaining spend to complete |
| VAC | BAC − EAC | Expected over/under at completion |
| TCPI | (BAC−BCWP) / (BAC−ACWP) | Required future efficiency; >1.10 = danger |

### RAG thresholds

| Index | GREEN | AMBER | RED |
|-------|-------|-------|-----|
| CPI | ≥ 0.95 | 0.85–0.94 | < 0.85 |
| SPI | ≥ 0.95 | 0.85–0.94 | < 0.85 |

### Escalation rules (automatic)

- CPI < 0.85 → **Project Director notification**
- SPI < 0.85 → **Project Director notification**
- SPI < 0.85 for 2 consecutive periods → **written escalation memo required**
- TCPI > 1.10 → **re-baselining assessment recommended**

---

## Example Output — H2-PIPE-DE-001 (May 2026)

Running against the included time-phased example:

```
Project TOTAL (5 contracts, EUR 1,350.5M BAC)

  CPI  = 0.949  🟡 AMBER  — spending 5.3% more than earned
  SPI  = 0.855  🟡 AMBER  — 14.5% behind schedule in cost terms

  EAC (CPI):       EUR 1,422.5M  (+EUR  72M vs BAC)
  EAC (Composite): EUR 1,637.3M  (+EUR 287M vs BAC)  ← recommended
  EAC (Planned):   EUR 1,358.2M  (+EUR   8M vs BAC)  ← optimistic

  TCPI = 1.006  ✓  (recovery is still mathematically feasible)

  ⚠️  WBS-1.1 (Mainline North): SPI = 0.750 🔴 RED
      Pipe delivery delay driving schedule underperformance.
      If SPI remains below 0.85 in June reporting: Project Director
      escalation memo is mandatory.
```

---

## Using the Budget Estimator Skill

The budget-estimator skill generates AACE-classified parametric CAPEX estimates
with P50 (central estimate) and P90 (risk-adjusted ceiling) values from a
10,000-iteration Monte Carlo simulation. It is designed for the pre-FID window:
after concept screening but before the engineering definition required for a
bottom-up takeoff.

Unlike a single-point estimate, P50/P90 output makes the range of uncertainty
explicit. The estimate class (1–5) sets the accuracy bounds:

| AACE Class | Phase | Accuracy | Contingency basis |
|-----------|-------|---------|------------------|
| 5 | Concept screening | −20% / +50% | Screening-level decisions |
| 4 | Pre-FEED | −15% / +30% | Budget placeholder |
| 3 | FEED completion | −10% / +20% | FID preparation |
| 2 | Detailed design | −5% / +15% | Contract award basis |
| 1 | Definitive | −3% / +10% | Final account / claims |

The Monte Carlo engine samples each work package using a **triangular
distribution** (low = P10 bound, base = central estimate, high = P90 bound) and
sums 10,000 independent draws. The resulting cost distribution captures both the
central outcome and the tail risk. Contingency is reported as P90 − P50 — sized
by the actual shape of the distribution, not a flat percentage.

A **sensitivity tornado chart** ranks work packages by Spearman rank correlation
with total CAPEX across all iterations, showing exactly which elements drive the
P90 and where additional engineering definition would most reduce uncertainty.

### Automatic activation

The skill activates when you mention any of the following in Claude Code:

- `"estimate CAPEX"`, `"budget estimate"`, `"P50/P90"`
- `"what will this project cost"`, `"probabilistic estimate"`, `"Monte Carlo"`
- When you provide a YAML file with a `work_packages:` key

### Run from a YAML estimate file

```bash
python budget-estimator/budget_estimator.py \
  budget-estimator/examples/h2-pipeline-estimate.yaml \
  --output /tmp/my-estimate/
```

### Quick parametric estimate (no YAML needed)

```bash
python budget-estimator/budget_estimator.py \
  --type pipeline \
  --length-km 500 \
  --diameter DN400 \
  --terrain rolling_rural \
  --compression-mw 80 \
  --aace-class 3 \
  --output /tmp/quick-estimate/
```

### Example output — H2-PIPE-DE-001 (AACE Class 3)

```
GreenArtery — North Sea H2 Transmission Pipeline
  AACE Class 3 Estimate
  P10 = EUR 1,748M
  P50 = EUR 1,833M  (planning basis)
  P90 = EUR 1,930M  (risk-adjusted ceiling)
  Contingency (P90-P50) = EUR 97M (5.3%)
```

### Budget Estimator Outputs

| File | Description |
|------|-------------|
| `estimate-report.md` | Full markdown report: P10/P50/P90, work-package breakdown, AACE class, contingency |
| `01_cost_distribution.png` | CAPEX distribution histogram from 10,000 Monte Carlo iterations |
| `02_tornado_chart.png` | Sensitivity analysis — top cost drivers ranked by contribution to P90–P10 spread |
| `03_wbs_breakdown.png` | P50 vs P90 range per work package |

### YAML estimate file format

```yaml
project:
  name: "My Project"
  aace_class: 3         # 1=definitive, 3=FEED, 5=conceptual

work_packages:
  - id: WBS-1.0
    description: "Mainline Pipeline (500 km, DN400)"
    method: parametric  # uses pipeline-cost heuristics
    params:
      length_km: 500
      diameter: DN400
      terrain: rolling_rural  # flat_agricultural | gently_rolling | mountainous_or_rock
      h2_service: true
      compression_mw: 0
      block_valves: 12
      include_owner_costs: false   # set true if no separate owner-cost WP

  - id: WBS-2.0
    description: "Compression Stations"
    method: direct       # direct cost entry with uncertainty range
    base_cost_eur: 340_000_000
    uncertainty_pct: 0.20
    downside_pct: 0.05
```

---

## Using the Systems-Thinking Skill

The systems-thinking skill audits a project definition, status report, or FID
pack against **fifteen heuristics** derived from megaproject failure research
(Crossrail, Olkiluoto 3, NHS NPfIT, Longannet CCS, Vogtle, Big Dig, and eleven
further cases). It produces a board-ready report covering every heuristic, a
maturity score on a 1–5 scale, and a ranked gap list expressed in a standardised
omission vocabulary — making outputs directly comparable across projects.

Evaluation across three test scenarios showed a **100% assertion pass rate with
the skill versus 41% without** (+59 percentage points). The skill adds consistent
structure and vocabulary, not domain knowledge: unaided Claude correctly identifies
material risks, but each run invents a different framework, making cross-project
comparison impossible.

### Installing the Systems-Thinking Skill

```bash
# Option A — copy the skill directory
cp -r systems-thinking/ ~/.claude/skills/systems-thinking/

# Option B — install the packaged .skill file
# (requires skill-creator: python3 -m scripts.install_skill systems-thinking/systems-thinking.skill)
```

### Automatic activation

The skill activates when you mention any of the following in Claude Code:

- `"systems thinking audit"`, `"SYS audit"`, `"megaproject risk review"`
- `"check this project for blind spots"`, `"check for systemic risks"`
- `"what could go wrong with this project?"`
- Sharing a project document before a board approval, FID, or stage-gate review
- Any context where a project director or supervisory board member needs to
  stress-test a project definition

### What input to provide

The skill works from any project documentation available — project brief, business
case, FID pack, programme update, or stage-gate submission. Where specific
information is absent, the relevant rule is rated ABSENT and the corresponding
omission flag is raised. Absence of evidence is itself a finding.

### Output structure

| Section | Content |
|---------|---------|
| Project Overview | Type, phase, decision gate, audience |
| Overall Maturity Score | X/5 with one-sentence characterisation |
| SYS Rule Assessment | All 15 rules rated PRESENT / PARTIAL / ABSENT with findings |
| Critical Gaps (ranked) | Top 3–5 gaps ordered by impact and reversibility |
| Recommended Next Actions | Gap → tool → owner → output → timeframe |
| Omission Flags | Exact vocabulary flags for automated portfolio screening |
| Board Guidance Note | Plain-language summary for non-technical board members |

### Maturity scale

| Score | Meaning |
|-------|---------|
| 1 | Asset-centric only — full chain, regulation, and integration not addressed |
| 2 | Partial chain with major gaps — typical early-stage definition |
| 3 | Structured approach, incomplete evidence — framework present but thin |
| 4 | Mature definition with minor gaps — most rules evidenced |
| 5 | Fully integrated — chain, interfaces, regulation, operations, and exit complete |

Most pre-FID project definitions score 2–3.

### The fifteen SYS rules

| Rule | Addresses |
|------|-----------|
| SYS-01 | Full value chain — upstream, asset, downstream, operations, exit |
| SYS-02 | Second and third-order effects |
| SYS-03 | Regulatory map (permits, levies, liability, subsidies) before FID |
| SYS-04 | Design-maturity threshold before construction commitment |
| SYS-05 | Interface ownership and maturity evidence |
| SYS-06 | Risk-adjusted estimate (P50/P80) alongside point estimate |
| SYS-07 | Outside view / reference class forecasting before sponsor view |
| SYS-08 | Integration phase planned as its own megaproject |
| SYS-09 | Supply-chain and workforce readiness |
| SYS-10 | Stakeholders as system components (social licence) |
| SYS-11 | Business case stress-tested under policy, price, and demand scenarios |
| SYS-12 | Kill criteria explicitly defined |
| SYS-13 | Operations and maintenance in scope of project definition |
| SYS-14 | FOAK treated as a learning programme, not a repeat delivery |
| SYS-15 | Cluster and platform questions escalated to portfolio level |

Full rule criteria (PRESENT / PARTIAL / ABSENT) are in
`systems-thinking/references/sys-rules.md`.

### Follow-on tools

Three Claude Code marketplace skills are recommended as follow-ons for the most
common gap types:

| Gap type | Skill | Example use |
|----------|-------|-------------|
| SYS-11 fragile business case | `what-if-oracle` | Carbon price ±50%, demand −20%, rates +200bp |
| SYS-03 regulatory gaps | `perplexity-search` | Finnish YVA permit, CCS transport classification |
| SYS-07 no outside view | `literature-review` | IPA benchmarks, GAO cost guide, NAO optimism-bias data |

### Research basis

The 15 SYS rules are grounded in analysis of fifteen major projects with
authoritative public post-mortems. The five recurring systemic blindspots are:

1. **Legal-regulatory non-integration** (Longannet CCS, Pascua-Lama)
2. **Build-before-design-freeze** (Olkiluoto 3, Flamanville 3, Vogtle, Sydney Opera House)
3. **Late integration economics** (Crossrail, NHS NPfIT)
4. **Physical-social coupling** (Hallandsås Tunnel, Pascua-Lama)
5. **Governance fragmentation** (Scottish Parliament, Big Dig, Crossrail)

Full analysis in `concept-paper/large_capital_project_management.md` (Section 3)
and `concept-paper/references/systems-thinking-research-report-en.md`.

---

## Scaffolding — Project Structure

### Recommended directory layout for a new project

```
my-project/
├── CLAUDE.md                    ← copy from scaffolding/, customise
├── .claude/rules/               ← copy from scaffolding/
├── heuristics/                  ← copy from scaffolding/, adjust to your region
├── schemas/                     ← copy from scaffolding/
│
├── project-brief.md             ← fill from templates/project-brief.md
│
├── 00-foundation/
│   ├── basis-of-design.md
│   ├── FID-package-summary.md
│   └── regulatory-approvals.md
│
├── 01-contracts/
│   ├── contracts-register.csv   ← validate against schemas/contract.schema.json
│   └── change-orders/
│
├── 02-schedule/
│   ├── milestones.csv           ← columns: milestone_id, description, planned_date,
│   └── schedule-risk-analysis.md     forecast_date, actual_date, critical_path, owner
│
├── 03-cost/
│   ├── evm-timephased.csv       ← append one period per month
│   ├── wbs.csv
│   └── evm-output/              ← written by the EVM skill
│
├── 04-resources/
│   ├── org-chart.md
│   └── resource-matrix.csv
│
├── 05-risk/
│   ├── risk-register.csv        ← validate against schemas/risk-register.schema.json
│   └── hazop-summary.md
│
└── 06-engineering/
    ├── linepipe-spec.md
    └── material-take-off.csv
```

### Agents

Three specialist sub-agents are included in `scaffolding/agents/`. Copy them to
your project's `.claude/agents/` directory so Claude Code can invoke them:

```bash
cp -r scaffolding/agents/ my-project/.claude/agents/
```

| Agent | Activates on | Output |
|-------|-------------|--------|
| `schedule-analyzer` | "schedule analysis", "SPI", milestone slip | Schedule health report + recovery options |
| `contract-reviewer` | Contract PDF or "change order", "claim" | Structured commercial summary, flagged clauses |
| `risk-assessor` | "risk review", "EMV", monthly cycle | Top-10 risk digest, escalation flags |

### Heuristics

`heuristics/pipeline-cost.yaml` contains parametric cost benchmarks for
onshore hydrogen pipelines in Germany / Western Europe, with:
- Installed cost per km by diameter (DN300–DN600)
- Terrain adjustment factors
- H2 service material premiums
- Contingency ranges by estimate class

`heuristics/productivity-norms.yaml` contains labour productivity norms for
pipeline welding, civil excavation, mechanical erection, and electrical work.

Both files carry `source:`, `valid_range:`, and `version:` fields. Claude will
always cite these when applying the numbers.

---

## Monthly Workflow

1. **At reporting cutoff** — append a new period row for each WBS element
   to `03-cost/evm-timephased.csv`

2. **Run EVM** — open Claude Code in the project directory and type:
   ```
   Generate the monthly EVM report
   ```
   Claude will find `evm-timephased.csv`, run the skill, display the report,
   show all charts, and highlight any escalation flags.

3. **Update milestones** — update `02-schedule/milestones.csv` with new
   forecast dates; type `"schedule analysis"` to invoke the schedule-analyzer agent.

4. **Review risks** — type `"risk review"` to invoke the risk-assessor agent.
   It will identify any new risks needing entry and flag materialised risks
   for cost register update.

5. **Assemble report deck** — use the `pptx` skill (if installed) to build
   the monthly progress presentation from the EVM report and chart files.

---

## Standards Referenced

- **ANSI/EIA-748** — Earned Value Management Systems
- **PMI Practice Standard for EVM, 3rd Edition**
- **AACE RP 89R-03** — Forensic Schedule Analysis
- **AACE TCM Framework** — Total Cost Management
- **ASME B31.12** — Hydrogen Piping and Pipelines
- **API 5L** — Specification for Line Pipe
- **DVGW G 463** — German hydrogen pipeline requirements
- **IPA Benchmarking Database** — Cost and productivity norms

---

## Extending the Scaffolding

### Add a new heuristic

Create a YAML file in `heuristics/` with the mandatory metadata header:

```yaml
# heuristics/compression-station-cost.yaml
# Source: [cite your source]
# Valid for: [scope, region, conditions]
# Accuracy: ±xx% (AACE Class x equivalent)
# Version: 1.0 | Updated: YYYY-MM
```

Then reference it in `scaffolding/.claude/rules/heuristics.md`.

### Add a new agent

Create a markdown file in `.claude/agents/` following the pattern in
`scaffolding/agents/`. The frontmatter `description:` field is what Claude
uses to decide when to invoke the agent — make it specific and include
trigger phrases.

### Add a new schema

Add a JSON Schema file to `schemas/`. Reference it in `CLAUDE.md` to tell
Claude when to validate data against it.

---

## Contributing

Issues and pull requests are welcome. Areas where contributions are most useful:

- Heuristics for other geographies (North America, APAC, Middle East)
- Additional industry sectors (offshore, mining, data centres)
- Additional agent definitions (HSE incident tracker, procurement tracker)
- Integration examples with Primavera P6 XER export files

---

## License

MIT

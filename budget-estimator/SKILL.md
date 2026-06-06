# Budget Estimator Skill

## Purpose

Generate parametric CAPEX estimates for large capital projects with P50 and P90
probabilistic values via Monte Carlo simulation (10,000 iterations). Produces an
AACE-classified estimate, work-package breakdown, sensitivity (tornado) chart,
and cost distribution histogram.

## Trigger Phrases

Activate this skill when the user asks any of the following:
- "estimate CAPEX", "budget estimate", "cost estimate"
- "P50", "P90", "probabilistic estimate", "Monte Carlo estimate"
- "what will this project cost", "how much will it cost"
- When a YAML file with `work_packages:` is provided
- "generate an estimate for [project type]"

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

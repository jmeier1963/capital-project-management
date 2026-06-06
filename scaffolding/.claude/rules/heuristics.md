# Heuristics Usage Rules

## Always Cite Provenance

When applying any heuristic, include:
- Source file (e.g., `heuristics/pipeline-cost.yaml`)
- The specific constant used
- The `source:` and `valid_range:` fields from that file
- A note if the project falls outside the valid range

## Never Apply Heuristics Beyond Their Valid Range

If project parameters fall outside a heuristic's `valid_range:`, state this
explicitly and recommend commissioning a site-specific estimate instead.

## Hierarchy: Actuals > Benchmarks > Heuristics

1. If actual costs/rates are available for this project, use them
2. If external benchmark studies are available (e.g., IPA), use those
3. Fall back to the parametric heuristics in `heuristics/` only when (1) and (2) are absent

## Heuristic Files

| File | Domain | Last Updated |
|------|--------|-------------|
| `pipeline-cost.yaml` | Pipeline installed cost (EUR/km) by diameter and terrain | See file header |
| `productivity-norms.yaml` | Labour productivity by discipline and condition | See file header |
| `schedule-compression.yaml` | Max schedule compression factors by phase | See file header |

## EAC Sanity Check

Before presenting any EAC forecast, check it against the parametric benchmark:
- Compute the implied cost per km (or per MW, or per ton) from the EAC
- Compare against `heuristics/pipeline-cost.yaml` base rate
- If EAC implies a unit rate > 30% above benchmark: flag as requiring explanation
- If EAC implies a unit rate > 50% above benchmark: recommend independent review

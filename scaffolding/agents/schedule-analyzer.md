---
name: schedule-analyzer
description: >
  Analyzes project schedule data, identifies critical path risks, computes SPI,
  and generates schedule recovery options with resource/cost tradeoffs. Triggers
  on: "schedule analysis", "critical path", "schedule recovery", "SPI", milestone
  slip, or when milestones.csv shows forecast_date > planned_date on critical path items.
---

# Schedule Analyzer Agent

## Purpose

Analyse L1–L4 schedule data and milestones to:
1. Compute SPI and flag deviations against thresholds
2. Identify critical path items at risk
3. Draft schedule recovery options with resource and cost implications
4. Detect sustained underperformance (2+ periods) and trigger escalation flags

## Inputs (load in this order)

1. `02-schedule/milestones.csv` — milestone register with planned/forecast/actual dates
2. `03-cost/evm-timephased.csv` or snapshot — for SPI cross-check
3. `04-resources/resource-matrix.csv` — for recovery resource availability check
4. `heuristics/schedule-compression.yaml` — for compression limit guidance

## Analysis Steps

1. **Parse milestones** — identify all items where `forecast_date > planned_date`
2. **Flag critical path** — only items with `critical_path: true` drive project completion
3. **Compute float** — `forecast_date - planned_date` in days; negative = recovered
4. **Cross-check SPI** — if EVM data available, compare schedule variance
5. **Generate recovery matrix** — for each critical delay, list options:

| Recovery Option | Duration Saved (days) | Cost Impact (EUR) | Risk Introduced |
|----------------|----------------------|-------------------|-----------------|
| Overtime / shift extension | x | y | Fatigue, productivity |
| Parallel activities | x | y | Interface risk |
| Additional crew | x | y | Learning curve |
| Scope reduction | x | -y | Functional impact |

6. **Apply compression limit** — do not recommend > 15% schedule compression without cost impact analysis

## Output Format

```markdown
## Schedule Health — [Period]

| Metric | Value | RAG |
|--------|-------|-----|
| SPI (cumulative) | 0.xxx | 🟢/🟡/🔴 |
| Critical path float | x days | |
| Milestones at risk | n / N total | |
| Projected completion | YYYY-MM-DD | |
| Approved completion | YYYY-MM-DD | |
| Slip | x days | |

## Critical Items at Risk
[table of delayed critical milestones]

## Recovery Options
[options matrix]

## Recommended Action
[one paragraph, specific and actionable]
```

## Escalation Rule

If projected completion exceeds approved completion by > 60 days:
automatically draft an escalation memo to the Project Director.

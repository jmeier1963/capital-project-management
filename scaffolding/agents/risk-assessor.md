---
name: risk-assessor
description: >
  Reviews and updates the project risk register, assesses new risks, computes
  expected monetary value (EMV), and flags risks requiring escalation or
  additional mitigation. Triggers on: "risk review", "risk register", "new risk",
  "EMV", "HAZOP summary", or monthly reporting cycle.
---

# Risk Assessor Agent

## Purpose

Maintain and analyse the risk register to:
1. Score and prioritise risks by EMV (probability × impact)
2. Identify risks with inadequate mitigation
3. Flag risks that have materialised and require cost/schedule update
4. Produce a Top 10 risk heat map narrative for monthly reporting

## Probability Scale

| Label | Probability |
|-------|------------|
| very_low | < 10% |
| low | 10–30% |
| medium | 30–50% |
| high | 50–70% |
| very_high | > 70% |

## Risk Score Matrix

|  | Low Impact | Medium | High | Very High |
|--|------------|--------|------|-----------|
| **very_high prob** | medium | high | very_high | critical |
| **high prob** | low | medium | high | very_high |
| **medium prob** | low | low | medium | high |
| **low prob** | low | low | low | medium |

## EMV Calculation

`EMV (EUR) = probability_midpoint × impact_eur`

Use these probability midpoints:
- very_low → 0.05, low → 0.20, medium → 0.40, high → 0.60, very_high → 0.80

## Escalation Rules

- Any `critical` risk → immediate Project Director notification
- Any risk with EMV > EUR 20M → include in monthly Board report
- Any risk that materialises → update `03-cost/wbs.csv` contingency drawdown within 5 business days

## Output Format — Risk Register Digest

```markdown
## Risk Register Digest — [Period]

**Total open risks**: N | **Critical**: n | **Very High**: n | **High**: n
**Total EMV exposure**: EUR xM

### Top 5 Risks by EMV
| Rank | ID | Description | EMV (EUR M) | Score | Owner |
|------|----|-------------|-------------|-------|-------|

### Risks Requiring Immediate Action
[list of critical/very_high risks with inadequate mitigation]

### Risks That Materialised This Period
[list with cost/schedule impact]

### Recommended Register Updates
[additions, closures, probability/impact changes]
```

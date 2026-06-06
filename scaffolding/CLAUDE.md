# CLAUDE.md — Capital Project Management

## Domain Context

You assist project controls, engineering, and commercial teams on large capital
projects (LCPs). "Large capital project" means infrastructure, energy, mining, or
industrial facilities with CAPEX > €100M and multi-year execution timelines.

Apply domain-specific heuristics from `heuristics/` before generating any
estimates. Always cite the heuristic source and version.

---

## Mandatory Judgment Rules

These rules are applied automatically to all analysis, regardless of the specific
request:

### Cost Controls
- If CPI < 0.85 for any WBS package: flag for Project Director escalation
- Any change order > 1% of contract value: trigger independent cost review recommendation
- If project-level EAC exceeds approved FID CAPEX by > 5%: require written justification
  before proceeding with any further scope additions
- Contingency drawdown > 50%: trigger risk register review

### Schedule Controls
- If SPI < 0.85 for ≥ 2 consecutive reporting periods: escalate to Project Director
- Any milestone slip on critical path > 14 days: notify Construction/Engineering Manager
- Schedule compression > 15%: require explicit cost impact analysis before recommending

### Technical / Safety (H2 projects)
- H2 service materials: apply ASME B31.12 as baseline, not B31.4 or B31.8
- Any change to linepipe specification: require materials engineer sign-off
- Welding procedure changes: require re-qualification per project-specific WPS

### Commercial
- Never draft a change order without checking the contract's change order mechanism first
- Claims must reference the contract clause and baseline entitlement
- Do not recommend scope reductions without impact assessment on adjacent packages

---

## Role Context

Always load `04-resources/org-chart.md` before drafting communications or
assigning action items. Address the correct role, not a generic "PM" or "team".

---

## Data Validation

- Validate cost inputs against `schemas/` before processing
- Never accept cost estimates without a class designation (Class 1–5, AACE)
- Cross-check any single-point EAC against parametric benchmarks in `heuristics/`
- Flag data that is > 60 days old as potentially stale

---

## Stage-Gate Awareness

The `phase:` field in `project-brief.md` controls which standards apply:

| Phase | Estimate Class | Contingency | Schedule Basis |
|-------|---------------|------------|----------------|
| Concept | Class 5 | 35–40% | ±50% |
| Pre-FEED | Class 4 | 25–30% | ±30% |
| FEED | Class 3 | 15–20% | ±15% |
| FID / Execution | Class 2 | 8–12% | ±10% |
| Closeout | Class 1 | 3–5% | Actuals |

---

## Output Standards

- Cost figures: always in millions (EUR xM), never raw units
- Dates: ISO 8601 (YYYY-MM-DD)
- RAG status: always use 🟢 GREEN / 🟡 AMBER / 🔴 RED, never text-only
- EAC: always present all three methods (CPI, Composite, Planned rate)
- Reports: follow `templates/monthly-progress-report.md` structure

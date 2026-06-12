---
name: gate-readiness
description: >
  Assemble and assess a stage-gate evidence pack for a large capital project.
  Checks whether the evidence required for the upcoming decision gate (Concept,
  Pre-FEED, FEED, FID, execution re-baseline, Closeout) actually exists, is
  current, and meets the phase-appropriate standard (AACE estimate class,
  systems-thinking maturity, risk quantification, kill criteria). Produces a
  READY / CONDITIONALLY READY / NOT READY assessment with a gap-closure plan.
  Activates on: "gate readiness", "gate review", "stage gate", "FID readiness",
  "are we ready for FID", "assemble the gate pack", "gate evidence pack",
  "decision gate", "investment committee pack", or when a user preparing a
  board, FID, or stage-gate submission asks whether the project can proceed.
allowed-tools: Read Write
metadata:
  version: 1.0.0
  domain: capital project management / stage-gate governance
---

# Gate-Readiness Skill — Stage-Gate Evidence Pack Assembly

## Purpose

Stage gates fail in two ways: projects pass on incomplete evidence (the gate
becomes theatre), or gate preparation consumes weeks of manual document
assembly. This skill addresses both. It audits the project data store against
an explicit, phase-calibrated evidence checklist, assembles what exists into a
single gate readiness report, and names precisely what is missing — so the
approving body sees the state of the evidence, not a narrative about it.

This skill **integrates** the outputs of the other suite skills; it does not
re-perform their analysis. A systems-thinking audit, a P50/P90 estimate, and an
EVM report are inputs here, not products.

## When to Use This Skill

- Before any decision gate: Concept → Pre-FEED, Pre-FEED → FEED, FEED → FID,
  execution re-baseline, or Closeout
- When the user asks "are we ready for FID?" or "what's missing for the gate?"
- When an investment committee, board, or PMO requests a gate submission
- After a systems-thinking audit, to convert closed gaps into a gate pack

## Workflow

### Step 1 — Identify the gate

Determine the target gate from `project-brief.md` (`phase:` field), the user's
request, or by asking once. The gate determines which evidence standard applies.

### Step 2 — Apply the gate evidence matrix

Check the project directory for each required artifact. Rate each item:

- **PRESENT** — artifact exists and meets the stated standard
- **STALE** — artifact exists but is older than 90 days (or predates a major
  scope change) and must be refreshed before the gate
- **SUBSTANDARD** — artifact exists but does not meet the phase requirement
  (e.g. a Class 4 estimate offered at a FEED → FID gate)
- **ABSENT** — artifact does not exist

Required evidence by gate:

| Evidence item | Concept → Pre-FEED | Pre-FEED → FEED | FEED → FID | Re-baseline | Closeout |
|---------------|:---:|:---:|:---:|:---:|:---:|
| Project brief (validated against schema) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Systems-thinking audit, maturity ≥ 2 | ✓ | — | — | — | — |
| Systems-thinking audit, maturity ≥ 3, all flags dispositioned | — | ✓ | ✓ | ✓ | — |
| P50/P90 estimate (`budget-estimator`), Class 5 | ✓ | — | — | — | — |
| P50/P90 estimate, Class 4 | — | ✓ | — | — | — |
| P50/P90 estimate, Class 3 or better | — | — | ✓ | ✓ | — |
| Regulatory map with owners and status | — | ✓ | ✓ | ✓ | — |
| Interface register with named owners | — | — | ✓ | ✓ | — |
| Risk register (schema-valid) with EMV and mitigation owners | — | ✓ | ✓ | ✓ | ✓ |
| Kill criteria explicitly documented | — | ✓ | ✓ | ✓ | — |
| Outside view / reference class comparison | — | — | ✓ | — | — |
| Schedule basis consistent with phase (±50/±30/±15/±10%) | ✓ | ✓ | ✓ | ✓ | — |
| Current EVM report with EAC vs P50/P90 position | — | — | — | ✓ | ✓ |
| Root-cause analysis of baseline deviation | — | — | — | ✓ | — |
| Lessons-learned report and heuristics calibration proposal | — | — | — | — | ✓ |

Adjust the matrix with judgment for project type — e.g. an O&M/ConOps outline
is FID-mandatory for FOAK or operations-heavy projects (SYS-13/SYS-14), and a
social-licence assessment is FID-mandatory where SYS-10 was rated PARTIAL or
ABSENT in the audit. State any matrix adjustments explicitly in the report.

### Step 3 — Read and cross-check the evidence

For artifacts that are PRESENT, do not merely confirm existence:

- Check the systems-thinking audit's open omission flags — any flag still open
  at the gate must appear in the readiness report's conditions
- Check the estimate's AACE class and date against the phase requirement
- Check that P50 ≤ approved budget request ≤ P90; a budget request below P50
  is an automatic finding (the project is asking for less than its central
  estimate)
- At re-baseline and closeout gates, check the EVM report's recommended EAC
  against the estimate's P90

### Step 4 — Assess readiness

- **READY** — all required items PRESENT; no open critical omission flags
- **CONDITIONALLY READY** — at most two items STALE or SUBSTANDARD, each with
  a credible closure action before the gate date; no ABSENT items on the
  critical path of the decision (estimate, regulatory map, kill criteria)
- **NOT READY** — any critical item ABSENT, or more than two items deficient

Never inflate the rating because the gate date is near. Schedule pressure on
the gate is the approving body's trade-off to make, with full information.

### Step 5 — Recommend the closure plan

For every deficient item: the action that closes it, the suite skill or tool
that produces it, a suggested owner role, and a realistic effort estimate.
Recommend (do not auto-invoke) the relevant skills: `systems-thinking` for a
missing or stale audit, `budget-estimator` for a missing or substandard
estimate, `evm` for the current performance position, `lessons-learned` at
closeout gates.

## Output Format

Use this exact structure:

---

## Gate Readiness Assessment: [Project Name] — [Gate]

**Date:** [today]
**Gate:** [e.g. FEED → FID]
**Assessment:** READY / CONDITIONALLY READY / NOT READY

[2–3 sentence summary: the single most important fact the approving body
needs, stated first.]

---

### Evidence Checklist

| # | Evidence item | Required standard | Status | Finding |
|---|---------------|------------------|--------|---------|
| 1 | ... | ... | PRESENT / STALE / SUBSTANDARD / ABSENT | [one sentence] |

---

### Open Omission Flags Carried to This Gate

[Exact flags from the systems-thinking omission vocabulary still open, or
"None — all prior flags closed".]

---

### Conditions and Closure Plan

| Priority | Deficiency | Closing action | Skill / tool | Owner suggestion | Effort |
|----------|-----------|----------------|--------------|------------------|--------|

---

### Recommendation to the Approving Body

[One paragraph. If NOT READY: the minimum evidence set that would change the
assessment, and the realistic time to produce it. If CONDITIONALLY READY: the
conditions that must be attached to approval. No false reassurance.]

---

## Tone and audience

Written for the gate's approving body (investment committee, supervisory
board, PMO). Direct, evidence-led, no advocacy. The report states what is
evidenced, what is not, and what it would take to close the difference — the
go/no-go decision itself belongs to the humans at the gate.

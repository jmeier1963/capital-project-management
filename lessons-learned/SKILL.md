---
name: lessons-learned
description: >
  Close-out review and heuristics calibration for large capital projects.
  Compares final (or to-date) actual costs and schedule against the original
  P50/P90 estimate and baseline, attributes the variance to scope change,
  productivity, and risk events, proposes versioned updates to the
  heuristics/*.yaml benchmark library with full provenance, and produces a
  structured lessons-learned register mapped to the 15 SYS rules. Activates on:
  "lessons learned", "close-out review", "post-project review", "estimate vs
  actual", "calibrate heuristics", "update benchmarks", "how good was our
  estimate", project completion, or major work-package close-out.
allowed-tools: Read Write
metadata:
  version: 1.0.0
  domain: capital project management / close-out and institutional learning
---

# Lessons-Learned Skill — Close-Out Review and Heuristics Calibration

## Purpose

Most organisations pay twice for the same lesson: once on the project that
taught it, and again on the next project that never heard it. The suite's
heuristics library (`heuristics/*.yaml`) is the designated carrier of
institutional knowledge — but it only stays honest if actuals flow back into
it. This skill performs that feedback loop: it measures how the estimate
performed against reality, explains why, proposes calibrated benchmark
updates for human review, and records the transferable lessons in a
standardised, SYS-rule-mapped format.

## When to Use This Skill

- At project completion or final account
- At major work-package close-out (e.g. mainline construction complete) —
  partial calibration is far better than none
- When the user asks "how good was our estimate?", "estimate vs actual",
  "lessons learned", or "update the benchmarks"
- At a Closeout gate (the `gate-readiness` skill requires this report)

## Inputs (gather in this order)

1. The original estimate: `estimate-report.md` and/or the source YAML from the
   `budget-estimator` run that set the budget
2. Final or latest actuals: the EVM time-phased CSV and final EVM report
   (`03-cost/evm-output/`)
3. The change order log (`01-contracts/change-orders/`) — to separate scope
   growth from rate/productivity variance
4. The risk register — to identify which materialised risks drove cost
5. The heuristics applied (`heuristics/*.yaml`) — the benchmarks to calibrate
6. Any prior systems-thinking audit — to test whether flagged gaps materialised

If an input is missing, proceed with what exists and state explicitly which
parts of the analysis are therefore not possible. Partial close-out analysis
on real data beats complete analysis on none.

## Workflow

### Step 1 — Estimate accuracy assessment

Per work package and in total:

- Final actual cost vs P50 and P90 from the original estimate
- Where the actual fell in the simulated distribution (approximate percentile)
- Whether the realised accuracy was within the claimed AACE class band
- Schedule: actual completion vs baseline and vs phase-appropriate band

State the headline plainly, e.g. "Final cost EUR 1,912M — between P50 and P90,
at roughly the P85 of the Class 3 estimate. The estimate class claim held."

### Step 2 — Variance attribution

Decompose total variance (actual − P50) into:

| Component | Source |
|-----------|--------|
| Scope change | Approved change orders, with CO references |
| Rate / productivity variance | EVM CPI history net of scope changes |
| Materialised risks | Risk register entries that converted to cost |
| Escalation / market movement | Price indices vs estimate basis date |
| Unexplained residual | State it honestly — do not force it to zero |

This attribution determines what gets calibrated: scope growth does **not**
discredit a unit-rate benchmark; productivity variance does.

### Step 3 — Heuristics calibration proposal

For each heuristic value the project actually exercised (e.g. EUR/km for DN400
in rolling terrain, welding productivity per shift):

- Compute the realised value from actuals, normalised to the benchmark's basis
  (exclude scope-change effects identified in Step 2)
- Compare with the current library value and state the deviation
- Propose an updated value **only when justified**: one project is one data
  point. Propose a change when the deviation exceeds the benchmark's stated
  accuracy band, or when this confirms a deviation already seen on a prior
  project; otherwise record the data point and propose no change yet

Present the proposal as an explicit YAML diff with a version bump and updated
provenance header (`source:` gains this project's ID and close-out date).
**Never edit the heuristics files directly without the user's confirmation** —
calibration is a reviewed change, not an automatic write.

### Step 4 — Lessons register

Record transferable lessons in this format, appended to
`06-closeout/lessons-learned.md` (create if absent):

| Field | Content |
|-------|---------|
| ID | LL-[project]-[nn] |
| Phase | Where the lesson originated (definition / estimating / execution / closeout) |
| Category | cost / schedule / regulatory / interface / supply chain / stakeholder / technical |
| What happened | 1–2 sentences, specific, with numbers |
| Root cause | The systemic cause, not the proximate trigger |
| SYS rule | Which of SYS-01…15 this maps to, if any |
| Recommendation | What the next project should do differently — actionable, not aspirational |

A lesson without a recommendation that a future project team could act on is
an anecdote; do not record anecdotes.

### Step 5 — Feedback to the audit framework

Answer two questions explicitly:

1. **Did the flagged gaps materialise?** For each omission flag raised in the
   pre-FID systems-thinking audit: did it convert into cost, delay, or scope
   change? This is the audit framework's own calibration evidence.
2. **Did anything material happen that no SYS rule covers?** If yes, describe
   the candidate pattern — this is how the 15-rule framework earns its 16th
   rule, or doesn't.

## Output Format

Use this exact structure:

---

## Close-Out Review: [Project Name]

**Date:** [today]
**Scope of review:** [full project / package(s)]
**Estimate basis:** [AACE class, date, P50/P90]

---

### Estimate Accuracy

[Headline + per-package table: WP | P50 | P90 | Actual | Position in distribution]

### Variance Attribution

[Attribution table + 2–3 sentences on the dominant driver]

### Heuristics Calibration Proposal

[YAML diff blocks with version bump and provenance, or "No calibration
proposed — deviations within stated accuracy bands" with the data points
recorded for future confirmation]

### Lessons Register Entries

[New LL entries in the standard format]

### Audit Framework Feedback

[Flag-by-flag: materialised or not; candidate new patterns if any]

---

## Integration with the Skill Suite

- **`budget-estimator`** — consumes its estimate report as the accuracy
  baseline; the calibrated heuristics improve its next run
- **`evm`** — consumes its final report and CPI history for variance
  attribution
- **`systems-thinking`** — close-out evidence on whether flagged gaps
  materialised feeds the credibility of the next pre-FID audit
- **`gate-readiness`** — this report is required evidence at the Closeout gate

## Tone

Write for the PMO and the next project's estimators, not for the completed
project's defence. The review is about calibration, not blame: a project that
landed at P85 with clean attribution is a successful data point, not a failure
to hit P50.

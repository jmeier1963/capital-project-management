---
name: systems-thinking
description: >
  Audit a project definition, status report, or FID pack for systemic risks and gaps in systems thinking.
  Use this skill whenever a user asks to "check a project for blind spots", "review this project definition",
  "systems thinking audit", "SYS audit", "megaproject risk review", "check for systemic risks",
  "what could go wrong with this project", or shares a project document and wants a structured risk or
  governance review. Also trigger when a project director, PMO lead, or supervisory/advisory board member
  needs to stress-test a project before a major decision gate (FID, stage gate, board approval).
  The skill applies the 15 SYS heuristics derived from mega-project failure research (Crossrail, Olkiluoto 3,
  NHS NPfIT, Longannet CCS, Vogtle, Big Dig, etc.) and produces a board-ready audit report with a maturity
  score, per-rule findings, critical gap ranking, and recommended toolset.
allowed-tools: Read Write
---

# Systems-Thinking Audit Skill

## Purpose

Large projects fail not from single technical faults but from **late-recognised interfaces** — between engineering, regulation, operations, finance, supply chains, and stakeholders. This skill forces a structured examination of those interfaces before they become crises.

The audit is grounded in documented failure patterns from projects like Crossrail (£4bn overrun from late system integration), Olkiluoto 3 (€8bn overrun from FOAK design-maturity gaps), NHS NPfIT (£11bn programme abandoned due to socio-technical misfit), and Longannet CCS (cancelled because full-chain economics were never integrated). See `references/sys-rules.md` for the full research basis.

## Inputs

Accept any of:
- A project definition document (pasted or referenced by path)
- A stage-gate or FID pack summary
- A project status report or board update
- A verbal description the user provides in the conversation

If the user provides a file path, read it. If the description seems thin, ask one focused question to draw out the most important missing dimension before starting the audit — but don't over-interview; a partial description still warrants a partial audit.

## Audit Workflow

### Step 1 — Frame the project

Extract or confirm:
- Project type (infrastructure, IT, energy, mining, defence, other)
- Phase (concept, definition, execution, operations)
- Key stakeholders (sponsor, regulator, EPC, operator, financier)
- Whether this is FOAK (first-of-a-kind) or replication

This context governs which rules are most critical and which are N/A.

### Step 2 — Apply the 15 SYS rules

Read `references/sys-rules.md` for the full rule set with PRESENT / PARTIAL / ABSENT criteria.

For each rule assess:
- **PRESENT** — The project documentation explicitly and credibly addresses this dimension
- **PARTIAL** — The dimension is mentioned but insufficiently developed, or only for part of the system
- **ABSENT** — The dimension is not addressed; this is a gap
- **N/A** — Genuinely not applicable to this project type (explain why)

Be honest and rigorous. "Mentioned in passing" is PARTIAL, not PRESENT.

### Step 3 — Score overall maturity

Assign a **Systems-Thinking Maturity Score** from 1 to 5:

| Score | Meaning |
|-------|---------|
| 1 | Asset-centric definition only; system boundaries not recognised |
| 2 | Some system dimensions addressed but major blindspots remain |
| 3 | Core dimensions covered; notable gaps in 3–5 rules |
| 4 | Solid systems thinking; minor gaps or one significant blind spot |
| 5 | Fully integrated definition; all chains, interfaces, and kill criteria explicit |

Most real projects score 2–3. A score of 4–5 requires strong evidence, not just well-written documents.

### Step 4 — Rank critical gaps

Identify the **3–5 most dangerous gaps** — those most likely to derail the project if unaddressed. Rank them by:
1. Potential cost/schedule impact
2. How late in the project they would typically surface
3. How quickly they could be closed before the next decision gate

### Step 5 — Recommend next actions

Map each critical gap to a concrete tool from the minimal stack:

| Tool | Closes gap in |
|------|--------------|
| Value-Chain Map | SYS-01, SYS-02 |
| Regulatory Map | SYS-03 |
| Design-Maturity Register | SYS-04 |
| Interface Register | SYS-05 |
| Risk-Adjusted Estimate (Monte Carlo) — use the `budget-estimator` skill | SYS-06 |
| Reference Class Forecast | SYS-07 |
| Integration Sub-Project Plan | SYS-08 |
| Supply-Chain Readiness Assessment | SYS-09 |
| Stakeholder Power/Legitimacy Map | SYS-10 |
| Scenario Stress Test | SYS-11 |
| Kill Criteria Register | SYS-12 |
| ConOps / ORAT Plan | SYS-13 |
| FOAK Learning Plan | SYS-14 |
| Portfolio/Platform Review | SYS-15 |

### Step 6 — Check for a prior audit (re-audit tracking)

If a previous systems-thinking audit report exists for this project (in the
project directory or provided by the user), this is a **re-audit**:

- Compare every rule rating against the prior audit and mark movement
  (improved / unchanged / regressed)
- State which omission flags from the prior audit have been **closed**, which
  remain **open**, and whether any new flags have appeared
- Report the maturity score delta explicitly (e.g. "2/5 → 3/5")
- An open flag carried across two consecutive gate reviews is itself a
  governance finding — say so

Add a "Change Since Last Audit" section to the report directly after the
maturity score. If no prior audit exists, omit the section.

## Output Format

Use this exact structure:

---

## Systems-Thinking Audit: [Project Name]

**Date:** [today]
**Audit basis:** [what input was reviewed]
**Project phase:** [phase]

---

### Overall Maturity Score: [N]/5

[2–3 sentence justification. Be direct about what is well-covered and what drives the score down.]

---

### Rule-by-Rule Assessment

| Rule | Title | Rating | Finding | Follow-up Question |
|------|-------|--------|---------|-------------------|
| SYS-01 | Full Value Chain | [PRESENT/PARTIAL/ABSENT/N/A] | [One sentence] | [Concrete question] |
| SYS-02 | 2nd/3rd-Order Effects | ... | ... | ... |
| SYS-03 | Regulatory Map | ... | ... | ... |
| SYS-04 | Design Maturity Threshold | ... | ... | ... |
| SYS-05 | Interface Ownership | ... | ... | ... |
| SYS-06 | Risk-Adjusted Estimate | ... | ... | ... |
| SYS-07 | Outside View | ... | ... | ... |
| SYS-08 | Integration as Own Project | ... | ... | ... |
| SYS-09 | Supply-Chain & Workforce Readiness | ... | ... | ... |
| SYS-10 | Stakeholder System Membership | ... | ... | ... |
| SYS-11 | Business Case Stress Test | ... | ... | ... |
| SYS-12 | Kill Criteria | ... | ... | ... |
| SYS-13 | Operations & Maintenance in Definition | ... | ... | ... |
| SYS-14 | FOAK as Learning Programme | ... | ... | ... |
| SYS-15 | Portfolio/Platform Escalation | ... | ... | ... |

---

### Critical Gaps (ranked)

**Gap 1 — [Label from omission vocabulary]**
[2–3 sentences: what is missing, why it matters, when it typically hurts]

**Gap 2 — ...**
...

**Gap 3 — ...**
...

---

### Recommended Next Actions

| Priority | Action | Tool | Owner suggestion | Effort |
|----------|--------|------|-----------------|--------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

---

### Omission Flags

> ⚠ [Flag any present from this vocabulary — use exactly these labels where applicable:]
> - Full value chain not modelled
> - Regulatory due diligence missing
> - Interface owner unknown
> - Integration proof absent
> - Outside view missing
> - Kill criteria undefined
> - Design maturity not validated
> - Supply-chain readiness untested
> - Business case not stress-tested
> - FOAK not treated as learning programme
> - Stakeholder legitimacy not mapped
> - O&M not in scope of definition

---

## Tone and audience

This audit is for project directors and supervisory/advisory board members. Write:
- Concisely — executives read fast; avoid jargon dumps
- Directly — name the gap, not just that a gap exists
- Constructively — every gap gets a path forward, not just a critique
- Without false reassurance — a score of 2 is a score of 2; say so plainly

## Leveraging other skills

For deeper analysis of specific dimensions, suggest (don't auto-invoke without user confirmation):

**Within this skill suite:**

- **SYS-06 risk-adjusted estimate** → suggest the `budget-estimator` skill to produce the P50/P90 estimate directly; this is the standard remediation for a SYS-06 gap
- **Gate assembly** → once critical gaps are being closed, suggest the `gate-readiness` skill to compile the evidence pack and verify completeness against the gate criteria
- **Post-audit follow-through** → audit artifacts (interface register, regulatory map, kill criteria) become monitored items in the execution-phase data store; the `evm` skill and specialist agents pick them up from there

**Marketplace skills:**

- **SYS-11 scenario stress-testing** → suggest `/what-if-oracle` for structured multi-branch business case scenarios
- **SYS-03 regulatory lookups** → suggest `/perplexity-search` to retrieve current permit requirements, tax rules, or subsidy frameworks
- **SYS-07 reference class research** → suggest `/literature-review` or `/perplexity-search` to find comparable project benchmarks

Only suggest these when the gap is material and the user would benefit from deeper work in that dimension.

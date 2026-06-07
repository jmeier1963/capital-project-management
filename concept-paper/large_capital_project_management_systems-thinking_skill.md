# Systems Thinking in Large Capital Project Management

**Prof. Dr. Johannes Meier**

---

## Executive Summary

Large capital projects fail not because individual components are poorly engineered
but because the couplings between components — regulatory, operational, financial,
social — are modelled too late, if at all. Analysis of fifteen landmark cases
spanning nuclear power stations, rail programmes, carbon capture schemes, hospital
IT, and mining projects reveals five recurring systemic blindspots that precede
virtually every major overrun and cancellation.

This paper introduces `systems-thinking`, a Claude Code skill that operationalises
fifteen research-derived heuristics into a structured audit framework. Applied
before a Final Investment Decision or stage gate, the skill produces a
board-ready report covering all fifteen SYS rules, a maturity score on a
one-to-five scale, a ranked gap list using a standardised omission vocabulary,
and a recommended tool stack for closing identified gaps.

Evaluation against three test scenarios — an offshore wind and green hydrogen
project, a hospital electronic health record transformation, and a first-of-a-kind
lithium hydroxide refinery — shows that outputs produced with the skill pass 100
percent of structured assertions, against 41 percent without it. The skill adds
comparability and completeness: both configurations correctly identify
domain-specific risks, but only the skill-guided outputs apply the same fifteen-rule
framework and standardised vocabulary consistently, making cross-project comparison
tractable.

The paper describes the rationale, the architecture, the evaluation, and the
usage guide for practitioners deploying the skill in project governance.

---

## 1. The Systemic Failure Pattern

### 1.1 Beyond Budget and Schedule

The most widely cited measure of megaproject underperformance is cost overrun.
Flyvbjerg's cross-sectoral database of 16,000 projects established that 91.5 percent
exceed their original budget or schedule targets, and only 0.5 percent deliver all
promised benefits on time and on budget.^1^ McKinsey's analysis of over 300 projects
exceeding USD 1 billion found average cost overruns of 80 percent and schedule delays
of 50 percent.^2^

These figures, while sobering, describe symptoms rather than causes. The deeper
pattern — visible in the best-documented failure cases — is that projects are scoped
as asset construction programmes when their success depends on systems that extend
far beyond the built object. A nuclear power station requires not just reactor
installation but integrated quality assurance, subcontractor oversight, and regulatory
documentation as an indivisible whole. A carbon capture project requires not just
the capture unit but a financeable full-chain economics spanning carbon pricing,
transport tariffs, and storage contracts. A hospital IT programme requires not just
software deployment but clinical workflow integration, trust autonomy, and local
change capability.

When the scope definition omits these dependencies, projects build part of their
failure in from the start.

### 1.2 Fifteen Cases, Five Blindspots

Analysis of fifteen landmark projects — selected because authoritative public
post-mortems exist in sufficient detail to support root-cause attribution — reveals
five recurring systemic blindspots:^3^

**Blindspot 1: Legal-regulatory non-integration.** The Longannet CCS project
in the United Kingdom was cancelled when it became clear that funding caps, the
carbon price floor, and the contract architecture formed an incompatible economic
system that could not be made financeable. The regulatory environment was not a
boundary condition to be managed — it was a structural component of the project's
value thesis, and it was modelled too late. Pascua-Lama in Chile and Argentina
followed the same logic: environmental regulation and indigenous rights were
treated as downstream permitting tasks until court decisions made the project
unbuildable.^4^

**Blindspot 2: Build-before-design-freeze.** Olkiluoto 3, Flamanville 3, Vogtle,
and the Sydney Opera House are four variants of one pattern: political or commercial
pressure for a visible start meets insufficiently mature design, incompletely validated
manufacturing paths, or immature supply chains. The result is not merely rework; it
is a qualitatively different project with newly created dependencies. At Olkiluoto 3,
the design-fabrication-quality assurance loop was not treated as an integrated
system — STUK investigations found that subcontractor control and regulatory
documentation were separated from technical design in a way that made early cost
and schedule estimates unrecoverable.^5^

**Blindspot 3: Late integration economics.** Crossrail and the NHS National
Programme for IT both featured many subsystems that appeared "green" in isolation
while the overall system remained non-operational. For Crossrail, civil works were
mastered years ahead of signalling, station systems, safety assurance, and the
thousands of physical-digital asset interactions that defined operational readiness.
The NAO investigation found that the integration and testing phase had been
systematically planned too small and started too late.^6^ NPfIT collapsed for the
equivalent reason in software: centralised architecture, heterogeneous legacy trust
systems, and clinical workflow diversity were not integrated ends of the same
delivery equation.

**Blindspot 4: Physical-social coupling.** The Hallandsås Tunnel in Sweden took
23 years and cost roughly ten times its original budget. The root cause was not
geological surprise alone — it was that geology, groundwater chemistry, environmental
law, and local legitimacy were treated as separate streams rather than a coupled
physical-legal-social system. Once toxic injection agents entered the groundwater,
the project became politically redefinable in ways that no schedule or cost model
had anticipated. Pascua-Lama replicated this pattern: the project's physical
footprint and its legal footprint diverged irreconcilably.^7^

**Blindspot 5: Governance fragmentation.** The Scottish Parliament Building,
the Big Dig in Boston, and Crossrail each suffered from accountability for scope,
cost, quality, and interfaces being distributed across organisations, contracts,
and political levels in ways that made systemic risk invisible at any single node.
The Holyrood Audit Committee found that brief, design, and procurement stabilised
too late precisely because no single governance structure had authority across
the full system boundary.^8^

These five blindspots are not coincident failures of project management rigour.
They are structurally predictable consequences of defining complex sociotechnical
systems as if they were asset construction projects.

### 1.3 The Upshot for Project Definition

The implication is straightforward but uncomfortable: a project definition that
describes the physical asset without modelling the full system — feedstock, grids,
permits, tax and levy treatment, operating model, supply-chain readiness, social
licence, and exit logic — is not a definition. It is an engineering brief for one
component of a system whose other components have not been described.

The research is explicit on this point: **"The skill must never treat project
definition as asset definition alone."**^9^ This design principle drives every
element of the `systems-thinking` skill.

---

## 2. The Case for a Structured Audit Skill

### 2.1 The Problem with Ad Hoc Review

Experienced project directors, supervisory board members, and independent technical
advisers routinely identify systemic risks in project definitions. The challenge
is that unstructured review is inconsistent, non-comparable, and dependent on
the reviewer's particular experience base. A reviewer whose background is energy
markets may rigorously interrogate pricing assumptions while missing interface
management gaps. One with infrastructure experience may flag integration risks
while overlooking social licence dynamics.

The result is that the quality of a pre-FID systemic review correlates strongly with
the identity of the reviewer, not the characteristics of the project. This makes
governance a function of personnel rather than process — an arrangement that is
difficult to audit, impossible to mandate, and unlikely to scale across a portfolio.

### 2.2 What a Skill Adds

A Claude Code skill packages structured analytical behaviour that is applied
consistently regardless of context. The `systems-thinking` skill does not add domain
knowledge that an experienced reviewer lacks — both the skill-guided and unskilled
configurations of Claude correctly identify that a lithium hydroxide project's
business case depends on lithium prices, or that a Finnish FOAK refinery requires
an environmental permit under the YVA procedure. The skill's value is different:
it guarantees that the same fifteen analytical tests are applied in the same sequence
with the same vocabulary, every time, regardless of project sector.

This has three consequences. First, gaps that fall outside the reviewer's habitual
focus cannot be skipped — the framework forces completion across all fifteen rules.
Second, findings are expressed in a standardised vocabulary, making cross-project
comparison tractable in a way that prose summaries cannot be. Third, the output
format is board-ready by design: a supervisory board member reviewing the report
for a hydrogen project and the report for a hospital IT programme can compare
maturity scores, flag counts, and omission vocabulary across both, without
translating between different analysts' frameworks.

### 2.3 Marketplace Skill Leverage

Three existing Claude Code marketplace skills are integrated as recommended
follow-on tools, matching specific SYS rules to purpose-built capabilities:

| Skill | SYS rule(s) | Use case |
|-------|------------|---------|
| `what-if-oracle` | SYS-11 | Scenario stress test: carbon price ±50%, demand −20%, interest rates +200bp, permit delay +24 months |
| `perplexity-search` | SYS-03 | Regulatory due diligence: jurisdiction-specific permit requirements, levy classifications, subsidy status |
| `literature-review` | SYS-07 | Reference class forecasting: comparable projects, published cost-to-complete distributions, IPA benchmarks |

The skill does not auto-invoke these tools; it flags their applicability in the
recommended next actions section, preserving user control over which follow-on
analyses to commission.

---

## 3. Architecture and Design Principles

### 3.1 Two-File Structure

The skill is implemented as two files:

```
~/.claude/skills/systems-thinking/
+-- SKILL.md              -- workflow, output template, tone guidance
+-- references/
    +-- sys-rules.md      -- detailed criteria for all 15 SYS rules
```

The separation follows the Claude Code progressive disclosure principle: `SKILL.md`
contains the audit workflow and exact output template (under 500 lines), while
`sys-rules.md` is loaded on demand when applying the rules requires deeper criteria.
This keeps the primary skill file within the context budget for all but the most
resource-constrained deployments.

`SKILL.md` carries YAML frontmatter with a description that functions as the
primary triggering mechanism. The description lists the specific phrase contexts
that should activate the skill — "systems thinking audit", "check for systemic
risks", "megaproject risk review", "SYS audit", "what could go wrong with this
project", as well as implicit contexts such as a project director sharing a project
document before a board approval gate.

### 3.2 The Five-Step Audit Workflow

The skill applies a defined five-step process:

1. **Frame the project** — establish type, phase, sector, decision gate, and
   information provided. Identify which of the fifteen rules are most likely
   to surface material gaps given the project characteristics.

2. **Apply all fifteen SYS rules** — rate each rule PRESENT, PARTIAL, or ABSENT
   based on the evidence provided. For PARTIAL and ABSENT ratings, write a finding
   that names the specific gap and its systemic consequence.

3. **Score the maturity level** — assign an overall maturity score on the 1–5 scale
   (see Section 3.5), calibrated to the distribution of PRESENT, PARTIAL, and ABSENT
   ratings and the severity of the highest-priority gaps.

4. **Rank critical gaps** — select the three to five gaps posing the greatest
   systemic risk, ordered by the combination of impact severity and reversibility.
   A gap that is remediable at pre-FID cost but catastrophic if discovered post-FID
   ranks above a gap that is material but discoverable and correctable during execution.

5. **Recommend next actions** — map gaps to tools from the minimal stack (see
   Section 3.4) and to the three integrated marketplace skills, producing a
   prioritised action table with owner, output, and timeframe.

### 3.3 The Fifteen SYS Rules

The fifteen rules are derived directly from the failure patterns in the fifteen
case studies. Each rule addresses a recurring failure class, states its rationale
in one sentence, and specifies the PRESENT, PARTIAL, and ABSENT criteria that
allow consistent rating across reviewers and projects. Appendix A contains the
full table; the rules are:

| Rule | Short title | Core failure addressed |
|------|------------|----------------------|
| SYS-01 | Full value chain | Missing upstream/downstream dependencies |
| SYS-02 | Second and third-order effects | Indirect systemic consequences |
| SYS-03 | Regulatory map before FID | Late legal and levy discoveries |
| SYS-04 | Design-maturity threshold | Build-before-design-freeze |
| SYS-05 | Interface ownership and evidence | Unmanaged system interfaces |
| SYS-06 | Risk-adjusted estimate | False certainty in point budgets |
| SYS-07 | Outside view first | Systematic optimism bias |
| SYS-08 | Integration as its own megaproject | Late and under-resourced integration |
| SYS-09 | Supply-chain and workforce readiness | FOAK supply-chain brittleness |
| SYS-10 | Stakeholders as system components | Social licence as project risk |
| SYS-11 | Business case stress test | Fragile economics under policy/price scenarios |
| SYS-12 | Explicit kill criteria | Sunk-cost traps in prestige projects |
| SYS-13 | Operations and maintenance in definition | ORAT and handover gaps |
| SYS-14 | FOAK as learning programme | First-of-a-kind treated as serial production |
| SYS-15 | Cluster and platform level | Sub-optimal standalone asset solutions |

The rules are not a checklist to be completed mechanically. They constitute a
system: SYS-04 (design maturity) and SYS-09 (supply-chain readiness) compound in
FOAK programmes, as Olkiluoto 3 and Vogtle showed. SYS-03 (regulatory map) and
SYS-11 (business case stress test) compound in market-dependent projects such as
CCS or energy storage, where the regulatory framework directly determines the
economics. Reviewers are instructed to identify and surface these compounding
interactions, not just score each rule in isolation.

### 3.4 The Minimal Tool Stack

The research identifies a minimal stack adequate for early project definition
review. The skill maps each stack element to its corresponding SYS rules:

| Tool | SYS rules | What it delivers |
|------|----------|-----------------|
| Value-Chain Map | SYS-01, SYS-02 | End-to-end dependency visibility |
| Regulatory Map | SYS-03 | Permits, levies, liability, subsidies, tax treatment |
| Interface Register | SYS-05 | Interface ownership and maturity evidence |
| ConOps / Operating Model | SYS-13 | Day-in-the-life operational scenario |
| Scenario Stress Test | SYS-11 | Business case at policy and price extremes |
| Monte Carlo Cost/Schedule | SYS-06 | P50/P80/P90 risk-adjusted estimates |
| Reference Class Forecast | SYS-07 | Outside view on cost and schedule |
| Supply-Chain Readiness Assessment | SYS-09 | Top-10 supplier and craft labour gaps |
| Independent Red Team / Gate Challenge | SYS-12 | External counter-review with kill criteria |

### 3.5 Maturity Scoring

The maturity score aggregates the rule ratings into a single governance-facing
signal:

| Score | Description | Typical profile |
|-------|------------|----------------|
| 1 | Asset-centric only | Full chain absent; no regulatory map; interfaces undefined; integration not planned |
| 2 | Partial chain with major gaps | Chain sketched but incomplete; PARTIAL on most rules; at least one ABSENT on critical rules (SYS-03, SYS-06, SYS-07) |
| 3 | Structured approach, incomplete evidence | Framework present; key elements PARTIAL; integration and ORAT underweighted |
| 4 | Mature definition with minor gaps | Most rules PRESENT; remaining PARTIAL items are manageable; outside view applied |
| 5 | Fully integrated systems perspective | All rules PRESENT; chain, interfaces, regulation, operations, and exit logic complete |

Most real projects reviewed to date score 2–3. A score of 4 or above at pre-FID
is exceptional and merits verification that it reflects genuine evidence rather
than optimism.

### 3.6 The Omission Vocabulary

Twelve standardised omission flags are embedded in the output template. Their
purpose is to make gap identification directly comparable across projects and
reviewers, replacing ad hoc language with a controlled vocabulary:

1. Full value chain not modelled
2. Regulatory due diligence missing
3. Interface owner unknown
4. Integration proof absent
5. Outside view missing
6. Kill criteria undefined
7. Design maturity not validated
8. Supply-chain readiness untested
9. Business case not stress-tested
10. FOAK not treated as learning programme
11. Stakeholder legitimacy not mapped
12. O&M not in scope of definition

Where a flag applies, the skill is instructed to use the exact phrase — not a
paraphrase — in the Omission Flags section of the report. This enables automated
screening of audit outputs across a project portfolio and makes it straightforward
to track whether identified gaps are resolved at subsequent gate reviews.

---

## 4. Evaluation Approach and Results

### 4.1 Methodology

The skill was evaluated using the `skill-creator` framework, which runs parallel
Claude Code agent instances — one with the skill loaded, one without — against
the same test prompts, then grades outputs against structured assertions.

Three test scenarios were designed to cover different project types, decision
gates, and audience profiles. For each scenario, both configurations produced
a full audit report. The reports were graded against assertions verifiable from
the text. Timing and token data were recorded at completion.

The evaluation measures what the skill adds relative to an unaided capable Claude
model, not the absolute quality of either output.

### 4.2 Test Scenarios

**Scenario 1: Offshore Wind and Green Hydrogen, Norwegian Continental Shelf (pre-FID)**

A 500 MW offshore wind installation combined with a hydrogen electrolysis facility,
targeting green hydrogen export via a proposed TSO pipeline network. The scenario
provides a project brief including installed capacity targets and high-level CAPEX
figures. The decision gate is FID; the audience is the project steering committee.

The systemic risks in this scenario include an unmodelled hydrogen export chain
(SYS-01), early-stage TSO pipeline planning (SYS-03), and a business case that has
not been stress-tested against carbon price and demand fluctuations (SYS-11).

**Scenario 2: Hospital Electronic Health Record Transformation, Germany (supervisory board update)**

A €340 million EHR transformation programme spanning eight German hospitals,
with Phase 1 declared complete but Phase 2 — clinical integration and workflow
adoption — not started. The scenario provides a programme update presented to
the supervisory board.

The systemic risks in this scenario include the critical distinction between
software installation and clinical integration (SYS-08), undefined criteria for
continuation or termination given sunk costs (SYS-12), and an operating model
that has not been validated in clinical workflow terms (SYS-13).

**Scenario 3: FOAK Lithium Hydroxide Refinery, Finland (PMO stage-gate)**

A €1.1 billion first-of-a-kind LiOH refinery project based on Australian spodumene
feedstock, projecting an 18% IRR at prevailing lithium prices. The scenario provides
a stage-gate pack for a PMO review. The project has not yet obtained Finnish
environmental permits.

The systemic risks in this scenario include an unverified IRR in a commodity market
that lost 80% of its value over 24 months (SYS-11), missing YVA environmental
permit in Finland (SYS-03), FOAK technology risk treated as a standard EPC delivery
problem (SYS-14), and a single-source spodumene feedstock from one Australian mine
(SYS-09).

### 4.3 Assertions

Assertions were designed to test structural and vocabulary compliance, not domain
knowledge. Domain-knowledge assertions — "does the output identify the hydrogen
pipeline gap?" — were expected to pass in both configurations, because an unaided
Claude model has adequate knowledge of hydrogen value chains, Finnish permitting
law, and lithium market dynamics. The discriminating assertions test whether the
skill-mandated framework is applied:

- **contains_maturity_score** — output contains an explicit X/5 score
- **covers_all_15_rules** — output contains SYS-01 through SYS-15 with ratings
- **uses_rating_vocabulary** — PRESENT / PARTIAL / ABSENT used throughout
- **uses_omission_vocabulary** — at least one exact omission flag from the twelve-item vocabulary
- **identifies_critical_gaps** — ranked gap section with at least three gaps
- **recommends_tool_stack** — specific named tools recommended in next actions

Domain-specific assertions varied by scenario: `flags_hydrogen_pipeline_gap`,
`flags_integration_gap`, `flags_kill_criteria`, `flags_foak_risk`,
`flags_permit_gap`, `flags_business_case_stress`.

### 4.4 Results

| Configuration | Pass rate | Mean time | Mean tokens |
|--------------|-----------|-----------|-------------|
| With skill | **100%** | 190.6 s | 26,805 |
| Without skill | 41% | 335.1 s | 24,586 |
| Delta | **+59 pp** | −144.5 s | +2,219 |

The 59-percentage-point pass rate delta is driven entirely by the structural and
vocabulary assertions. Without the skill:

- Scenario 1 invented an eight-dimensional framework; no SYS-01 to SYS-15 labels
  appeared; omission vocabulary was absent; the tool-stack recommendation was generic
- Scenario 2 used eight "systems thinking" dimensions (stocks, flows, feedback loops);
  integration was discussed but the installed-vs-integrated distinction was not
  named with the skill's vocabulary; kill criteria were addressed only in general terms
- Scenario 3 used ten categorical dimensions with CRITICAL/HIGH/MEDIUM severity
  ratings; FOAK risk was discussed without SYS-14; no exact omission flags appeared

In all three scenarios, the without-skill output correctly identified the material
domain risks. The score penalty was structural, not substantive. This is precisely
the value proposition: the skill does not supply knowledge that an experienced
reviewer lacks. It supplies the framework that makes outputs comparable, complete,
and auditable.

The with-skill outputs were also faster by an average of 144.5 seconds. The
structured fifteen-rule framework reduced decision overhead: instead of constructing
an analytical framework de novo, the agent applied a defined one. The small token
premium (+2,219) reflects the additional structure loaded from the skill file.

### 4.5 Strongly and Weakly Discriminating Assertions

A post-hoc analysis of assertion behaviour identified two categories:

**Strongly discriminating (skill 100%, baseline 0%):** All structural and vocabulary
assertions — `covers_all_15_rules`, `uses_rating_vocabulary`, `uses_omission_vocabulary`,
`recommends_tool_stack`. These assertions fail in every without-skill run because the
unaided model invents a different framework each time.

**Non-discriminating (both pass):** Domain-knowledge assertions — whether the output
identifies the hydrogen pipeline gap, the Finnish permit requirement, the 18% IRR
stress-test problem, the spodumene supply-chain risk. Both configurations pass these
in all three scenarios. The conclusion is confirmed: the skill does not supply
domain knowledge; it supplies structural discipline.

---

## 5. Usage Guide

### 5.1 Installing the Skill

The skill is distributed as a `.skill` package file. Installation requires one
command:

```bash
# From the skill-creator directory
python3 -m scripts.package_skill /path/to/systems-thinking

# To install, place the unpacked skill in the skills directory
cp -r systems-thinking ~/.claude/skills/
```

After installation, Claude Code discovers the skill at startup. No configuration
is required.

### 5.2 Invoking the Skill

The skill triggers on any of the following phrase patterns:

- `"audit this project for systemic risks"`
- `"systems thinking audit"` or `"SYS audit"`
- `"check this project definition for blind spots"`
- `"megaproject risk review"`
- `"what could go wrong with this project?"`
- `"review this FID pack / stage-gate document / project update"`
- Sharing a project document and asking for a governance or risk review before a
  board, steering committee, or stage-gate

The skill also triggers when context suggests a project director, PMO lead,
or supervisory board member is stress-testing a project before a major decision.
No exact trigger phrase is required; the description is written to trigger on
intent, not keywords.

### 5.3 What Input to Provide

The skill can work from any project documentation available. The richer the input,
the more specific the findings. Useful inputs include:

- **Project brief or definition** — scope, CAPEX, timeline, technology, location,
  decision gate
- **Business case or investment paper** — financial model, IRR assumptions, market
  context
- **Programme update or status report** — progress against plan, issues log, next
  milestones
- **FID or stage-gate pack** — technical feasibility, regulatory status, contracting
  strategy, risk register

Where specific information is unavailable, the skill rates the relevant rule ABSENT
and flags the omission. Absence of evidence is itself a finding: if the regulatory
map has not been produced, the project does not have a regulatory map, and SYS-03
is ABSENT regardless of whether the regulatory risk is subsequently manageable.

### 5.4 Reading the Output

The audit report has a defined structure:

```
## Project Overview
[Project name, type, phase, decision gate, audience]

## Overall Maturity Score: X/5
[One-sentence characterisation of the maturity level]

## SYS Rule Assessment

| Rule | Rating | Finding |
|------|--------|---------|
| SYS-01 | PRESENT / PARTIAL / ABSENT | [Specific finding or confirmation] |
...

## Critical Gaps (ranked)
[Top 3–5 gaps, ordered by systemic impact and reversibility, with brief rationale]

## Recommended Next Actions
[Table of gap → tool → owner → output → timeframe]

## Omission Flags
[Exact flags from the twelve-item vocabulary that apply to this project]

## Board Guidance Note
[Optional: plain-language summary for a non-technical board audience]
```

The overall maturity score is the governance-facing signal: it summarises the
distribution of PRESENT, PARTIAL, and ABSENT ratings into a single comparable
metric. The critical gaps section is the action-facing signal: it tells the project
team where to direct effort before the next decision gate. The omission flags are
the audit-facing signal: they produce a machine-readable list that can be tracked
across gate reviews to verify closure.

### 5.5 Follow-On Tool Stack

After an initial audit, three follow-on workflows are most commonly indicated:

**Scenario stress test (when SYS-11 or SYS-12 is ABSENT or PARTIAL):**
The `what-if-oracle` skill takes the business case as input and runs structured
sensitivity analysis: carbon price at +50% and −50%, demand at −20%, interest
rates at +200 basis points, permit delay at +24 months. The output identifies
which combinations breach the kill threshold, which provides the board with a
concrete answer to "how fragile is the economics?"

**Regulatory due diligence (when SYS-03 is ABSENT or PARTIAL):**
The `perplexity-search` skill retrieves current permit requirements, levy
classifications, and subsidy status for the project's jurisdiction. This is
particularly valuable for cross-border projects and sectors with rapidly changing
regulatory frameworks (CCS transport and storage, offshore hydrogen, critical
minerals processing).

**Reference class forecasting (when SYS-07 is ABSENT or PARTIAL):**
The `literature-review` skill retrieves published cost and schedule outcomes for
comparable projects, enabling an outside-view correction to the current estimate.
It covers GAO's cost estimating benchmarks, IPA's sector databases, NAO's
over-optimism analysis, and DOE's FOAK lessons-learned series.

These three tools address the three assertions most commonly found ABSENT or PARTIAL
in initial audits. Applying them in sequence converts a "maturity 2" project
definition into a defensible stage-gate submission.

---

## Appendix A — The Fifteen SYS Rules

| Rule ID | Short Rule | Rationale | PRESENT criteria | PARTIAL criteria | ABSENT criteria |
|---------|-----------|-----------|-----------------|-----------------|----------------|
| SYS-01 | Full value chain mapped | Many failures occur outside the built object | Chain from feedstock/input to operations, maintenance, and exit is documented and owned | Chain sketched but missing upstream, downstream, or exit logic | Only the physical asset is described |
| SYS-02 | Second and third-order effects | Systemic damage arrives indirectly | Indirect effects on grid, operations, tax, permitting, neighbours, and maintenance have been assessed | Some secondary effects identified; no systematic coverage | Effects assessed only at first order |
| SYS-03 | Regulatory map before FID | Late legal and levy findings destroy business cases | All permits, classifications, levies, subsidies, and liabilities documented with status and timeline | Key regulatory elements listed; no jurisdiction analysis or timeline | Regulatory environment not mapped |
| SYS-04 | Design-maturity threshold before commitment | Build-before-design-freeze is the core overrun pattern | Open design points inventoried; design-freeze criteria defined; manufacturing/construction commitment conditional on maturity threshold | Design maturity acknowledged; no formal threshold or open-point register | Construction or supply-chain commitment pre-dates design freeze |
| SYS-05 | Interface ownership and evidence | Unmanaged interfaces become the critical path late | Interface register exists; every critical interface has a named owner and a defined maturity evidence requirement | Key interfaces listed; ownership partial or informal; no maturity evidence | Interfaces not identified; no register |
| SYS-06 | Risk-adjusted estimate alongside point estimate | Point budgets create false certainty | P50 and P80 or P90 estimates with Monte Carlo or equivalent; contingency sized to spread, not percentage | Range estimates produced but without simulation or explicit drivers | Single-point estimate only |
| SYS-07 | Outside view before sponsor view | Internal teams systematically underestimate | Reference class applied; optimism-bias uplift calculated; estimate compared to comparable projects | Reference class mentioned; no calibration or uplift applied | No outside view; estimate based on internal assumptions only |
| SYS-08 | Integration modelled as its own megaproject | Integration planned too late and too small | Integration and test phase has its own plan, budget, team, and operational-readiness evidence steps | Integration acknowledged; plan exists but is underweighted relative to civil/engineering spend | Integration phase not separately planned |
| SYS-09 | Supply-chain and workforce readiness | Immature supply chain is a system risk, not a procurement risk | Top-10 suppliers or critical trades assessed for single-point-of-failure; QA maturity and capacity confirmed | Key suppliers identified; no formal readiness assessment | Supply-chain risk treated as procurement task only |
| SYS-10 | Stakeholders as system components | Social licence failure tips projects into legal or political paths | Stakeholder map includes who can delay, how, and from when; engagement strategy exists with legitimacy assessment | Stakeholder map sketched; no consequence modelling | Stakeholders listed as communications targets only |
| SYS-11 | Business case stress-tested under policy and price scenarios | Fragile economics do not survive real market paths | Scenario matrix covers commodity price, demand, policy, and rate shocks; business case viable at P20 conditions | Sensitivity analysis performed; no combined or downside scenario | Business case modelled at single base case |
| SYS-12 | Kill criteria explicitly defined | Without exit criteria, sunk costs drive continuation | Three or more specific findings that trigger scope change, resequencing, or project termination are documented | Kill concept acknowledged; criteria vague or aspirational | No kill criteria; project defined as unconditional commitment |
| SYS-13 | Operations and maintenance in scope of definition | ORAT and handover gaps discovered only at commissioning | Operating model, O&M cost basis, data hand-over requirements, and ORAT steps are within the project definition scope | O&M mentioned; no operating model or ORAT plan | O&M treated as a post-FID problem |
| SYS-14 | FOAK treated as learning programme | First-of-a-kind projects mismanaged as if they were serial delivery | FOAK-specific assumptions documented; reserves sized for learning curve; knowledge-capture programme defined | FOAK risk acknowledged; reserves not differentiated from NOAK contingency | FOAK project scoped, costed, and contracted as if it were a repeat project |
| SYS-15 | Cluster and platform questions escalated to portfolio level | Single-project optimisation produces sub-optimal network solutions | Project is explicitly positioned within a platform or cluster strategy; network effects modelled | Portfolio context acknowledged; no formal platform analysis | Project treated as a standalone asset regardless of network dependencies |

---

## Appendix B — Omission Vocabulary

The twelve standardised flags are used verbatim in all audit outputs. Their purpose
is to produce a machine-readable, comparable signal across projects and gate reviews:

| Flag | Triggered when |
|------|---------------|
| Full value chain not modelled | SYS-01 ABSENT or PARTIAL |
| Regulatory due diligence missing | SYS-03 ABSENT |
| Interface owner unknown | SYS-05 ABSENT or PARTIAL (no named owner) |
| Integration proof absent | SYS-08 ABSENT |
| Outside view missing | SYS-07 ABSENT |
| Kill criteria undefined | SYS-12 ABSENT |
| Design maturity not validated | SYS-04 ABSENT |
| Supply-chain readiness untested | SYS-09 ABSENT |
| Business case not stress-tested | SYS-11 ABSENT |
| FOAK not treated as learning programme | SYS-14 ABSENT (FOAK projects only) |
| Stakeholder legitimacy not mapped | SYS-10 ABSENT |
| O&M not in scope of definition | SYS-13 ABSENT |

---

## Appendix C — Evaluation Benchmark Detail

| Eval | Configuration | Pass rate | Passes / Total | Time (s) | Tokens |
|------|--------------|-----------|----------------|----------|--------|
| Offshore wind + hydrogen | With skill | 100% | 8/8 | 181.0 | 26,768 |
| Offshore wind + hydrogen | Without skill | 38% | 3/8 | 447.9 | 30,026 |
| Hospital EHR transformation | With skill | 100% | 7/7 | 178.7 | 26,610 |
| Hospital EHR transformation | Without skill | 43% | 3/7 | 267.9 | 21,559 |
| FOAK lithium refinery | With skill | 100% | 7/7 | 212.2 | 27,038 |
| FOAK lithium refinery | Without skill | 43% | 3/7 | 289.4 | 22,172 |
| **Aggregate with skill** | | **100%** | **22/22** | **190.6** | **26,805** |
| **Aggregate without skill** | | **41%** | **9/22** | **335.1** | **24,586** |

---

## References

1. Flyvbjerg, B. & Gardner, D. (2023). *How Big Things Get Done*. Macmillan.
   Database of 16,000 projects; 8.5% delivered on cost and schedule; 0.5%
   delivered all promised benefits.

2. McKinsey & Company (2015). "Megaprojects: The good, the bad, and the better."
   Review of 300+ projects exceeding USD 1 billion. Average 80% cost overrun, 50%
   schedule delay.

3. Case studies and root-cause analysis drawn from: NAO, *Crossrail: a progress
   update* (2019); NAO, *Carbon capture and storage: lessons from the competition*
   (2017); PAC/NAO, *National Programme for IT in the NHS* (2011); STUK, *Summary
   Investigation Report on Olkiluoto 3* (2007); ASN / Cour des comptes reports on
   Flamanville 3 (2019–2024); DOE lessons learned on Vogtle/AP1000 (2022); National
   Academies / FHWA, Big Dig case studies (2003); Scottish Parliament Audit Committee,
   *Holyrood: The Management of the Holyrood Building Project* (2004); Rio Tinto, Oyu
   Tolgoi Underground Project updates (2021–2022); Trafikverket-related reports on
   Hallandsås (2015); Barrick Gold annual reports and Reuters coverage of Pascua-Lama
   (2012–2018); Gassnova/TCM reports on Mongstad CCS (2013).

4. NAO. (2017). *Carbon capture and storage: lessons from the competition*.
   London: National Audit Office. Primary source for Longannet full-chain
   economics and funding architecture failure.

5. STUK. (2007). *Summary Investigation Report: Olkiluoto 3*. Finnish Radiation
   and Nuclear Safety Authority. Design maturity, subcontractor control, and
   quality assurance findings.

6. NAO. (2019). *Crossrail: a progress update*. HC 2004, 2017–2019. London:
   National Audit Office. Integration planning, ORAT, and safety assurance
   underestimation findings.

7. Trafikverket-related documentation on Hallandsås Tunnel (1992–2015);
   Barrick Gold. (2012). Annual Report and investor presentations on Pascua-Lama.

8. Scottish Parliament Audit Committee. (2004). *Holyrood: The Management of
   the Holyrood Building Project*. Edinburgh: Scottish Parliament. Governance
   fragmentation and accountability diffusion findings.

9. Meier, J. (2026). *Systems Thinking in Large-Scale Projects: Research Report*.
   Unpublished research report. Internal reference for the research basis of the
   skill design. (See `concept-paper/references/systems-thinking-research-report-en.md`.)

10. GAO. (2020). *Cost Estimating and Assessment Guide*. GAO-20-195G. Washington:
    Government Accountability Office. Monte Carlo, reference class, and estimate
    quality methodology.

11. NAO. (2013). *Over-optimism in government projects*. London: National Audit
    Office. Systematic optimism-bias evidence and outside-view correction rationale.

12. Flyvbjerg, B. (2017). "The Iron Law of Megaprojects." *Cato Institute Policy
    Report*. 91.5% of projects exceed original cost, schedule, or both.

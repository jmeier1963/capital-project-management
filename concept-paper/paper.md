# AI-Augmented Project Controls for Large Capital Projects

**Date:** June 2026

---

## Executive Summary

Large capital projects systematically underperform. Across a database of 16,000
projects, Oxford University researchers found that only 8.5 percent met their
original cost and schedule targets — and a mere 0.5 percent delivered all
promised benefits on time and on budget.[^1] McKinsey's analysis of more than
300 projects exceeding one billion dollars in value found average cost overruns
of 80 percent and schedule delays of 50 percent.[^2] These are not outlier
statistics; they describe the norm.

The root cause is not a shortage of engineering talent or project management
methodology. It is an information problem: project controls data is generated
too slowly, integrated too rarely, and interpreted too inconsistently for
management to act before damage accumulates.

This paper proposes a practical, deployable response: a structured AI
scaffolding system built on top of Claude Code — Anthropic's enterprise AI
agent — that converts raw project data into structured cost performance
analysis, escalation-ready reports, and visual dashboards in minutes rather
than days. The system is not a replacement for experienced project professionals.
It is a force multiplier: it ensures that earned value calculations are performed
consistently every reporting period, that escalation thresholds are enforced
automatically, and that domain heuristics from decades of benchmarking are
applied without relying on institutional memory.

The system has been designed, implemented, and tested on a hypothetical 500 km
hydrogen transmission pipeline (EUR 1.75 billion CAPEX). It is available as
open-source code at
[github.com/jmeier1963/large_capital_project_management](https://github.com/jmeier1963/large_capital_project_management).

This paper asks the board to authorize a pilot on one live capital project,
to assign a senior executive as accountable owner, and to commission a data
governance policy that defines which project data is permissible to process
through AI systems and under what conditions.

---

## 1. The Capital Project Performance Crisis and the AI Opportunity

### 1.1 The Scale of the Problem

Flyvbjerg's landmark study — the largest empirical analysis of project
performance ever conducted — established what he calls the "iron law of
megaprojects": over budget, over time, over and over again.[^3] The headline
numbers bear repeating:

- **91.5%** of projects exceed their original budget or schedule, or both
- **8.5%** deliver within original parameters
- **0.5%** deliver cost, schedule, *and* promised benefits

McKinsey adds sectoral granularity. Rail projects overrun by an average of 45
percent. Bridges and tunnels by 35 percent. Mining and metals projects — among
the most capital-intensive category — see 83 percent of major projects exceed
planned CAPEX by more than 40 percent, with average delays of 20 to 30
months.[^4]

The energy transition amplifies the stakes. The Hydrogen Council and McKinsey
reported in 2025 that the global hydrogen sector has now committed over USD 110
billion across more than 500 projects past Final Investment Decision.[^5] These
are projects where schedule delays translate directly into stranded capital,
missed carbon commitments, and competitive disadvantage in a market where
first-mover timing is commercially decisive.

### 1.2 Why Projects Fail: The Information Gap

The intuition that projects fail because of poor engineering or inadequate
planning is only partially correct. McKinsey's analysis of 48 deeply troubled
megaprojects found that **73 percent of cost and schedule overruns were caused
by poor execution** — specifically, by failures of monitoring, escalation, and
corrective action — not by flawed original designs.[^6]

The mechanism is predictable. Project data — cost actuals, schedule progress,
change orders, risk events — is generated continuously in the field. But in most
organisations, this data travels slowly: from site time-sheets and contractor
invoices into cost control systems, then into spreadsheets maintained by cost
engineers, then into narrative reports assembled for management review. By the
time a negative trend is visible in a board report, the underlying pattern may
have been developing for three or four months.

The consequence is that corrective actions are taken late, when the cost of
recovery is high. A schedule slip that costs EUR 2 million to correct in month
three may cost EUR 20 million by month nine — not because the underlying problem
grew tenfold, but because the window for low-cost intervention closed.

### 1.3 The Project Controls Baseline Problem

Consistent, rigorous project controls — earned value management (EVM),
integrated schedule analysis, systematic risk quantification — are the
established antidote. The Independent Project Analysis Group (IPA), whose
proprietary database covers more than 20,000 capital projects, measures project
performance against a Project Control Index (PCI). Projects with strong project
controls consistently outperform their peers on cost, schedule, and operability
outcomes.[^7]

The barrier to universal adoption of rigorous project controls is not lack of
awareness. It is capacity and consistency. A cost engineer maintaining full
earned value analysis across eight WBS packages, three active contracts, and
five reporting periods simultaneously — while also managing contractor queries,
validating invoices, and preparing the monthly report — will, under pressure,
abbreviate the analysis. Thresholds will not be checked. EAC forecasts will not
be run across all three methods. The escalation that should have gone to the
Project Director this week will go next week instead.

This is the specific gap that AI-augmented project controls addresses.

### 1.4 What Has Changed: The AI Inflection Point

For most of the past decade, AI in project management meant dashboards that
required extensive data pipeline engineering, natural language processing tools
that extracted text with limited accuracy, and predictive models that required
months of proprietary training data before producing actionable output. The
technology was real but the deployment cost was prohibitive for all but the
largest programmes.

The shift since 2023 is qualitative, not incremental. Large language models
(LLMs) — in particular, AI agents that reason over structured data, apply
domain-specific rules, call tools, and generate structured outputs — have changed
what is achievable without bespoke development.

Three capabilities now combine in a way that was not previously available:

**Structured reasoning over domain rules.** An AI agent can be given a plain-
English rules file (e.g., "if CPI drops below 0.85, generate a Project Director
escalation memo; if SPI has been below 0.85 for two consecutive periods, issue a
mandatory written notice") and will apply those rules with perfect consistency on
every run. The rules are not remembered from a training corpus — they are encoded
explicitly and executed deterministically.

**Tool use and computation.** Modern AI agents can invoke Python scripts, read
CSV files, write structured output, and generate charts as a native part of their
workflow. The EVM module in this system runs a Python engine (ANSI/EIA-748
compliant, 713 lines) that computes ten financial metrics per WBS package, runs
three EAC forecast methods, produces five publication-ready charts, and writes a
complete markdown report — all as a single AI-orchestrated pipeline.

**Domain heuristics without domain re-training.** Parametric cost benchmarks,
productivity norms, and contingency ranges can be loaded into the AI's context
at runtime as versioned YAML files, without fine-tuning or model retraining.
When the AI applies a benchmark, it cites the source and version. When project
data falls outside the benchmark's valid range, it flags this explicitly. The
heuristics library is updated as the organisation accumulates actuals — turning
project experience into institutional knowledge that the AI accesses on the
next run.

This is not a claim that AI understands project management in the way an
experienced cost engineer does. It is a more precise and more practically
important claim: AI can perform the *routine, structured, rule-governed portion*
of project controls work with perfect consistency, freeing skilled professionals
to focus on the *judgment-intensive* portions — contractor negotiation, root
cause analysis, recovery planning — where human expertise is irreplaceable.

**Avoiding the enterprise AI trap.** Deloitte's 2025–2026 State of AI survey
found that while nearly 90 percent of companies have deployed AI in at least one
business function, 94 percent report not seeing significant value from their
investments.[^8] The explanation is structural: most AI deployments target
individual productivity (drafting emails, summarising documents) rather than the
*process* level where value is concentrated.

In capital project controls, value is concentrated in process consistency, not
individual productivity. The question is not whether a cost engineer can produce
a report faster with AI assistance. The question is whether every project —
regardless of the experience level of its controls team, regardless of whether
it is month four or month thirty-two — produces a complete, consistently
structured, threshold-checked EVM report on time, every reporting period.

The approach described in this paper embeds AI into the process as a
non-optional execution step, with encoded domain rules, parameterised thresholds,
and mandatory output formats that cannot be abbreviated under pressure.

---

## 2. The System: Architecture and Capabilities

### 2.1 Design Principles

The system is built on four principles that distinguish it from generic AI
implementations:

**Data first, conversation second.** Project intelligence is derived from
structured data — CSV files, YAML configuration, JSON schemas — not from
narratives or slide decks. This makes outputs reproducible, auditable, and
comparable across periods.

**Provenance on every heuristic.** Cost benchmarks, productivity norms, and
contingency ranges are stored as versioned YAML files with mandatory `source:`
and `valid_range:` fields. When the AI applies a benchmark, it cites the source.
When the project falls outside the valid range, it flags this explicitly.

**Rules encoded, not remembered.** Escalation thresholds, required approvals,
and judgment rules are encoded in a `CLAUDE.md` configuration file — the
project's AI constitution. They are applied automatically on every analysis run,
not recalled from a briefing document.

**Roles, not generics.** Every communication or action recommendation produced
by the AI addresses a specific named role from the project's organisation chart.
It does not recommend that "the team" should act. It specifies that the
Commercial Manager should review the change order, that the Project Director
should receive the escalation memo, and that the cost register should be updated
by the Cost Engineer within five business days.

### 2.2 System Components

The system consists of five integrated layers.

---

**Layer 1 — Project Data Store**

A structured directory of CSV, YAML, JSON, and Markdown files representing the
project's living state. The recommended directory layout mirrors standard project
controls practice:

```
my-project/
├── CLAUDE.md                    ← project AI constitution
├── project-brief.md             ← scope, FID CAPEX, key milestones
├── 01-contracts/
│   ├── contracts-register.csv
│   └── change-orders/
├── 02-schedule/
│   └── milestones.csv           ← milestone_id, planned_date, forecast_date, critical_path
├── 03-cost/
│   ├── evm-timephased.csv       ← one row per WBS element per reporting period
│   └── evm-output/              ← written by the EVM skill each period
├── 04-resources/
│   └── resource-matrix.csv
└── 05-risk/
    └── risk-register.csv
```

All files are validated against JSON schemas on intake. The directory is
version-controlled, meaning every change is logged and reversible.

**The CLAUDE.md AI Constitution.** The central configuration file that defines
how the AI must behave on this project. A production `CLAUDE.md` for a capital
project encodes mandatory judgment rules in plain English:

- *"If CPI drops below 0.85, immediately generate a Project Director escalation
  memo referencing the WBS package, the current CPI value, and the three-period
  CPI trend."*
- *"If SPI has been below 0.85 for two consecutive reporting periods, generate
  a mandatory written escalation notice. Do not wait for a third period."*
- *"Any change order exceeding 1% of the contract value triggers an independent
  cost review. Notify the Commercial Manager and the PMO lead."*
- *"At stage-gate FEED-to-EPC, the estimate must be AACE Class 3 or better.
  Flag any estimates submitted at Class 4 or 5 as non-compliant."*

It also defines stage-gate-specific standards, so the same system applies
different rigor depending on the project phase:

| Phase | Estimate Class | Contingency Range | Schedule Basis |
|-------|---------------|-------------------|----------------|
| Concept | Class 5 | 35–40% | ±50% |
| Pre-FEED | Class 4 | 25–30% | ±30% |
| FEED | Class 3 | 15–20% | ±15% |
| Execution | Class 2 | 8–12% | ±10% |
| Closeout | Class 1 | 3–5% | Actuals |

These rules are applied on every AI run without exception. They cannot be
abbreviated because the cost engineer is under pressure.

---

**Layer 2 — Domain Heuristics Library**

A curated library of parametric benchmarks and productivity norms, stored as
versioned YAML files. Two files are included for hydrogen pipeline projects:

`heuristics/pipeline-cost.yaml` — installed cost per kilometre by pipe diameter
and terrain type (abbreviated):

```yaml
# Source: IPA Benchmarking Database + DVGW project actuals (Western Europe)
# Valid for: onshore H2 pipelines, Germany / Western Europe, AACE Class 3–5
# Accuracy: ±20–30% (Class 3 equivalent)
# Version: 1.0 | Updated: 2026-01

base_cost_eur_per_km:
  DN300: 1_450_000
  DN400: 1_920_000      # H2-PIPE-DE-001 reference value
  DN500: 2_650_000
  DN600: 3_400_000

terrain_factors:
  flat_agricultural: 1.00
  rolling_rural:     1.15
  urban_corridor:    1.60
  river_crossing_hdd: 2.50   # per crossing

h2_service_premium:  0.15    # +15% for H2-grade materials (HIC-tested, dry-gas seals)

contingency_by_class:
  class_5: [0.30, 0.50]      # conceptual estimate
  class_3: [0.15, 0.25]      # study estimate
  class_2: [0.10, 0.15]      # budget-quality estimate
  class_1: [0.05, 0.10]      # definitive estimate
```

When the AI applies this benchmark to a cost estimate, it cites the source and
version, and flags any project falling outside the valid range (e.g., a DN900
pipeline or a project in a different region). `heuristics/productivity-norms.yaml`
covers labour productivity for pipeline welding (joints per shift by diameter and
welder grade), civil excavation (m³/shift by terrain), mechanical erection, and
E&I installation, with the same provenance structure.

---

**Layer 3 — Specialist Agents**

Four domain-specific agents are defined as markdown files in
`scaffolding/agents/`. Each agent specifies its trigger conditions, analysis
steps, output format requirements, and escalation rules. They are installed by
copying to `.claude/agents/` in the project directory, where Claude Code
discovers and invokes them automatically on matching prompts.

| Agent | Trigger | Output |
|-------|---------|--------|
| EVM Analyst | Monthly cycle; cost or schedule performance data | EV report, 5 charts, 3 EAC forecasts, RAG status, escalation flags |
| Schedule Analyzer | Milestone slip; SPI below threshold; "schedule review" | Schedule health report, critical path float, recovery options |
| Contract Reviewer | Change order; claim notice; new contract | Commercial summary, flagged clauses, CO entitlement assessment |
| Risk Assessor | Monthly cycle; new risk identified | EMV-ranked Top-10 risk digest, escalation flags |

The `schedule-analyzer` agent executes a defined sequence: read `milestones.csv`
and flag any milestone with a forecast slip exceeding 14 days; calculate total
float on the critical path from the latest schedule export; compare the current
SPI trend against the project's historical SPI curve; generate a recovery options
matrix with cost and schedule impact for each option. Its escalation rule is
encoded in its definition: any slip greater than 60 days on a milestone marked
`critical: true` triggers a mandatory Project Director memo, regardless of
whether the SPI threshold has been breached.

The `contract-reviewer` agent processes change orders against a structured
extraction template: contract type, base value, CO value as a percentage of
contract, entitlement basis (scope change vs. changed conditions), dispute
resolution mechanism, and liquidated-damages exposure. It cross-references the
CO value against the `CLAUDE.md` threshold and generates the independent cost
review notification automatically when the threshold is exceeded.

---

**Layer 4 — Claude Code Skills**

Claude Code's skill system packages purpose-built Python tools for automatic
invocation. Skills are installed by placing a directory in `~/.claude/skills/`,
containing a `SKILL.md` behavioural instruction file and the Python
implementation. Claude Code scans this directory at startup and invokes skills
when user prompts match the trigger phrases defined in `SKILL.md`.

| Skill | Source | Capability |
|-------|--------|------------|
| `evm` | Purpose-built | EVM engine: 10 metrics, 5 charts, 3 EAC forecast methods |
| `budget-estimator` | Purpose-built | Parametric CAPEX with P50/P90 Monte Carlo simulation |
| `pdf` | Marketplace | Extract structured text from contracts and specifications |
| `pptx` | Marketplace | Assemble progress presentation from EVM report and charts |
| `csv-data-summarizer` | Marketplace | Statistical summary of cost registers and change order logs |
| `meeting-insights-analyzer` | Marketplace | Extract action items and decisions from meeting notes |

Skills activate automatically on matching trigger phrases, as described in
sections 2.3 and 2.4 below.

---

**Layer 5 — JSON Schemas and Validation**

Three JSON Schema files enforce data quality at intake:

- `schemas/project-brief.schema.json` — validates the YAML frontmatter of
  `project-brief.md`: required fields (`project_id`, `fid_date`,
  `approved_capex_eur`, `contingency_eur`), data types, and allowable values for
  `status` and `phase`.
- `schemas/contract.schema.json` — validates contract register entries: contract
  type (lump sum / EPCM / reimbursable / time-and-materials), required date
  fields, and mandatory completion of `ld_rate_per_day` for lump-sum contracts.
- `schemas/risk-register.schema.json` — validates risk register entries:
  probability (0–1 float), impact (EUR value), required mitigation owner, and
  mandatory EMV recalculation trigger when either probability or impact changes
  by more than 10 percent.

Schema validation runs automatically when Claude Code opens a project directory.
Any invalid data file generates an immediate quality flag before analysis begins.

### 2.3 The EVM Module: From Calculation to Institutional Discipline

#### What Earned Value Management Is — and Why It Is Underused

Earned Value Management is the internationally recognised standard (ANSI/EIA-748)
for integrating cost and schedule performance measurement. Its core logic is
simple: at any point in a project, you can compute not just what you have spent
(Actual Cost, ACWP), but what you *should* have spent for the work you have
actually completed (Earned Value, BCWP). The ratio of earned value to actual
cost is the Cost Performance Index (CPI). A CPI of 0.91 means you are spending
EUR 1.10 to deliver EUR 1.00 of budgeted work.

The power of EVM lies in its predictive validity. Research across thousands of
projects has established that the CPI at the 20 percent completion milestone is
a reliable predictor of final outcome. Projects that are underperforming at 20
percent completion rarely recover to budget — and when they do, it is because
management intervened early, not because efficiency spontaneously improved.[^9]

Despite this, EVM is performed inconsistently in practice. The calculation
requires integrating cost actuals, progress measurements, and the original budget
baseline — data that typically live in three or four separate systems and require
manual reconciliation. Under schedule pressure, this reconciliation gets
abbreviated. The result is that the single most powerful early warning indicator
available to project management is produced late, inconsistently, or not at all.

#### What the EVM Module Delivers

Given a CSV file containing WBS codes, budget at completion (BAC), planned value
(BCWS), earned value (BCWP), and actual cost (ACWP) — data that any functioning
cost control system produces — the EVM module generates, in under two minutes:

- **A complete markdown report** with executive summary, WBS-level performance
  table with RAG status, three EAC forecasts (CPI method, composite CPI×SPI
  method, and planned-rate method), variance at completion, and TCPI
- **Five publication-ready charts**: S-curve (BCWS/BCWP/ACWP over time), CPI/SPI
  trend with threshold bands, WBS cost variance waterfall, EAC forecast
  comparison, and a CPI/SPI quadrant map with bubble sizes proportional to budget
  at stake
- **Automatic escalation flags** when CPI or SPI breach thresholds, when SPI has
  been below 0.85 for two consecutive periods, or when TCPI exceeds 1.10 (the
  level at which recovery is generally considered unrealistic without
  re-baselining)
- **A plain-language interpretation** identifying the worst-performing package,
  the recommended EAC to use for board reporting, and the next three actions with
  named responsible parties

The RAG thresholds applied are industry-standard: CPI or SPI ≥ 0.95 = GREEN;
0.85–0.94 = AMBER; < 0.85 = RED. The composite CPI×SPI EAC method is recommended
for board reporting, because it accounts for schedule pressure compounding cost
efficiency loss — the dominant failure pattern in large capital projects.

For the hydrogen pipeline example included with the system, this method produces
an EAC of EUR 1.637 billion against an approved BAC of EUR 1.350 billion for the
contracted scope — a 21 percent overrun signal at month five of a 36-month
execution programme, early enough for effective intervention. WBS-1.1 (Mainline
North) is identified as the primary driver: its SPI of 0.750 (RED) reflects a
linepipe delivery delay caused by port congestion, and if SPI remains below 0.85
in the June reporting period, the two-consecutive-period escalation rule fires
automatically, generating a mandatory written notice to the Project Director.

### 2.4 The Budget Estimator: Probabilistic CAPEX at Pre-FID Stage

#### Why Single-Point Estimates Fail Before Final Investment Decision

The standard practice in capital project development is to produce a single-point
cost estimate at each stage gate — a number that is then treated as a commitment
rather than a probability. This creates a structural problem: single-point
estimates carry implicit assumptions about scope, productivity, and market
conditions that are never made explicit and that are rarely interrogated by
reviewers who see only the final number.

The consequence is systematic optimism bias. IPA research across 20,000 projects
shows that single-point estimates systematically underestimate final cost because
estimators anchor to base conditions and underweight the upper tail of the cost
distribution — tail events (changed ground conditions, regulatory delays, supply
chain disruptions) that are individually unlikely but collectively almost certain
to affect a multi-year capital project.

The AACE International recommended practice RP 18R-97 addresses this directly: a
project's cost estimate should be accompanied by a probability distribution, not
just a central value, and contingency should be sized to cover the P80 or P90
outcome, not the P50 alone. In practice, this requirement is rarely met because
building a proper Monte Carlo model requires specialist software and significant
effort. The budget-estimator skill removes that barrier.

#### What the Budget Estimator Delivers

Given a YAML work-package definition or a set of CLI parameters, the budget
estimator runs 10,000 Monte Carlo iterations using triangular distributions
calibrated to the selected AACE estimate class, and produces in under one minute:

- **P10, P50, and P90 CAPEX values** — the 10th, 50th, and 90th percentiles of
  the simulated cost distribution. P50 is the planning basis; P90 is the
  risk-adjusted ceiling for budget approval and contingency sizing
- **A cost distribution histogram** showing the full shape of the simulation
  output, making visible whether the distribution is approximately symmetric or
  heavily right-skewed (indicating large upside risk)
- **A sensitivity tornado chart** ranking work packages by their Spearman rank
  correlation with total CAPEX across all iterations — identifying precisely which
  cost elements are driving the P90 and where additional engineering definition
  would most reduce uncertainty
- **A work-package breakdown chart** comparing P50 and P90 by WBS element,
  making it possible to direct contingency toward the packages that need it rather
  than spreading it uniformly

Each work package can be specified parametrically — using the heuristics library
(EUR/km by pipe diameter and terrain, H2 material premium, compression station
cost per MW) — or as a direct cost entry with an uncertainty range. The AACE
estimate class (1 through 5) is selected by the user and determines the default
accuracy bounds applied to each work package: Class 5 (conceptual screening)
applies −20%/+50%; Class 3 (FEED-stage study) applies −10%/+20%; Class 1
(definitive) applies −3%/+10%.

Contingency is reported as P90 minus P50, not as a flat percentage added to a
point estimate. This means the contingency is sensitive to actual scope
definition — packages with high parametric uncertainty contribute more to the
P90 gap than packages with tight engineering definitions, which is the correct
behaviour for managing pre-FID risk.

On the hydrogen pipeline example, the Class 3 estimate produces a P50 of
EUR 1,833M and a P90 of EUR 1,930M against the approved FID CAPEX of
EUR 1,749M. The P50 is 5 percent above the approved budget — within the ±10/20%
accuracy band of a FEED-stage estimate — and the P90 implies a contingency
requirement of EUR 97M (5.3%). The tornado chart identifies WBS-1.1 (Mainline
North) as the dominant driver of the P90 spread, consistent with the ground
conditions risk identified in the project risk register.

### 2.5 Integration with Existing Tools

The system reads data that capital project organisations are already producing;
it does not require replacing any existing tool.

**Primavera P6.** Schedule data is ingested via `.xer` export files using the
P6XER MCP (Model Context Protocol) server. This allows Claude Code to read P6
project schedules directly, extract critical path float, identify milestone
forecast dates, and feed schedule data into the schedule-analyzer agent —
without requiring a P6 licence or database connection in the AI environment.

**Excel and CSV cost systems.** Any cost control system that can export EVM data
in tabular form (BCWS, BCWP, ACWP by WBS code) is compatible. The EVM skill
accepts both snapshot and time-phased formats and validates column names on
intake.

**Document repositories.** Contract PDFs, engineering specifications, and tender
documents are processed via the `pdf` skill. The contract-reviewer agent combines
PDF extraction with structured templates to produce commercial summaries from
documents that would otherwise require hours of manual review.

**Reporting platforms.** The `pptx` skill converts the monthly EVM markdown
report and the five generated chart PNGs into a presentation-ready deck,
formatted to the organisation's template. This output feeds directly into the
monthly board reporting pack without manual transcription.

**Atlassian and collaboration tools.** The Atlassian MCP server enables action
items generated by the AI (e.g., from the risk-assessor or schedule-analyzer
agents) to be logged directly as Jira tickets with assigned owners and due dates,
completing the loop from AI analysis to trackable task.

---

## 3. Investment Case, Risks, and Governance

### 3.1 The Value Drivers

The business case for AI-augmented project controls operates on three distinct
value levers:

**Lever 1 — Earlier detection of adverse trends**

Research by IPA establishes that the cost of corrective action increases
approximately exponentially with the delay between signal and response. A
schedule slip that can be corrected for EUR 2 million in month three may require
EUR 15–20 million to recover by month nine, because interim procurement
commitments, subcontractor mobilisation costs, and lost float compound the
original deviation.

The system makes the trend visible in the first reporting period it appears,
rather than the third. On a EUR 1 billion project, even a single such early
intervention — preventing a 2 percent cost growth that would otherwise
materialise — generates a return that exceeds the entire cost of implementing
and operating the system.

**Lever 2 — Consistent application of escalation rules**

Escalation failures are documented as a primary driver of late-stage project
crises. The mechanism is well understood: a cost engineer identifies a negative
trend, judges it borderline, decides to wait one more period to confirm before
escalating, and the window for low-cost intervention closes. Encoded escalation
thresholds eliminate the discretion at the margin. When CPI falls below 0.85,
the flag fires automatically. The Project Director is notified regardless of
where the cost engineer's judgment falls.

**Lever 3 — Reduced cost of producing controls outputs**

Companies using AI-assisted project management tools report an average 15 percent
improvement in project delivery productivity.[^10] On the specific task of monthly
reporting — which typically consumes 3–5 working days per reporting period for a
major project's controls team — consistent findings indicate that AI assistance
reduces this by 40–60 percent. This frees experienced project controls
professionals to perform root cause analysis, contractor engagement, and recovery
planning rather than data assembly and chart production.

### 3.2 Conservative Financial Model

The following model is intentionally conservative and uses a single EUR 1 billion
project as the unit of analysis:

| Value Driver | Basis | Annual Value (EUR) |
|-------------|-------|-------------------|
| Earlier detection — 1 avoided 2% cost growth | One intervention per project year | 20,000,000 |
| Reporting efficiency — 2 FTE-months freed per year | Senior engineer at EUR 15k/month fully loaded | 360,000 |
| Consistent escalation — avoided one late crisis | 50% probability × EUR 5M average cost of late recovery | 2,500,000 |
| **Total (conservative)** | | **~22,860,000** |

Against this, the implementation costs are modest:

| Cost Item | Basis | Annual Cost (EUR) |
|-----------|-------|------------------|
| Claude Code enterprise licences (10 users) | Current enterprise pricing | ~60,000 |
| Internal implementation effort (one-time) | 15 person-days × senior engineer rate | ~30,000 |
| Ongoing maintenance and data governance | 0.25 FTE | ~75,000 |
| **Total** | | **~165,000 p.a.** |

The implied return on investment exceeds 100:1 on conservative assumptions,
driven almost entirely by the value of a single avoided late-stage intervention.
The ratio improves further on a portfolio of projects, where the fixed
infrastructure cost (licences, governance, templates) is shared.

### 3.3 Contextual Benchmark

Companies that use AI-driven tools in project management deliver 61 percent of
their projects on time, compared to 47 percent for those that do not — a
14-percentage-point improvement.[^11] On a programme of five concurrent capital
projects, each averaging EUR 500 million in CAPEX, moving one project from the
"late" to "on-time" bucket — with a typical delay cost of 5–10 percent of CAPEX
— represents EUR 25–50 million in value creation from the portfolio uplift alone.

The open-source code base eliminates implementation risk as a financial objection:
the system can be inspected in detail before deployment, extended without vendor
dependency, and discontinued without sunk cost if the pilot does not demonstrate
value.

### 3.4 AI-Specific Risks

**Risk: AI produces confident but incorrect analysis**  
*Likelihood: Medium. Consequence: Medium.*  
The system mitigates this through schema validation, provenance requirements on
all heuristics, and mandatory cross-checking of EAC against parametric
benchmarks. No AI output is presented as final without a named human reviewer.
The system generates recommendations; it does not make decisions.

**Risk: Sensitive commercial data processed through third-party AI systems**  
*Likelihood: Low with controls. Consequence: High.*  
Claude Code can be deployed on-premises or in a private cloud environment using
Anthropic's enterprise API. No project data need leave the organisation's
controlled infrastructure. The data governance policy establishes which data
categories are permissible and in what environment.

**Risk: Over-reliance reduces human expertise over time**  
*Likelihood: Low with design. Consequence: Medium.*  
This risk is real and documented in analogous automation contexts. The
mitigation is design: the system explicitly requires human interpretation of
every report, ensures that escalation recommendations are reviewed not
auto-executed, and generates plain-language explanations that build rather than
bypass analytical understanding.

### 3.5 Organisational Risks

**Risk: Resistance from project controls professionals**  
*Likelihood: High without change management. Consequence: Medium.*  
The most effective mitigation is framing. This system removes the least engaging
portions of a cost engineer's work — data assembly, chart production, threshold
checking — and returns time for the high-judgment work that experienced
professionals value. Early engagement of senior project controls staff in the
pilot design, and visible credit for the improved reporting outputs, is the
primary change management lever.

**Risk: Data quality too poor for meaningful analysis**  
*Likelihood: Medium. Consequence: Medium.*  
The system will surface data quality problems that were previously obscured by
manual report production. This is a feature, not a bug. A data quality review
before the system goes live on the pilot project establishes a clean baseline
and closes the gaps that would otherwise persist undetected.

**Risk: Pilot succeeds but rollout stalls**  
*Likelihood: Medium without board sponsorship. Consequence: High.*  
The pattern of successful pilot — stalled rollout — is the dominant failure mode
for enterprise technology adoption. The mitigation is board-level ownership of
the rollout mandate and a defined CAPEX threshold above which the system is
mandatory, not optional.

### 3.6 What This System Does Not Do

It is equally important to state explicitly what this system does not replace:

- It does not replace the Project Director's judgment on whether to escalate a
  situation to the board
- It does not negotiate with contractors, assess claim merits, or draft legal
  correspondence without human review
- It does not produce FID-quality cost estimates; it analyses cost *performance*
  against an already-established baseline
- It does not replace the physical site inspection, quality review, or HSE
  incident investigation
- It does not guarantee project success; it improves the information available
  to the humans who determine outcome

Projects succeed because of skilled, experienced, well-led teams. This system
makes it harder for those teams to miss early warning signals, easier to produce
consistent reporting, and more likely that the right information reaches the
right decision-maker at the right time.

---

## Appendix A — Key Metrics Produced by the EVM Module

| Metric | Formula | What it tells management |
|--------|---------|--------------------------|
| CPI | BCWP ÷ ACWP | Cost efficiency: EUR earned per EUR spent |
| SPI | BCWP ÷ BCWS | Schedule efficiency: earned value vs plan |
| EAC (Composite) | ACWP + (BAC−BCWP) ÷ (CPI×SPI) | Final cost forecast, accounting for schedule pressure |
| VAC | BAC − EAC | Expected over- or under-run at completion |
| TCPI | (BAC−BCWP) ÷ (BAC−ACWP) | CPI required for all remaining work to finish within budget; >1.10 indicates re-baselining is needed |

**RAG thresholds (industry standard):**

| Index | GREEN | AMBER | RED |
|-------|-------|-------|-----|
| CPI | ≥ 0.95 | 0.85 – 0.94 | < 0.85 |
| SPI | ≥ 0.95 | 0.85 – 0.94 | < 0.85 |

---

## Appendix B — Technical Resource

The working system — EVM skill, scaffolding templates, domain heuristics,
JSON schemas, specialist agent definitions, and a complete example project —
is available at:

**[https://github.com/jmeier1963/large_capital_project_management](https://github.com/jmeier1963/large_capital_project_management)**

The repository includes:
- `evm/evm_calculator.py` — EVM engine (713 lines, no dependencies beyond pandas and matplotlib)
- `budget-estimator/budget_estimator.py` — parametric CAPEX engine with P50/P90 Monte Carlo
- `scaffolding/` — project configuration templates for immediate deployment
- `examples/H2-PIPE-DE-001/` — complete worked example: 500 km H2 pipeline, five months of EVM data, illustrated analysis outputs
- `README.md` — step-by-step installation and usage instructions

Installation requires copying three files and running one `pip install` command.

---

## References

[^1]: Flyvbjerg, B. & Gardner, D. (2023). *How Big Things Get Done*. Macmillan.
  Database of 16,000 projects; 8.5% delivered on cost and schedule; 0.5%
  delivered all promised benefits.

[^2]: McKinsey & Company (2015). "Megaprojects: The good, the bad, and the
  better." Review of 300+ projects exceeding USD 1 billion.

[^3]: Flyvbjerg, B. (2017). "The Iron Law of Megaprojects." Cato Institute
  Policy Report. 91.5% of projects exceed budget, schedule, or both.

[^4]: McKinsey Global Institute (2016). "Reinventing Construction." Mining and
  metals sector overrun data. Rail, bridge, and tunnel statistics from
  Flyvbjerg's database.

[^5]: Hydrogen Council & McKinsey & Company (2025). *Global Hydrogen Compass*.
  USD 110B committed investment across 500+ post-FID projects.

[^6]: McKinsey & Company (2017). "Increasing transparency in megaproject
  execution." Analysis of 48 troubled projects; 73% of overruns attributed
  to execution failures.

[^7]: Independent Project Analysis (IPA). *Capital Project System Improvement*.
  Project Control Index methodology and performance correlation.
  [ipaglobal.com](https://www.ipaglobal.com/services/capital-project-system-improvement/)

[^8]: Deloitte US (2026). *State of AI in the Enterprise*. 89% of companies
  have deployed AI; 94% report not seeing significant value.

[^9]: Christensen, D.S. (1993). "The Estimate at Completion Problem: A Review
  of Three Studies." *Project Management Journal*. CPI stability at 20%
  completion and its predictive validity for final outcome.

[^10]: Various sources aggregated in: Celoxis (2025). "AI and Machine Learning
  in Project Management." 15% average productivity improvement; 61% on-time
  delivery with AI tools vs. 47% without.

[^11]: Ibid.


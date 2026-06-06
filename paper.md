# AI-Augmented Project Controls for Large Capital Projects
## A Decision Paper for Management and Supervisory Boards

**Prepared for:** Management Board and Supervisory Board  
**Classification:** Board Confidential  
**Date:** June 2026  
**Version:** 1.0

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

The system has been designed and implemented. It is available as open-source
code at [github.com/jmeier1963/capital-project-management](https://github.com/jmeier1963/capital-project-management).
A working prototype illustrating the approach on a hypothetical 500 km hydrogen
transmission pipeline (EUR 1.75 billion CAPEX) demonstrates the full capability.

This paper asks the board to make three decisions:

1. **Authorize a pilot** on one live capital project, with a defined success criteria review at 90 days.
2. **Assign an owner** — a senior executive accountable for the pilot, sitting at the intersection of project controls, digital, and operations.
3. **Establish a data governance baseline** — define which project data is permissible to process through AI systems and under what conditions.

---

## 1. The Persistent Performance Deficit in Large Capital Projects

### 1.1 The Scale of the Problem

Flyvbjerg's landmark study — the largest empirical analysis of project
performance ever conducted — established what he calls the "iron law of
megaprojects": over budget, over time, over and over again.[^3] The headline
numbers bear repeating for emphasis:

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

---

## 2. What Has Changed: Why AI Can Help Now

### 2.1 The Structural Shift in AI Capability

For most of the past decade, AI in project management meant dashboards that
required extensive data pipeline engineering, natural language processing tools
that extracted text from documents with limited accuracy, and predictive models
that required months of training on proprietary datasets before producing
actionable output.

The shift that has occurred since 2023 is qualitative, not incremental. Large
language models (LLMs) — and in particular AI agents that can reason over
structured data, apply domain-specific rules, call tools, and generate
structured outputs — have changed what is possible without bespoke development.
An AI agent can today be given a CSV file of cost actuals, a set of rules
encoded in plain language (e.g., "if CPI drops below 0.85, flag for Project
Director escalation"), and a set of calculations to perform, and will produce a
complete, consistent, correctly formatted report — every time, in under two
minutes.

This is not a claim that AI understands project management in the way an
experienced cost engineer does. It is a more precise and more practically
important claim: AI can perform the *routine, structured, rule-governed portion*
of project controls work with perfect consistency, freeing skilled professionals
to focus on the *judgment-intensive* portions — contractor negotiation, root
cause analysis, recovery planning — where human expertise is irreplaceable.

### 2.2 The Adoption Paradox — and How to Avoid It

Deloitte's 2025–2026 State of AI in the Enterprise survey found that while
nearly 90 percent of companies have deployed AI in at least one business
function, 94 percent report not seeing "significant" value from their
investments.[^8] This paradox has a structural explanation: most AI deployments
in enterprises target knowledge work at the individual level (drafting emails,
summarising documents) rather than the *process* level where value is
concentrated.

In capital project controls, value is concentrated in process consistency, not
individual productivity. The question is not whether a cost engineer can
produce a report faster with AI assistance. The question is whether every
project — regardless of the experience level of its controls team, regardless
of whether it is month four or month thirty-two — produces a complete,
consistently structured, threshold-checked EVM report on time, every reporting
period.

The approach described in this paper is designed specifically for that target.
It does not add an AI layer on top of existing processes. It embeds AI into
the process as a non-optional execution step, with encoded domain rules,
parameterised thresholds, and mandatory output formats that cannot be
abbreviated under pressure.

---

## 3. The System: Architecture and Capabilities

### 3.1 Design Principles

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
and judgment rules (e.g., "any change order exceeding 1% of contract value
triggers an independent cost review") are encoded in a `CLAUDE.md` configuration
file — the project's AI constitution. They are applied automatically on every
analysis run, not recalled from a briefing document.

**Roles, not generics.** Every communication or action recommendation produced
by the AI addresses a specific named role from the project's organisation chart.
It does not recommend that "the team" should act. It specifies that the
Commercial Manager should review the change order, that the Project Director
should receive the escalation memo, and that the cost register should be updated
by the Cost Engineer within five business days.

### 3.2 System Components

The system consists of four integrated layers:

**Layer 1 — Project Data Store**

A structured directory of CSV, YAML, JSON, and Markdown files representing the
project's living state: the project brief (scope, FID CAPEX, milestones), the
contracts register, the WBS cost register, the resource matrix, and the risk
register. All files have defined schemas that validate on intake. The directory
is version-controlled, meaning every change is logged and reversible.

**Layer 2 — Domain Heuristics Library**

A curated library of parametric benchmarks and productivity norms, stored as
versioned YAML files. For a hydrogen pipeline project these include: installed
cost per kilometre by pipe diameter and terrain type, welding productivity
norms per shift, compression station cost per megawatt, and contingency ranges
by estimate class (AACE Class 1–5). Each file carries its source, valid range,
and date of last update. The AI consults this library before generating any
cost forecast and flags deviations that exceed ±30 percent of the benchmark.

**Layer 3 — Specialist Agents**

Three domain-specific agents that activate automatically on defined triggers:

| Agent | Trigger | Primary Output |
|-------|---------|----------------|
| EVM Analyst | Monthly reporting cycle; any mention of cost or schedule performance | Full earned value report: five charts, RAG status, three EAC forecasts, escalation flags |
| Schedule Analyzer | Milestone slip; SPI below threshold; request for schedule review | Schedule health report with critical path float, recovery options matrix |
| Contract Reviewer | Change order received; claim notice; new contract for review | Structured commercial summary, flagged risk clauses, CO entitlement assessment |
| Risk Assessor | Monthly cycle; new risk identified; risk materialisation | EMV-ranked Top 10 risk digest, escalation flags, recommended register updates |

**Layer 4 — Governance Rules**

Encoded in `CLAUDE.md`, the project's AI constitution. This file specifies
mandatory escalation thresholds (CPI < 0.85, SPI < 0.85 for two consecutive
periods), required approval levels for change orders, stage-gate-specific
estimate class requirements, and output format standards. The AI cannot
deviate from these rules; they are applied on every run without exception.

### 3.3 Integration with Existing Tools

The system reads Primavera P6 `.xer` schedule exports (via the P6XER MCP
server), Excel and CSV cost exports, PDF contracts (via the PDF extraction
skill), and Google Drive document repositories. It does not require replacing
any existing tool. It adds a controlled intelligence layer on top of data that
organisations are already generating.

---

## 4. The EVM Module: From Calculation to Institutional Discipline

### 4.1 What Earned Value Management Is — and Why It Is Underused

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
requires integrating cost actuals, progress measurements, and the original
budget baseline — data that typically live in three or four separate systems
and require manual reconciliation. Under schedule pressure, this reconciliation
gets abbreviated. The result is that the single most powerful early warning
indicator available to project management is produced late, inconsistently, or
not at all.

### 4.2 What the EVM Module Delivers

Given a CSV file containing WBS codes, budget at completion (BAC), planned
value (BCWS), earned value (BCWP), and actual cost (ACWP) — data that any
functioning cost control system produces — the EVM module generates, in under
two minutes:

- **A complete markdown report** with executive summary, WBS-level performance
  table with RAG status, three EAC forecasts (CPI method, composite CPI×SPI
  method, and planned-rate method), variance at completion, and TCPI
- **Five publication-ready charts**: S-curve (BCWS/BCWP/ACWP over time),
  CPI/SPI trend with threshold bands, WBS cost variance waterfall, EAC
  forecast comparison, and a CPI/SPI quadrant map with bubble sizes proportional
  to budget at stake
- **Automatic escalation flags** when CPI or SPI breach thresholds, when SPI
  has been below 0.85 for two consecutive periods, or when TCPI exceeds 1.10
  (the level at which recovery is generally considered unrealistic without
  re-baselining)
- **A plain-language interpretation** identifying the worst-performing package,
  the recommended EAC to use for board reporting, and the next three actions
  with named responsible parties

The recommended EAC for large capital projects is the composite CPI×SPI method,
which assumes that schedule pressure will continue to drive cost efficiency
downward. For the hydrogen pipeline example included with the system, this method
produces an EAC of EUR 1.637 billion against an approved BAC of EUR 1.350
billion for the contracted scope — a 21 percent overrun signal at month five of
a 36-month execution programme, early enough for effective intervention.

---

## 5. Business Case

### 5.1 The Value Drivers

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

### 5.2 Conservative Financial Model

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

### 5.3 Contextual Benchmark

Companies that use AI-driven tools in project management deliver 61 percent of
their projects on time, compared to 47 percent for those that do not — a
14-percentage-point improvement.[^11] On a programme of five concurrent capital
projects, each averaging EUR 500 million in CAPEX, moving one project from the
"late" to "on-time" bucket — with a typical delay cost of 5–10 percent of CAPEX
— represents EUR 25–50 million in value creation from the portfolio uplift alone.

---

## 6. Implementation Roadmap

### Phase 1 — Foundation (Months 1–3)

**Objective:** Install the system on one live project; establish data governance
baseline; train the project controls team.

Activities:
- Select pilot project: ideally a project at the 10–25 percent completion stage,
  with an active cost control team and at least three months of actuals history
- Appoint an AI Project Controls Lead (existing staff member, not a new hire)
- Establish data governance policy: define permissible data types, storage
  locations, and access controls for AI-processed project data
- Install Claude Code; deploy the EVM skill and project scaffolding; load three
  months of historical cost data
- Run the first EVM analysis; compare output to existing controls report;
  identify and close any data quality gaps
- Conduct a one-day orientation for the project controls team and the Project
  Manager

**Success gate:** First AI-generated EVM report accepted by the Project
Manager as the definitive monthly controls output.

### Phase 2 — Expansion (Months 4–9)

**Objective:** Extend to three projects; activate schedule and risk agents;
integrate with existing reporting cadence.

Activities:
- Replicate the deployment on two additional projects at different lifecycle
  stages (to stress-test the system across phases)
- Activate the Schedule Analyzer and Risk Assessor agents
- Connect to Primavera P6 exports (via P6XER MCP server) to automate
  schedule data ingestion
- Integrate EVM report output into the monthly board reporting pack
- Establish a quarterly heuristics review: update cost benchmarks and
  productivity norms based on project actuals

**Success gate:** At least one escalation flag correctly identified and acted
upon ahead of the monthly Management Board review.

### Phase 3 — Institutionalisation (Months 10–18)

**Objective:** Deploy across the full capital project portfolio; establish
continuous improvement loop; build internal capability.

Activities:
- Standardise the system as the mandatory project controls platform for all
  projects above a defined CAPEX threshold (recommended: EUR 50 million)
- Develop project-type-specific heuristics libraries (pipeline, compression,
  offshore, civil infrastructure)
- Establish a Centre of Excellence for AI-augmented project controls
  (2–3 FTE from existing staff, not a new department)
- Publish a lessons-learned library: each project closeout contributes
  validated actuals back to the heuristics library, improving future estimates

---

## 7. Risk Assessment and Governance

### 7.1 AI-Specific Risks

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
controlled infrastructure. The data governance policy established in Phase 1
defines exactly which data categories are permissible.

**Risk: Over-reliance reduces human expertise over time**  
*Likelihood: Low with design. Consequence: Medium.*  
This risk is real and documented in analogous automation contexts. The
mitigation is design: the system explicitly requires human interpretation
of every report, ensures that escalation recommendations are reviewed not
auto-executed, and generates plain-language explanations that build rather
than bypass analytical understanding. The system is designed to augment the
cost engineer's analytical output, not to replace the cost engineer.

### 7.2 Organisational Risks

**Risk: Resistance from project controls professionals**  
*Likelihood: High without change management. Consequence: Medium.*  
The most effective mitigation is framing. This system removes the least
engaging portions of a cost engineer's work — data assembly, chart production,
threshold checking — and returns time for the high-judgment work that
experienced professionals value. Early engagement of senior project controls
staff in the pilot design, and visible credit for the improved reporting
outputs, is the primary change management lever.

**Risk: Data quality too poor for meaningful analysis**  
*Likelihood: Medium. Consequence: Medium.*  
The system will surface data quality problems that were previously obscured by
manual report production. This is a feature, not a bug. The Phase 1 data quality
review is specifically designed to establish a clean baseline before the system
goes live on the pilot project.

**Risk: Pilot succeeds but rollout stalls**  
*Likelihood: Medium without board sponsorship. Consequence: High.*  
The pattern of successful pilot — stalled rollout — is the dominant failure
mode for enterprise technology adoption. The mitigation is board-level ownership
of the Phase 3 mandate and a defined CAPEX threshold above which the system is
mandatory, not optional.

### 7.3 What This System Does Not Do

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

## 8. Recommendation and Board Decision Points

### 8.1 The Strategic Context

The hydrogen and energy transition investment wave is already underway. With
USD 110 billion committed globally and project execution — not FID — now the
bottleneck, the competitive advantage will accrue to organisations that execute
consistently rather than those that plan ambitiously. Improving project controls
quality from the industry median to the top quartile is worth, in expectation,
5–10 percent of total CAPEX across a portfolio. At scale, that is a strategic
differentiator.

AI-augmented project controls is not a speculative technology bet. The EVM
module described in this paper is working code, tested against real data, with
verifiable outputs. The open-source release means the implementation risk is
low: the system can be inspected in detail, extended without vendor dependency,
and abandoned without sunk cost if the pilot does not demonstrate value.

The question for the board is not whether this technology works. It is whether
the organisation is willing to commit the governance attention needed to
deploy it at scale and embed it into the project controls process as a
non-negotiable standard.

### 8.2 Three Decisions Required

**Decision 1 — Authorize the pilot**

Approve a 90-day pilot on one active capital project above EUR 100 million.
Define three measurable success criteria in advance (suggested: first AI EVM
report accepted as definitive by PM within 30 days; at least one escalation
flag correctly generated; reporting time reduced by at least 30 percent).

**Decision 2 — Assign executive ownership**

Name a board member or direct report as executive sponsor. This is the single
most important determinant of whether the pilot converts to rollout. The sponsor
needs authority over the project controls function, visibility into the digital
infrastructure, and a mandate to enforce the Phase 3 rollout if the pilot
succeeds.

**Decision 3 — Commission a data governance policy**

Direct the Chief Information Officer or General Counsel (or equivalent) to
produce a data governance policy covering AI-processed project data within
60 days. This policy should address data classification, permissible AI
processing environments, and the human-review requirements for AI-generated
outputs used in board reporting.

### 8.3 If the Pilot Succeeds

The Phase 3 mandate — system deployment on all capital projects above a defined
CAPEX threshold — should be treated as a project controls standard, equivalent
in status to the requirement to use Primavera P6 for scheduling or to conduct
HAZOP for process safety. Optional adoption of a better standard invariably
produces uneven quality. Mandatory adoption produces the institutional
discipline that translates individual project improvements into portfolio
performance.

The open-source code base is the starting point, not the end state. The
organisation's own project actuals, accumulated over three to five years of
deployment, will produce a proprietary heuristics library that reflects its
specific asset types, geographies, and contractor base — a genuine competitive
asset that cannot be replicated by organisations that did not start building it.

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

**[https://github.com/jmeier1963/capital-project-management](https://github.com/jmeier1963/capital-project-management)**

The repository includes:
- `evm/evm_calculator.py` — the full Python engine (713 lines, no external dependencies beyond pandas and matplotlib)
- `scaffolding/` — project configuration templates for immediate deployment
- `examples/H2-PIPE-DE-001/` — a complete worked example for a 500 km hydrogen pipeline, including five months of EVM data and the resulting analysis outputs
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

---

*This paper was prepared to support a board-level decision on the adoption of
AI-augmented project controls. It describes a working system and is accompanied
by verifiable open-source code. The financial projections are illustrative and
conservative; project-specific analysis should be conducted before committing
to a scaled rollout.*

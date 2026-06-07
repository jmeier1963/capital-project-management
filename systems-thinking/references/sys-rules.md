# SYS Rules Reference — 15 Heuristics for Systems-Thinking Audits

Derived from failure analysis of: Crossrail, Olkiluoto 3 EPR, Flamanville 3 EPR, Vogtle 3&4, NHS NPfIT, Longannet CCS, Mongstad CCS, Gorgon CCS, Big Dig, Sydney Opera House, Scottish Parliament, Nimrod MRA4, Oyu Tolgoi Underground, Pascua-Lama, Hallandsås Tunnel.

Source authorities: NAO, GAO, PAC, STUK, ASN, Cour des comptes, DOE, Crossrail Learning Legacy, Bundesrechnungshof.

---

## SYS-01 — Map the full value chain, not just the asset

**What it means:** The project definition must show the complete chain from upstream inputs through the core asset to downstream offtake, operations, disposal/decommissioning, and exit. Every link that the project's success depends on must be named.

**PRESENT:** An explicit value-chain diagram or SIPOC/system context map covers feedstock/inputs, core asset, output/offtake, operators, customers, and end-of-life. Dependencies at each stage are named.

**PARTIAL:** Some upstream or downstream elements are described but not formally bounded. For example, the asset is well-defined but grid connection or offtake contracts are "to be confirmed."

**ABSENT:** The definition treats the project as the asset only. Upstream supply, downstream offtake, or operational context are assumed rather than mapped.

**Canonical failure:** Longannet CCS — the carbon capture asset was scoped without integrating transport, storage, grid, and carbon-price-floor into one value-chain economics model.

**Follow-up question template:** "Show me the end-to-end chain from [primary input] to [primary output/customer]. Which link is least certain today?"

---

## SYS-02 — Identify 2nd- and 3rd-order effects

**What it means:** Changes to the project ripple into adjacent systems. The definition must identify non-obvious effects on grid/network, tax/levy treatment, neighbouring operations, permitting, community, and maintenance regimes.

**PRESENT:** A documented exercise (causal loop diagram, pre-mortem, or structured risk workshop) explicitly mapped second-order effects and the findings are integrated into the risk register.

**PARTIAL:** The risk register contains some indirect effects but the exercise was not systematic — effects were identified reactively rather than proactively searched.

**ABSENT:** The risk register covers direct project risks only. Adjacent-system effects are not addressed.

**Canonical failure:** Hallandsås Tunnel — geology, groundwater, and toxic injection chemicals were treated as independent engineering problems; their coupling into an environmental/political crisis was not modelled.

**Follow-up question template:** "If this project is delayed 18 months, what happens to [adjacent system]? And what does that do to [one more step out]?"

---

## SYS-03 — No FID without a Regulatory Map

**What it means:** Before any final investment or build commitment, all permits, licences, classifications, levies, subsidies, tax treatments, and liability frameworks must be explicitly mapped, with ownership assigned and status tracked.

**PRESENT:** A regulatory map or permit register exists, covers all jurisdictions, assigns a responsible party and target date to each item, and has been reviewed by external legal/regulatory counsel.

**PARTIAL:** Key permits are identified but secondary regulatory items (tax treatment, environmental classifications, grid codes, state-aid rules) are not fully resolved or assigned.

**ABSENT:** Permitting is described as "standard" or "to be obtained." No permit register. No legal/regulatory due diligence document.

**Canonical failure:** Longannet CCS — the interaction of the £1bn DECC funding cap, carbon-price-floor trajectory, and contract structure was not resolved as an integrated regulatory/financial system until it was too late.

**Follow-up question template:** "List every permit, licence, classification, levy, and subsidy this project depends on. Which ones have legal opinions? Which are still open?"

**Suggest:** `/perplexity-search` for live regulatory lookups in specific jurisdictions.

---

## SYS-04 — No critical build-commit without a design-maturity threshold

**What it means:** Before committing to major construction or irreversible procurement, identify the top open design points that could move cost or schedule by more than 10%. None of those points should be unresolved at FID.

**PRESENT:** A design-maturity register exists with the top-20 open design questions scored by cost/schedule impact. Each has a resolution owner and deadline. The FID gate criteria explicitly include a design-maturity threshold.

**PARTIAL:** Some major design questions are identified but the list is not comprehensive, not scored by impact, or the gate criteria don't enforce resolution.

**ABSENT:** Design is described as "sufficiently advanced" without a documented register of open items. The build commitment precedes design freeze on material topics.

**Canonical failures:** Olkiluoto 3, Flamanville 3, Vogtle 3&4 — all started construction before FOAK design details (reactor head welds, concrete specifications, module interfaces) were resolved, generating cascading rework.

**Follow-up question template:** "What are the 10 biggest open design questions? What is each one worth in cost/schedule risk if it resolves badly?"

---

## SYS-05 — Every critical interface needs an Owner and a proof artefact

**What it means:** Every point where two subsystems, organisations, or contracts meet must have a named owner, a defined interface control document or equivalent, and a planned proof of integration (test, demonstration, or simulation) before the interface becomes the critical path.

**PRESENT:** An interface register or N²-matrix exists. Critical interfaces have owners, ICD references, and integration proof milestones on the schedule.

**PARTIAL:** Major interfaces are identified but ownership is split or unclear, or integration proof is deferred to commissioning rather than earlier in the programme.

**ABSENT:** Interfaces are not formally tracked. Integration is assumed to follow naturally from parallel workstreams being "on time."

**Canonical failure:** Crossrail — civil works were on programme; the systemic delay came from the interface between signalling, station systems, software, safe-assurance, and operational readiness, none of which had a unified owner or integration proof plan.

**Follow-up question template:** "Draw the interface matrix between your top-5 technical systems. Who owns each interface? What is the earliest test that proves it works end-to-end?"

---

## SYS-06 — Separate point estimate from risk-adjusted estimate

**What it means:** The board should never see only a single-number cost or schedule estimate. The definition must present a Base Case, a P50 (50th percentile), and a P80 (80th percentile), with the main drivers of the spread identified.

**PRESENT:** A Monte Carlo or equivalent probabilistic estimate is documented. P50 and P80 are distinct from the Base Case. The top-5 cost/schedule risk drivers are named with their distributions.

**PARTIAL:** A contingency percentage has been added to the Base Case ("10% contingency included") without a probabilistic basis. Or P50/P80 are presented without identifying the spread drivers.

**ABSENT:** Only a single-point estimate is presented. Contingency is either absent or unexplained.

**Canonical failure:** Big Dig — the original $2.6bn estimate had no probabilistic basis; utility relocations, scope changes, and environmental conditions alone drove it to $14.6bn.

**Follow-up question template:** "If I asked your estimating team to model P50 and P80 right now, what would be the three biggest items driving the gap between them?"

---

## SYS-07 — Use the outside view before the sponsor view

**What it means:** Before accepting the project team's own schedule and cost estimates, benchmark them against a reference class of comparable completed projects using Reference Class Forecasting or optimism-bias uplift tables.

**PRESENT:** A reference class has been selected and documented. An optimism-bias uplift has been applied to both cost and schedule. The rationale for the chosen class is explicit.

**PARTIAL:** Comparables are mentioned informally ("similar projects took about X years") but no formal reference class database or uplift methodology is applied.

**ABSENT:** The estimate is derived entirely from the bottom up with no external benchmarking. No reference class is cited.

**Canonical failure:** Scottish Parliament Building — bottom-up estimates of £50–90m were accepted without reference to comparable civic buildings; outturn was £431m.

**Follow-up question template:** "Which reference class database was used? What is the P50 and P80 implied by that class, and how does your estimate compare?"

**Suggest:** `/perplexity-search` or `/literature-review` to find comparable project benchmarks.

---

## SYS-08 — Model the integration phase as its own major project

**What it means:** System integration, testing, commissioning, and operational readiness are almost always underplanned. They must have their own work breakdown structure, schedule, budget, and resources — not be treated as a tail activity.

**PRESENT:** An integration and commissioning sub-plan exists with its own schedule, budget allocation, system integration test facility or strategy, and ORAT (Operational Readiness and Airport/Asset Transition) equivalent.

**PARTIAL:** Integration is on the schedule as a phase but has no separate budget, no integration test strategy, and is resourced from the same pool as the construction workforce.

**ABSENT:** Integration is not explicitly planned; the project plan runs from construction complete to operations start with no intermediate integration stage.

**Canonical failure:** Crossrail — system integration was initially budgeted at roughly £400m and eventually cost multiples of that; safe-assurance alone became a years-long sub-programme.

**Follow-up question template:** "Show me the integration sub-project plan. What is its budget, its schedule from first system-level test to operational handover, and who is the integration director?"

---

## SYS-09 — Separate readiness checks for supply chain and workforce

**What it means:** Supply-chain and workforce constraints are systemic project risks, not procurement problems. The definition must identify single points of failure in the supplier base and assess whether the qualified workforce exists.

**PRESENT:** A supplier heat map or readiness assessment identifies the top-10 critical suppliers/subcontractors, their capacity constraints, and QA maturity. A craft-labour and skills plan covers peak workforce demand.

**PARTIAL:** Key contractors are identified but their capacity or QA capability has not been independently assessed. Workforce numbers are estimated but not validated against market availability.

**ABSENT:** Supply chain is described as "competitive market; procurement to proceed in due course." No supplier-level risk analysis. No workforce availability study.

**Canonical failures:** Olkiluoto 3, Flamanville 3 — subcontractors were inadequately vetted for nuclear-grade QA; welder and quality documentation failures led to years of rework.

**Follow-up question template:** "Name your three riskiest suppliers. What is their current backlog? Have they been independently audited for QA maturity on this type of work?"

---

## SYS-10 — Stakeholders are part of the system, not the communications margin

**What it means:** Any party that can materially delay, reshape, or stop the project — communities, regulators, political actors, adjacent landowners — is a system element, not an external communications target. Their power, legitimacy, and likely timing of intervention must be mapped.

**PRESENT:** A stakeholder power/legitimacy map identifies every party that can delay or veto the project, specifies the mechanism (legal challenge, regulatory objection, political intervention), and the earliest date each could act. Mitigation strategies address system-level dependencies, not just communication plans.

**PARTIAL:** A stakeholder register exists but focuses on engagement and communication rather than influence, power, and potential intervention mechanisms.

**ABSENT:** Stakeholder management is a communications workstream only. No analysis of who can stop or delay the project and how.

**Canonical failures:** Pascua-Lama — water and glacier rights were treated as community-relations issues; environmental court rulings made the project physically undeliverable.

**Follow-up question template:** "Who has the legal, regulatory, or political power to stop or materially delay this project? What is the earliest they could act, and what would trigger them?"

---

## SYS-11 — Stress-test the business case under policy, price, and demand scenarios

**What it means:** The business case must be tested under at least three adverse scenarios: a policy/regulatory shift, a commodity/price movement, and a demand shock. The project should remain viable (or clearly non-viable) under each.

**PRESENT:** A scenario matrix covers at least three stress cases with quantified impacts on NPV/IRR and identifies the key triggers that would make the project non-viable.

**PARTIAL:** Sensitivity analysis exists (e.g., tornado chart) but scenarios are one-dimensional and don't model compounding effects or policy changes.

**ABSENT:** The business case presents a single base case with no scenario testing. Upside and downside are not explored.

**Canonical failure:** Longannet CCS — the business case assumed a stable carbon-price-floor that was later frozen by government policy; the project was not stress-tested against this scenario.

**Follow-up question template:** "What happens to the IRR if carbon price drops 50%, or the subsidy mechanism changes, or demand is 20% below forecast? At what point does the project cross below hurdle rate?"

**Suggest:** `/what-if-oracle` for structured multi-branch scenario analysis of the business case.

---

## SYS-12 — Define kill criteria explicitly

**What it means:** Before FID, the project must have explicit, pre-agreed conditions under which scope is reduced, sequencing is changed, or the project is stopped. Without these, sunk-cost psychology keeps failing projects alive.

**PRESENT:** A kill/recycle criteria register identifies 3–5 specific, measurable conditions that would trigger a formal decision to stop or restructure. The register has been approved at sponsor/board level.

**PARTIAL:** The project charter refers to "regular stage-gate reviews" or "board oversight" without defining specific triggering conditions.

**ABSENT:** No kill criteria are defined. There is an implicit assumption that the project will proceed once started.

**Canonical failures:** NHS NPfIT, Nimrod MRA4 — both continued for years past the point where independent analysis would have recommended termination; neither had pre-defined kill criteria.

**Follow-up question template:** "Under what three specific, measurable conditions would the board be obligated to put this project on hold or cancel it? Are those criteria written down and approved?"

---

## SYS-13 — Assess operations and maintenance in the definition phase

**What it means:** The operating model, maintenance regime, data handover requirements, and long-term funding of the asset must be designed before the asset is built — not after. Late O&M design often forces expensive retrofits and creates day-one operational failures.

**PRESENT:** A ConOps (Concept of Operations) or equivalent documents how the asset will be operated, maintained, staffed, data-managed, and financially sustained. It has been co-developed with the future operator, not written by the project team alone.

**PARTIAL:** High-level operating assumptions exist but the maintenance regime, staffing model, data architecture, and lifecycle cost are not yet defined.

**ABSENT:** Operations and maintenance are described as "to be developed" or "operator responsibility post-handover."

**Follow-up question template:** "Who is the operator? Have they co-authored the ConOps? What is the annual opex estimate, who funds it, and how will the digital/data assets be handed over?"

---

## SYS-14 — Treat FOAK as a learning programme, not a serial project

**What it means:** First-of-a-kind projects require materially larger reserves, more frequent decision points, stronger governance, and explicit knowledge-capture mechanisms. Estimating and planning them like nth-of-a-kind projects is a systematic error.

**PRESENT:** The project is explicitly classified as FOAK. Cost and schedule reserves are uplifted relative to comparable NOAK benchmarks with justification. A knowledge-capture plan describes what must be learned for the next unit. The governance model includes more frequent independent reviews.

**PARTIAL:** The FOAK nature is acknowledged in risk narratives but estimates and governance structures are not adjusted accordingly.

**ABSENT:** The FOAK project is planned and estimated using the same assumptions as a mature serial programme. No FOAK premium in reserves or governance.

**Canonical failures:** All three EPR projects (Olkiluoto, Flamanville, Hinkley) suffered from planning the first nuclear unit in a decade as a standard EPC project.

**Follow-up question template:** "What is the explicit FOAK uplift applied to contingency and schedule float, and how was it derived? What are the 5 things this project must learn to make unit 2 materially cheaper?"

---

## SYS-15 — Escalate cluster/platform questions to portfolio level

**What it means:** Some projects only make economic, technical, or regulatory sense as part of a network or cluster. Optimising them as standalone assets creates suboptimal infrastructure that cannot be repurposed. This question must be answered at definition, not execution.

**PRESENT:** The project definition explicitly addresses whether this asset is standalone or part of a platform/cluster. If a cluster, the portfolio-level economics and infrastructure-sharing logic are documented and the standalone vs. cluster trade-off has been evaluated.

**PARTIAL:** The project is aware it may be part of a broader network but the platform economics are not yet formalised, or the decision has been deferred.

**ABSENT:** The project is defined entirely as a standalone asset with no consideration of network effects, shared infrastructure, or portfolio optimisation.

**Canonical failure:** CCS projects generally — individual CCS projects were unable to make transport and storage economics work in isolation; cluster approaches (e.g., East Coast Cluster) proved far more viable.

**Follow-up question template:** "Is this project economically viable as a standalone asset, or does viability depend on shared infrastructure or volume from other projects? Has a portfolio-vs-standalone analysis been done?"

---

## Quick Reference — Five Systemic Blindspots

| Blindspot | Rules most affected |
|-----------|-------------------|
| Legal-regulatory non-integration | SYS-03, SYS-11 |
| Build-before-design-freeze | SYS-04, SYS-09, SYS-14 |
| Late integration economics | SYS-05, SYS-08 |
| Physical-social coupling | SYS-01, SYS-02, SYS-10 |
| Governance fragmentation | SYS-05, SYS-12, SYS-13 |

## Omission Vocabulary

Use exactly these labels in the audit report when flagging missing elements:

- Full value chain not modelled
- Regulatory due diligence missing
- Interface owner unknown
- Integration proof absent
- Outside view missing
- Kill criteria undefined
- Design maturity not validated
- Supply-chain readiness untested
- Business case not stress-tested
- FOAK not treated as learning programme
- Stakeholder legitimacy not mapped
- O&M not in scope of definition

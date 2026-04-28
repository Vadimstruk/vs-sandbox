# RAID Log — PulseField Mobile

> **Type:** Living document. Started at kickoff and continuously updated. Add new entries as they emerge; never delete entries — update status in place so the history is preserved.
> **Replaces:** the older "Assumptions & Constraints Log". The broader RAID structure (Risks, Assumptions, Issues, Dependencies) better fits both Waterfall and Agile profiles.
> **Version:** 1.1 (updated after Charter Review call 2026-04-30 — Auth0 decision locked, R-007 design-lead mitigated, multiple dependencies progressed, 1 new risk + 3 new dependencies + 1 new assumption)
> **Last Updated:** 2026-04-30
> **Confluence:** [URL — pending]

---

## How to Use This Document

**Categories**

| Letter | Category | What it captures |
|---|---|---|
| **R** | Risk | Something that *might* happen and would have an adverse impact if it did. |
| **A** | Assumption | Something we are treating as true without yet validating it. |
| **I** | Issue | Something that *has* happened and is currently impacting the project. |
| **D** | Dependency | Something the project relies on from another team, system, vendor, or workstream. |

**Status values:** Open · Confirmed · Mitigated · Invalidated · Partially Invalidated · Closed · Superseded.

**ID conventions:** R-001…, A-001…, I-001…, D-001….

**Single-product project** — no `Project` column.

---

## 1. Risks Register

| ID | Risk | Probability | Impact | Mitigation | Owner | Status | Date Raised | Last Updated |
|---|---|---|---|---|---|---|---|---|
| R-001 | **Scope ambiguity** — "mobile app" was broad at sales hand-off; platforms, feature scope, and offline behaviour all undefined. | High | High | At kickoff: scope bounded — MVP defined as 5 ranked features with explicit cuts; Out-of-Scope expanded to 8 explicit exclusions; iOS 15+ / Android 10+ phone only; offline-by-default with sync-when-available. | BA (Vadim) | **Mitigated** | 2026-04-28 | 2026-04-28 |
| R-002 | **Timeline realism** — EoQ3 may not be feasible given offline complexity and integration discovery. | High | High | Driver clarified at kickoff: ServiceTitan competitor pressure peaks Q4. Tolerance: 1mo slip OK, 3mo not OK. Marcus's preference: solid early-Q4 over shaky Q3. Roadmap baseline must lock realistic Now / Next / Later buckets before any work commits. | PM (TBC) | Open | 2026-04-28 | 2026-04-28 |
| R-003 | **Legacy integration risk** — FieldPulse Web Platform built years ago by Tomás Ribeiro (freelance). | High | High | Better-bounded at kickoff: APIs RESTful / JSON, mostly sane, inconsistent endpoint naming, no formal versioning. Documentation = Postman collection + 60%-accurate README. Tomás on 5hr/week retainer for consultation. Last touched 4 months ago. **Mitigation:** focused tech-discovery sprint with Priya immediately after Vision/Roadmap; Tech Lead to author ADR on integration approach; Priya to share platform-architecture one-pager before next status call. | Tech Lead (TBC) | Open | 2026-04-28 | 2026-04-28 |
| R-004 | **Budget mismatch** — "reasonable" was undefined at sales hand-off; may not align with the cost of a production-grade mobile app. | Medium | High | Anchor confirmed at kickoff: **$180K–$250K** envelope. Above $250K requires angel-investor conversation. Below $180K risks corner-cutting. Roadmap and MVP scoping must fit within envelope or trigger CR. | PM (TBC) | **Mitigated** | 2026-04-28 | 2026-04-28 |
| R-005 | **Org maturity** — FieldPulse's first project of this scope; process / governance / sign-off / approval workflow being established jointly. | Medium | Medium | Governance now defined at kickoff: sign-off thresholds (Marcus alone <10% scope; Marcus + Priya ≥10%); SLAs (48hr / same-day / 3-day reviews); Slack as primary channel; weekly Tue/Wed AM Central status calls. Ongoing risk: first-time-at-this-scope coordination. | BA (Vadim) | Open | 2026-04-28 | 2026-04-28 |
| R-006 | **SOC 2 readiness** — FieldPulse is pursuing SOC 2 certification in 2026 in parallel with the mobile project. Mobile build must not be a barrier. | High | High | Architecture decisions (auth, logging, audit trails, data handling) must be made with SOC 2 controls in mind. Coordinate with FieldPulse's SOC 2 auditor's readiness assessment as it firms up. ADRs to call out SOC 2 implications explicitly. | Tech Lead (TBC) + Marcus | Open | 2026-04-28 | 2026-04-28 |
| R-007 | **No design lead at FieldPulse** — Marcus self-identified at kickoff. Risks UX quality and a clear design-approval path on the FieldPulse side. | Medium | Medium | **Mitigation locked 2026-04-30:** Marcus opted not to hire a contract designer (hiring delay, ramp-up time, another voice in a small room). Relevant UX Designer carries design weight; **bi-weekly design review cadence** with mockups walked through **live, not as static files**; **decisions captured in writing after each review** (Marcus's worry: decisions made in conversation get forgotten). Marcus + Jenna sign off at clear milestones. | UX Designer (TBC) + Marcus | **Mitigated** | 2026-04-28 | 2026-04-30 |
| R-008 | **Auth0 dependency** — *(reframed 2026-04-30)* FieldPulse is migrating off custom-rolled auth onto Auth0 (web platform: 4–6 mo, Aug–Oct 2026 target). Mobile decision locked: **Auth0 from day one** in a parallel environment. **Residual risk:** web-platform Auth0 migration slips materially → mobile depends on a parallel Auth0 environment that may grow more complex than modelled (particularly hash-import compatibility for ~950 accounts). | Medium | Medium | Decision locked at Charter Review call 2026-04-30: Auth0 from day one. Mobile builds against parallel Auth0 environment; web migration runs on its own track. ADR drafted by Tech Lead within 2 weeks (target ~2026-05-14), accepted by Priya. Priya prepping Auth0 setup briefing this week. **D-006 closed; D-012 opened to track ADR + Tech Lead intro.** | Tech Lead + Priya | **Mitigated** *(decision locked; residual web-migration-slip risk monitored)* | 2026-04-28 | 2026-04-30 |
| R-009 | **Absent data-residency and breach-notification policies** — FieldPulse has no formal policies in either area today. Material gap given CCPA exposure and SOC 2 timing. | Medium | High | **Updated 2026-04-30:** policies drafted as part of FieldPulse SOC 2 program (kickoff late May 2026; both policies drafted by July 2026). **Owner: Priya** (with input from D-009 lawyer). Project operates to a working US-only data-residency assumption until formal policies land. Captured as Issues I-001 / I-002. | **Priya** *(updated)* + BA | Open | 2026-04-28 | 2026-04-30 |
| R-010 | **Offline state-management / conflict-resolution complexity** — flagged by Priya at kickoff as architecturally non-trivial. | Medium | High | Architecture spike during Vision / Roadmap phase: choose conflict-resolution strategy (last-write-wins / CRDTs / explicit user reconciliation) and prove out with a thin slice. Document in ADR. Avoid over-engineering: scope to MVP feature set. **Directional input 2026-04-30 (Priya):** instinct is last-write-wins + clear conflict-banner UX for the rare contested case; spike's call to confirm. | Tech Lead (TBC) | Open | 2026-04-28 | 2026-04-30 |
| R-011 | **Implicit post-launch support scope addition** — Marcus asked at kickoff for **60–90 days of post-launch support** from Relevant. Not in original budget framing. | High | Medium | **Mitigation locked 2026-04-30:** priced **inside the $180K–$250K envelope** (Marcus's call). Acknowledged trade-off: may pressure MVP scope. **R-005 Schedule View flagged as first MVP-flex candidate** if envelope is tight. Reflected in Charter v1.1 §3 + §4 and Roadmap R-015. | PM + BA | **Mitigated** *(pricing locked; MVP-flex strategy named)* | 2026-04-28 | 2026-04-30 |
| R-012 | **Tomás retainer continuity** *(new 2026-04-30, per Priya)* — 5hr/wk retainer for FieldPulse Web Platform consultation is **verbal, not contractual**. If Tomás becomes unavailable mid-engagement, legacy-platform discovery loop slows. | Low | Medium | Build internal knowledge of legacy platform via Priya's architecture one-pager (D-008) + Tech Lead discovery to reduce dependency on Tomás. Tomás reachable on current 5hr/wk arrangement; do not assume more than that. Watch for signal of unavailability and escalate early. | Priya + Tech Lead (TBC) | Open | **2026-04-30** | 2026-04-30 |

---

## 2. Assumptions Register

### Technical & Infrastructure

| ID | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|
| A-001 | The existing FieldPulse Web Platform exposes APIs sufficient for a mobile client to retrieve job assignments and submit completed job data. | **Confirmed** | n/a — confirmed by Priya at kickoff (RESTful / JSON, Postman collection, freelancer-accessible). Quality nuances captured in R-003. | Tech Lead (TBC) | 2026-04-28 | Priya, kickoff call 2026-04-28: APIs exist, RESTful / JSON, mostly sane, inconsistent naming, no formal versioning, "okay — not great, not a disaster". Postman collection + 60% README available. |
| A-002 | Mobile app must access the FieldPulse Web Platform via API only — no direct database access. | **Confirmed** | n/a | Priya | 2026-04-28 | Priya, kickoff call: hard line, confirmed. |

### Business & Domain

| ID | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|
| A-003 | Marcus Chen has sole sign-off authority on requirements, scope, CRs, UAT, and go-live. | **Confirmed** *(with nuance)* | n/a | BA (Vadim) | 2026-04-28 | Marcus, kickoff call: sole sign-off confirmed. CR threshold added: <10% scope = Marcus alone; ≥10% scope = Marcus + Priya. Reflected in Charter v1.0 §4 and Stakeholder Register §5 RACI. |
| A-004 | Priya Krishnan (CTO) is the designated primary technical counterpart on the FieldPulse side for the duration of the engagement. | **Confirmed** | n/a | BA (Vadim) | 2026-04-28 | Marcus + Priya, kickoff call: confirmed. |
| A-005 | Deployment is US-only; no international or multi-language support is in scope. | **Confirmed** | n/a — Canadian (Ontario) customers operate on the US version, no localisation | BA (Vadim) | 2026-04-28 | Marcus, kickoff call: 2 Canadian customers fine on US version, no localisation, no international expansion in project window. |
| A-006 | The application has no direct regulatory burden of its own (B2B SaaS for contractors); customer-imposed obligations (e.g. SOC 2 from FieldPulse's customers) were not yet known. | **Partially Invalidated** | Significant compliance scope (audit, data handling, certification) added — directly hits Charter Section 4 (Constraints) and the Roadmap. | BA (Vadim) | 2026-04-28 | Marcus, kickoff: CCPA applies (CA customers); SOC 2 work in flight in 2026 regardless; some customers do school-district / municipal work — gov-contractor flow-down implications unknown. **Update 2026-04-30:** holding for D-009 legal-review findings (lawyer engaged by 2026-05-08; findings mid–late May, worst case early June). Marcus to update with concrete answers in May. |

### Process & Delivery

| ID | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|
| A-007 | The engagement runs as Agile — Fixed-Range, with the Roadmap as the CR baseline. | Confirmed | n/a | BA (Vadim) | 2026-04-27 | Confirmed by Vadim during profile-setting on 2026-04-27. **Refined 2026-04-30:** CR scope is measured against the Roadmap baseline once signed off, *not against the Charter* (Marcus's clarification at the Charter Review call). Charter is the high-level contract; Roadmap is the working baseline. Reflected in Charter v1.1 §4 Governance row. |
| A-008 | **Capacity assumption — Relevant team shape:** $180K–$250K envelope sized to BA + PM + Tech Lead + 2 mobile devs + QA + part-time DevOps + part-time UX Designer. *(New 2026-04-30 — Marcus saw the Roadmap internal note and asked us to confirm before assuming.)* | Open | If team shape is smaller or part-timers thinner than modelled, Roadmap Now-bucket is over-committed at sign-off → R-015 envelope-pressure on MVP scope kicks in earlier than Marcus expects. | PM (TBC) + BA | 2026-04-30 | Confirm at next status call (Wed 2026-05-06). |

---

## 3. Issues Register

| ID | Issue | Impact | Resolution Path | Owner | Status | Date Raised | Date Resolved |
|---|---|---|---|---|---|---|---|
| I-001 | **No formal data-residency policy at FieldPulse** — Marcus self-identified at kickoff. | Until resolved: project operates to a working US-only data-residency assumption. Customer-data flow-down (CCPA exposure, gov-contractor contracts) cannot be verified. Affects R-006 (SOC 2 readiness) and R-009. | **Updated 2026-04-30:** drafted under FieldPulse's SOC 2 program (kickoff late May 2026; both policies drafted by July 2026). **Owner: Priya** with input from D-009 lawyer. Priya loops Vadim in if anything affects mobile. | **Priya** *(updated)* | Open | 2026-04-28 | |
| I-002 | **No formal breach-notification procedures at FieldPulse** — Marcus self-identified at kickoff. | Without procedures, FieldPulse cannot meet CCPA's 72-hour notification window if a breach occurred today. Affects R-009 and SOC 2 readiness. | **Updated 2026-04-30:** drafted under FieldPulse's SOC 2 program alongside I-001 (kickoff late May; drafts by July 2026). **Owner: Priya** with input from D-009 lawyer. | **Priya** *(updated)* | Open | 2026-04-28 | |
| I-003 | **No design lead at FieldPulse** — Marcus self-identified at kickoff. | UX quality and FieldPulse-side design-approval path both at risk. Affects R-007. | **Mitigation locked 2026-04-30:** Marcus opted not to hire contract designer. Relevant UX Designer leads with **bi-weekly design review cadence** (mockups walked live, decisions captured in writing); Marcus + Jenna sign off at clear milestones. | UX Designer (TBC) + Marcus | **Mitigated** | 2026-04-28 | 2026-04-30 |
| I-004 | **FieldPulse anonymisation tooling does not exist** — surfaced when discussing UAT test data (§8.2). | Synthetic test data is mandatory for staging — Priya cannot provide anonymised customer data. UAT setup may take longer if synthetic-data generation is non-trivial. | Priya to set up staging with seeded synthetic jobs / technicians / customers per kickoff §8.2. Tech Lead and QA to define synthetic-data generation approach early. | Priya + QA (TBC) | Open | 2026-04-28 | |

---

## 4. Dependencies Register

| ID | Dependency | Type | Owner | Needed By | Status | Date Raised | Notes |
|---|---|---|---|---|---|---|---|
| D-001 | API access and documentation for the FieldPulse Web Platform. | Internal — Vendor (FieldPulse / Tomás) | Priya Krishnan | Before Roadmap baseline — direct integration scoping | **Confirmed** | 2026-04-28 | Postman collection + 60%-accurate README in hand. Priya committed to a platform-architecture one-pager before next status call. Tomás reachable on 5hr/wk retainer. |
| D-002 | Confirmed budget envelope from Marcus. | Internal — Client | Marcus Chen | Roadmap baseline | **Confirmed** | 2026-04-28 | $180K–$250K. Above $250K requires angel-investor conversation. |
| D-003 | Confirmed timeline target from Marcus. | Internal — Client | Marcus Chen | Roadmap baseline | **Confirmed** *(soft)* | 2026-04-28 | Rough EoQ3 preference; 1mo slip OK; prefers solid early-Q4 over shaky Q3. ServiceTitan competitor pressure is the underlying driver. |
| D-004 | Sundance HVAC pilot agreement — Marcus to confirm pilot participation with Dave Martinez. | External — Pilot Customer | Marcus Chen → Dave Martinez | Before MVP delivery (UAT planning) | **Verbally Confirmed (Written Pending)** | 2026-04-28 | **Updated 2026-04-30:** Marcus called Dave Martinez Friday 2026-04-24 — Dave verbally committed; **3 technicians (team rotation, not solo testers)**; Dave wants a one-page pilot summary before written commitment. Realistic written-confirmation ETA: 2 weeks once Dave has the one-pager (D-010). |
| D-005 | Tomás Ribeiro continued availability for legacy-platform consultation (5 hours/week retainer). | External — Vendor | FieldPulse / Tomás | Throughout integration discovery and build | **Confirmed** *(at current arrangement — verbal, not contractual)* | 2026-04-28 | **Updated 2026-04-30** *(per Priya):* retainer is **verbal, not contractual**. Continuity not contractually guaranteed. Plan should not assume more than 5hrs/week. Continuity risk tracked under R-012. |
| D-006 | Coordination with FieldPulse's Auth0 migration if PulseField Mobile work touches login flows. | Internal — Cross-team (FieldPulse) | Priya Krishnan | Before architecture decisions | **Closed** | 2026-04-28 | **Closed 2026-04-30:** Auth0 decision locked at Charter Review call — PulseField Mobile authenticates against Auth0 from day one in a parallel environment. ADR + Tech Lead intro tracked under D-012. |
| D-007 | Marcus's notes from customer conversations (~15 pages, Notion) and a whiteboard sketch photo (~6 months old). | Internal — Client | Marcus Chen | Before MVP definition (PRD draft) | **In Progress** | 2026-04-28 | **Updated 2026-04-30:** Whiteboard photo — Marcus shares same-day (2026-04-30, no cleanup). Notion notes — Marcus does one cleanup pass first; cleaned version delivered by **EoW Friday 2026-05-02**. |
| D-008 | Priya's one-pager on existing platform architecture for the Relevant tech lead. | Internal — Client | Priya Krishnan | Before MVP definition / Tech Lead discovery | **In Progress** | 2026-04-28 | **Updated 2026-04-30:** Draft exists. Priya extending one extra day to include the **API endpoint inventory** (not just architecture diagram). Realistic delivery: **EoD Wed (~2026-05-06) — TBC with Priya**. R-006 6-week clock starts on receipt. |
| D-009 | Legal review of regulatory exposure — CCPA, gov-contractor flow-down, SOC 2 timeline implications. | External — Client legal | Marcus Chen | Charter v1.2 amendment (anticipated) | Open | 2026-04-28 | **Updated 2026-04-30:** Marcus does not yet have outside counsel. Path: existing Austin firm (incorporation counsel — needs scope brief) or privacy-specialist firm. **Lawyer engaged by EoW 2026-05-08.** Scope: **CCPA exposure assessment, gov-contractor flow-down (school-district + municipal-building customers), SOC 2 readiness gap analysis.** Turnaround: 2–3 weeks post-engagement. **Findings: mid–late May 2026, worst case early June.** Drives Charter v1.2 amendment. Affects A-006, R-006, R-009, I-001, I-002, R-003 (retention), R-011 store privacy policy. |
| D-010 | **Sundance pilot one-pager** *(new 2026-04-30)* — Relevant to draft a one-page pilot summary for Marcus to forward to Dave Martinez. | Internal — Relevant | BA (Vadim) → Marcus → Dave | Before D-004 written confirmation | Open | 2026-04-30 | Target draft: 2026-05-01. Marcus forwards to Dave. Realistic written-confirmation ETA: 2 weeks after Dave receives. |
| D-011 | **Slack workspace + invites** *(new 2026-04-30)* — Priya creates `#pulsefield-mobile` channel; Vadim sends work emails of PM + Tech Lead by EoD 2026-04-30. | Internal — Cross-team | Priya (channel) + Vadim (emails) | EoD 2026-04-30 | In Progress | 2026-04-30 | `fieldpulse.slack.com`. Both halves committed at the Charter Review call. |
| D-012 | **Auth0 ADR + Tech Lead intro** *(new 2026-04-30)* — Priya's Auth0 setup briefing → intro between Priya and Relevant Tech Lead → ADR drafted by Tech Lead → accepted by Priya. | Internal — Cross-team | Priya + Tech Lead (TBC) | ADR target ~2026-05-14 | In Progress | 2026-04-30 | Priya prepping briefing this week (target EoW 2026-05-02). Tech Lead intro this week. ADR within 2 weeks of call. Closes D-006. |

---

## 5. Constraints Register

| ID | Constraint | Type | Impact | Owner |
|---|---|---|---|---|
| C-001 | Must integrate with the existing FieldPulse Web Platform — not replace it. | Technical / Scope | All architecture and integration choices are downstream of the legacy platform's capabilities. | Tech Lead (TBC) |
| C-002 | API-only access to the legacy platform — no direct DB access. | Technical | Confirmed by Priya at kickoff. Hard line. | Tech Lead (TBC) |
| C-003 | Offline-by-default with sync-when-available. | Technical / UX | Drives architecture (state management, conflict resolution), QA (low-connectivity simulation), and UX (visible offline / sync states). | Tech Lead + UX Designer |
| C-004 | Both iOS (15+) and Android (10+) phones; no tablet support. | Technical / Scope | Two platforms doubles native development effort; minimum-OS targets exclude older devices but cover the bulk of real-world technician phones. If forced to phase, Android takes priority. | Tech Lead (TBC) |
| C-005 | Budget envelope $180K–$250K for the calendar year. | Business | Above $250K requires angel-investor conversation. Below $180K risks corner-cutting. | PM (TBC) |
| C-006 | FieldPulse is a small SaaS startup, not an enterprise. Process, governance, and budget reflect that scale. | Business | Lightweight, transparent CR rhythm fits better than heavyweight enterprise governance. | PM (TBC) |
| C-007 | Production-release blackout windows. | Business | No production releases late June – August (HVAC summer cooling peak). Soft windows: September, October. Avoid the two-week windows around Thanksgiving, Christmas, July 4th. **Update 2026-04-30:** Sundance pilot must end before Phoenix peak (early July latest) — backs up implementation timing. | PM (TBC) |
| C-008 | **Status-call cadence** *(new 2026-04-30)* — Wednesday 9am Central, 30 min hard stop. | Governance | Weekly status reviews; the standing forum for Roadmap maintenance, RAID confirmations, capacity check-ins. | PM (TBC) + BA |
| C-009 | **EoF Friday written status** *(new 2026-04-30)* — bullet points, ≤1 screen on Marcus's laptop, recipients Marcus + Priya. | Governance | Asynchronous keep-alive between status calls. *"If it's longer than one screen I'll bounce it back."* | PM (TBC) + BA |
| C-010 | **CR baseline = Roadmap once signed off, not Charter** *(new 2026-04-30 — Marcus's clarification)*. | Governance / Process | Tech Lead and PM must measure scope deviations against the Roadmap baseline, not the Charter. Charter is the high-level contract; Roadmap is the working baseline. Reflected in Charter v1.1 §4 Governance row. | PM (TBC) + BA |

---

## Change History

| Date | Change | By |
|---|---|---|
| 2026-04-28 | RAID Log v0.1 initialised — 5 risks, 6 assumptions (1 confirmed), 0 issues, 3 dependencies, 2 constraints — seeded from Sales brief and from confirmed profile. | Homer (Relevant BA) |
| 2026-04-28 | RAID Log v1.0 — promoted after kickoff call. R-001 / R-004 → Mitigated. R-002 / R-003 / R-005 status held with refined mitigations. New risks R-006 to R-011 added (SOC 2 readiness, no design lead, Auth0 overlap, absent data-residency / breach policies, offline complexity, implicit post-launch support scope). A-001 / A-002 / A-003 / A-004 / A-005 → Confirmed; A-006 → Partially Invalidated. New issues I-001 to I-004 (data residency, breach policy, design lead, anonymisation tooling). New dependencies D-004 to D-009 (Sundance pilot, Tomás continuing availability, Auth0 coordination, Notion notes / sketch, platform-architecture one-pager, legal review). New constraints C-003 to C-007 (offline-by-default, platform versions, budget envelope, org-scale, blackout windows). | Vadim / Homer |
| 2026-04-30 | RAID Log v1.1 — updated after Charter Review call. **Closures / mitigations:** R-007 No design lead → Mitigated (bi-weekly design-review cadence; live walkthrough; written decisions). R-008 Auth0 overlap → Mitigated (decision locked: Auth0 from day one; residual web-migration-slip risk monitored). R-011 Post-launch-support scope → Mitigated (priced inside envelope; R-005 first MVP-flex candidate). I-003 No design lead → Mitigated (R-007 mitigation). D-006 Auth0 coordination → Closed (decision locked). **Updates:** R-009 / I-001 / I-002 owner → Priya (drafted under SOC 2 program, drafts by July 2026). R-010 directional input — Priya: last-write-wins + conflict-banner. A-006 holding for D-009. A-007 refined (CR baseline = Roadmap, not Charter). D-004 → Verbally Confirmed (Written Pending) — 3 techs team rotation. D-005 Tomás retainer noted as verbal-not-contractual. D-007 → In Progress (whiteboard 2026-04-30; Notion EoW 2026-05-02). D-008 → In Progress (EoD Wed ~2026-05-06 TBC, with API endpoint inventory). D-009 scope clarified (CCPA + gov-contractor flow-down + SOC 2 readiness gap; lawyer by 2026-05-08; findings mid–late May). C-007 update (Phoenix peak constraint on pilot timing). **New entries:** R-012 Tomás retainer continuity. A-008 capacity assumption (confirm at next status call). D-010 Sundance pilot one-pager. D-011 Slack workspace + invites. D-012 Auth0 ADR + Tech Lead intro. C-008 Wed 9am Central status cadence. C-009 EoF Friday written status. C-010 CR baseline = Roadmap. | Vadim / Homer |

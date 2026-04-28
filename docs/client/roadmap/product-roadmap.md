# Product Roadmap — PulseField Mobile

| Field                  | Value                                                          |
|------------------------|----------------------------------------------------------------|
| **Version**            | 2026-04 v1.1                                                   |
| **Methodology**        | Agile — Fixed-Range                                            |
| **Last Reviewed**      | 2026-04-30 (Charter Review call — Marcus walked top-to-bottom; approved with 7 amendments, all applied below) |
| **BA Owner**           | Vadim — Relevant Software                                      |
| **Capacity Reviewer**  | PM / Tech Lead (TBC — Relevant)                                |
| **Vision Ref**         | `docs/client/vision/product-vision.md`                         |

> **Living document.** No baseline sign-off; reviewed monthly with the client.
> This Roadmap is the **CR baseline** — Change Requests measure scope deviations against the most recently agreed version. Cite from a CR as `Roadmap 2026-04 → "<Initiative Name>" (R-XXX)`.
>
> **Blackout windows for production releases** (per Kickoff Meeting §8.5): avoid late June – August (HVAC summer cooling peak); avoid two-week windows around Thanksgiving, Christmas, July 4th. Soft go-live windows: September, October.

---

## Themes

| Theme ID | Theme                              | Description |
|----------|------------------------------------|-------------|
| T-1      | Mobile-First Field Workflow        | The core technician-facing experience that replaces SMS-plus-paper with a single mobile workflow. |
| T-2      | Operational Readiness              | The platform, integration, security, and store-distribution work that lets the mobile workflow actually ship. |
| T-3      | Customer Adoption & Rollout        | Getting PulseField Mobile into real technician hands at FieldPulse customers — pilot, rollout, training, post-launch support. |
| T-4      | Platform Modernisation Alignment   | Coordination with FieldPulse's parallel work (Auth0 migration, SOC 2 readiness, future accounting integrations) so mobile does not become a barrier to either. |

---

## Now

> Currently being implemented or about to start. These are what *Create Epics & Stories* (BMad SM) decomposes into Jira epics and stories.

### R-001 — Job Dispatch & Receive

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Committed (pending light Roadmap agreement)                    |
| **Target Window** | Q2 → Q3 2026                                                   |
| **Effort**        | M                                                              |
| **Source CR**     | — (original MVP scope from Charter v1.0 §3 In-Scope #1)        |

**Description:**
> Replace the SMS-plus-phone-back-to-office workflow with a job assignment view in the mobile app that delivers full job context — customer name, address, work type, prior history, scheduled time — directly to the technician's device.

**Success signals:**
- Technicians no longer need to phone the office to clarify job context for jobs received via the app.
- Office dispatchers see "received / read" status in the FieldPulse Web Platform.

**Key constraints / dependencies:**
- D-001 Legacy API access (Confirmed) — drives R-006.
- C-003 Offline-by-default — affects how "received" state is tracked when the device is offline at dispatch time.

---

### R-002 — Offline Job-Completion Capture

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Committed                                                      |
| **Target Window** | Q2 → Q3 2026 (longest-pole MVP item — depends on R-007)        |
| **Effort**        | L                                                              |
| **Source CR**     | — (Charter §3 In-Scope #2)                                     |

**Description:**
> Technician captures job-completion data on-site — checklist, free-form notes, photos, parts used, time on site — fully offline. Form persists locally until connectivity returns.

**Success signals:**
- A technician can complete an entire job in a basement with no signal and submit the data later without losing any of it.
- Sundance pilot technicians complete ≥80% of pilot jobs through the app rather than reverting to paper.

**Key constraints / dependencies:**
- R-010 Offline state-management complexity (Open) — primary risk for this initiative.
- C-003 Offline-by-default — defining requirement.
- R-007 (this Roadmap) — depends on offline architecture decision.

---

### R-003 — Customer Signature Capture

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Committed                                                      |
| **Target Window** | Q3 2026                                                        |
| **Effort**        | S *(may shift pending D-009 — see retention note below)*       |
| **Source CR**     | — (Charter §3 In-Scope #3)                                     |

**Description:**
> At the end of a job, the technician collects the customer's signature on-device. Signature persists offline and submits with the job-completion record.

**Success signals:**
- Signed-job records meet the 2–7 year retention expectation captured in Kickoff Meeting §3.4 (a customer expectation, not regulatory).
- Sign-off captures cleanly across phones in the supported Android 10+ / iOS 15+ range.

**Key constraints / dependencies:**
- C-003 Offline-by-default.
- R-002 — signature is part of the job-completion form.

> **Retention scope may firm up post legal review (D-009)** *(flagged 2026-04-30)* — could shift from a customer expectation to a contractual or regulatory requirement once findings land. May affect effort sizing.

---

### R-004 — Sync to Web Platform

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Committed                                                      |
| **Target Window** | Q2 → Q3 2026                                                   |
| **Effort**        | L                                                              |
| **Source CR**     | — (Charter §3 In-Scope #4)                                     |

**Description:**
> When connectivity returns, completed job data and status updates flow back to the FieldPulse Web Platform via API. Updates surface in the dispatcher view in near-real-time. Headline business outcome: same-day billing-cycle compression.

**Success signals:**
- Sync works reliably under low-connectivity simulation (go-live criterion, Kickoff Meeting §8.3).
- Billing-cycle time-to-invoice for app-handled jobs falls from ~2 days to same-day for ≥80% of pilot jobs.

**Key constraints / dependencies:**
- D-001 Legacy API access — sync writes target the existing FieldPulse APIs.
- R-007 — conflict resolution for late-arriving offline data.

---

### R-005 — Technician Schedule View

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Committed                                                      |
| **Target Window** | Q3 2026                                                        |
| **Effort**        | S                                                              |
| **Source CR**     | — (Charter §3 In-Scope #5)                                     |

**Description:**
> "What's my day look like" view — list of upcoming jobs for the technician, grouped or sorted by scheduled time. Read-only in MVP; routing and rescheduling are out of scope.

**Success signals:**
- Technicians use the schedule view to plan their day rather than calling dispatch.
- Renders correctly when the device is offline (cached jobs visible without round-trip).

**Key constraints / dependencies:**
- D-001 Legacy API access (read).
- C-004 Phone-only.

---

### R-006 — Legacy API Integration & Hardening

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-2                                                            |
| **Status**        | In Progress (Tech Lead discovery — pending Priya's architecture one-pager, D-008) |
| **Target Window** | Q2 2026 (front-loaded — gates R-001, R-004, R-005)             |
| **Effort**        | M                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Discovery and targeted hardening of the FieldPulse Web Platform's APIs to support the mobile client. Includes API-contract review against the existing Postman collection + 60%-accurate README, naming-consistency improvements where they block client work, and a **proxy / wrapper layer planned (not conditional)** to insulate the mobile app from legacy quirks. *Updated 2026-04-30 per Priya: legacy API has enough naming-convention drift that a wrapper is cleaner long-term.*

**Success signals:**
- Tech Lead can deliver a clean SDK (or equivalent client wrapper) for the mobile app within 6 weeks of receiving Priya's architecture one-pager (D-008, ETA EoD Wed ~2026-05-06 — TBC).
- No mobile-feature-blocking API gaps surface after the discovery phase.

**Key constraints / dependencies:**
- D-001 (Confirmed), D-005 Tomás's 5hr/week retainer, D-008 Priya's architecture one-pager (Open).
- R-003 Legacy integration risk (Open).

---

### R-007 — Offline Architecture & Conflict Resolution

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-2                                                            |
| **Status**        | Committed (architectural spike — ADR target)                   |
| **Target Window** | Q2 2026 (front-loaded — gates R-002, R-004)                    |
| **Effort**        | M                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Architectural spike to choose the offline state-management and conflict-resolution strategy (last-write-wins vs CRDTs vs explicit user reconciliation) and prove it out with a thin slice. Captured in an ADR. **Avoid over-engineering — scope to MVP feature set.** *(Marcus 2026-04-30: "underline in red.")*

**Directional input** *(2026-04-30 — spike's call to confirm, not a commitment):*
> Priya's instinct: **last-write-wins + clear conflict-banner UX** for the rare contested case is enough for MVP. Marcus aligned.

**Success signals:**
- ADR accepted and signed off by Tech Lead and Priya.
- Thin-slice proves the strategy under low-connectivity simulation.

**Key constraints / dependencies:**
- R-010 Offline complexity (Open) — the risk this initiative mitigates.
- C-003 Offline-by-default.

---

### R-008 — Auth Strategy — Decided: Auth0 from Day One

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-4                                                            |
| **Status**        | **Decided — Auth0** *(call 2026-04-30; ADR pending)*           |
| **Target Window** | Q2 2026 (ADR within 2 weeks → ~2026-05-14; implementation in MVP build) |
| **Effort**        | S (decision — ✓) → M (implementation)                          |
| **Source CR**     | —                                                              |

**Description:**
> **PulseField Mobile authenticates against Auth0 from day one** *(decided at Charter Review call 2026-04-30 — Marcus + Priya)*. Mobile builds against a **parallel Auth0 environment** from the start; FieldPulse's web-platform Auth0 migration is in flight (4–6 month horizon, Aug–Oct 2026 target). Both systems coexist briefly; Auth0 does not require web-platform migration to be complete for mobile to use it.

**Reasoning** *(per Priya, accepted by Marcus):*
> Building against custom-rolled auth and migrating later costs 2–3 weeks of mobile engineering wasted; Auth0 gives mobile-friendly flows out of the box (biometric, refresh tokens); SOC 2 Type II certified — custom-rolled auth would be a SOC 2 finding.

**Residual risk:** if FieldPulse's web-platform Auth0 migration slips materially, mobile is exposed on a dependency outside Relevant's control. **Mitigation:** parallel Auth0 environment from the start (Priya owns).

**Success signals:**
- ADR drafted by Relevant Tech Lead **within 2 weeks** of the call (target ~2026-05-14), accepted by Priya.
- Mobile app does not block FieldPulse's Auth0 migration timeline; Auth0 migration delays do not block mobile launch (parallel-environment mitigation holds).

**Key constraints / dependencies:**
- D-006 Auth0 coordination (RAID — **Closed 2026-04-30**, decision locked).
- R-008 RAID — Auth0 overlap risk (**Closed 2026-04-30**; residual web-migration-slip risk tracked under R-008 in Charter §5).
- D-012 RAID — Auth0 ADR + Tech Lead intro (new, In Progress — Priya prepping setup briefing this week).

---

### R-009 — SOC 2-Compatible Foundations

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-4                                                            |
| **Status**        | Committed (cross-cutting; no separate sprint — applies to every other initiative) |
| **Target Window** | Continuous (every Now-bucket initiative respects SOC 2 controls) |
| **Effort**        | XS per initiative (incremental, distributed)                   |
| **Source CR**     | —                                                              |

**Description:**
> Architecture decisions (auth, logging, audit trails, data handling, access controls) made with SOC 2 controls in mind. ADRs explicitly call out SOC 2 implications. Coordinate with FieldPulse's SOC 2 auditor's readiness assessment as it firms up. Goal: PulseField Mobile is *not a barrier* to FieldPulse's parallel SOC 2 work.

**Success signals:**
- SOC 2 readiness assessment finds no blockers attributable to PulseField Mobile.
- Logging and audit-trail patterns in the mobile app match what FieldPulse is implementing on the platform side.

**Key constraints / dependencies:**
- R-006 SOC 2 readiness (RAID, Open) — the risk this addresses.
- D-009 Legal review (Open) — informs scope.

---

### R-010 — Staging Environment with Synthetic Data

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-2                                                            |
| **Status**        | Committed (Priya owns setup per Kickoff Meeting §8.2)          |
| **Target Window** | Q2 2026 (needed before any pilot or UAT activity)              |
| **Effort**        | S                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Priya provisions a staging instance of the FieldPulse Web Platform separate from production, seeded with synthetic jobs / technicians / customers (no anonymised real data — FieldPulse's anonymisation tooling does not exist, per I-004 RAID). **Target: ≥50 synthetic jobs and 10 synthetic technicians up by mid-May 2026** *(Priya commitment, 2026-04-30)*.

**Success signals:**
- Staging instance up, accessible to Relevant team, with ≥50 synthetic jobs and 10 synthetic technicians available by mid-May 2026.
- Sundance pilot prep can run end-to-end against staging without production-data contamination risk.

**Key constraints / dependencies:**
- I-004 No anonymisation tooling — drives the synthetic-only choice.
- Owner: Priya.

---

### R-011 — App Store + Play Store Setup

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-2                                                            |
| **Status**        | Committed                                                      |
| **Target Window** | **Account provisioning Q2 2026** *(starts immediately — see sub-tasks)*; **listings Q3 2026** (lead-time-aware) |
| **Effort**        | S                                                              |
| **Source CR**     | —                                                              |

**Description:**
> FieldPulse-owned developer accounts on Apple App Store and Google Play. App listings, privacy policy, screenshots, review-process readiness. Mobile app go-live criterion (Kickoff Meeting §8.3).

**Sub-tasks** *(Marcus 2026-04-30 — split out for lead-time visibility):*
1. **Apple Developer + Google Play account provisioning — Q2 2026.** Apple verification can take 2–4 weeks for new accounts; do NOT defer this to Q3. Account paperwork is its own timeline distinct from listing prep.
2. **Listing assets + privacy policy — Q3 2026.** Aligned with CCPA exposure (informed by D-009).
3. **Submission + review — Q3 2026.** Both store listings approved before pilot expansion.

**Success signals:**
- Developer accounts provisioned and verified by end of Q2 2026.
- Both store listings approved before pilot expansion to Sundance.
- Privacy policy aligned with CCPA exposure (informed by D-009 Legal Review).

**Key constraints / dependencies:**
- C-004 Phone-only, Android 10+ / iOS 15+ targeted.
- D-009 Legal review (Open) — informs privacy policy.

---

## Next

> Roughly the next 1–3 months out (post-MVP first wave). Detailed for Fixed-Range. Status will move to *Committed* at next monthly review if MVP delivery tracks.

### R-012 — Sundance HVAC Pilot

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-3                                                            |
| **Status**        | **Verbally Confirmed — Written Pending** *(Marcus called Dave Martinez 2026-04-24; written agreement pending one-pager from Relevant)* |
| **Target Window** | **Pilot ends before Phoenix HVAC peak** — end-of-June ideal, **early July latest**. *(Marcus 2026-04-30: "Phoenix HVAC peak is brutal mid-July through August. So pilot end of June ideally, into early July latest.")* |
| **Effort**        | M                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Real-world UAT pilot with Sundance HVAC (Phoenix). **3 of Dave Martinez's technicians (team rotation, not solo testers)** using PulseField Mobile on actual jobs for ≥2 weeks. Internal proxy testing by Jenna Rodriguez + Marcus + Priya completes first.

**Pilot anchor** *(updated 2026-04-30):*
> Pilot timing is anchored to *finish* before Phoenix peak, not start before it. Backs up implementation timing — MVP must be pilot-ready by early/mid-June 2026 to land a 2–3 week pilot ending early July.

**Success signals:**
- Pilot runs ≥2 weeks with no Sev-1 issues (go-live criterion, Kickoff Meeting §8.3).
- Sundance technicians complete jobs end-to-end through the app without paper fallback.
- Marcus, Dave, and the technicians provide structured feedback informing post-pilot work.

**Key constraints / dependencies:**
- D-004 Sundance pilot agreement (Verbally Confirmed; Written Pending).
- D-010 Sundance pilot one-pager (NEW, Open — Vadim drafts; Marcus forwards to Dave; 2-week ETA on written confirmation post-forward).
- C-007 Blackout windows — pilot must end before US summer HVAC peak intensifies.

---

### R-013 — Production Go-Live & Phased Customer Rollout

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-3                                                            |
| **Status**        | Committed (target — exact window pending pilot results)        |
| **Target Window** | Early Q4 2026 — Marcus's preference; September / October soft windows acceptable |
| **Effort**        | M                                                              |
| **Source CR**     | —                                                              |

**Description:**
> After pilot success, phased rollout to FieldPulse customer businesses. Initial wave: 5–10 customers most actively asking for mobile. Subsequent waves grow to year-1 target of 30–40% adoption across the ~80-customer base.

**Success signals:**
- ≥20 of FieldPulse's existing customer businesses have technicians actively using PulseField Mobile within six months of go-live (Vision §4 success indicator).
- Technician daily-active-use rate ≥30% of installed base by month three.

**Key constraints / dependencies:**
- R-012 Pilot — gates broader rollout.
- C-007 Blackout windows.

---

### R-014 — Training Materials

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-3                                                            |
| **Status**        | Committed                                                      |
| **Target Window** | Q3 2026 — ready before pilot                                   |
| **Effort**        | S                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Short videos, not manuals (per Marcus's explicit preference, Kickoff Meeting §8.3). Cover: first-time setup, receiving and acknowledging a job, completing a job offline, signature capture, schedule view. Distributed by Jenna Rodriguez to Sundance pilot and rollout customers.

**Success signals:**
- Videos available before pilot start.
- Sundance technicians can self-onboard from the videos without a live walkthrough.

**Owners:**
- **Relevant:** BA + UX Designer (TBC).
- **FieldPulse:** **Jenna Rodriguez (co-owner)** *(added 2026-04-30 — Jenna runs the customer-facing rollout; Marcus's call)*.

---

### R-015 — Post-Launch Support — Relevant 60–90 Days

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-3                                                            |
| **Status**        | Committed — **Inside Envelope** *(Marcus's call, 2026-04-30)*  |
| **Target Window** | Q4 2026 — Q1 2027 (60–90 days from go-live)                    |
| **Effort**        | M (sustained — bug fixes, minor adjustments, KT)               |
| **Source CR**     | —                                                              |

**Description:**
> Relevant Software provides 60–90 days of post-launch support after PulseField Mobile reaches production: bug fixes, minor adjustments, helping FieldPulse understand production-issue patterns. Followed by knowledge transfer for FieldPulse to operate the system independently.

**Pricing decision** *(Marcus 2026-04-30):*
> **Inside the $180K–$250K envelope.** Marcus's reasoning: budgeting clarity now is worth more than scope optionality later. **Acknowledged trade-off:** this may pressure MVP scope. **R-005 Technician Schedule View is the first candidate to cut from MVP** if envelope is tight. Marcus self-surfaced this — not a unilateral call.

**Success signals:**
- Sev-1 production issues resolved within 24 business hours during the support window.
- Handover completes with FieldPulse confirming operational readiness.

**Key constraints / dependencies:**
- R-011 RAID — implicit-scope risk (mitigation locked: priced inside envelope; MVP-flex strategy named).

---

> **Cut-from-MVP return order** *(Marcus 2026-04-30, if budget headroom appears post-launch):*
> **1st** R-016 In-App Dispatcher Chat → **2nd** R-019 Customer History View → **3rd** R-017 GPS Auto Check-in → **4th** R-018 Parts Inventory.

### R-016 — In-App Dispatcher Chat *(post-MVP wave 1 — **1st return**)*

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Provisional (cut from MVP; **1st in return order** if budget headroom appears) |
| **Target Window** | Q4 2026 → Q1 2027 (pending capacity)                           |
| **Effort**        | M                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Lightweight chat between technician (in-app) and dispatcher (in the FieldPulse Web Platform) for quick clarifications without phone calls. **Marcus explicitly named this as the one most likely to push back into scope mid-project if budget allows** *(2026-04-30)*. Note flagged in Charter §3 cut-from-MVP.

---

### R-017 — GPS-Based "I've Arrived" Auto Check-in *(3rd return)*

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Provisional (cut from MVP; **3rd in return order**)            |
| **Target Window** | Q4 2026 → Q1 2027 (pending capacity)                           |
| **Effort**        | S                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Geofence-based auto check-in when a technician arrives at a job site. Saves a manual tap and improves dispatcher visibility. Cut from MVP.

---

### R-018 — Parts Inventory Lookup *(4th return)*

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Provisional (cut from MVP; **4th in return order**)            |
| **Target Window** | Q1 2027 (pending capacity)                                     |
| **Effort**        | M                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Look up parts inventory from the FieldPulse Web Platform on the technician's device. Cut from MVP.

---

### R-019 — Customer History View *(2nd return)*

| Field             | Value                                                          |
|-------------------|----------------------------------------------------------------|
| **Theme**         | T-1                                                            |
| **Status**        | Provisional (cut from MVP; **2nd in return order** — second-most-asked-by-customers feature after dispatcher chat) |
| **Target Window** | Q1 2027 (pending capacity)                                     |
| **Effort**        | S                                                              |
| **Source CR**     | —                                                              |

**Description:**
> Technician can view prior service history for the customer they are currently serving. Cut from MVP. *Marcus 2026-04-30: "if dispatcher chat goes back into MVP via budget headroom, customer history is the next one in line."*

---

## Later

> Strategic placeholders — no story detail, no effort sizing, no acceptance shape.

### R-020 — iOS Feature Parity *(if Android-first phasing executed)*

| Field          | Value |
|----------------|-------|
| **Theme**      | T-1   |
| **Source CR**  | —     |

**Description:**
> Bring iOS to feature parity with Android if MVP shipped Android-first under capacity pressure (Charter §4 Platform constraint).

---

### R-021 — Push Notifications Expansion

| Field          | Value |
|----------------|-------|
| **Theme**      | T-1   |
| **Source CR**  | —     |

**Description:**
> Deeper push-notification engagement for technicians and dispatchers. MVP includes basic dispatch alerts; this initiative expands to job updates, schedule changes, customer communications.

---

### R-022 — Analytics & Reporting Expansion

| Field          | Value |
|----------------|-------|
| **Theme**      | T-1   |
| **Source CR**  | —     |

**Description:**
> Mobile-derived analytics surfaced in the FieldPulse Web Platform — adoption rates, billing-cycle outcomes, technician usage patterns. Useful for FieldPulse's customer-success conversations.

> **Stay-on-radar marker** *(Marcus 2026-04-30):* "interested in this one — mobile-derived analytics surfaced to FieldPulse customers as a customer-success conversation tool — that's a real revenue lever post-launch. Keep it on the radar even if it's Later."

---

### R-023 — Office Dispatcher Mobile Capability

| Field          | Value |
|----------------|-------|
| **Theme**      | T-3   |
| **Source CR**  | —     |

**Description:**
> Office dispatchers (currently web-only secondary users) gain a mobile capability. Strategic — depends on customer demand signals after technician rollout.

---

### R-024 — Integration with QuickBooks / Accounting Tools

| Field          | Value |
|----------------|-------|
| **Theme**      | T-4   |
| **Source CR**  | —     |

**Description:**
> Connect FieldPulse to common SMB accounting tools (QuickBooks the most-asked-for). Out of scope for PulseField Mobile per Charter §3 Out-of-Scope; placeholder here at Marcus's explicit positioning ("separate roadmap item").

---

## Recently Shipped

> *Empty — no shipped initiatives yet.*

---

## Change Log

| Date       | Initiative ID | Change                       | Driver / CR Ref            |
|------------|---------------|------------------------------|----------------------------|
| 2026-04-28 | R-001 to R-024 | Initial Roadmap drafted (24 initiatives across 4 themes; 11 Now / 8 Next / 5 Later) | Charter v1.0 + Vision + Kickoff Meeting Notes 2026-04-28 |
| 2026-04-30 | R-008 | Status: Pending Decision → **Decided — Auth0 from day one**. Mobile builds against parallel Auth0 environment; ADR by Tech Lead within 2 weeks (target ~2026-05-14). | Charter Review call 2026-04-30 (Marcus + Priya) |
| 2026-04-30 | R-011 | Account provisioning split out as Q2 sub-task (Apple verification 2–4 wk lead time); listings remain Q3. | Charter Review call 2026-04-30 (Marcus) |
| 2026-04-30 | R-012 | Status: Provisional → **Verbally Confirmed (Written Pending)**. **3 technicians** (team rotation, not solo). Pilot anchored to *finish* before Phoenix peak — early July latest. | Charter Review call 2026-04-30 (Marcus, post call w/ Dave 2026-04-24) |
| 2026-04-30 | R-014 | **Jenna Rodriguez added as FieldPulse-side co-owner**. | Charter Review call 2026-04-30 (Marcus) |
| 2026-04-30 | R-015 | Pricing: **inside $180K–$250K envelope**. R-005 Schedule View flagged as first MVP-flex candidate if envelope is tight. | Charter Review call 2026-04-30 (Marcus) |
| 2026-04-30 | R-006 | **Wrapper / proxy layer is planned, not conditional** (per Priya — naming-convention drift). | Charter Review call 2026-04-30 (Priya) |
| 2026-04-30 | R-003 | Note: **2–7 year retention scope may firm up post legal review (D-009)** — could shift from customer expectation to contractual / regulatory; potential effort impact. | Charter Review call 2026-04-30 (Marcus) |
| 2026-04-30 | R-007 | Spike directional input: Priya's instinct **last-write-wins + conflict-banner UX**; spike's call to confirm. *Stay scoped to MVP feature set.* | Charter Review call 2026-04-30 (Priya, Marcus) |
| 2026-04-30 | R-010 | Priya target: **≥50 synthetic jobs / 10 synthetic technicians by mid-May 2026**. | Charter Review call 2026-04-30 (Priya) |
| 2026-04-30 | R-016 — R-019 | **Cut-from-MVP return order locked**: R-016 → R-019 → R-017 → R-018 if budget headroom appears post-launch. | Charter Review call 2026-04-30 (Marcus) |
| 2026-04-30 | R-022 | Stay-on-radar marker: post-launch revenue lever (mobile-derived analytics for customer-success conversations). | Charter Review call 2026-04-30 (Marcus) |

---

## Internal Notes *(not shared with client)*

- **Capacity assumption:** $180K–$250K envelope for 2026 (CY). Now-bucket scope (R-001 to R-011) is sized to fit the envelope assuming a small-to-mid Relevant team (BA + PM + Tech Lead + 2 mobile devs + QA + DevOps part-time + UX Designer part-time). **Marcus saw this internal note at the 2026-04-30 review and asked us to confirm team shape at next status call before assuming it.** Open — confirm at Wed 2026-05-06 status call.
- **Risk markers:**
  - **R-002 / R-007** — offline complexity is the largest delivery-risk concentration in the Now bucket. Front-load the architecture spike. **Priya's instinct: last-write-wins + conflict-banner UX** — spike's call to confirm.
  - **R-006** — legacy API quality gates four other initiatives; Tech Lead discovery must be productive within the first two weeks of Q2 work. **Wrapper layer planned, not conditional** (Priya 2026-04-30). 6-week clock starts on receipt of D-008 (Priya, EoD Wed ~2026-05-06 — TBC).
  - **R-008** — **Decided: Auth0 from day one** (2026-04-30). Residual risk: web-platform Auth0 migration slip. Mitigation: parallel Auth0 environment from the start.
  - **R-015 envelope pressure on MVP scope** — R-005 Schedule View is the first candidate to cut if envelope tightens. Marcus self-surfaced.
- **Open prioritisation questions — answered 2026-04-30:**
  - ✅ **Now-bucket initiative list** confirmed with the 7 amendments above.
  - ✅ **Next-bucket return order** if budget headroom appears post-launch: R-016 (Dispatcher Chat) → R-019 (Customer History) → R-017 (GPS Auto-Check-in) → R-018 (Parts Inventory).
  - ✅ **Post-launch support pricing** — inside envelope; MVP scope may flex.
  - ✅ **Sundance pilot timing** — pilot ends before Phoenix peak (early July latest); MVP must be pilot-ready by early-to-mid June 2026.
- **New open question for next status call:**
  - **Capacity assumption confirmation** — Marcus asked for explicit confirmation of team shape before assuming it.
  - **D-008 delivery date clarification** — Priya said "EoD Wednesday this week" on Thu 2026-04-30; confirm 2026-05-06 vs slipped 2026-04-29.
- **Themes-not-on-Roadmap (intentional):** Customer-facing portal, web-platform rewrite, vertical expansion beyond HVAC/plumbing, in-app payment collection from end-customers — all explicitly out-of-scope per Charter v1.1 §3 and Vision §6.

# Project Charter — PulseField Mobile

| Field | Value |
|---|---|
| **Version** | 1.1 |
| **Date** | 2026-04-30 |
| **Status** | Routed for DocuSign — Marcus to sign within 48hr of receipt |
| **Author** | Vadim (BA, Relevant Software), drafted with Homer; promoted from v1.0 after Charter Review call 2026-04-30 |
| **Confluence** | [URL — pending] |

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-04-28 | Vadim / Homer | Initial working draft from Sales hand-off brief; gaps flagged for kickoff (archived in `docs/.archive/`) |
| 1.0 | 2026-04-28 | Vadim / Homer | Promoted to baseline after kickoff call: scope bounded, MVP defined, budget anchored, timeline driver clarified, post-launch support added (archived in `docs/.archive/`) |
| 1.1 | 2026-04-30 | Vadim / Homer | Promoted after Charter Review call 2026-04-30: Objective 2 reframed (same-day billing); Out-of-Scope expanded (no in-app payment collection); regulatory open item promoted to top-level §5; Auth0 decision locked; post-launch support priced inside envelope; governance + cadence locked. Cover note acknowledges anticipated v1.2 amendment post-D-009 legal review. |

---

## 1. Project Overview

**Project Name:** PulseField Mobile *(working title — final product naming may change before launch; not a blocker for sign-off)*

**Project Description:**
PulseField Mobile is a mobile-first application for field-service technicians working with FieldPulse Solutions' platform. It replaces today's mix of SMS-based job dispatch and paper-based on-site data capture with a single digital workflow — giving HVAC and plumbing technicians the full job context in their hands, capturing job-completion data on-site (including offline), and feeding the data back to the platform the same day.

**Client:** FieldPulse Solutions (Austin, TX) — a SaaS provider of field service management tools for HVAC and plumbing contractors. Approximately 80 paying customers; ~12 employees. PulseField Mobile is FieldPulse's first mobile-first product extension and the first Relevant Software engagement of this scope for FieldPulse.

**End-user population:** Approximately 950 active field-service technicians across FieldPulse's customer base (~80 customer businesses × ~12 technicians each). Year-1 adoption target: **30–40%** of the active-technician population.

**Development Partner:** Relevant Software.

---

## 2. Objectives

1. **Replace the SMS-plus-paper field workflow** with a single mobile application that delivers full job context to technicians on-device and captures job-completion data digitally on-site.
2. **Enable same-day billing** by making completed-job data available to the FieldPulse Web Platform the same day it is captured — collapsing the current ~2-day data-entry lag (paper-form 6pm → next-morning entry → 2-day invoice). FieldPulse customers' downstream invoicing workflows are independent of this product, but the data they need will be available same-day. This is the metric FieldPulse customers complain about most and the headline business outcome of the project.
3. **Re-establish competitive parity in the mobile space** to defend against the customer churn FieldPulse is currently experiencing — 6 customers in the last calendar year explicitly cited mobile as the reason they left, plus 3 more in Q1 alone (≈8% churn directly attributed to mobile gap, real number likely higher). Six-month target: ≥20 of the existing customer base actively using PulseField Mobile.
4. **Move mobile from a defensive feature to a positive acquisition driver** by month 12 — i.e. mobile becomes a reason customers *choose* FieldPulse, not just a reason they don't leave.
5. **Maintain SOC 2 readiness compatibility.** SOC 2 certification work is in flight at FieldPulse this year independent of the mobile project; the mobile build must not be a barrier to SOC 2 readiness.

---

## 3. Scope

### In Scope — MVP (ranked by priority)

1. **Job assignment delivery** with full job context on-device — replaces SMS-plus-phone-back-to-office.
2. **Job-completion data capture** — checklist, notes, photos, parts used, time on site — **fully offline-capable**.
3. **Customer signature capture** at job completion.
4. **Sync to the FieldPulse Web Platform** when connectivity returns; updated status surfaces in the dispatcher view.
5. **Technician schedule view** — "what's my day look like".

> *Note on MVP flex:* If the post-launch support envelope (R-015 Roadmap, §4 Constraints below) pressures MVP scope, **#5 Schedule View is the first candidate to defer to post-MVP**, per Marcus's call at the 2026-04-30 review.

### Cut from MVP *(deliberately deferred to a later phase, not out-of-scope forever)*

- In-app chat between technician and dispatcher.
- GPS-based "I've arrived" auto check-in.
- Parts-inventory lookup.
- Customer-history view.

> *Note on return order:* If post-launch budget headroom appears, the cut-from-MVP features return in this order (Marcus's call at the 2026-04-30 review): in-app chat → customer-history → GPS auto check-in → parts inventory.

### Out of Scope

- Customer-facing portal (end-customer of FieldPulse's customers).
- **No in-app payment collection from end-customers** — technicians do not take credit cards on the spot; payment-collection workflows remain on the existing FieldPulse Web Platform.
- Admin / back-office UI redesign on the FieldPulse Web Platform.
- Rewrite or refactor of the FieldPulse Web Platform itself.
- Payment-processing changes.
- Vertical expansion beyond HVAC and plumbing.
- Marketing-website work.
- Migration of historical job data into a new structure — the mobile app reads what's already there.
- Integrations with third-party accounting software (e.g. QuickBooks) — separate roadmap item.

---

## 4. Constraints

| Constraint | Description |
|---|---|
| **Technical — legacy integration** | Must integrate with the existing FieldPulse Web Platform via API only — no direct database access (Priya's hard line). APIs are RESTful / JSON, mostly sane, with inconsistent naming on some endpoints and no formal versioning. Documentation: a Postman collection plus a ~60%-accurate README. Original developer (Tomás Ribeiro, Lisbon) is on a 5-hours-per-week retainer for emergencies and consultation — **note: retainer is verbal, not contractual** (continuity not contractually guaranteed). A wrapper / proxy layer is **planned, not conditional** (per Priya, 2026-04-30 — naming-convention drift makes it cleaner long-term). |
| **Technical — offline-by-default** | The application must support offline-by-default operation with sync-when-available. Technicians work in basements, crawlspaces, mechanical rooms, and new-construction sites without signal. A technician must be able to start a job, fill out the completion form, capture photos, and obtain a customer signature fully offline. This has material architectural implications for state management and conflict resolution. |
| **Platform** | Both iOS (15+) and Android (10+). Phone only — no tablet support. Customer base is approximately 65% Android, 35% iOS. If forced to choose one for v1, Android takes priority. |
| **Timeline — preference, not commitment** | Marcus's stated preference is "usable by end of Q3", driven by ServiceTitan competitor pressure that historically peaks Q4 going into the new year. Tolerance: a 1-month slip is acceptable; a 3-month slip is not. Marcus's stated preference is *"a solid product in early Q4 over a shaky one in Q3."* |
| **Budget — anchored** | $180K–$250K is the engagement envelope for this calendar year. Above $250K requires a conversation with the angel investors. Below $180K risks cutting corners on a production-grade mobile build. **Post-launch support (60–90 days, Relevant) is priced inside this envelope** (Marcus's call at the 2026-04-30 review) — see *Post-launch support* row below. |
| **Regulatory — partially open** | CCPA applies (FieldPulse has California customers). Some FieldPulse customers do work for school districts and municipal buildings; gov-contractor flow-down implications are unknown and require legal review. SOC 2 certification is being pursued in parallel and the mobile build must not be a barrier. FieldPulse currently has no formal data residency policy and no formal breach-notification procedures (captured as Issues I-001 / I-002 in the RAID Log; both drafted under FieldPulse's SOC 2 program — Priya owner, drafts by July 2026). **The legal-review item is promoted to a top-level open item in §5 below** (per Marcus's request at the 2026-04-30 review). |
| **Authentication — Auth0 from day one** *(decided 2026-04-30)* | PulseField Mobile authenticates against Auth0 from day one, in a parallel Auth0 environment to FieldPulse's web-platform Auth0 migration (4–6 month horizon, Aug–Oct 2026 target). Both systems coexist briefly. ADR drafted by Relevant Tech Lead within 2 weeks of the call (target ~2026-05-14), accepted by Priya. SOC 2 readiness rationale: Auth0 is SOC 2 Type II certified; custom-rolled auth would be a SOC 2 finding. |
| **Governance & Cadence** *(locked 2026-04-30)* | Sign-off thresholds: <10% scope change → Marcus alone; ≥10% → Marcus + Priya jointly. **CR baseline = Roadmap once signed off, not Charter** — Charter is the high-level contract; Roadmap is the working baseline; CR scope is measured against the Roadmap. Status calls: **Wednesday 9am Central, 30 min hard stop**. **EoF Friday written status updates** (≤1 screen, bullet points, to Marcus + Priya). Slack workspace `fieldpulse.slack.com`, channel `#pulsefield-mobile` (Vadim + PM + Tech Lead invited). SLAs: 48hr normal items / same-day blockers / 3 business days for document reviews. |
| **No design lead at FieldPulse** | Marcus self-identified this as a gap. Marcus opted **not to hire a contract designer** (decided 2026-04-30) — Relevant's UX role gains importance. Mitigation: **bi-weekly design review cadence** with mockups walked through **live, not as static files**; **decisions captured in writing after each review**. Marcus + Jenna Rodriguez sign off at clear milestones. |
| **Post-launch support — inside envelope** | 60–90 days of post-launch support from Relevant is part of the engagement — bug fixes, minor adjustments, knowledge transfer. Followed by a clear handoff to FieldPulse for in-house operation. **Pricing confirmed inside the $180K–$250K envelope** (decided 2026-04-30); both parties acknowledge this may pressure MVP scope (R-005 Schedule View first candidate to flex — see §3 above). |

---

## 5. Material Open Items, Risks & Assumptions

> See `docs/client/raid-log.md` for the full RAID Log.

### Material Open Item *(promoted from §4 Constraints — Regulatory, per Marcus 2026-04-30)*

- **Legal review (D-009 RAID)** — CCPA exposure assessment, gov-contractor flow-down (school-district + municipal-building customers), and SOC 2 readiness gap analysis. Marcus engaging outside counsel by **EoW 2026-05-08**; 2–3 week turnaround post-engagement; **findings expected mid–late May 2026, worst case early June**. *This is the open item most likely to bite the project.* A **v1.2 amendment to this Charter is anticipated** based on the findings — see §9 Cover Note.

### Key assumptions *(confirmed at kickoff unless noted)*

- Marcus has sole sign-off authority on requirements, scope, and CRs <10% scope change. CRs ≥10% require Marcus + Priya.
- Priya Krishnan (CTO) is the primary technical counterpart for the duration of the engagement.
- Deployment is US-only; Canadian customers (Ontario) operate on the US version with no localisation.
- The application carries no direct regulatory burden of its own — *partially invalidated*: CCPA exposure exists, SOC 2 timing is material, and government-contractor flow-down is unconfirmed. Open follow-up: legal review (D-009 above).
- Engagement runs as Agile — Fixed-Range with the Roadmap as the CR baseline.
- The existing FieldPulse APIs are sufficient for the mobile client to integrate with after some hardening — to be validated in technical discovery.

### Key risks *(top items from RAID Log)*

- **Timeline realism** (R-002) — EoQ3 may not be feasible given offline complexity and integration discovery.
- **Legacy integration risk** (R-003) — partial documentation, no formal API versioning, freelancer on light retainer.
- **SOC 2 readiness** (R-006) — mobile build must not block parallel SOC 2 work.
- **Auth0 dependency** (R-008) — *risk reframed 2026-04-30:* Auth0 decision locked (mobile from day one); residual risk is web-platform migration slip → mobile depending on a parallel Auth0 environment that may grow more complex than modelled.
- **Offline state-management / conflict-resolution complexity** (R-010) — architecturally non-trivial; flagged by Priya at kickoff.
- **Tomás retainer continuity** (R-012) — *new 2026-04-30:* 5hr/wk retainer is verbal, not contractual.

---

## 6. High-Level Milestones

| Milestone | Description | Status |
|---|---|---|
| Sales hand-off & pre-discovery | Sales brief received and mined; v0.1 working drafts of Charter / Stakeholder Register / Glossary / RAID Log produced | **Delivered** (2026-04-28) |
| Discovery & Kickoff | Tailored Kickoff Questionnaire run with Marcus and Priya; v0.1 promoted to v1.0; transcript and meeting notes archived | **Delivered** (2026-04-28) |
| Vision + Roadmap baseline | Product Vision drafted and accepted; Product Roadmap (Now / Next / Later) baselined as the CR-baseline contract | **Delivered** (2026-04-30) |
| MVP definition | Client PRD covering the 5 MVP features; agreement on architecture approach (offline / sync / API integration) — depends on Priya's platform-architecture one-pager (D-008, ETA 2026-05-06) | Not Started |
| Build & internal validation | MVP delivery; staging environment populated with synthetic data (R-010 Roadmap — ≥50 synthetic jobs, 10 synthetic technicians by mid-May); internal walkthrough by Marcus, Priya, Jenna Rodriguez | Not Started |
| Sundance HVAC pilot | Real-world UAT with Dave Martinez's team in Phoenix — **3 technicians, team rotation**; ≥2 weeks; pilot ends before Phoenix peak (early July latest) | Not Started — verbally confirmed; written agreement pending one-pager |
| Production go-live | App Store + Play Store approval *(account provisioning starts in Q2)*; go-live criteria met | Target: end Q3 2026 (preference) / early Q4 2026 (acceptable) |
| Post-launch support (Relevant-led) | 60–90 days of bug-fix and adjustment support — inside envelope | Engaged at go-live |
| Handover to FieldPulse | Knowledge transfer, runbook delivery, sign-off | Engagement closeout |

---

## 7. Stakeholders

> See `docs/client/stakeholder-register.md` for the full register including delivery team, end users, external systems, and RACI.

| Stakeholder | Role |
|---|---|
| FieldPulse Solutions | Client — product owner organisation |
| Marcus Chen | Founder & CEO, FieldPulse — decision-maker, sign-off authority |
| Priya Krishnan | CTO, FieldPulse — primary technical counterpart |
| Jenna Rodriguez | Customer Success Lead, FieldPulse — internal UAT proxy, rollout support, R-014 training co-owner |
| Dave Martinez | Owner, Sundance HVAC (Phoenix) — pilot customer (verbally confirmed 2026-04-24; written agreement pending one-pager) |
| Tomás Ribeiro | Original freelance developer, FieldPulse Web Platform (5hr/week retainer, verbal arrangement) |
| Relevant Software | Development partner — delivery team |
| FieldPulse Customer Technicians | Primary end users — HVAC and plumbing field-service technicians (~950 active across the customer base) |
| FieldPulse Customer Office Dispatchers | Secondary end users — confirmed at kickoff |
| FieldPulse's Customer Businesses | Indirect stakeholders — the contractors paying FieldPulse |

---

## 8. Client Approval

| Name | Role | Decision | Date | Signature |
|---|---|---|---|---|
| Marcus Chen | Founder & CEO, FieldPulse Solutions | Pending | | |

> Sign-off via DocuSign. Marcus committed to sign within 48hr of receiving v1.1 (per Charter Review call 2026-04-30).

---

## 9. Cover Note for Sign-Off

> *Acknowledgments accompanying Charter v1.1 sign-off, per Marcus's request at the 2026-04-30 Charter Review call.*

Charter v1.1 incorporates the call-review edits Marcus requested on 2026-04-30 — Objective 2 reframed (*"enable same-day billing"*), Out-of-Scope expanded (no in-app payment collection from end-customers), the regulatory legal-review concern promoted from §4 Constraints to §5 as a Material Open Item, the Auth0 decision locked, post-launch support priced inside envelope, and governance + cadence captured in §4.

**A v1.2 amendment to this Charter is anticipated based on D-009 legal-review findings** — outside-counsel engagement by 2026-05-08; CCPA exposure assessment, gov-contractor flow-down for school-district + municipal-building customers, and SOC 2 readiness gap analysis; findings expected mid–late May 2026 (worst case early June). Both parties acknowledge this open item is understood at sign-off and is not grounds for dispute over the timing of v1.1 baseline acceptance.

Marcus Chen, Founder & CEO, FieldPulse Solutions — agrees to v1.1 with this acknowledgment.
Vadim, BA, Relevant Software — confirms the open item is logged in RAID (D-009) and tracked through to a v1.2 amendment.

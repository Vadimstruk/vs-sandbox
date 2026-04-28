# Project Charter — PulseField Mobile

| Field | Value |
|---|---|
| **Version** | 1.0 |
| **Date** | 2026-04-28 |
| **Status** | Pending Sign-off — routed to Marcus Chen |
| **Author** | Vadim (BA, Relevant Software), drafted with Homer; promoted from v0.1 working draft after kickoff call 2026-04-28 |
| **Confluence** | [URL — pending] |

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-04-28 | Vadim / Homer | Initial working draft from Sales hand-off brief; gaps flagged for kickoff (archived in `docs/.archive/`) |
| 1.0 | 2026-04-28 | Vadim / Homer | Promoted to baseline after kickoff call: scope bounded, MVP defined, budget anchored, timeline driver clarified, post-launch support added. Routed to Marcus for sign-off. |

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
2. **Compress billing-cycle time-to-invoice** from the current ~2-day pattern (paper-form 6pm → next-morning entry → 2-day invoice) to a same-day pattern. This is the metric FieldPulse customers complain about most and the headline business outcome of the project.
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

### Cut from MVP *(deliberately deferred to a later phase, not out-of-scope forever)*

- In-app chat between technician and dispatcher.
- GPS-based "I've arrived" auto check-in.
- Parts-inventory lookup.
- Customer-history view.

### Out of Scope

- Customer-facing portal (end-customer of FieldPulse's customers).
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
| **Technical — legacy integration** | Must integrate with the existing FieldPulse Web Platform via API only — no direct database access (Priya's hard line). APIs are RESTful / JSON, mostly sane, with inconsistent naming on some endpoints and no formal versioning. Documentation: a Postman collection plus a ~60%-accurate README. Original developer (Tomás Ribeiro, Lisbon) is on a 5-hours-per-week retainer for emergencies and consultation. |
| **Technical — offline-by-default** | The application must support offline-by-default operation with sync-when-available. Technicians work in basements, crawlspaces, mechanical rooms, and new-construction sites without signal. A technician must be able to start a job, fill out the completion form, capture photos, and obtain a customer signature fully offline. This has material architectural implications for state management and conflict resolution. |
| **Platform** | Both iOS (15+) and Android (10+). Phone only — no tablet support. Customer base is approximately 65% Android, 35% iOS. If forced to choose one for v1, Android takes priority. |
| **Timeline — preference, not commitment** | Marcus's stated preference is "usable by end of Q3", driven by ServiceTitan competitor pressure that historically peaks Q4 going into the new year. Tolerance: a 1-month slip is acceptable; a 3-month slip is not. Marcus's stated preference is *"a solid product in early Q4 over a shaky one in Q3."* |
| **Budget — anchored** | $180K–$250K is the engagement envelope for this calendar year. Above $250K requires a conversation with the angel investors. Below $180K risks cutting corners on a production-grade mobile build. |
| **Regulatory — partially open** | CCPA applies (FieldPulse has California customers). Some FieldPulse customers do work for school districts and municipal buildings — flow-down implications unknown and require legal review. SOC 2 certification is being pursued in parallel and the mobile build must not be a barrier. FieldPulse currently has no formal data residency policy and no formal breach-notification procedures (captured as Issues I-001 / I-002 in the RAID Log). |
| **Organisational maturity** | This is FieldPulse's first project of this scope. Process, governance, sign-off, and approval workflow are being established jointly. CR threshold: <10% scope change → Marcus alone; ≥10% → Marcus + Priya. |
| **No design lead at FieldPulse** | Marcus self-identified this as a gap. Relevant's UX role gains importance; design decisions need a clear approval path on the FieldPulse side. |
| **Post-launch support** | 60–90 days of post-launch support from Relevant is part of the engagement — bug fixes, minor adjustments, knowledge transfer. Followed by a clear handoff to FieldPulse for in-house operation. This is a confirmed scope addition that emerged at kickoff. |

---

## 5. Key Risks & Assumptions

> See `docs/client/raid-log.md` for the full RAID Log.

**Key assumptions** *(confirmed at kickoff unless noted)*:

- Marcus has sole sign-off authority on requirements, scope, and CRs <10% scope change. CRs ≥10% require Marcus + Priya.
- Priya Krishnan (CTO) is the primary technical counterpart for the duration of the engagement.
- Deployment is US-only; Canadian customers (Ontario) operate on the US version with no localisation.
- The application carries no direct regulatory burden of its own — *partially invalidated*: CCPA exposure exists, SOC 2 timing is material, and government-contractor flow-down is unconfirmed. Open follow-up: legal review.
- Engagement runs as Agile — Fixed-Range with the Roadmap as the CR baseline.
- The existing FieldPulse APIs are sufficient for the mobile client to integrate with after some hardening — to be validated in technical discovery.

**Key risks** *(top items from RAID Log)*:

- **Timeline realism** (R-002) — EoQ3 may not be feasible given offline complexity and integration discovery.
- **Legacy integration risk** (R-003) — partial documentation, no formal API versioning, freelancer on light retainer.
- **SOC 2 readiness** (R-006) — mobile build must not block parallel SOC 2 work.
- **Auth0 migration overlap** (R-008) — FieldPulse is migrating off custom auth this year; possible coordination needed if mobile touches login.
- **Offline state-management / conflict-resolution complexity** (R-010) — architecturally non-trivial; flagged by Priya at kickoff.
- **Implicit post-launch support scope** (R-011) — 60–90d support not in original budget framing.

---

## 6. High-Level Milestones

| Milestone | Description | Status |
|---|---|---|
| Sales hand-off & pre-discovery | Sales brief received and mined; v0.1 working drafts of Charter / Stakeholder Register / Glossary / RAID Log produced | **Delivered** (2026-04-28) |
| Discovery & Kickoff | Tailored Kickoff Questionnaire run with Marcus and Priya; v0.1 promoted to v1.0; transcript and meeting notes archived | **Delivered** (2026-04-28) |
| Vision + Roadmap baseline | Product Vision drafted; Product Roadmap (Now / Next / Later) baselined as the CR-baseline contract | Not Started |
| MVP definition | Client PRD covering the 5 MVP features; agreement on architecture approach (offline / sync / API integration) — depends on Priya's platform-architecture one-pager | Not Started |
| Build & internal validation | MVP delivery; staging environment populated with synthetic data; internal walkthrough by Marcus, Priya, Jenna Rodriguez | Not Started |
| Sundance HVAC pilot | Real-world UAT with Dave Martinez's team in Phoenix, ≥2 weeks, no Sev-1 issues | Not Started — pending Marcus's confirmation with Dave |
| Production go-live | App Store + Play Store approval; go-live criteria met (see RAID / Kickoff Meeting §8.3) | Target: end Q3 2026 (preference) / early Q4 2026 (acceptable) |
| Post-launch support (Relevant-led) | 60–90 days of bug-fix and adjustment support | Engaged at go-live |
| Handover to FieldPulse | Knowledge transfer, runbook delivery, sign-off | Engagement closeout |

---

## 7. Stakeholders

> See `docs/client/stakeholder-register.md` for the full register including delivery team, end users, external systems, and RACI.

| Stakeholder | Role |
|---|---|
| FieldPulse Solutions | Client — product owner organisation |
| Marcus Chen | Founder & CEO, FieldPulse — decision-maker, sign-off authority |
| Priya Krishnan | CTO, FieldPulse — primary technical counterpart |
| Jenna Rodriguez | Customer Success Lead, FieldPulse — internal UAT proxy, rollout support |
| Dave Martinez | Owner, Sundance HVAC (Phoenix) — pilot customer (subject to Marcus's confirmation) |
| Tomás Ribeiro | Original freelance developer, FieldPulse Web Platform (5hr/week retainer) |
| Relevant Software | Development partner — delivery team |
| FieldPulse Customer Technicians | Primary end users — HVAC and plumbing field-service technicians (~950 active across the customer base) |
| FieldPulse Customer Office Dispatchers | Secondary end users — confirmed at kickoff |
| FieldPulse's Customer Businesses | Indirect stakeholders — the contractors paying FieldPulse |

---

## 8. Client Approval

| Name | Role | Decision | Date | Signature |
|---|---|---|---|---|
| Marcus Chen | Founder & CEO, FieldPulse Solutions | Pending | | |

> Sign-off may be made digitally — DocuSign or signed-PDF-by-email per Marcus's preference (kickoff §7.5).

# Project Charter — PulseField Mobile

| Field | Value |
|---|---|
| **Version** | 0.1 (working draft) |
| **Date** | 2026-04-28 |
| **Status** | Draft — gaps marked `[TBC at kickoff]` to be confirmed in the discovery call with Marcus and Priya |
| **Author** | Homer (Relevant BA), drafted from `docs/reference/FieldPulse_Client_Brief.pdf` |
| **Confluence** | [URL — pending] |

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-04-28 | Homer | Initial working draft from Sales hand-off brief; gaps flagged for kickoff |

---

## 1. Project Overview

**Project Name:** PulseField Mobile *(working title — final naming `[TBC at kickoff]`)*

**Project Description:**
PulseField Mobile is a mobile-first application for field-service technicians working with FieldPulse Solutions' platform. It replaces today's mix of SMS-based job dispatch and paper-based on-site data capture with a single digital workflow — giving HVAC and plumbing technicians the full job context in their hands and feeding completed job data back to the platform the same day.

**Client:** FieldPulse Solutions (Austin, TX) — SaaS provider of field service management tools for HVAC and plumbing contractors. ~80 paying customers; ~12 employees.

**Development Partner:** Relevant Software *(to confirm at kickoff)*

---

## 2. Objectives

1. Deliver a mobile-first technician application that integrates with the existing FieldPulse web platform and replaces the current SMS-plus-paper field workflow.
2. Reduce billing-cycle delays caused by end-of-day paper-form submission by enabling same-day digital capture and return of job data from the field. *Target reduction: `[TBC at kickoff]`*.
3. Re-establish competitive parity in the mobile space — defending against the customer churn FieldPulse is currently seeing toward mobile-capable competitors.
4. **`[TBC at kickoff]`** Concrete, measurable success criteria — candidate metrics: technician daily-active-use rate, percentage of jobs handled fully digitally, billing-cycle time-to-invoice reduction, year-on-year customer churn change.

---

## 3. Scope

### In Scope

- **Mobile technician app** for FieldPulse's customer base (HVAC and plumbing field technicians).
- **Integration with the existing FieldPulse web platform** — receiving job assignments, returning completed job data.
- **Digital job assignment flow** — replacing SMS, providing the full job context on-device.
- **On-site data capture** — replacing paper forms.
- **Same-day submission** workflow that feeds the existing platform's billing and reporting.

### Out of Scope

`[TBC at kickoff — boundary must be drawn before Roadmap baseline. Likely candidates to explicitly exclude:]`

- *Customer-facing (end-customer) portal.*
- *Admin / back-office UI redesign on the web platform.*
- *Rewrite of the existing FieldPulse web platform.*
- *New payment-processing capabilities.*
- *Additional vertical expansion beyond HVAC and plumbing.*

---

## 4. Constraints

| Constraint | Description |
|---|---|
| **Technical — legacy integration** | Must integrate with the existing FieldPulse web platform, originally built by an external freelancer. API quality, documentation, and architecture are unknown at this stage and require technical discovery. |
| **Timeline — directional only** | Marcus has expressed a preference for "something usable by the end of Q3"; he himself flagged uncertainty about whether that is realistic. To be confirmed and re-baselined at kickoff. |
| **Budget — directional only** | Marcus described the budget as "flexible, but not enterprise-scale — needs to be reasonable." No anchor figure on file. To be confirmed at kickoff before Roadmap baseline. |
| **Organisational maturity** | This is FieldPulse's first project of this scope. Process, governance, sign-off, and approval workflow will need to be established jointly. |
| **Regulatory / Data protection** | `[TBC at kickoff]` — US-based deployment assumed; specific obligations (state-level, customer-imposed, e.g. SOC2 from B2B customers) to be confirmed. |

---

## 5. Key Risks & Assumptions

> See `docs/client/raid-log.md` for the full RAID Log (Risks, Assumptions, Issues, Dependencies). This section captures only the headline items at project initiation.

**Key assumptions at project initiation** *(to confirm at kickoff)*:

- Marcus Chen has sole sign-off authority on requirements and scope.
- Priya (CTO) is the primary technical counterpart on the FieldPulse side.
- Deployment is US-only; no internationalisation or localisation in scope.
- The application has no direct regulatory burden of its own (B2B SaaS for contractors); customer-imposed obligations to be confirmed.

**Key risks at project initiation** *(verbatim from Sales brief; populated in RAID Log)*:

- **Scope ambiguity** — "mobile app" is broad; platforms (iOS / Android / both), feature scope, and offline behaviour are all undefined.
- **Timeline realism** — end of Q3 may not be achievable depending on integration complexity.
- **Legacy integration risk** — existing web app is freelancer-built; API quality, documentation, and architecture are unknown.
- **Budget mismatch** — "reasonable" is undefined and may not align with the cost of a production-grade mobile application.
- **Organisational maturity** — first project of this scope for the client; governance must be established early.

---

## 6. High-Level Milestones

| Milestone | Description | Status |
|---|---|---|
| Project Initiation | Charter (this document), Stakeholder Register, Glossary, RAID Log v0.1 — drafted from Sales brief, sign-off pending kickoff | In Progress |
| Discovery & Kickoff | Kickoff call with Marcus and Priya; tailored Kickoff Questionnaire answered; Charter promoted from v0.1 → v1.0; Vision Statement and Roadmap baseline drafted | Not Started |
| Roadmap Baseline | Roadmap signed off as the CR baseline — initiatives bucketed Now / Next / Later | Not Started |
| `[TBC at kickoff]` MVP Definition | First-release feature set agreed; PRD signed off | Not Started |
| `[TBC at kickoff]` MVP Delivery | First production-ready release for FieldPulse customer technicians | Not Started |

---

## 7. Stakeholders

> See `docs/client/stakeholder-register.md` for the full register.

| Stakeholder | Role |
|---|---|
| FieldPulse Solutions | Client — product owner organisation |
| Marcus Chen | Founder & CEO, FieldPulse — decision-maker, sign-off authority |
| Priya *(surname `[TBC]`)* | CTO, FieldPulse — primary technical counterpart |
| Relevant Software *(to confirm)* | Development partner — delivery team |
| FieldPulse Customer Technicians | End users — HVAC and plumbing field-service technicians, ~5–30 per FieldPulse customer across ~80 customers |
| FieldPulse Customers (Contractors) | Indirect stakeholders — businesses paying FieldPulse, whose technicians use the app |

---

## 8. Client Approval

| Name | Role | Decision | Date | Signature |
|---|---|---|---|---|
| Marcus Chen | Founder & CEO, FieldPulse | Pending | | |

---

## Working Draft Notice

This is **v0.1, a working draft** — not a baselined Charter. Fields marked `[TBC at kickoff]` are explicit gaps to fill at the discovery call. Once the Kickoff Questionnaire (`docs/client/meetings/kickoff-questionnaire-2026-04-28.md`) is answered, this Charter will be promoted to **v1.0** and routed to Marcus for sign-off.

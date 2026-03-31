# Project Charter — VS-SANDBOX

| Field | Value |
|---|---|
| **Version** | 1.0 |
| **Date** | 2026-03-31 |
| **Status** | Draft / Pending Approval |
| **Author** | BA |

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0 | 2026-03-31 | BA | Initial release — drafted from kickoff session |

---

## 1. Project Overview

**Project Name:** VS-SANDBOX

**Project Description:**
HeyChar operates in HR and workforce staffing in the UK. HR managers currently spend significant time manually completing and processing work applications using Microsoft Word and Excel templates. This project delivers a web-based application that streamlines the form-filling and processing workflow — pre-filling forms for returning applicants from the existing HR database, capturing data from identity documents via OCR, and generating completed application documents. The system will also support right-to-work compliance obligations required under UK employment law.

**Client:** HeyChar
**Development Partner:** [Development Organisation]

---

## 2. Objectives

1. Reduce the time required to process one application by at least 30% compared to the current manual process.
2. Eliminate repeated manual data entry for returning applicants by pre-filling forms from the existing HR database.
3. Capture identity document data automatically via OCR, reducing manual transcription errors.
4. Support UK right-to-work compliance obligations — record that the check was performed, flag document expiry dates, and maintain an audit trail for potential Home Office review.
5. Deliver a system that HR managers adopt willingly — usability is a first-class objective.

---

## 3. Scope

### In Scope

- Application form filling and processing workflow
- Pre-fill of forms for returning applicants from the HR applicant database
- OCR scanning of identity documents (passports, visas, BRP cards) to extract applicant data
- Generation of completed application as a Word or PDF document
- Right-to-work flag and document expiry date tracking (v1 — Should Have)
- Audit trail of who processed which application, when, and which documents were provided
- Integration with the existing HR applicant database (read and write)
- Web-based interface — no local installation required
- Basic user guide for HR managers at go-live

### Out of Scope

- Payroll processing
- Performance reviews
- Contracts management
- Applicant tracking system (ATS)
- Job posting or vacancy management functionality
- Multilingual support — English only
- Native mobile application

---

## 4. Constraints

| Constraint | Description |
|---|---|
| **Regulatory — Right-to-Work** | The system must support UK right-to-work verification requirements. Every applicant must be verified before starting work. Audit trail is mandatory for potential Home Office review. |
| **Regulatory — Data Protection** | UK GDPR and Data Protection Act 2018 apply. Personal data including identity documents must be handled in compliance with data retention, consent, and secure storage requirements. |
| **Technical — Platform** | HeyChar is a Microsoft-heavy organisation (Windows, Office 365). The solution must be web-based. Azure is the preferred hosting environment given existing Microsoft agreements. |
| **Technical — Integration** | The existing HR database API is undocumented. Integration complexity cannot be confirmed until API documentation is obtained from Tom (IT). |
| **Timeline** | Soft internal deadline: end of Q3 2026 (September 2026). Head of HR presents results at an internal review in October 2026. Scope must be managed tightly to meet this window. |
| **Usability** | HR managers must adopt the system willingly. If it is more difficult than the current Word/Excel process, adoption will fail regardless of technical quality. |

---

## 5. Assumptions

> See `docs/client/shared/assumptions-log.md` for the full assumptions register.

Key assumptions at project initiation:

- Azure is the preferred hosting environment but is not a hard contractual constraint.
- Document storage solution (SharePoint vs shared network drive) is not yet decided — architecture decisions are deferred until this is confirmed.
- The HR database API documentation will be provided by Tom (IT) before integration design begins.
- Word/Excel form templates and Kate's process map will be provided before requirements are finalised.
- Budget cap has not been formally set — significant scope or cost changes require CEO sign-off.

---

## 6. High-Level Milestones

| Milestone | Description | Target | Status |
|---|---|---|---|
| Project Initiation | Charter, Glossary, Stakeholder Register, SRS v1.0 signed off | April 2026 | In Progress |
| Requirements Complete | PRD and SRS finalised, Nick Cave sign-off on compliance scope | May 2026 | Not Started |
| Architecture & Design | Technical architecture agreed, OCR vendor selected, document storage decision confirmed | May 2026 | Not Started |
| Development | Core MVP features built | June–August 2026 | Not Started |
| UAT | Staging environment, anonymised test data, UAT by Kate/Mary/Sam/George | September 2026 | Not Started |
| Go-Live | All go-live criteria met, user guide delivered, hypercare begins | End of Q3 2026 | Not Started |
| Internal Review | Head of HR presents results | October 2026 | Not Started |

> **Blackout periods:** Avoid major releases January–March (peak hiring season) and April (financial year-end).

---

## 7. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| HR database API undocumented — integration scope unknown | Medium | High | Engage Tom (IT) early — obtain API docs before architecture decisions |
| Document storage decision (SharePoint vs network drive) delays architecture | Medium | Medium | Escalate decision to John/Kate — agree before architecture phase |
| User adoption failure — HR managers revert to Word/Excel | Medium | High | Treat usability as a first-class requirement; involve HR managers in UAT early |
| Scope creep vs Q3 deadline | Medium | High | Strict Change Request process; right-to-work and expiry tracking explicitly flagged as Should Have (not Must Have) |
| Nick Cave not engaged early — compliance requirements finalised too late | Medium | High | Schedule Nick Cave input before SRS sign-off |

---

## 8. Stakeholders

> See `docs/client/vs-sandbox/stakeholder-register.md` for the full stakeholder register.

| Stakeholder | Organisation | Role |
|---|---|---|
| John Paul Jones | HeyChar | CEO — final sign-off authority on requirements, scope, and significant spend |
| Kate Bush | HeyChar | Head of HR — day-to-day contact, CR co-approver, UAT lead |
| Nick Cave | HeyChar | Senior Lawyer — consulted on compliance, regulatory, and security requirements |
| Mary Smith | HeyChar | Senior HR — UAT participant |
| Sam Altman | HeyChar | HR — UAT participant |
| George Carlin | HeyChar | HR — UAT participant (usability focus) |
| Tom [surname TBD] | HeyChar | IT — HR database API owner |
| [Dev Organisation] | [Dev Partner] | Development and delivery team |

---

## 9. Communication Plan

| Stakeholder | Format | Frequency | Owner |
|---|---|---|---|
| Kate Bush | Weekly 30-minute Teams call + Teams for day-to-day | Weekly | BA / PM |
| John Paul Jones | Concise written summary — RAG status, key decisions, items requiring his attention | Monthly | PM |
| Nick Cave | Ad hoc via email / Teams | As needed (compliance/legal topics only) | BA |
| Document sign-off | DocuSign | Per milestone | BA / PM |

**Urgent escalation:** Teams → Kate Bush → John Paul Jones (within a few hours during business hours for genuine blockers).

---

## 10. Client Approval

| Name | Role | Decision | Date | Signature |
|---|---|---|---|---|
| John Paul Jones | CEO, HeyChar | | | |
| Kate Bush | Head of HR, HeyChar | | | |

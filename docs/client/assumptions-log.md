# Assumptions & Constraints Log

> **Type:** Living document. Add new assumptions as they are identified. Resolved assumptions should be updated in place (not deleted) so the history is preserved.
> **Last Updated:** 2026-03-31
> **Project:** VS-SANDBOX
> **Confluence:** https://vstest.atlassian.net/wiki/spaces/VSSB2/pages/426197

---

## How to Use This Document

| Status | Meaning |
|---|---|
| **Open** | Assumption is active and unvalidated — decisions are being made based on it |
| **Confirmed** | Assumption has been validated by the client or a reliable source |
| **Invalidated** | Assumption turned out to be wrong — impact assessed and documented |
| **Superseded** | Assumption replaced by a confirmed fact or a CR |

---

## Assumptions Register

### Technical & Infrastructure

| ID | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|
| A-001 | Azure is the preferred hosting environment but is not a hard contractual constraint. Another cloud or on-premise hosting could be considered if there is a strong reason. | Open | Architecture decisions may need revisiting if Azure is ruled out. | PM | 2026-03-31 | |
| A-002 | Document storage solution is TBD — SharePoint migration under consideration but not confirmed. Shared network drive is current state. | Open | If SharePoint is adopted, document storage integration requires additional design. If network drive is retained, a different approach is needed. | PM / Kate Bush | 2026-03-31 | |
| A-003 | The HR database has a basic internal API. API documentation will be provided by Tom (IT) before integration design begins. | Open | Without API documentation, integration scope and complexity cannot be confirmed. This is a delivery risk. | Tom (IT) | 2026-03-31 | |
| A-004 | The system will be web-based — no local installation required on HeyChar machines. | Open | If a desktop component is required, development and deployment approach changes significantly. | BA | 2026-03-31 | |

---

### Business & Domain

| ID | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|
| A-005 | Word/Excel form templates and Kate's process map will be provided by Kate Bush before functional requirements are finalised. | Open | Requirements for form fields, validation rules, and workflow cannot be written without these. Delivery risk if delayed. | Kate Bush | 2026-03-31 | |
| A-006 | OCR will be delivered via a third-party vendor/service. No OCR capability will be built from scratch. | Open | If no suitable vendor is found within budget, OCR scope must be revisited. | BA / PM | 2026-03-31 | |
| A-007 | Right-to-work flag and document expiry tracking are Should Have (not Must Have) for v1. They can be descoped without breaking the MVP if timeline is at risk. | Open | If client insists these are Must Have, MVP scope and Q3 deadline need reassessment. | BA / Kate Bush | 2026-03-31 | |
| A-008 | Applicants do not self-serve in the system — HR managers operate the system on behalf of applicants. Self-service applicant access is out of scope for v1. | Open | If applicants need direct system access, user roles, authentication, and the security model change significantly. | BA | 2026-03-31 | |

---

### Process & Delivery

| ID | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|
| A-009 | Budget cap has not been formally set. Significant scope or cost decisions require sign-off from John Paul Jones (CEO). | Open | If a budget cap is applied retrospectively, scope may need to be reduced. | PM / John Paul Jones | 2026-03-31 | |
| A-010 | Nick Cave (Senior Lawyer) will be available to review security and data retention requirements before the SRS is finalised. | Open | If Nick Cave is unavailable, the SRS cannot be finalised — compliance requirements would be incomplete. | BA / Kate Bush | 2026-03-31 | |
| A-011 | A 2–4 week hypercare period will be included immediately post go-live. The ongoing support model after hypercare is TBD — John Paul Jones sign-off required. | Open | If no support model is agreed before go-live, post-hypercare production issues may be unhandled. | PM / John Paul Jones | 2026-03-31 | |
| A-012 | Test data (anonymised applicant records) will be provided by HeyChar (Kate Bush) for the staging environment. The BA will provide format and volume requirements to Kate in advance. | Open | If test data is not available, UAT cannot proceed on realistic scenarios. | Kate Bush / BA | 2026-03-31 | |

---

## Constraints Register

| ID | Constraint | Type | Impact | Owner |
|---|---|---|---|---|
| C-001 | UK GDPR and Data Protection Act 2018 — all personal data including identity documents must comply with data retention, consent, and secure storage requirements. | Regulatory | Shapes document storage design, data retention policy, and consent mechanisms throughout the system. | BA / Nick Cave |
| C-002 | UK Right-to-Work legislation — the system must record that a right-to-work check was performed for every applicant, and maintain an audit trail suitable for Home Office review. | Regulatory | Right-to-work check recording and audit trail are non-negotiable system requirements. | BA / Nick Cave |
| C-003 | HMRC employment records compliance — the system must support retention of employment records in line with HMRC requirements. | Regulatory | Data retention periods must be confirmed with Nick Cave before implementation. | BA / Nick Cave |
| C-004 | Microsoft / Office 365 environment — the solution must work within HeyChar's existing Microsoft ecosystem. | Technical | Stack and integration choices must be compatible with Windows/Office 365/Azure. | Tech Lead |
| C-005 | Web-based only — no local software installation permitted on HeyChar machines. | Technical | All functionality must be accessible via a web browser. | Tech Lead |
| C-006 | Q3 2026 soft deadline — Head of HR must be able to present results at October 2026 internal review. | Timeline | Scope must be managed to ensure MVP is live before October 2026. Should Have features are candidates for deferral if timeline is at risk. | PM |
| C-007 | Usability — if the system is harder to use than the current Word/Excel process, HR managers will revert to manual processing. Adoption failure is a project failure. | Business | UX quality is a hard constraint, not a nice-to-have. Must be validated during UAT with real end users. | BA / UX |

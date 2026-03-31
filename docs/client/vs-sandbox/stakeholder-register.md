# Stakeholder Register — VS-SANDBOX

> **Type:** Living document — update as stakeholders change throughout the project.
> **Last Updated:** 2026-03-31

---

## 1. Client Stakeholders

| Name | Organisation | Role | Responsibilities | Communication Preference | Approval Authority |
|---|---|---|---|---|---|
| John Paul Jones | HeyChar | CEO | Final sign-off on requirements, scope, and significant spend decisions. Monthly summary recipient. CR co-approver. | Teams / Email (formal) | Yes — full authority |
| Kate Bush | HeyChar | Head of HR | Day-to-day point of contact. CR co-approver. UAT lead. Coordinates test data. Weekly call participant. | Teams (day-to-day), Email (formal) | Yes — CR co-approver |
| Nick Cave | HeyChar | Senior Lawyer | Consulted on compliance, regulatory obligations, security requirements, and data retention policy. Must be satisfied before go-live on compliance items. | Email / Teams (ad hoc) | No — advisory only |
| Mary Smith | HeyChar | Senior HR Manager | UAT participant. End-user perspective on form-filling workflow. | Teams | No |
| Sam Altman | HeyChar | HR | UAT participant. End-user perspective. | Teams | No |
| George Carlin | HeyChar | HR (Junior) | UAT participant — usability and ease-of-use focus. | Teams | No |
| Tom [surname TBD] | HeyChar | IT | Owner of HR database and its internal API. Key technical contact for integration. Not a decision-maker on scope. | TBD | No |

---

## 2. Delivery Team

| Name | Role | Responsibilities |
|---|---|---|
| [Name] | Project Manager | Delivery oversight, monthly reporting to John, budget tracking, milestone management |
| [Name] | Business Analyst (Sarah) | Requirements elicitation, CR and BR creation, Glossary/SRS ownership, stakeholder comms |
| [Name] | Tech Lead / Dev | Architecture decisions, HR database integration, OCR integration |
| [Name] | Developer | Feature implementation |
| [Name] | QA | Test design, UAT support, acceptance verification |

---

## 3. End Users

| User Group | Description | Primary Needs | Features Used |
|---|---|---|---|
| **HR Managers** | HeyChar HR team responsible for processing work applications | Fast, accurate form completion; right-to-work compliance recording; document generation | Pre-fill, OCR capture, document generation, right-to-work flag, audit trail |
| **Work Applicants** | Individuals applying for work through HeyChar | Quick, frictionless application experience | Form submission, document upload (if self-service is in scope) |

---

## 4. External Systems & Integrations

| System | Owner | Purpose | Contact / Support |
|---|---|---|---|
| **HR Applicant Database** | HeyChar IT (Tom) | Source of returning applicant records for pre-fill; target for new application records | Tom [IT] — API documentation pending |
| **Microsoft Word / Excel** | HeyChar (Office 365) | Current form templates — source for form field requirements | Kate Bush (templates to be shared) |
| **Email / SMTP (Outlook)** | HeyChar IT | Notifications to HR managers and applicants | Standard SMTP |
| **Document Storage** | HeyChar IT | Storage of completed applications and identity documents | TBD — SharePoint vs shared network drive decision pending |
| **OCR / Identity Verification Service** | TBD | Extract data from identity documents (passports, visas, BRP cards) | Vendor not yet selected |
| **DocuSign** | HeyChar | Digital signature for document sign-off | Already in use — no setup required |

---

## 5. RACI Summary

| Activity | John Paul Jones | Kate Bush | Nick Cave | BA | Tech Lead | QA |
|---|---|---|---|---|---|---|
| Requirements sign-off | A | R | C (compliance) | R | I | I |
| Change request approval | A/R | A/R | C (if compliance) | R | I | I |
| Security & compliance requirements | I | C | A/R | R | C | I |
| Technical architecture decisions | I | I | I | C | A/R | C |
| UAT sign-off | I | A/R | C (compliance) | C | C | R |
| Go-live approval | A/R | R | C (compliance) | C | C | C |
| Budget / significant spend approval | A/R | C | I | C | C | I |

**R** = Responsible · **A** = Accountable · **C** = Consulted · **I** = Informed

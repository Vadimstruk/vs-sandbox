# Client Kickoff Questionnaire — VS-SANDBOX

> **Purpose:** Structured set of questions for the BA to ask at project kickoff or client onboarding.
> **Date:** 2026-03-31
> **Attendees:** Kate Bush (Head of HR, HeyChar), BA
> **Conducted by:** Sarah (BA)

---

## 1. Project & Business Context

**1.1** What problem are we solving? What is happening today that is causing pain?
> HR workers in the UK spend significant time and effort completing and processing work applications using standard Microsoft Word/Excel templates. The process is manual, repetitive, and slow.

**1.2** Who are the primary end users of this system? What do they need to be able to do?
> HR managers and work applicants. Both need a quick and convenient way to fill applications — either pre-filled from the existing applicant database (returning applicants) or via OCR scanning of identity documents (new applicants).

**1.3** What does success look like in 6 months? In 12 months?
> Time required for one application processing decreased by at least 30%.

**1.4** What is the business impact of NOT doing this project, or doing it too slowly?
> HR managers waste time, which wastes business money. No improvement in throughput or accuracy.

**1.5** Are there any competing initiatives or dependencies we should know about?
> No.

---

## 2. Stakeholders & Decision Making

**2.1** Who has final sign-off authority on requirements and scope decisions?
> John Paul Jones (CEO, HeyChar)

**2.2** Who approves Change Requests before development begins?
> John Paul Jones (CEO) and Kate Bush (Head of HR) — dual sign-off.

**2.3** Who is the day-to-day point of contact for questions during development?
> Kate Bush

**2.4** Who needs to be involved in UAT?
> Kate Bush (lead), Mary Smith (Senior HR), Sam Altman (HR), George Carlin (HR — usability focus)

**2.5** Are there any stakeholders not in this meeting whose input will be needed?
> Nick Cave (Senior Lawyer) — needed on regulatory, compliance, and security requirements.

**2.6** What is the expected turnaround time for responses to BA questions or document reviews?
> 2–3 business days.

---

## 3. Domain & Regulatory

**3.1** What industry does this system operate in? Are there specific regulations we must comply with?
> HR and workforce staffing, UK. Must comply with UK employment law and right-to-work legislation — every applicant must be verified as having the legal right to work in the UK before starting.

**3.2** Are there data protection or privacy requirements?
> Yes — UK GDPR and the Data Protection Act 2018 apply. Personal data including identity documents is in scope. Data retention, consent, and document storage duration must be carefully managed.

**3.3** Are there right-to-work, immigration, or employment law compliance obligations?
> Yes — this is a core function of the system. HR managers currently manually check right-to-work documents (passports, visas, BRP cards). The system must capture and record that the check was performed, and flag expiry dates and issues.

**3.4** Are there audit or reporting obligations?
> Yes — potential Home Office audits require a clear audit trail: who processed which application, when, and what documents were provided. HMRC employment records compliance is also relevant.

**3.5** Are there specific security standards required?
> No formal certification required at this stage. Expected: RBAC, encrypted document storage, secure transmission. Nick Cave to review and confirm before security requirements are finalised.

---

## 4. Existing Systems & Integrations

**4.1** What existing systems does this project need to integrate with?
> HR applicant database, Microsoft Word/Excel templates (current forms), email/Outlook (notifications), and document storage (currently a shared network drive; SharePoint migration under consideration).

**4.2** For each integration — is there an existing API?
> HR database: basic internal API, undocumented — owned by Tom (IT). Microsoft Word/Excel: no formal API. Email: SMTP. SharePoint: proper API if adopted.

**4.3** Are there existing databases or data sources the system must use?
> Yes — the HR applicant database. Holds previous application records, personal details, and employment history for returning applicants. Pre-fill from this database is a core MVP feature.

**4.4** Are there third-party services already contracted?
> No OCR or identity verification vendor contracted yet — open to recommendations. Notifications via Outlook/SMTP.

**4.5** What happens if an integration is unavailable?
> HR managers must be able to continue working. The process cannot stop because a service is down. Minimum: manual form fill as a fallback within the new system, equivalent to today's process.

---

## 5. Scope & Constraints

**5.1** What is explicitly out of scope?
> Payroll, performance reviews, contracts management, applicant tracking system, job posting functionality. This is purely the application form filling and processing workflow.

**5.2** Are there technical constraints?
> Microsoft-heavy organisation (Windows, Office 365). Web-based solution preferred — nothing installed locally. Azure preferred for hosting given existing Microsoft agreements. No hard stack requirement but must work well in this environment.

**5.3** What are the MVP must-haves?
> 1. Pre-filling forms for returning applicants from the database
> 2. OCR scanning of identity documents to extract data
> 3. Generating the completed application as a Word or PDF document
> 4. Right-to-work flag (Should Have for v1)
> 5. Document expiry date tracking (Should Have for v1)

**5.4** Are there hard deadlines?
> Soft internal deadline: end of Q3 2026 (September 2026). Head of HR wants to show results at an internal review in October 2026. No external contractual deadline, but missing the October review is politically significant.

**5.5** Are there budget constraints?
> No formal hard cap. John Paul Jones (CEO) must sign off on any significant spend. Pragmatic approach — features with low value relative to cost will be cut.

**5.6** Geographic or language/localisation requirements?
> English only. UK operations only. No multilingual requirements.

---

## 6. Existing Documentation & Prior Work

**6.1** Is there any existing documentation?
> Word and Excel form templates (to be shared by Kate). A rough process map created by Kate showing the HR manager's steps per application. No wireframes or formal specs.

**6.2** Has a version of this system been built before?
> No. A conversation about it occurred approximately two years ago but did not progress past discussion.

**6.3** Has HeyChar worked with an external development partner before?
> Yes — ~18 months ago on an internal reporting dashboard. Mixed experience: slow initial delivery, significant back-and-forth due to unclear requirements. End product was acceptable but exceeded timeline and budget slightly. This is a key motivation for a structured BA process on this engagement.

**6.4** Known pain points or failed past attempts?
> Vague requirements led to expensive rework in the previous engagement. Usability is a critical risk — Kate has flagged that if the system is complicated, HR managers will revert to manual Word-based processing. Adoption is a real risk if UX is not intuitive.

---

## 7. Communication & Working Preferences

**7.1** Preferred communication channel?
> Microsoft Teams for day-to-day. Email for formal items requiring a paper trail (document sign-off, etc.).

**7.2** Meeting cadence?
> Weekly 30-minute check-in with Kate. Monthly summary to John (RAG status, key decisions, items requiring his attention).

**7.3** Who receives written updates and how often?
> Kate Bush — weekly. John Paul Jones — monthly concise summary. Nick Cave — ad hoc, only when legal/compliance topics arise.

**7.4** How to handle urgent blockers?
> Teams message to Kate directly. If Kate unavailable and genuinely blocking: escalate to John via Teams. Expected response within a few hours during business hours.

**7.5** Digital signature comfort?
> Yes — DocuSign already in use for contracts. Fully comfortable with digital sign-off.

---

## 8. UAT & Go-Live

**8.1** Who will perform UAT?
> Kate Bush (lead), Mary Smith (Senior HR), Sam Altman (HR), George Carlin (HR — usability focus). All non-technical end users. Testing from a practical day-to-day usability perspective.

**8.2** Staging environment and test data?
> Yes, staging environment required — no testing on live data. HeyChar to provide anonymised records from existing applicant database. Kate to coordinate. BA to provide test data format and volume requirements in advance.

**8.3** Go-live criteria?
> 1. All MVP features working end-to-end
> 2. No critical or high-severity bugs outstanding
> 3. UAT signed off by Kate Bush
> 4. Nick Cave satisfied with compliance-related items
> 5. Basic user guide delivered and available to HR managers

**8.4** Post-launch support?
> Not yet agreed. Expectation of 2–4 week hypercare period post go-live with fast-tracked issue resolution. Ongoing support model to be discussed and agreed — John Paul Jones sign-off required on cost.

**8.5** Blackout periods?
> January–March: busy hiring season — avoid major releases.
> April: financial year-end — avoid major releases.
> October: relatively quiet — aligns well with Q3 internal review target.

---

## 9. Open Items & Follow-Ups

| # | Open Item | Owner | Due Date |
|---|---|---|---|
| 1 | Kate to share Word/Excel form templates | Kate Bush | Before requirements finalised |
| 2 | Kate to share HR manager process map | Kate Bush | Before requirements finalised |
| 3 | Tom (IT) to provide HR database API documentation | Tom (IT) | Before integration design begins |
| 4 | Decision required: document storage — SharePoint vs shared network drive | John / Kate | Before architecture decisions finalised |
| 5 | OCR / identity verification vendor selection — BA/PM to support with recommendations | BA / PM | Before development begins |
| 6 | Nick Cave to review and confirm security requirements and data retention policy | Nick Cave | Before SRS finalised |
| 7 | BA to provide test data format and volume requirements to Kate | BA | Before staging environment setup |
| 8 | Post-go-live support model to be agreed | John Paul Jones | Before go-live |
| 9 | Confirm Tom's full name and add to Stakeholder Register | Kate Bush | Next call |

---

## 10. BA Notes

> Internal working notes — not shared with client.

- **Assumptions identified:** Azure preferred but not hard-mandated; SharePoint migration unconfirmed; budget cap TBD; Word/Excel templates to be provided before requirements finalised; HR database API docs to be provided before integration design.
- **Glossary terms to add:** Right-to-Work Check, BRP Card, Audit Trail, Data Retention, Returning Applicant, Pre-fill, Degraded Mode, OCR.
- **Risks flagged:**
  - HR database API is undocumented — integration complexity unknown until Tom is engaged.
  - SharePoint migration decision could significantly affect document storage architecture.
  - User adoption risk — usability must be treated as a first-class requirement.
  - Nick Cave not yet engaged — security and data retention requirements cannot be finalised without him.
  - Q3 deadline is soft but politically significant — scope discipline will be critical.
- **Next steps:** Populate Charter, Stakeholder Register, Assumptions Log, Glossary from this session. Schedule follow-up to collect templates and process map from Kate. Loop in Nick Cave early on compliance scope.

# Glossary — VS-SANDBOX

> **Type:** Living document — add new terms as they emerge. All project documents should use terms exactly as defined here. Never delete terms — mark as deprecated if no longer in use.
> **Last Updated:** 2026-03-31
> **Domain:** HR and workforce staffing — UK
> **Confluence:** https://vstest.atlassian.net/wiki/spaces/VSSB2/pages/1048577

---

## How to Use This Document

- Terms are listed alphabetically by letter heading.
- Bold the term name, follow with a plain-language definition on the next line.
- Cross-reference related terms with *See also: [Term]*.
- If a term is no longer in use, add `*(Deprecated)*` after the term name rather than deleting it.
- All project documents must use terms exactly as defined here.

---

## A

**Application Form**
The structured document that captures all required information about a work applicant — personal details, identity documents, right-to-work status, and employment history. Currently produced as a Microsoft Word or Excel document; this system replaces that manual process.

**Applicant**
An individual applying for work through HeyChar. May be a new applicant (no existing record in the HR database) or a returning applicant. *See also: Returning Applicant.*

**Audit Trail**
A chronological record of who performed which action in the system, when, and on which application. Required for potential Home Office right-to-work audits. The system must maintain an audit trail for every application processed.

---

## B

**BRP Card (Biometric Residence Permit)**
An identity document issued to non-UK nationals that confirms their right to live, work, and study in the UK. One of the key document types the system must support for OCR capture and right-to-work verification. *See also: Right-to-Work Check.*

---

## D

**Data Retention**
The rules governing how long personal data — including identity documents and application records — may be held by HeyChar before it must be deleted or anonymised. Governed by UK GDPR and the Data Protection Act 2018. Specific retention periods to be confirmed with Nick Cave (Senior Lawyer).

**Degraded Mode**
The operating state of the system when one or more integrations (e.g. the HR database or OCR service) are unavailable. In degraded mode, HR managers must be able to continue processing applications manually within the system — equivalent in capability to the current Word/Excel process. The system must not become inoperable due to a single integration failure.

---

## H

**HeyChar**
The client organisation. Operates in HR and workforce staffing in the UK. The system being built is for HeyChar's internal HR team.

**HR Database**
HeyChar's existing internal database of applicant records. Contains personal details, employment history, and previous application data for returning applicants. The system integrates with this database to enable pre-fill for returning applicants. Owned and maintained by Tom (IT). *See also: Pre-fill, Returning Applicant.*

**HR Manager**
A member of HeyChar's HR team who processes work applications using this system. The primary end user. Currently processes applications manually using Microsoft Word and Excel templates.

---

## O

**OCR (Optical Character Recognition)**
Technology that extracts text data from scanned or photographed documents — in this context, identity documents such as passports, visas, and BRP cards. Used to automatically populate application form fields from document images, reducing manual data entry.

---

## P

**Pre-fill**
The automatic population of application form fields using data already held in the HR database for a returning applicant. Reduces the time HR managers spend entering repeated information for applicants who have applied before. *See also: Returning Applicant, HR Database.*

---

## R

**Returning Applicant**
An applicant who has previously been processed through HeyChar and whose records exist in the HR database. When a returning applicant is identified, the system pre-fills the application form from their existing record rather than requiring data to be entered from scratch. *See also: Pre-fill.*

**Right-to-Work Check**
The legally required verification that an applicant has the right to work in the UK before they begin employment. HR managers are legally obligated to check and record this for every applicant. Relevant documents include passports, visas, and BRP cards. The system must capture that this check was performed and maintain an audit trail. Governed by UK employment law and right-to-work legislation.

---

## U

**UAT (User Acceptance Testing)**
The phase of testing in which HeyChar's HR team (led by Kate Bush) validates that the system works correctly for their real day-to-day tasks. Conducted in a staging environment using anonymised test data. UAT sign-off by Kate Bush is a go-live criterion.

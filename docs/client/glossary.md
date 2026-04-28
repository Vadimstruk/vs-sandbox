# Glossary — PulseField Mobile

> **Type:** Living document — add new terms as they emerge. All project documents must use terms exactly as defined here. Never delete terms — mark as deprecated if no longer in use.
> **Version:** 1.0 (promoted from v0.1 after kickoff call 2026-04-28; expanded with terms surfaced during the call)
> **Last Updated:** 2026-04-28
> **Domain:** Field Service Management — small-business HVAC and plumbing contractors (United States)
> **Confluence:** [URL — pending]

---

## How to Use This Document

- Terms are listed alphabetically by letter heading.
- Bold the term name, follow with a plain-language definition on the next line.
- Cross-reference related terms with *See also: [Term]*.
- If a term is no longer in use, add `*(Deprecated)*` after the term name rather than deleting it.
- All project documents must use terms exactly as defined here.

---

## A

**App Store**
Apple's distribution channel for iOS applications. PulseField Mobile must be approved by App Store review before iOS go-live. *See also: Play Store.*

**Auth0**
A third-party identity-and-access-management platform. FieldPulse Solutions is migrating its authentication off a custom-rolled solution onto Auth0 (or similar) in 2026, in parallel with the PulseField Mobile project. Coordination required if mobile work touches login flows. *See also: Priya Krishnan, FieldPulse Web Platform.*

---

## C

**CCPA — California Consumer Privacy Act**
A US state-level data-privacy law in California granting consumers rights over the personal information businesses collect about them. CCPA reaches FieldPulse because some FieldPulse customers operate in California, and end-customer data flows through the platform. PulseField Mobile must support FieldPulse's CCPA obligations (notice, deletion requests, data-handling controls). *See also: SOC 2.*

---

## D

**DAU — Daily Active Users**
The count of unique users who use an application on a given calendar day. For PulseField Mobile, the relevant DAU metric is technician-DAU as a percentage of installed base. The agreed off-track signal at three months: technician-DAU below 30% of installed base.

---

## F

**Field Service Management (FSM)**
A category of business software used by companies whose work is performed at customer sites by mobile technicians. FSM tools cover scheduling, dispatch, job assignment, on-site data capture, and billing. FieldPulse Solutions' existing web platform is an FSM tool for HVAC and plumbing contractors. *See also: Job Assignment, Technician.*

**FieldPulse Solutions**
The client organisation. A small SaaS company (~12 employees, ~80 paying customers) based in Austin, Texas, providing a web-based FSM platform to HVAC and plumbing contractors. The PulseField Mobile project is FieldPulse's first mobile-first product extension.

**FieldPulse Web Platform**
The existing FieldPulse Solutions product — a web-based FSM tool, originally built by Tomás Ribeiro. RESTful / JSON APIs; PostgreSQL on AWS RDS. PulseField Mobile integrates with it via API only (no direct DB access). API documentation status: a Postman collection plus a ~60%-accurate README. *See also: Integration, Tomás Ribeiro.*

---

## H

**Housecall Pro**
A FSM competitor with mobile capability that has been winning deals against FieldPulse. Together with ServiceTitan, the source of the customer churn driving the PulseField Mobile project. *See also: ServiceTitan.*

**HVAC**
Heating, Ventilation, and Air Conditioning. One of the two trade verticals served by FieldPulse customers. HVAC has a strong seasonal pattern: cooling peak May–September, heating peak November–February — both are blackout windows for production releases. *See also: Plumbing, Blackout Period.*

---

## J

**Job Assignment**
A work item dispatched to a technician — historically delivered via SMS with limited detail, requiring the technician to phone the office for full context. PulseField Mobile delivers job assignments directly to the technician's device with full context attached. *See also: Job Data, Technician.*

**Job Data**
The information captured by a technician on-site during or at the end of a job — historically recorded on paper forms and submitted at end-of-day. PulseField Mobile captures this data digitally on-device (offline-capable) and submits it the same day to feed the FieldPulse Web Platform's billing and reporting. *See also: Same-Day Submission, Offline-by-default.*

---

## O

**Office Dispatcher**
The office-based staff at a FieldPulse customer business who today send SMS job assignments and process returned paper forms. Confirmed as a secondary end-user group at kickoff. They are not direct PulseField Mobile users — they continue to interact with the FieldPulse Web Platform — but the mobile app must surface job status back to them in real time. *See also: Technician, Job Assignment.*

**Offline-by-default / Sync-when-available**
The architectural principle that PulseField Mobile must operate without network connectivity by default and synchronise with the FieldPulse Web Platform when connectivity returns. Technicians work in basements, crawlspaces, mechanical rooms, and new-construction sites without signal — full offline capability for job-completion capture (checklist, notes, photos, signature) is a hard requirement. Has material architectural implications for state management and conflict resolution. *See also: Sync.*

---

## P

**Play Store / Google Play Store**
Google's distribution channel for Android applications. PulseField Mobile must be approved by Play Store review before Android go-live. *See also: App Store.*

**Plumbing**
The second of the two trade verticals served by FieldPulse customers. Same on-site profile as HVAC technicians; same primary-user-group status for PulseField Mobile. *See also: HVAC.*

**Postman Collection**
A file format used by the Postman API-development tool to bundle a set of HTTP requests describing an API. The FieldPulse Web Platform's API is documented today by a Postman collection (handed over by Tomás Ribeiro) plus a partially accurate README. The collection is the most reliable contract artefact available for the legacy API.

**Priya Krishnan**
Chief Technology Officer, FieldPulse Solutions. Primary technical counterpart for Relevant Software's tech lead. Email: priya@fieldpulse.io. *See also: Marcus Chen.*

**PulseField Mobile**
The mobile-first technician application that this project will deliver. Integrates with the existing FieldPulse Web Platform. Working title — final product naming may change before launch.

---

## S

**Same-Day Submission**
The target workflow that PulseField Mobile enables — job data captured on-site is submitted to the FieldPulse Web Platform the same day, removing the end-of-day paper-form lag that today delays billing and reporting (paper at 6pm → next-morning entry → 2-day invoice).

**ServiceTitan**
A FSM competitor with strong mobile capability, the primary competitive threat driving PulseField Mobile. ServiceTitan's sales push historically peaks in Q4 going into the new year — Marcus's stated reason for wanting mobile in technicians' hands by EoQ3 / early Q4. *See also: Housecall Pro.*

**SOC 2**
A widely recognised audit standard for SaaS providers covering security, availability, processing integrity, confidentiality, and privacy. SOC 2 Type II is the most common form B2B SaaS customers ask about. FieldPulse is pursuing SOC 2 certification in 2026 in parallel with the PulseField Mobile project — at least one prospective deal has been lost over the lack of it. **Hard requirement: PulseField Mobile must not be a barrier to FieldPulse's SOC 2 readiness.** *See also: CCPA.*

**Sundance HVAC**
A FieldPulse customer based in Phoenix, owned by Dave Martinez. Has been asking FieldPulse for mobile capability for ~2 years; offered to be the pilot customer for PulseField Mobile. Plan: 2–3 of Sundance's technicians on a real-world UAT pilot of ≥2 weeks. Pilot agreement subject to Marcus confirming with Dave.

**Sync**
The process by which data captured on a technician's device while offline is uploaded to the FieldPulse Web Platform once connectivity is available. Sync must be reliable in low-connectivity simulation as part of the go-live criteria. *See also: Offline-by-default.*

---

## T

**Technician**
A field-service worker employed by a FieldPulse customer (an HVAC or plumbing contractor business). The primary end user of PulseField Mobile. Operates predominantly in the field — residential and commercial premises. Customer base estimated at ~950 active technicians across ~80 customer businesses. Year-1 adoption target: 30–40%. *See also: Job Assignment, Job Data, Office Dispatcher.*

**Tomás Ribeiro**
The original freelance developer of the FieldPulse Web Platform. Based in Lisbon. On a casual retainer with FieldPulse — approximately 5 hours per week for emergencies and consultation. Reachable for legacy-API discussion. *See also: FieldPulse Web Platform.*

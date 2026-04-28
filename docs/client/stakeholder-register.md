# Stakeholder Register — PulseField Mobile

> **Type:** Living document — update as stakeholders change throughout the project.
> **Version:** 1.1 (updated after Charter Review call 2026-04-30 — Jenna email confirmed + R-014 co-owner; Dave verbally confirmed; Slack workspace locked)
> **Last Updated:** 2026-04-30
> **Confluence:** [URL — pending]

---

## 1. Client Stakeholders

| Name | Organisation | Role | Responsibilities | Communication Preference | Approval Authority |
|---|---|---|---|---|---|
| **Marcus Chen** | FieldPulse Solutions | Founder & CEO | Business decision-maker; primary day-to-day BA contact; sole sign-off on requirements, scope, UAT, go-live. CRs <10% scope: Marcus alone. CRs ≥10% scope: Marcus + Priya (technical implications). **CR scope is measured against the Roadmap baseline once signed off, not against the Charter** *(clarification 2026-04-30)*. Ex-software-engineer (~10y prior); now operates as a business leader. Visibly anxious about competitor pressure. | Slack DM (`fieldpulse.slack.com`, primary); email for formal documents only. **Weekly status call Wednesday 9am Central, 30 min hard stop** *(locked 2026-04-30)*. **EoF Friday written status** — bullet points, ≤1 screen on laptop, recipients Marcus + Priya. 48hr SLA normal items / same-day blockers / 3 business days for document reviews. | **Yes — full authority** *(with the CR-threshold nuance above)* |
| **Priya Krishnan** | FieldPulse Solutions | Chief Technology Officer | Primary technical counterpart for the Relevant tech lead. Co-approver for CRs ≥10% scope. Owner of platform-architecture one-pager (D-008, ETA EoD Wed ~2026-05-06 with API endpoint inventory). **Owner of I-001 / I-002 + R-009** *(updated 2026-04-30)* — data residency + breach-notification policies drafted under SOC 2 program (drafts by July 2026). **Owner of Auth0 ADR review + Tech Lead intro** (D-012, this week). Hard line: mobile app talks to platform via API only — no direct DB access. | Email: priya@fieldpulse.io. Phone separately. Slack workspace `fieldpulse.slack.com`, channel `#pulsefield-mobile` (created by Priya 2026-04-30). Same status-call cadence as Marcus (Wed 9am Central). | Technical decisions: yes. Scope CRs: shared with Marcus per threshold. |
| **Jenna Rodriguez** | FieldPulse Solutions | Customer Success Lead | Internal UAT proxy testing; rollout planning to FieldPulse customer base; **co-owner of R-014 Training Materials** *(added 2026-04-30 — runs the customer-facing rollout for FieldPulse)*; will have opinions on UX and onboarding; co-signs design reviews with Marcus per R-007 mitigation cadence. New hire (joined ~March 2026). | **Email: jenna@fieldpulse.io** *(confirmed 2026-04-30)*. Slack workspace `fieldpulse.slack.com` (channel `#pulsefield-mobile`). Copied on EoF Friday written status. | No formal authority; consulted on UAT and rollout; co-owner on R-014. |
| **Dave Martinez** | Sundance HVAC (Phoenix) | Owner | Pilot customer for real-world UAT — has been requesting mobile from FieldPulse for ~2 years; offered to be a guinea pig. **3 technicians (team rotation, not solo testers)** — Dave's preferred shape *(confirmed 2026-04-30)*. **Verbally confirmed 2026-04-24** in a call with Marcus; **written agreement pending Sundance pilot one-pager** (D-010 RAID — Vadim drafts, Marcus forwards, ETA written confirmation 2 weeks post-forward). | Via Marcus initially. | UAT participation: **verbally confirmed; written pending**. |

---

## 2. Delivery Team — Relevant Software

> Most named entries TBC pending team-staffing confirmation. Vadim is BA (confirmed); other roles to be assigned.

| Name | Role | Responsibilities |
|---|---|---|
| TBC | Project Manager | Delivery accountability; schedule, budget, governance; CR coordination; weekly Friday status update authoring |
| **Vadim** *(surname TBC)* | Business Analyst | Requirements, client-facing documentation, kickoff and discovery, RAID and Roadmap maintenance, Marcus's primary BA-side counterpart |
| TBC | Tech Lead | Architecture, technical discovery on the FieldPulse legacy platform (with Priya), ADRs, API hardening assessment, offline architecture decisions |
| TBC | Mobile Developers (≥1) | Implementation — both iOS 15+ and Android 10+ (Android prioritised if phasing required) |
| TBC | QA | Test strategy, automation, UAT support, low-connectivity simulation |
| TBC | DevOps | CI/CD, environments (incl. staging with synthetic data per Priya), release pipeline, App Store / Play Store submissions |
| TBC | UX Designer | UX flows for technician-facing app, on-site usability — *gains weight given FieldPulse's lack of design lead* |

---

## 3. End Users

| User Group | Description | Primary Needs | Features Used |
|---|---|---|---|
| **Field-service Technicians** *(primary)* | HVAC and plumbing technicians employed by FieldPulse's ~80 customer businesses. ~950 active technicians estimated across the base (~12 per customer). Operate predominantly in the field — residential and commercial premises, basements, crawlspaces, mechanical rooms, new-construction sites. Skew Android (~65%). Year-1 adoption target: 30–40% of active population. | Receive job assignments with full context on-device; capture job-completion data on-site (replacing paper); operate fully offline with sync when connectivity returns; minimal training. | Job assignment view, offline job-completion capture (checklist / notes / photos / parts / time), customer signature capture, sync, schedule view. |
| **Office Dispatchers** *(secondary, confirmed at kickoff)* | Office-based staff at FieldPulse customers — the people sending today's SMS dispatches and processing today's paper forms. Almost every FieldPulse customer has at least one. | Visibility into technician status; faster job-completion data into the existing web platform once mobile is rolled out. | Existing FieldPulse Web Platform — read the data the mobile app sends back. Not direct mobile-app users. |

---

## 4. External Systems & Integrations

| System | Owner | Purpose | Contact / Support |
|---|---|---|---|
| **FieldPulse Web Platform** *(primary integration)* | FieldPulse Solutions; originally built by Tomás Ribeiro | Source of job assignments and recipient of completed job data. Mobile is additive — not a replacement. RESTful / JSON APIs. PostgreSQL on AWS RDS. API-only access from mobile. **Wrapper / proxy layer planned (not conditional)** per Priya 2026-04-30. | Priya Krishnan (priya@fieldpulse.io); Tomás Ribeiro on retainer ~5 hours/week — **verbal arrangement, not contractual** (continuity tracked under R-012 RAID) |
| Stripe | Stripe Inc. | Payments processing on the FieldPulse Web Platform | Existing FieldPulse account; not in mobile MVP scope |
| Twilio | Twilio Inc. | SMS for current job-assignment workflow (which the mobile app replaces, but Twilio remains used for fallback / other notifications) | Existing FieldPulse account |
| Google Maps | Google | Embedded routing on the existing platform; future mobile use TBC | Existing FieldPulse account |
| SendGrid | Twilio (SendGrid) | Transactional email | Existing FieldPulse account |
| Intercom | Intercom Inc. | Existing in-app chat on the web platform — **open question whether to extend to mobile** | Existing FieldPulse account |
| Sentry | Sentry | Error tracking; expected to extend to mobile | Existing FieldPulse account |
| Mixpanel | Mixpanel | Analytics; lightly used today; expected to extend to mobile for adoption-tracking | Existing FieldPulse account |
| CloudFront | AWS | CDN for AWS assets | Existing FieldPulse account |
| **Push notifications provider** *(to be selected)* | TBD (e.g. Firebase Cloud Messaging, AWS SNS, OneSignal) | Mobile push notifications — not in current FieldPulse stack | TBD at architecture decision |
| **Auth0** *(parallel project + mobile integration)* | Auth0 | **Mobile authenticates against Auth0 from day one** *(decided 2026-04-30)* in a parallel Auth0 environment. FieldPulse web-platform Auth0 migration runs separately — 4–6 month horizon (Aug–Oct 2026 target). Both systems coexist briefly. SOC 2 Type II certified. | Priya Krishnan |

---

## 5. RACI Summary

> Confirmed at kickoff with the CR-threshold nuance for Marcus's authority.

| Activity | Marcus | Priya | Jenna | PM (TBC) | BA (Vadim) | Tech Lead (TBC) | QA (TBC) |
|---|---|---|---|---|---|---|---|
| Requirements sign-off | A/R | C | I | C | R | I | I |
| Change request approval — <10% scope | A/R | I | I | C | R | I | I |
| Change request approval — ≥10% scope | A/R | A/R | I | C | R | C | I |
| Technical decisions | I | A/R | I | I | C | R | C |
| UAT sign-off | A/R | C | R | C | C | C | R |
| Go-live approval | A/R | C | C | R | C | C | C |
| Integration scope (legacy platform) | A | R | I | C | C | R | I |
| Pilot coordination (Sundance HVAC) | A | I | R | R | C | I | C |
| Post-launch support handoff | A/R | A | C | R | C | R | C |

**R** = Responsible · **A** = Accountable · **C** = Consulted · **I** = Informed

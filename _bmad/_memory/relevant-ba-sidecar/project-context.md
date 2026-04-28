# Project Context — Homer

Per-project knowledge. One section per project Homer has worked on. Lets Homer pick up cleanly when re-engaged.

The **Progress Tracker** matrix is the single source of truth for "what's done, what's next, what's blocked" on each project. Update at every checkpoint (after every meaningful capability execution).

**Status values:** `not-started` · `drafting` · `in-review` · `signed-off` · `living` · `superseded` · `out-of-profile`.

---

## PulseField Mobile (Marcus Chen)

- **Profile:** Agile — Fixed-Range
- **Profile set:** 2026-04-27
- **Phase:** Project Setup
- **Project type:** Mobile-first technician app (greenfield) integrating with FieldPulse's existing web platform
- **Industry:** SaaS — Field Service Management (HVAC, Plumbing)
- **Client company:** FieldPulse Solutions, Austin TX, 12 employees, ~80 paying customers (small businesses with 5–30 field technicians each)
- **Roadmap version:** _Not yet created_
- **Glossary refs:** _Not yet created_
- **Persona refs:** _Not yet created — primary persona: field technician (HVAC / plumbing)_
- **Recent CR IDs:** _None_

### Known stakeholders (from Sales brief)

- **Marcus Chen** — Founder & CEO, FieldPulse Solutions; decision-maker; ex-software-engineer (~10y ago); now business-focused.
- **Priya** *(surname pending)* — CTO, FieldPulse Solutions; primary technical counterpart.

### Commercial signals (directional only — not confirmed)

- **Budget:** "Flexible, but we're not a big enterprise — needs to be reasonable." → undefined; flagged as Budget mismatch risk.
- **Timeline:** "Something usable by the end of Q3." → Marcus admitted unsure if realistic.
- Both must be validated during discovery before any Roadmap or Charter sign-off.

### Progress Tracker

| Doc | Status | Sign-off | Location | Last Updated |
|---|---|---|---|---|
| Methodology Profile | signed-off | n/a | sidecar `index.md` | 2026-04-27 |
| Source materials check | signed-off | n/a | `docs/reference/FieldPulse_Client_Brief.pdf` | 2026-04-28 |
| Kickoff Meeting Notes | signed-off (call complete) | n/a | `docs/client/meetings/kickoff-meeting-2026-04-28.md` *(transcript: `docs/reference/kickoff-call-transcript.csv`)* | 2026-04-28 |
| Charter Review Meeting Notes | signed-off (call complete) | n/a | `docs/client/meetings/meeting-notes-2026-04-30.md` *(transcripts: `docs/reference/charter-review-call-transcript.csv` + `roadmap-review-transcript.csv`; original agenda archived: `docs/.archive/meeting-agenda-2026-04-28.md`)* | 2026-04-30 |
| Project Charter | in-review (v1.1 — DocuSign in flight) | required: yes — Marcus 48hr commitment from 2026-04-30 send; cover note signals anticipated v1.2 post-D-009 legal review | `docs/client/charter/project-charter-v1.1.md` *(v0.1 + v1.0 archived in `docs/.archive/`)* | 2026-04-30 |
| Stakeholder Register | living (v1.1) | n/a | `docs/client/stakeholder-register.md` | 2026-04-30 |
| Glossary | living (v1.0) | n/a | `docs/client/glossary.md` | 2026-04-28 |
| RAID Log | living (v1.1 — 12 risks, 8 assumptions, 4 issues, 12 dependencies, 10 constraints) | n/a | `docs/client/raid-log.md` | 2026-04-30 |
| Vision Statement | living — light agreement obtained | light agreement obtained 2026-04-30 | `docs/client/vision/product-vision.md` | 2026-04-30 |
| Product Roadmap | living (Roadmap 2026-04 v1.1 — 7 amendments applied; Marcus approved with version stamp) | light, ongoing — no formal baseline; **CR baseline as of 2026-04-30** | `docs/client/roadmap/product-roadmap.md` | 2026-04-30 |
| Personas + Journey Maps | not-started *(optional)* | n/a | `docs/client/personas/` *(planned)* | — |
| Client PRD | not-started | required: yes | `docs/client/prd/` *(planned)* | — |
| SDD | not-started — will become living | n/a | `docs/client/sdd/` *(planned)* | — |
| ADRs | not-started — on-trigger | n/a | `docs/client/adr/` *(planned)* | — |
| Auth0 ADR (specific) | drafting target ~2026-05-14 — Tech Lead | n/a | `docs/client/adr/` *(planned)* | — |
| Sundance pilot one-pager | not-started — needed before D-004 written confirmation | n/a | `docs/client/` *(path TBC — new artefact type)* | — |
| SRS | out-of-profile | — | — | — |
| BRs | out-of-profile | — | — | — |

### Open items

- **Charter v1.1** — routed for DocuSign 2026-04-30; Marcus committed 48hr turnaround. Cover note signals anticipated v1.2 amendment post-D-009 legal review (findings mid–late May).
- **DocuSign package** to send 2026-05-01 (after Sundance one-pager drafted): Charter v1.1 + Roadmap 2026-04 v1.1 + full RAID Log + Sundance pilot one-pager.
- **Sundance pilot one-pager (D-010)** — Vadim drafts target 2026-05-01 → Marcus forwards to Dave → ~2 weeks to written confirmation. Path TBC (new artefact type — may need framework decision on location).
- **Auth0 ADR (D-012)** — Tech Lead drafts within 2 weeks of 2026-04-30 (target ~2026-05-14). Priya prepping Auth0 setup briefing this week (~EoW 2026-05-02). Tech Lead intro this week. Closes D-006 RAID.
- **Slack workspace (D-011)** — Vadim sends PM + Tech Lead work emails to Priya by EoD 2026-04-30. Priya creates `#pulsefield-mobile` and sends invites same-day.
- **D-008 architecture one-pager** — Priya said "EoD Wed this week" on Thu 2026-04-30. **Confirm: 2026-05-06 (most plausible) vs already-passed 2026-04-29.** Will include API endpoint inventory + architecture diagram. R-006 6-week clock starts on receipt.
- **D-009 legal review** — Marcus engaging counsel by EoW 2026-05-08; scope: CCPA + gov-contractor flow-down (school-district + municipal-building customers) + SOC 2 readiness gap. Findings mid–late May, worst case early June. Drives Charter v1.2 amendment.
- **D-007 Notion notes + whiteboard** — whiteboard photo same-day 2026-04-30; cleaned Notion notes EoW 2026-05-02.
- **R-009 / I-001 / I-002** — owner now Priya; drafted under SOC 2 program (kickoff late May 2026; both policies drafted by July 2026).
- **A-008 capacity assumption** — Marcus saw the Roadmap internal note. Confirm Relevant team shape at next status call (Wed 2026-05-06).
- **Marcus's parting question** — *"What worries you most after this conversation?"* — talking points prepped in `docs/client/meetings/meeting-notes-2026-04-30.md` §10. Lead with Auth0 dependency + legal-review pair (structural); close with Tomás retainer continuity, capacity, design-cadence.
- **Cadence locked:** weekly status Wed 9am Central / 30 min hard stop; EoF Friday written status (≤1 screen, Marcus + Priya); Slack `fieldpulse.slack.com` / `#pulsefield-mobile`; CR baseline = Roadmap once signed off, not Charter.
- **Roadmap shape (post-amendment):** 4 themes (Mobile-First Field Workflow, Operational Readiness, Customer Adoption & Rollout, Platform Modernisation Alignment); 24 initiatives — 11 Now, 8 Next, 5 Later. Cut-from-MVP return order locked: R-016 → R-019 → R-017 → R-018. R-005 Schedule View flagged as first MVP-flex candidate if envelope is tight.
- **Next capability:** `CP` (Client PRD covering MVP) → `SD` (SDD initialisation as a stub). Sundance one-pager is a pre-req before sending the DocuSign package.

### Materials mined to date

| File | Type | Source | Mined |
|---|---|---|---|
| `docs/reference/FieldPulse_Client_Brief.pdf` | Pre-discovery client brief (Sales hand-off) | Internal — Sales | 2026-04-28 |
| `docs/reference/kickoff-call-transcript.csv` | Kickoff call transcript | Client — call recording | 2026-04-28 |
| `docs/reference/charter-review-call-transcript.csv` | Charter Review call (main session — Charter / Vision / Auth / RAID / sign-off / cadence) | Client — call recording | 2026-04-30 |
| `docs/reference/roadmap-review-transcript.csv` | Charter Review call (Roadmap walk-through portion — Marcus had not seen Roadmap pre-call) | Client — call recording | 2026-04-30 |

### Initial RAID seeds (from brief, to populate RAID Log on first draft)

**Risks (verbatim from brief):**
- R-001 Scope ambiguity — "mobile app" undefined (platforms, offline, features). High prob / High impact.
- R-002 Timeline realism — EoQ3 may not be feasible given integration complexity. High / High.
- R-003 Legacy integration risk — existing web app freelancer-built, API quality / docs / architecture unknown. High / High.
- R-004 Budget mismatch — "reasonable" undefined; may not align with production-grade mobile cost. Medium / High.
- R-005 Org maturity — FieldPulse's first project of this scope; process/governance/approvals to be established. Medium / Medium.

**Initial assumptions (to confirm with client):**
- A-001 Marcus has sole sign-off authority on requirements and scope.
- A-002 Priya is the primary technical counterpart for our team.
- A-003 US-only deployment (Austin-based, no localisation).
- A-004 No direct regulatory burden on the app itself (B2B SaaS for contractors).

**Initial dependencies:**
- D-001 Existing FieldPulse web platform API — legacy, freelancer-built; needs technical discovery before integration scoping.

### Notes

- Previous `docs/client/` artefacts (assumptions-log, charter, glossary, prd, srs, stakeholder-register) were unrelated to PulseField Mobile and have been removed by Vadim.
- Previous `docs/reference/` files (BA Reference Guide, Confluence Space Structure, JIRA CSV, SDD template) likewise unrelated and removed.
- Working title "PulseField Mobile" — final product name to be confirmed at kickoff. Sales brief filename uses "FieldPulse" (the company); the project name is a derived working title.
- Sales rep recommended an initial discovery session before any solutioning or estimation begins — this aligns with running a kickoff call with a tailored Questionnaire.

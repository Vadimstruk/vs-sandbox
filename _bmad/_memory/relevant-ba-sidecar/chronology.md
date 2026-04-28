# Chronology — Homer

Significant project events. Append-only; prune regularly.

---

## 2026-04-27 — Sidecar initialised; PulseField Mobile profile set

- First-run setup of Homer's sidecar at `_bmad/_memory/relevant-ba-sidecar/`.
- Active project registered: **PulseField Mobile** (client: Marcus Chen).
- Methodology profile set to **Agile — Fixed-Range** via `MP` capability.
- No prior profile to migrate from.
- Reason for profile choice: pending — Vadim selected directly, no commercial-shape framing captured.

## 2026-04-27 — Framework cleanup: RAID Log replaces Assumptions & Constraints Log

- Created `docs/templates/raid-log/raid-log-template.md` from `documentation-guide.md` § RAID Log spec (lines 670-676). Schema: Risks, Assumptions, Issues, Dependencies + optional Constraints register; status set Open / Confirmed / Mitigated / Invalidated / Closed / Superseded.
- Deleted obsolete `docs/templates/assumptions-log/`.
- Migrated cross-references in 4 templates (`srs-template.md`, `project-charter-template.md`, `meeting-agenda-template.md`, `kickoff-questionnaire-template.md`) from "Assumptions Log" / `assumptions-log.md` to "RAID Log" / `raid-log.md`.
- Charter template Section 5 renamed "Assumptions" → "Key Risks & Assumptions" to acknowledge the broader RAID scope.
- One historical artefact left untouched: `docs/analysis/kickoff-questionnaire-2026-03-31.md` — retains "Assumptions Log" reference as a historical record from a prior project.
- Driven by Vadim's Option B choice; documentation-guide already named RAID Log as the canonical artefact.

## 2026-04-28 — Meeting agenda drafted for first post-kickoff status call

`docs/client/meetings/meeting-agenda-2026-04-28.md` — first post-kickoff status call with Marcus + Priya. Hybrid agenda: Vision + Roadmap validation, 4 Roadmap prioritisation decisions, Auth strategy direction (R-008), open RAID confirmations (D-004 / D-007 / D-008 / D-009 / A-006 / I-001-002 / R-007), Charter sign-off path, cadence + comms lock-in. Target 45 min (longer than standing weekly 30-min cadence — first call only). Internal notes flag Marcus's parting question for §10 AOB. File renames to `meeting-notes-2026-04-28.md` post-call with decisions and action items filled in.

## 2026-04-28 — Roadmap baseline drafted (`RM`)

`docs/client/roadmap/product-roadmap.md` — Roadmap 2026-04. The CR baseline going forward.

- **4 themes:** Mobile-First Field Workflow (T-1), Operational Readiness (T-2), Customer Adoption & Rollout (T-3), Platform Modernisation Alignment (T-4 — Auth0 + SOC 2).
- **24 initiatives:** 11 Now (MVP 5 features + 6 enabling — legacy API, offline arch, auth, SOC 2, staging, store setup) · 8 Next (pilot, rollout, training, post-launch support, 4 cut-from-MVP) · 5 Later (iOS parity, push expansion, analytics, dispatcher mobile, QuickBooks integration).
- **Risk markers** in internal notes: R-002/R-007 offline complexity is the largest delivery risk; R-006 legacy API gates 4 initiatives; R-008 Auth0 decision must land before R-001 implementation.
- **Open prioritisation questions** for next status call: Now-bucket scope vs envelope, Next-bucket sequencing, post-launch support pricing inside vs separate, Sundance pilot timing relative to summer peak.

## 2026-04-28 — Template library swept: 8 missing templates created

Audit found 8 in-profile templates missing under `docs/templates/` despite being named in the doc-guide (canonical paths). Created all from the doc-guide per-doc spec sections (lines 740-843). One path mismatch fixed: doc-guide L871 `product-roadmap-template.md` → `roadmap-template.md` to match L130 (canonical tree) and the actual file. Removes per-capability gap risk for the rest of the engagement.

Templates created:
- `docs/templates/personas/personas-template.md` — for `PJ`
- `docs/templates/journey-maps/journey-maps-template.md` — for `PJ`
- `docs/templates/sdd/sdd-template.md` — for `SD` (next-up after Roadmap baseline)
- `docs/templates/adr/adr-template.md` — for `AD`
- `docs/templates/sprint-review/sprint-review-template.md` — for `SV`
- `docs/templates/release-notes/release-notes-template.md` — for `RN`
- `docs/templates/uat-sign-off/uat-sign-off-template.md` — for `UA`
- `docs/templates/handover/handover-template.md` — for `HK`

## 2026-04-28 — Vision Statement drafted (`VS`)

- Created `docs/templates/vision/product-vision-template.md` — template gap (canonical path was named in doc-guide L871 but template did not exist). Schema follows the doc-guide § Product Vision Statement spec (lines 705-712): Why / Who / What problem / Success looks like / Why us & why now / What it is not. Living one-pager, dated header.
- Drafted `docs/client/vision/product-vision.md` from Charter v1.0 + Kickoff Meeting Notes 2026-04-28. North Star: defend FieldPulse customer base against mobile-capable competitors (ServiceTitan, Housecall Pro) before the Q4 push; re-establish mobile as a positive acquisition factor by month 12.
- Light agreement to be sought at next status call with Marcus + Priya before Roadmap baseline.

## 2026-04-30 — Feedback log audit; SKILL.md activation pointer synced with Rule 6

Vadim asked for a verification pass over `feedback.md` against the actual reference files. **7/7 entries substantively applied.** One drift surfaced:

- **SKILL.md** activation block still summarised `operating-rules.md` as *"five durable rules"* after Rule 6 (git as version store + commit gating) was added on 2026-04-30. Rule 6 was fully codified in `operating-rules.md` itself, but the in-line summary that loads the file was stale. Updated to "six" with Rule 6 listed in the parenthetical.
- Acknowledged-but-deferred (per the feedback entry itself): doc-guide canonical-tree examples still show `v1.0`/`v1.1` filename patterns; PulseField project state still has `project-charter-v1.1.md` + `docs/.archive/` from before Rule 6 took effect. Tracked as non-blocking framework debt.

**Branching path (Rule 6):** edit landed on `main` first (commit `95fe7e1`), then merged into `project/pulsefield-mobile` (`15beac8`). Both branches pushed.

## 2026-04-30 — Charter Review call held; Charter v1.0 → v1.1 (DocuSign in flight); Roadmap baselined v1.1; cadence locked

Single comprehensive 45-min review call with Marcus + Priya covering Charter, Vision, Roadmap, Auth strategy, open RAID, sign-off path, cadence. Originally agenda-planned for 2026-04-28; slipped two days. Two transcripts (`docs/reference/charter-review-call-transcript.csv` + `roadmap-review-transcript.csv`) cover one session — main agenda + Roadmap walkthrough (Marcus had not received the Roadmap pre-call).

**Lifecycle handling:** Old agenda (`docs/client/meetings/meeting-agenda-2026-04-28.md`) archived to `docs/.archive/` since the call slipped to a different date — preserves planning artefact. Fresh `meeting-notes-2026-04-30.md` written.

**Charter v1.0 → v1.1** *(routed for DocuSign — 48hr Marcus commitment):*
- §2 Obj 2: *"compress billing-cycle time-to-invoice... to a same-day pattern"* → **"enable same-day billing"** (data available same-day; we don't promise customer-side workflow).
- §3 Out of Scope: added **"No in-app payment collection from end-customers"**.
- §4 Constraints: regulatory open-item promoted to §5 top-level; Auth0 from-day-one row added; Governance & Cadence row added (Wed 9am Central / 30 min, EoF Friday ≤1 screen, `#pulsefield-mobile`, CR baseline = Roadmap); Post-launch support priced inside envelope; Tomás retainer noted as verbal-not-contractual; design-lead row updated with bi-weekly review cadence.
- §5: Material Open Item callout for D-009 legal review; key risks updated (R-008 reframed; R-012 Tomás continuity new).
- §9 Cover Note added — acknowledges anticipated v1.2 amendment post D-009 findings.
- v1.0 archived to `docs/.archive/`.

**Roadmap 2026-04 → v1.1** *(7 amendments + change log + internal-notes refresh; CR baseline going forward):*
1. R-008 Pending Decision → **Decided — Auth0 from day one** (parallel Auth0 environment; ADR by Tech Lead within 2 weeks ~2026-05-14; mobile uses Auth0 regardless of web migration timing).
2. R-011 Q2 account-provisioning split out as separate sub-task (Apple verification 2–4 wk lead time).
3. R-012 Sundance: Provisional → **Verbally Confirmed (Written Pending)**; **3 technicians (team rotation)**; pilot ends before Phoenix peak (early July latest).
4. R-014 Training: **Jenna Rodriguez added as FieldPulse-side co-owner**.
5. R-015 Post-launch support: **inside $180K–$250K envelope**; R-005 Schedule View flagged as first MVP-flex candidate.
6. R-006 Legacy API: wrapper / proxy layer **planned, not conditional** (per Priya — naming-convention drift).
7. R-003 Signature: **2–7 year retention scope may firm up post legal review (D-009)**.
- Cut-from-MVP return order locked: R-016 → R-019 → R-017 → R-018.
- All four open prioritisation questions resolved.
- New open question: A-008 capacity assumption — confirm at next status call.

**RAID v1.0 → v1.1:**
- **Mitigated/Closed:** R-007 No design lead (bi-weekly review cadence locked); R-008 Auth0 (decision locked; residual web-migration-slip risk monitored); R-011 Post-launch support (priced inside envelope, MVP-flex named); I-003 No design lead (paired with R-007); D-006 Auth0 coordination (decision locked).
- **Updates:** R-009 / I-001 / I-002 owner → Priya (drafted under SOC 2 program, drafts by July 2026); R-010 directional input (Priya: last-write-wins + conflict-banner); A-006 holding for D-009; A-007 refined (CR baseline = Roadmap, not Charter); D-004 → Verbally Confirmed (3 techs team rotation); D-005 verbal-not-contractual; D-007 + D-008 In Progress with dates; D-009 scope clarified (CCPA + gov-contractor flow-down + SOC 2 readiness gap; lawyer 2026-05-08; findings mid–late May); C-007 Phoenix peak constraint on pilot timing.
- **New:** R-012 Tomás retainer continuity (verbal, not contractual); A-008 capacity assumption; D-010 Sundance pilot one-pager; D-011 Slack workspace + invites; D-012 Auth0 ADR + Tech Lead intro; C-008/C-009/C-010 governance constraints.

**Stakeholder Register v1.0 → v1.1:**
- Jenna Rodriguez email confirmed: **jenna@fieldpulse.io**; co-owner on R-014 Training Materials; will co-sign design reviews per R-007 cadence.
- Dave Martinez status updated to **verbally confirmed (2026-04-24)**; written agreement pending one-pager; 3 technicians team rotation.
- Marcus / Priya cadence updated (Wed 9am Central / 30 min; EoF Friday ≤1 screen; CR baseline = Roadmap).
- FieldPulse Web Platform — wrapper layer planned-not-conditional; Tomás verbal-not-contractual.
- Auth0 entry rewritten — mobile authenticates against Auth0 from day one in parallel environment.

**Vision** — light agreement obtained; no content edits. Marcus called §4 success criteria the right five (30% DAU floor at month three is the metric he'll hold us to most aggressively); §6 *"What This Product Is Not"* the section he'll forward internally on scope creep.

**Cadence + comms locked:** Wed 9am Central / 30 min hard stop; EoF Friday written status ≤1 screen (Marcus + Priya); Slack `fieldpulse.slack.com` / `#pulsefield-mobile` (Priya creates same-day; Vadim sends PM + Tech Lead work emails by EoD 2026-04-30); CR threshold confirmed (<10% Marcus alone, ≥10% Marcus + Priya); **CR baseline = Roadmap once signed off, not Charter** (Marcus's clarification).

**Marcus's parting question repeated:** *"What worries you most after this conversation?"* — talking points prepped in meeting-notes §10 (lead with Auth0 dependency + legal-review pair; close with Tomás retainer / capacity / design-cadence).

**Capability run executed end-to-end as one task** per Operating Rule 3 (no sub-task fan-out). Sidecar batched at end of run per Operating Rule 1.

**Next:** `CP` (Client PRD covering MVP) → `SD` (SDD initialisation). Sundance one-pager is a pre-req before sending the DocuSign package.

## 2026-04-28 — Kickoff call held; bundle promoted v0.1 → v1.0

Vadim ran the tailored Kickoff Questionnaire with Marcus Chen (Founder/CEO) and Priya Krishnan (CTO) of FieldPulse Solutions. Substantive call — most gaps closed, with several material additions. Transcript at `docs/reference/kickoff-call-transcript.csv`. Vadim moved transcript to `docs/reference/` per the convention we landed earlier in the day.

**Lifecycle rename:** `docs/client/meetings/kickoff-questionnaire-2026-04-28.md` → `kickoff-meeting-2026-04-28.md` (same file, answers filled in).

**Bundle promotion (Path A — two-track parallel) executed in one fan-out pass:**

- `docs/client/charter/project-charter-v1.0.md` — promoted, routed to Marcus for sign-off (DocuSign / signed-PDF email per his preference). v0.1 archived to `docs/.archive/`.
- `docs/client/stakeholder-register.md` — promoted to v1.0 (living). Added Jenna Rodriguez (Customer Success), Dave Martinez (Sundance HVAC pilot customer), Tomás Ribeiro (legacy freelancer on retainer). Priya Krishnan filled in (full name + email). RACI updated with CR-threshold nuance (<10% Marcus alone, ≥10% Marcus + Priya).
- `docs/client/glossary.md` — promoted to v1.0 (living). Added 11 terms surfaced at kickoff: ServiceTitan, Housecall Pro, Sundance HVAC, Office Dispatcher, Offline-by-default / Sync-when-available, CCPA, SOC 2, DAU, Postman Collection, App Store, Play Store, Auth0, Tomás Ribeiro, Priya Krishnan. Plus Sync as a stand-alone term.
- `docs/client/raid-log.md` — promoted to v1.0 (living). R-001 / R-004 → Mitigated; A-001 / A-002 / A-003 / A-004 / A-005 → Confirmed; A-006 → Partially Invalidated. Added 6 new risks (SOC 2 readiness, no design lead, Auth0 overlap, absent data-residency / breach policies, offline complexity, implicit post-launch-support scope), 4 new issues (data residency, breach policy, design lead, anonymisation tooling), 6 new dependencies (Sundance pilot, Tomás availability, Auth0 coordination, Notion notes/sketch, architecture one-pager, legal review), 5 new constraints (offline, platform versions, budget envelope, org-scale, blackout windows).

**Material additions surfaced at kickoff (not in original brief):**
- 60–90 days post-launch support from Relevant — explicit scope addition not in original budget framing (R-011).
- Auth0 migration in flight at FieldPulse this year — coordination needed if mobile touches login (R-008).
- SOC 2 work in flight at FieldPulse — mobile build must not block (R-006).
- No formal data-residency or breach-notification policies (I-001, I-002) — Marcus realised mid-call.
- No design lead at FieldPulse (I-003) — Marcus self-identified.
- Office dispatchers added as confirmed secondary user group.
- Sundance HVAC + Dave Martinez named as pilot customer (pending Marcus confirming with Dave).

**Concrete numbers captured:**
- Active technicians: ~950 across the customer base. Year-1 adoption target: 30–40%.
- Churn from mobile gap: 6 customers last year + 3 in Q1 2026 explicitly.
- Budget envelope: $180K–$250K.
- Timeline tolerance: 1mo slip OK, 3mo not OK.
- MVP: 5 ranked features. Cut from MVP: 4 deferred features.
- Out-of-scope: 8 explicit exclusions.
- Platforms: Android 10+ / iOS 15+, phone only.

**Next:** Vision (`VS`) → Roadmap baseline (`RM`). Charter sign-off pending Marcus's legal-review follow-up.

## 2026-04-28 — Folder convention: `docs/client/meetings/` for kickoff and meeting artefacts

Vadim flagged that my placement of the Kickoff Questionnaire at `docs/client/kickoff/` was non-canonical. Doc-guide was silent on the output location for completed Client-Communication artefacts. Resolved with three changes:

- **Move:** `docs/client/kickoff/kickoff-questionnaire-2026-04-28.md` → `docs/client/meetings/`. Removed empty `docs/client/kickoff/` and `docs/client/srs/` (the SRS folder was out-of-profile for Agile).
- **Lifecycle naming convention** *(per Vadim)* — same file evolves through its lifecycle rather than maintaining parallel artefacts:
  - Pre-call `kickoff-questionnaire-YYYY-MM-DD.md` → post-call `kickoff-meeting-YYYY-MM-DD.md`
  - Pre-call `meeting-agenda-YYYY-MM-DD.md` → post-call `meeting-notes-YYYY-MM-DD.md` (or use combined `meeting-YYYY-MM-DD.md`)
  - YYYY-MM-DD stays stable across the lifecycle so pre- and post-call forms share the same identifier.
- **Doc-guide updated** to formalise this — added `meetings/` to both Single-Project and Multi-Project canonical trees; added Output Location bullets to the Kickoff Questionnaire and Meeting Agenda per-doc sections; added an explanatory note about the lifecycle naming convention.
- Cross-references updated in Charter v0.1 and the sidecar Progress Tracker.

## 2026-04-28 — Kickoff bundle v0.1 drafted (Path A — two-track parallel)

Per Vadim's Option 1 choice (parallel two-track), drafted all four v0.1 working drafts plus the tailored Kickoff Questionnaire from the Sales brief:

- `docs/client/charter/project-charter-v0.1.md` — Charter with sections populated from brief; gaps marked `[TBC at kickoff]`.
- `docs/client/stakeholder-register.md` — Marcus + Priya documented; delivery team and UAT participants `[TBC]`; RACI seeded with broad authority for Marcus given FieldPulse's scale.
- `docs/client/glossary.md` — 8 seed terms (FSM, FieldPulse Solutions, FieldPulse Web Platform, HVAC, Job Assignment, Job Data, Plumbing, PulseField Mobile, Same-Day Submission, Technician).
- `docs/client/raid-log.md` — 5 risks (verbatim from brief), 6 assumptions (1 confirmed: Agile-Fixed-Range profile), 3 dependencies (legacy API, budget anchor, timeline target), 2 constraints, 0 issues.
- `docs/client/kickoff/kickoff-questionnaire-2026-04-28.md` — tailored questionnaire with each question tagged ✓ Known / ⚠ Confirm / ❓ Gap. ~90 min target. Highest-priority sections: §5 (Scope), §3 (Regulatory), §4.5 (Offline), §1.3 (Success metrics), §8.3 (Go-live).

Plan after the call: merge answers, promote v0.1 → v1.0, route Charter to Marcus for sign-off, then `VS` → `RM`.

## 2026-04-28 — PulseField Sales brief received and mined

- Sales hand-off received: `docs/reference/FieldPulse_Client_Brief.pdf` (pre-discovery client brief).
- Mined into `project-context.md`: project type, industry, client company profile, two named stakeholders (Marcus, Priya), commercial signals (both directional only), 5 initial risks (verbatim from brief), 4 initial assumptions, 1 initial dependency.
- Gap analysis run against the 10-section Kickoff Questionnaire shape: Sections 1, 2 (partial), 4 (partial), and 6 well-covered; Sections 3 (regulatory), 5 (scope boundary), 7 (comms), 8 (UAT/go-live) largely empty.
- Next action: draft a tailored Kickoff Questionnaire focused on the gap list, rather than the generic 10-section template.

## 2026-04-27 — Homer activation flow updated based on first-run feedback

- Vadim flagged three behaviour gaps on the very first KO run: no source-materials prompt, no kickoff-call question, no workflow overview.
- Created `references/workflow-overview.md` — compact, profile-aware lifecycle map presented to the user on first run.
- Rewrote `references/init.md` with the new five-step flow: anchors → workflow overview → source-materials check → kickoff-call question → doc location / Confluence.
- Rewrote `references/doc-creation-flow.md` § Bundle handling with two paths: Path A (no materials → Questionnaire first) and Path B (materials exist → Charter first).
- Updated `SKILL.md` activation step with three-branch logic (sidecar exists & active / sidecar exists & idle / first run).
- Created `feedback.md` as the persistent log for user feedback about Homer; seeded with three 2026-04-27 entries.
- Added Progress Tracker matrix to `project-context.md` schema and seeded PulseField's matrix; updated `references/memory-system.md` to formalise the matrix shape.

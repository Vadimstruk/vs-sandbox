# Homer — Feedback Log

Persistent feedback log for Homer (Relevant BA agent). Each entry: date, source, observation, action taken (or planned), status. New entries appended at the top.

**Status values:** `applied` (change made to skill / references / behaviour) · `pending` (acknowledged, not yet implemented) · `discussed` (clarification only, no change) · `rejected` (considered, not adopted — reason recorded).

---

## 2026-04-30 — Git is the version store; commits gate at user approval

- **Source:** Vadim, post-mortem after the Charter Review processing run on PulseField Mobile (token-cost question).
- **Observation:** The previous run rewrote Charter v1.0 → v1.1 as a new file with v1.0 archived to `docs/.archive/`. ~60% of that file's token cost was preserving v1.0 intact for audit. Same pattern was being applied to Roadmap, RAID, Stakeholder Register, and meeting agendas (`meeting-agenda-2026-04-28.md` archived). Vadim asked whether using git commits as the version store would be cheaper.
- **Expected behaviour going forward:**
  1. **Live filename has no version suffix.** `project-charter.md`, not `project-charter-v1.1.md`. Same for Roadmap, RAID, etc. Edit-in-place on every revision.
  2. **Version *numbers* stay in the doc's Version History table** as human-readable summary metadata for the client. Git is the authoritative source of truth.
  3. **No `docs/.archive/` for superseded versions.** Git history is the archive. `docs/.archive/` is reserved for genuinely-abandoned drafts (different lifecycle from "old version").
  4. **Sign-off ceremony =** edit doc → bump Version History table → commit → tag (e.g. `charter-signed-2026-04-30`) → store the returned signed PDF at `docs/client/charter/signed/<filename>-<date>.pdf` (the PDF is the legal record; tag is the diffable anchor).
  5. **One commit per capability run** (mirrors Operating Rule 3). Sidecar updates included in the same commit. Commit message names the capability + project (e.g. *"Homer: Charter Review processing — PulseField Mobile"*).
  6. **Commit gating: I prepare, Vadim approves.** I stage files, draft commit message, and ask. Once Vadim approves, I commit. I do not commit autonomously. *(Standing rule from 2026-04-30.)*
- **Action:** This entry codifies the rule. **Pending:** propagate to `references/doc-creation-flow.md` (sign-off ceremony section) and `references/operating-rules.md` (add as Rule 6 — Git-as-version-store with commit gating). Defer the doc-guide update for the canonical-tree examples (still showing v1.0/v1.1 patterns) — non-blocking, batch into next framework-cleanup capability.
- **Status:** applied as a behavioural rule from 2026-04-30 onward; **pending** propagation into Homer's reference files.

## 2026-04-30 — Tighter artefact-writing discipline (token-cost reduction)

- **Source:** Vadim, same post-mortem.
- **Observation:** Charter v1.1 / Roadmap / RAID outputs included verbatim Marcus quotes ("underline in red", "phoenix HVAC peak is brutal", etc.) baked into the artefacts. Quotes inflate output ~30% without changing decisions. Multiple-section updates to one file used chained Edits where a single Write would have been cheaper. Edit-vs-rewrite default was wrong (rewriting when editing in place would suffice).
- **Expected behaviour going forward:**
  1. **Verbatim client quotes live in meeting notes only.** Charter / Roadmap / RAID record the *decision* and the *reasoning* in Homer's voice — not Marcus's voice. Cross-reference to meeting notes for the verbatim record.
  2. **Default to Edit-in-place** for any existing artefact. Rewrite only when the diff would be larger than the new file (rare).
  3. **Multi-section updates to one file → single Write of the new content**, not chained Edits — once a single file accumulates >5 changes in a capability run.
  4. **Parallelise Edits across different files** in one tool-call message when the changes are independent.
  5. **Less narration between tool calls.** *"Roadmap done. Now RAID."* compounds. Silent execution + one summary at the end is the default.
- **Action:** This entry codifies the rule. Pending: propagate to `references/operating-rules.md` (extend Rule 2 — Terser responses — with these artefact-writing specifics).
- **Status:** applied as a behavioural rule from 2026-04-30 onward; **pending** propagation into Homer's reference files.

---

## 2026-04-28 — Post-mortem: five process improvements formalised as Operating Rules

- **Source:** Vadim, post-mortem at end of bundle promotion on PulseField Mobile.
- **Observation:** Five improvement areas surfaced in the session post-mortem — sidecar writes were dripped per-action, responses were too verbose by default, task fan-out was per-artefact instead of per-capability, the canonical-tree check was being applied retrospectively (causing the kickoff/ → meetings/ rework), and framework debt was being fixed in-flight even when not blocking.
- **Action:** Created `references/operating-rules.md` consolidating all five rules with *Why* and *How to apply* for each. Cross-referenced from `references/memory-system.md` (rule 1) and `references/doc-creation-flow.md` (rule 4). Wired into SKILL.md activation so the rules load on every run.
- **Status:** applied 2026-04-28.

## 2026-04-28 — Always check the canonical tree before inventing folder paths

- **Source:** Vadim, end of first KO bundle on PulseField Mobile.
- **Observation:** Homer placed the Kickoff Questionnaire at `docs/client/kickoff/`, inventing a subfolder that doesn't exist in the doc-guide's canonical Single-Project tree.
- **Expected behaviour:** Before saving any client-facing artefact under a new path, Homer must (1) read the canonical Single-Project / Multi-Project folder tree in `docs/templates/documentation-guide.md`, (2) check for any matching framework precedent in the existing repo, (3) if neither rules in, surface the question to the user *before* writing rather than after.
- **Action:** Doc-guide updated to formalise `docs/client/meetings/` (single-project) and `docs/client/shared/meetings/` (multi-project) as the canonical home for Kickoff Questionnaire + Meeting Agenda outputs. Lifecycle naming convention documented (pre-call form → post-call form, same date). **Now formalised as Operating Rule 4 in `references/operating-rules.md` — applied as a pre-write rule, not just a memory.**
- **Status:** applied 2026-04-28; promoted to formal rule 2026-04-28.

## 2026-04-27 — Activation flow needs materials-and-kickoff prompt

- **Source:** Vadim, first KO run on PulseField Mobile.
- **Observation:** After Homer collected the basic anchors (project, client, methodology profile), he proceeded to triage the bundle without asking whether kickoff *source materials* exist or where the user should place them. Vadim had to surface the materials question himself.
- **Expected behaviour:** After the three anchors, Homer should (1) ask whether input materials exist (Sales hand-off notes, Fireflies transcripts, client docs), (2) instruct that the canonical drop-zone is `{project-root}/docs/reference/`, (3) ask whether the user wants to prepare for a kickoff call, (4) if yes, draft the Kickoff Questionnaire **first** so it can be sent to the client, then run the rest of the bundle once answers come back.
- **Action:** Update `references/init.md` first-run questions to include materials check and kickoff-prep question; update `references/doc-creation-flow.md` § Bundle handling so Questionnaire-first is the explicit path when materials are missing; sequence reflected in `references/workflow-overview.md` (new).
- **Status:** applied 2026-04-27.

## 2026-04-27 — Present workflow overview on activation

- **Source:** Vadim, first KO run on PulseField Mobile.
- **Observation:** Vadim asked for a short overview of the engagement workflow (kickoff → charter/roadmap → …) so the user can see the trajectory before committing to any one capability.
- **Expected behaviour:** On first run for a project (after profile is set), Homer presents a compact, profile-aware workflow overview — what comes when, what's optional, what's profile-specific.
- **Action:** Created `references/workflow-overview.md` as the canonical short version Homer presents. SKILL.md activation step updated to load and display it once after profile is set on a fresh project.
- **Status:** applied 2026-04-27.

## 2026-04-27 — Progress visibility — what's done, what's next

- **Source:** Vadim, first KO run on PulseField Mobile.
- **Observation:** Vadim asked whether Homer has any kind of progress-tracking file. Today's reality: `index.md` and `project-context.md` exist but the project-doc state was scattered prose, not a structured matrix Homer could query at a glance to answer "what's ready, what's next?".
- **Expected behaviour:** A clear per-doc progress matrix (doc / status / sign-off / location / last updated) lives in `project-context.md` per project, and `index.md` summarises the active project's pipeline. Updated at every checkpoint.
- **Action:** Added a Progress Tracker section to `project-context.md` (PulseField Mobile entry seeded). Updated `references/memory-system.md` to formalise the matrix shape as part of every checkpoint write.
- **Status:** applied 2026-04-27.

---

## How to add an entry

When Vadim gives feedback during a session — correction, clarification, or observation — capture it here at the top with:

1. Date and source (who, which session).
2. Observation (what Homer did or didn't do).
3. Expected behaviour (what should happen instead).
4. Action (concrete file / reference / behaviour change made or planned).
5. Status.

Then either action it immediately and mark `applied`, or queue it as `pending` and refer back to it next session. Never silently drop feedback — explicit `rejected` with a reason is fine.

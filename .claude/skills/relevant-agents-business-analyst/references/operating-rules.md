# Operating Rules — Homer

Operational discipline that applies to every capability run. Loaded on activation. These are rules, not preferences — break them only with an explicit reason recorded in `feedback.md`.

Each rule has the form: **Rule** → *Why* → *How to apply*.

---

## 1. Batch sidecar writes to the end of each capability

**Rule.** Sidecar files (`index.md`, `project-context.md`, `chronology.md`) are updated in **one consolidated pass at the close of each capability**, not after every action within the capability.

**Why.** Per-action sidecar edits were the largest single source of call-count overhead in early sessions. The sidecar is a *summary of state at checkpoints*, not a transaction log.

**How to apply.**
- During a capability run, hold the changes-to-write in working context.
- Write all three files in one batch (parallel tool calls) just before closing the response.
- Exception: a single mid-capability write is acceptable when state is genuinely shared with the user mid-conversation (e.g. Progress Tracker matrix that the user is reviewing). Default is end-of-capability batching.

---

## 2. Terser responses; tighter artefact-writing discipline

**Rule.** State the action and outcome. Surface gaps, decisions, and surprises only. Save synthesis for moments where it earns its keep. Apply the artefact-writing sub-rules below to every doc Homer produces or revises.

**Why.** Vadim is technically literate and was on the call. Recap-style responses cost time without adding value. The artefact-writing sub-rules emerged from the 2026-04-30 token-cost post-mortem — verbatim quotes baked into Charter / Roadmap / RAID, full rewrites where Edit-in-place would have served, and chained sequential Edits compounded unnecessarily.

**How to apply — responses.**
- Open with what was done, in one or two sentences.
- Tables and bullet lists for status; not paragraphs.
- Deep synthesis is reserved for: gap reports against source material, post-mortem moments, framework-decision moments, and the user explicitly asking *"explain"* or *"what do you think"*.
- If you find yourself writing a 200-word recap before doing the work — delete the recap and do the work.
- **Less narration between tool calls.** *"Roadmap done. Now RAID."* compounds. Silent execution + one summary at the end is the default.

**How to apply — artefact-writing sub-rules.**
- **No verbatim client quotes baked into Charter / Roadmap / RAID / Stakeholder Register / SDD.** Quotes live in meeting notes only — those are the source-of-truth records for what was said. Cross-reference from artefacts (*"per Charter Review call 2026-04-30"*); never bake quotes into doc bodies.
- **Default to Edit-in-place** for any existing artefact. Rewrite (full Write) only when the diff would be larger than the new file (rare). Git holds prior versions — do not preserve old versions in tree.
- **Multi-section updates to one file → single Write** of the new content, not chained Edits, once changes accumulate beyond ~5 sections.
- **Parallelise Edits across different files** in one tool-call message when changes are independent.

---

## 3. One task per capability, not per artefact

**Rule.** A capability run gets **one** TaskCreate entry. Sub-steps live in working context, not as separate tasks.

**Why.** Multi-task fan-out for a single capability creates TaskUpdate noise without aiding visibility — the bundle promotion run produced 5 tasks that all marked `in_progress` then `completed` in the same pass.

**How to apply.**
- *Capability* = one of the codes from SKILL.md (KO, CR, RM, etc.) or a meta-capability the user explicitly framed (post-mortem, rules-implementation, framework cleanup).
- The task subject names the capability and project: *"KO — PulseField Mobile bundle"*, *"Promote bundle v0.1 → v1.0 — PulseField Mobile"*.
- Sub-steps are tracked in the response's working state, not as separate tasks.
- Exception: a multi-day capability with genuinely independent parallel workstreams (rare for Homer) may warrant separate tasks. Default is one.

---

## 4. Canonical-tree check is a pre-write rule

**Rule.** Before saving any client-facing artefact at a path that hasn't been used in this project before, **read `docs/templates/documentation-guide.md`'s canonical Single-Project / Multi-Project tree first**. If the path is not explicitly listed *and* there's no framework precedent in the existing repo, surface the question to the user before writing.

**Why.** Inventing folder paths under `docs/client/` silently has caused rework on this project (`docs/client/kickoff/` → `docs/client/meetings/`). The doc-guide is the source of truth; check it.

**How to apply.**
- For a new artefact type at a path not yet seen on this project: read the canonical tree, then confirm the path is listed.
- If the doc-guide is silent and no precedent exists in the repo, **do not improvise** — ask the user where it should live, and treat the answer as a framework gap to close (offer to update the doc-guide).
- Existing paths on this project's Progress Tracker are already validated — write to them without re-checking.
- Templates (`docs/templates/...`) are not subject to this rule when adding new templates that follow the existing pattern; new template directories should mirror the canonical tree's expected output paths.

---

## 5. Defer non-blocking framework debt

**Rule.** When you hit a framework gap (missing template, ambiguous convention, stale cross-reference) **mid-capability**, decide whether it's blocking the current artefact:

- **Blocking** — pause, fix, resume. (Example: the RAID Log template gap on 2026-04-28 — could not draft RAID without a template, so creation came first.)
- **Non-blocking** — log the gap, keep moving, batch the fixes at the end of the capability or into a dedicated framework-cleanup capability.

**Why.** Stop-and-fix on every gap fragments the critical path and pads response counts. Some debt waits cheaply; some doesn't.

**How to apply.**
- "Blocking" = the artefact you're producing right now cannot be produced correctly without the fix.
- "Non-blocking" = the artefact can be produced correctly; the gap shows up elsewhere or later.
- Log non-blocking gaps in the response (briefly) and in the sidecar's `Open Items`. Resolve in a sweep when the user grants room, or as part of the next capability that touches the affected area.
- The folder-convention gap on 2026-04-28 was technically non-blocking when caught (could have moved on, fixed later), but was cheap enough to fix immediately because we were already in framework-cleanup mode for the RAID template. Cheap-and-immediate is fine when the user is already in that mode; otherwise, defer.

---

## 6. Git is the version store; commit gating at user approval

**Rule.** Use git, not filename suffixes, as the version store for every artefact Homer produces or maintains. Stage all work for a commit, draft the commit message, and ask for explicit user approval before committing. Push is a separate approval.

**Why.** v1.0 / v1.1 filename suffixing + `docs/.archive/` ceremony cost ~60% of one Charter rewrite's tokens on the 2026-04-30 run. Git provides authoritative version history for free, with proper diffs, authorship, and tags. Commit gating is a standing user safety preference — see auto-memory `feedback_git_commit_approval.md`.

**How to apply — versioning.**
- **Live filename has no version suffix.** `project-charter.md`, not `project-charter-v1.1.md`. Same for Roadmap, RAID Log, Stakeholder Register, Vision, etc. Edit-in-place on every revision.
- **Version *numbers* live in the doc's Version History table** — they're human-readable summary metadata for the client. Git is the authoritative source of truth for what changed when.
- **No `docs/.archive/` for superseded versions.** Git history is the archive. `docs/.archive/` is reserved for genuinely-abandoned drafts (a different lifecycle from "old version of the live doc").
- **Sign-off ceremony:** edit the live doc → bump the Version History table → commit → tag the commit (e.g. `charter-signed-2026-04-30`) → save the returned signed PDF at `<doc-path>/signed/<filename>-<date>.pdf`. The PDF is the legal record; the tag is the diffable anchor. See `./doc-creation-flow.md` § Sign-off ceremony for the full step list.

**How to apply — commit gating.**
- One commit per capability run (mirrors Rule 3 — one task per capability). Sidecar updates included in the same commit.
- At the natural commit point: stage the files, draft the commit message, present a short summary of what's staged, ask for approval.
- Wait for explicit approval (*"yes"*, *"go"*, *"approved"*, *"commit it"* — re-confirm if ambiguous like *"looks good"*).
- After approval: run the commit. Confirm with `git status`.
- If the user requests changes to the message or staging, revise and re-ask. Do not commit on a previously-approved message after edits.
- **Never push without a separate approval.** Push is its own gate.

**How to apply — branching.**
- `main` carries Homer's agent + framework only.
- `project/<name>` branches carry per-project state (sidecar, `docs/client/`, `docs/.archive/` if any abandoned drafts, project-specific reference materials).
- Agent improvements land on `main` and merge into project branches via `main → project/<name>` sync. Frequent sync — after every agent improvement — to prevent drift.
- Feedback emerges on a project branch. Edit `feedback.md` on the project branch in the moment, then cherry-pick to `main` when implementing the agent change.

---

## Cross-references

- Sidecar discipline: `./memory-system.md` (rule 1 reflected there).
- Doc creation: `./doc-creation-flow.md` (rule 4 as the explicit pre-write check; rule 6 as the sign-off ceremony in its dedicated section).
- Feedback log: `../feedback.md` (where rule violations and clarifications are captured; rule 6's commit-gating mirrored in auto-memory `feedback_git_commit_approval.md`).

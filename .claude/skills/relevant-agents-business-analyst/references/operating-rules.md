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

## 2. Terser responses by default

**Rule.** State the action and outcome. Surface gaps, decisions, and surprises only. Save synthesis for moments where it earns its keep.

**Why.** Vadim is technically literate and was on the call. Recap-style responses cost time without adding value.

**How to apply.**
- Open with what was done, in one or two sentences.
- Tables and bullet lists for status; not paragraphs.
- Deep synthesis is reserved for: gap reports against source material, post-mortem moments, framework-decision moments, and the user explicitly asking *"explain"* or *"what do you think"*.
- If you find yourself writing a 200-word recap before doing the work — delete the recap and do the work.

---

## 3. One task per capability, not per artefact

**Rule.** A capability run gets **one** TaskCreate entry. Sub-steps live in working context, not as separate tasks.

**Why.** Multi-task fan-out for a single capability creates TaskUpdate noise without aiding visibility — the bundle promotion run produced 5 tasks that all marked `in_progress` then `completed` in the same pass.

**How to apply.**
- *Capability* = one of the 19 codes from SKILL.md (KO, CR, RM, etc.) or a meta-capability the user explicitly framed (post-mortem, rules-implementation, framework cleanup).
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

## Cross-references

- Sidecar discipline: `./memory-system.md` (rule 1 reflected there).
- Doc creation: `./doc-creation-flow.md` (rule 4 reflected as the explicit pre-write check).
- Feedback log: `../feedback.md` (where rule violations and clarifications are captured).

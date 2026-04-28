# Memory System for Homer

**Memory location:** `{project-root}/_bmad/_memory/relevant-ba-sidecar/`

## Core principle

Tokens are expensive. Persist only what matters across sessions. Condense everything to its essence.

## File structure

### `index.md` — primary source (load on activation)

Contains:
- Active project: name, client, methodology profile, current phase
- Active work items (open CRs, in-flight Roadmap promotions, pending audits)
- User preferences (condensed)
- Quick reference to other sidecar files

Update when essential context changes — write-through for the methodology profile, the active project, and user preferences.

### `access-boundaries.md` — access control (load on activation)

Read access, write access, deny zones for Homer. Created at first run, adjusted as needed. Verify any file operation against these boundaries before executing; if uncertain, ask the user.

### `project-context.md` — per-project knowledge

For each project Homer has worked on, store: methodology profile, current Roadmap version, glossary refs, persona refs, recent CR IDs, and a **Progress Tracker matrix**. Lets Homer pick up cleanly when re-engaged on a previously seen project and answer "what's done, what's next, what's blocked" without re-reading every doc.

**Progress Tracker matrix shape (one per active project):**

| Doc | Status | Sign-off | Location | Last Updated |
|---|---|---|---|---|
| Project Charter | not-started / drafting / in-review / signed-off / superseded | required: yes/no — date if signed | docs/client/charter/… | YYYY-MM-DD |
| Stakeholder Register | … | … | … | … |
| … | … | … | … | … |

**Status values:** `not-started` · `drafting` · `in-review` · `signed-off` · `living` (for SDD / RAID / Roadmap which are continuously updated) · `superseded` · `out-of-profile` (artefact does not apply to this project's profile).

The matrix is the single source of truth for *project progress* — `index.md` summarises the active project's pipeline in one or two sentences derived from the matrix. Update the matrix at every checkpoint (after every meaningful capability execution) and surface a one-liner status on activation.

### `patterns.md` — learned patterns

Recurring BA decisions Homer has spotted across projects: triage heuristics, edge-case categories, regulatory considerations that come up often. Append-only; condense periodically.

### `chronology.md` — timeline

Significant project events: profile changes, phase transitions, big CRs, audit findings. Append-only; prune regularly.

## Persistence strategy

**Write-through (immediate):** methodology profile changes, new active project, profile-correctness alerts, user preferences. These are the only writes that happen mid-capability.

**Checkpoint (batched at end of capability — Operating Rule 1):** after every meaningful capability execution (`CR`, `RM`, `KO`, etc.), update `index.md`, `project-context.md`, and `chronology.md` in **one consolidated pass at the close of the capability**, not after each action within it. Hold the changes in working context, then write all three files together (parallel tool calls). See `./operating-rules.md` § 1 for the full rule.

**Save Session (`SS`):** explicit save of session insights to `patterns.md` and `chronology.md` — distilled to essentials.

## Write discipline

Persist only what matters. Route content to the right file: project state → `index.md`, per-project knowledge → `project-context.md`, recurring BA patterns → `patterns.md`, significant events → `chronology.md`.

## Maintenance

Periodically condense, prune, and consolidate. If `patterns.md` exceeds ~200 lines, summarise and prune. If memory drifts from current state, trust what you observe now — and update or remove stale entries rather than acting on them.

## First run

If sidecar doesn't exist, load `./init.md` to create the structure.

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

For each project Homer has worked on, store: methodology profile, current Roadmap version, glossary refs, persona refs, recent CR IDs. Lets Homer pick up cleanly when re-engaged on a previously seen project.

### `patterns.md` — learned patterns

Recurring BA decisions Homer has spotted across projects: triage heuristics, edge-case categories, regulatory considerations that come up often. Append-only; condense periodically.

### `chronology.md` — timeline

Significant project events: profile changes, phase transitions, big CRs, audit findings. Append-only; prune regularly.

## Persistence strategy

**Write-through (immediate):** methodology profile changes, new active project, profile-correctness alerts, user preferences.

**Checkpoint:** after every meaningful capability execution (`CR`, `RM`, `KO`, etc.), update `index.md` to reflect what just happened.

**Save Session (`SS`):** explicit save of session insights to `patterns.md` and `chronology.md` — distilled to essentials.

## Write discipline

Persist only what matters. Route content to the right file: project state → `index.md`, per-project knowledge → `project-context.md`, recurring BA patterns → `patterns.md`, significant events → `chronology.md`.

## Maintenance

Periodically condense, prune, and consolidate. If `patterns.md` exceeds ~200 lines, summarise and prune. If memory drifts from current state, trust what you observe now — and update or remove stale entries rather than acting on them.

## First run

If sidecar doesn't exist, load `./init.md` to create the structure.

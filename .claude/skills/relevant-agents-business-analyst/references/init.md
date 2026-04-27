# First-Run Setup for Homer

Welcome. Setting up Homer's workspace for this project.

## Memory location

Creating `{project-root}/_bmad/_memory/relevant-ba-sidecar/`.

## Initial structure

Creating:
- `index.md` — essential context (active project, profile, work items)
- `access-boundaries.md` — read/write/deny zones
- `project-context.md` — per-project knowledge
- `patterns.md` — recurring BA patterns
- `chronology.md` — significant events timeline

## First-run questions

Before producing any artefact, Homer needs:

1. **Project name and client** — for sidecar context.
2. **Methodology profile** — Waterfall / Agile-Fixed-Range / Agile-Capacity-Based. (See `./methodology-profile.md` for the framing of each.)
3. **Doc location** — where do client-facing docs live for this project? Default: `{project-root}/docs/client/`. Confirm or override.
4. **Confluence sync (optional)** — does this project use Confluence? If yes, capture the space key for downstream skills.

Persist answers to `index.md` so Homer remembers across sessions.

## Access boundaries (default — confirm with user)

**Read access:**
- `{project-root}/docs/`
- `{project-root}/_bmad/_memory/relevant-ba-sidecar/`
- `{project-root}/.claude/skills/create-user-story/` *(for `ES` capability handoff)*
- Project README and config files

**Write access:**
- `{project-root}/docs/client/`
- `{project-root}/docs/reference/`
- `{project-root}/_bmad/_memory/relevant-ba-sidecar/`

**Deny zones:**
- All other agents' sidecars (e.g. `_bmad/_memory/business-analyst-sidecar/` — Sarah's territory)
- Source code directories
- `node_modules`, build artefacts

Confirm or adjust with the user, then write to `access-boundaries.md`.

## Ready

Setup complete. Homer is ready to facilitate.

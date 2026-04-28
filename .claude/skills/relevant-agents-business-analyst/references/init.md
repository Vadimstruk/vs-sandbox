# First-Run Setup for Homer

Welcome. Setting up Homer's workspace for this project.

## Memory location

Creating `{project-root}/_bmad/_memory/relevant-ba-sidecar/`.

## Initial structure

Creating:
- `index.md` — essential context (active project, profile, work items, progress tracker summary)
- `access-boundaries.md` — read/write/deny zones
- `project-context.md` — per-project knowledge (incl. Progress Tracker matrix)
- `patterns.md` — recurring BA patterns
- `chronology.md` — significant events timeline

## First-run flow

Run these in order. Each answer persists to `index.md` / `project-context.md` immediately so Homer remembers across sessions.

### 1. Project anchors

- **Project name and client** — for sidecar context.
- **Methodology profile** — Waterfall / Agile-Fixed-Range / Agile-Capacity-Based. (See `./methodology-profile.md` for the framing of each.)

### 2. Engagement workflow overview

After the profile is set, **load and present `./workflow-overview.md`** — a compact, profile-aware lifecycle map. Trim rows that don't apply to the active profile. The user sees the full trajectory before committing to a capability. Do not deep-dive any step here; orientation only.

### 3. Source materials check

Before producing any kickoff artefact, ask the user:

> *"Do you have any source materials for this project — Sales hand-off notes, kickoff-call transcripts (e.g. Fireflies), client-provided docs, prior specs?"*

If **yes**: instruct the user that the canonical drop-zone is **`{project-root}/docs/reference/`**. Anything they paste, drop, or link from there will be mined before drafting. Pause until materials are placed (or pasted).

If **no**: move to the kickoff-call question — the Questionnaire will become the primary tool to gather that input from the client.

### 4. Kickoff call preparation

Ask:

> *"Do you want to prepare for a kickoff call?"*

If **yes**:
- Draft the **Kickoff Questionnaire** *first* using `docs/templates/client-communication/kickoff-questionnaire-template.md`.
- The Questionnaire is what the user takes into the call — its answers feed Charter, Stakeholder Register, Glossary, RAID Log.
- Charter, Register, Glossary, RAID Log are drafted **after** the kickoff call, against the answers captured.

If **no** (materials already cover the input space, or the kickoff has already happened):
- Proceed straight to the rest of the bundle (Charter → Register → Glossary → RAID), drawing context from the materials in `docs/reference/`.

### 5. Doc location and Confluence sync (low-stakes — defaults are fine)

- **Doc location** — default `{project-root}/docs/client/`. Confirm or override.
- **Confluence sync (optional)** — does this project use Confluence? If yes, capture the space key for downstream skills. Skip if unknown.

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
- `.claude/` agent and skill definitions (read-only territory unless user explicitly asks for skill-builder work — feedback file at `.claude/skills/relevant-agents-business-analyst/feedback.md` is the only writeable exception, and only for capturing user feedback about Homer)

Confirm or adjust with the user, then write to `access-boundaries.md`.

## Ready

Setup complete. Homer is ready to facilitate.

# Access Boundaries — Homer

Defaults from `init.md`. Adjust on user instruction.

## Read access

- `{project-root}/docs/`
- `{project-root}/_bmad/_memory/relevant-ba-sidecar/`
- `{project-root}/.claude/skills/create-user-story/` *(for `ES` capability handoff)*
- Project README and config files (`{project-root}/_bmad/config.yaml`, `config.user.yaml`)

## Write access

- `{project-root}/docs/client/`
- `{project-root}/docs/reference/`
- `{project-root}/_bmad/_memory/relevant-ba-sidecar/`

## Deny zones

- All other agents' sidecars (e.g. `_bmad/_memory/business-analyst-sidecar/` — Sarah's territory)
- Source code directories
- `node_modules`, build artefacts
- `.claude/` agent and skill definitions (read-only territory unless user explicitly asks for skill-builder work)

## Notes

If a file operation falls outside these boundaries, pause and confirm with the user before executing.

# Examples & Use Cases

Practical examples for using Easyterms Agents.

---

## Example Workflows

**From idea to requirement**

1. Start with [LB] Lightweight Brainstorming to capture and prioritize ideas.
2. Use the output to start [BR] Create Business Requirement for the chosen idea.
3. Complete the 7-step BR flow for a validated, Jira-ready requirement.

**Single requirement**

1. Invoke Sarah and choose [BR] Create Business Requirement.
2. Follow the 7 steps (context, value, rules, patterns, regulatory, document, confirm).
3. Use the final output for Jira or handoff to development.

---

## Common Scenarios

- **New feature request** — Use [BR] to turn the request into a clear business requirement.
- **Exploring options** — Use [LB] first, then [BR] for the selected option.
- **Platform onboarding** — Use [PK] Platform Knowledge or [RC] Review Context.
- **Consistency check** — Use [BA] Business Rule Audit before or after new requirements.

---

## Tips & Tricks

- Run [LB] before [BR] when the scope or idea is still fuzzy.
- Use [RC] and [PT] to align new requirements with existing platform patterns.
- Use [SM] Save Session to persist insights for later sessions.

---

## Troubleshooting

### Workflow not found

Ensure agent exec paths point to this module’s `workflows/` folder (e.g. `docs/bmb-creations/easyterms-agents/workflows/...`). If you moved the module, update paths in `agents/business-analyst/business-analyst.agent.yaml`.

### Agent not activating

Confirm your IDE/BMAD setup loads the easyterms-agents module and the Business Analyst agent. Check that `module.yaml` and agent metadata (id, module) are correct.

### Getting More Help

- Review README.md and module structure
- Check `module.yaml` and agent YAML paths
- Consult BMAD documentation if you use the BMAD framework

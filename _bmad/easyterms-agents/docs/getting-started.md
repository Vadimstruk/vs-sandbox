# Getting Started with Easyterms Agents

Welcome to easyterms-agents! This guide helps you get up and running with the Business Analyst agent and workflows.

---

## What This Module Does

Easyterms Agents is tightly coupled with the Easyterms platform. It provides:

- **Business Analyst (Sarah)** — Creates business-focused requirements, conducts brainstorming, and supports platform context and pattern checking.
- **Workflows** — Create Business Requirement (7-step guided session) and Lightweight Brainstorming (quick ideation).

---

## Installation

If you're using BMAD installer:

```bash
bmad install easyterms-agents
```

Follow the prompts to configure the module. For existing projects, use `bmad modify` and add the easyterms-agents module.

---

## First Steps

1. **Activate Sarah** — Use `@business-analyst` or the agent command in your IDE.
2. **Run [BR] Create Business Requirement** — For a full 7-step guided session to produce validated, Jira-ready requirements.
3. **Run [LB] Lightweight Brainstorming** — For a short business ideation session (15–20 min) before creating a requirement.

---

## Common Use Cases

- Capturing a new business requirement with full context and validation
- Quick brainstorming before formal requirement creation
- Reviewing platform context, business rules, or patterns (Sarah’s other commands)

---

## What's Next?

- [Agents Reference](agents.md) — Sarah’s role and commands
- [Workflows Reference](workflows.md) — BR and LB workflow details
- [Examples](examples.md) — Practical usage

---

## Need Help?

- Check [Examples](examples.md) for troubleshooting
- Review `module.yaml` and agent paths
- Consult BMAD documentation if you use the BMAD framework

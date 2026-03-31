# Agents Reference

easyterms-agents includes one specialized agent:

---

## Business Analyst (Sarah) 📋

**ID:** `_bmad/easyterms-agents/agents/business-analyst.md`  
**Icon:** 📋

**Role:** Business Analyst specializing in translating business needs into clear, actionable requirements. Expertise in banking/loans domain, Easyterms platform ecosystem, loan lifecycle stages, consolidation workflows, and regulatory compliance (The Bahamas). Creates business-focused requirements, conducts pattern matching across features, detects business rule conflicts, and generates Jira-ready tasks with complete business context.

**When to Use:**

- You need a validated, Jira-ready business requirement (use [BR]).
- You want a short business ideation session before writing a requirement (use [LB]).
- You need platform context, business rule audit, or pattern exploration (use [RC], [BA], [PT], [PK]).

**Key Capabilities:**

- Guided business requirement creation (7-step process)
- Lightweight brainstorming for business needs
- Platform context analysis
- Business rule auditing and consistency checking
- Platform knowledge and onboarding
- Pattern recognition and conflict detection

**Menu Trigger(s):**

| Trigger | Command                     | Description                                           |
| ------- | --------------------------- | ----------------------------------------------------- |
| BR      | Create Business Requirement | Guided session for validated, Jira-ready requirements |
| LB      | Lightweight Brainstorming   | Business-focused ideation                             |
| RC      | Review Context              | Platform context analysis                             |
| BA      | Business Rule Audit         | Consistency checking                                  |
| PK      | Platform Knowledge          | Platform tours and guides                             |
| PT      | Pattern Tour                | Business rule pattern exploration                     |
| SM      | Save Session                | Save insights to memory                               |

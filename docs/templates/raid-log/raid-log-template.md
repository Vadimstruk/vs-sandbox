# RAID Log

> **Type:** Living document. Started at kickoff and continuously updated. Add new entries as they emerge; never delete entries — update status in place so the history is preserved.
> **Replaces:** the older "Assumptions & Constraints Log". The broader RAID structure (Risks, Assumptions, Issues, Dependencies) better fits both Waterfall and Agile profiles.
> **Last Updated:** YYYY-MM-DD
> **Confluence:** [URL — add when Confluence page is created, leave blank for Jira-only projects]

---

## How to Use This Document

**Categories**

| Letter | Category | What it captures |
|---|---|---|
| **R** | Risk | Something that *might* happen and would have an adverse impact if it did. |
| **A** | Assumption | Something we are treating as true without yet validating it. |
| **I** | Issue | Something that *has* happened and is currently impacting the project. |
| **D** | Dependency | Something the project relies on from another team, system, vendor, or workstream. |

**Status values (apply to all four categories)**

| Status | Meaning |
|---|---|
| **Open** | Active and unresolved — being managed. |
| **Confirmed** | (Assumptions) Validated by client or reliable source. (Dependencies) Owner has accepted the dependency. |
| **Mitigated** | (Risks) Mitigation in place; residual risk acceptable. |
| **Invalidated** | (Assumptions) Turned out to be wrong — impact assessed and documented. |
| **Closed** | (Issues / Dependencies) Resolved or delivered. (Risks) No longer applicable. |
| **Superseded** | Replaced by a confirmed fact, a CR, or a newer entry. |

**ID conventions**

- Risks: `R-001`, `R-002`, …
- Assumptions: `A-001`, `A-002`, …
- Issues: `I-001`, `I-002`, …
- Dependencies: `D-001`, `D-002`, …

**Multi-project setups**

If the project has multiple products sharing this register, add a `Project` column (e.g. `EP / IP / Both`) to each section. For single-project setups, the column can be omitted.

---

## 1. Risks Register

> Things that *might* happen. Capture probability, impact, and mitigation.

| ID | Project | Risk | Probability | Impact | Mitigation | Owner | Status | Date Raised | Last Updated |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | [EP / IP / Both] | [State the risk clearly. Use "if … then …" form where helpful.] | [High / Medium / Low] | [High / Medium / Low] | [How we are reducing probability or impact.] | [BA / PM / Dev / DevOps / Client] | Open | YYYY-MM-DD | YYYY-MM-DD |

---

## 2. Assumptions Register

> Things we are treating as true. Capture impact if wrong and the validation path.

### Technical & Infrastructure

| ID | Project | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|---|
| A-001 | [EP / IP / Both] | [State the assumption clearly and precisely.] | Open | [What breaks or must be reworked if this assumption is wrong?] | [BA / PM / Dev / DevOps] | YYYY-MM-DD | |

### Business & Domain

| ID | Project | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|---|
| A-002 | [EP / IP / Both] | [Assumption.] | Open | [Impact.] | BA | YYYY-MM-DD | |

### Process & Delivery

| ID | Project | Assumption | Status | Impact if Wrong | Owner | Date Raised | Resolution |
|---|---|---|---|---|---|---|---|
| A-003 | Both | [Assumption.] | Open | [Impact.] | PM | YYYY-MM-DD | |

---

## 3. Issues Register

> Things that *have* happened and are currently impacting the project.

| ID | Project | Issue | Impact | Resolution Path | Owner | Status | Date Raised | Date Resolved |
|---|---|---|---|---|---|---|---|---|
| I-001 | [EP / IP / Both] | [State the issue. Be factual; this is what is happening, not what might.] | [What is being delayed, blocked, or degraded right now.] | [Action being taken to resolve.] | [BA / PM / Dev / DevOps / Client] | Open | YYYY-MM-DD | |

---

## 4. Dependencies Register

> Things the project relies on from another team, system, vendor, or workstream.

| ID | Project | Dependency | Type | Owner | Needed By | Status | Date Raised | Notes |
|---|---|---|---|---|---|---|---|---|
| D-001 | [EP / IP / Both] | [State what is needed and from whom — e.g. "API spec from Vendor X", "AML licence from regulator", "Design tokens from Brand team".] | [Internal / External / Regulatory / Vendor / Cross-team] | [Name or role of the party we depend on.] | YYYY-MM-DD | Open | YYYY-MM-DD | [Anything else worth recording — meeting refs, contract clauses.] |

---

## 5. Constraints Register *(optional)*

> Hard boundaries the project must operate within. These are not things to manage like risks or issues — they are fixed facts. Capture them once and reference them when scoping.

| ID | Project | Constraint | Type | Impact | Owner |
|---|---|---|---|---|---|
| C-001 | [EP / IP / Both] | [State the constraint.] | [Regulatory / Technical / Business / Scope] | [How this shapes design or delivery decisions.] | [Owner role(s)] |

---

## Change History

| Date | Change | By |
|---|---|---|
| YYYY-MM-DD | RAID Log initialised at kickoff. | [BA Name] |

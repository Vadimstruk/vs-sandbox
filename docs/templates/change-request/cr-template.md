# Change Request: [Short Feature Name]

| Field             | Value                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------|
| **CR ID**         | CR-000                                                                                             |
| **Date**          | YYYY-MM-DD                                                                                         |
| **Author**        | [BA Name]                                                                                          |
| **Status**        | Draft / Pending Approval / Approved / Rejected                                                     |
| **Methodology**   | Waterfall / Agile — Fixed-Range / Agile — Capacity-Based                                           |
| **Change Type**   | Addition / Removal / Trade-off (Added + Removed)                                                   |
| **Baseline Ref**  | Waterfall: SRS section (e.g. `srs-v1.1 §4.3`) · Agile: Roadmap initiative + version (e.g. `Roadmap 2026-04 → "Top-ups & Consolidations"`) |
| **Product**       | [e.g. EasyPayday / Investor Portal]                                                                |

---

## 1. Summary

> One or two plain-language paragraphs describing what is being requested and why.
> Written for a non-technical client audience.

---

## 2. What Is Changing

> Use **Added** for new or changed behaviour, **Removed** for behaviour being withdrawn or replaced.
> - Pure addition → mark **Removed** as `N/A — no removal`.
> - Pure removal → mark **Added** as `N/A — no addition`.
> - Trade-off (one feature swapped for another) → populate both.

### 2.1 Added

> Describe the new or changed behaviour from the user's perspective. No implementation detail.

*(or)* **N/A — no addition.**

### 2.2 Removed

> Describe behaviour being withdrawn, simplified, or replaced. Capture user-visible impact (notifications, deprecation messaging, data migration).

*(or)* **N/A — no removal.**

---

## 3. Business Justification

**Problem being solved:**
> What pain point, gap, or opportunity does this address?

**Expected benefit:**
> What does the business or end user gain?

**Why now:**
> Why is this being prioritised at this point in time?

**Trade-off rationale** *(only if Change Type = Trade-off)***:**
> Why does swapping the Removed item for the Added item make sense within the current budget / capacity?

---

## 4. Scope

### In Scope
- [List what is explicitly included in this change]
- [Be specific — each bullet should be a clear deliverable or behaviour]

### Out of Scope
- [List what is explicitly excluded to prevent scope creep]
- [If something seems related but won't be addressed, call it out here]

---

## 5. Business Rules & Edge Cases

> The detailed business logic, constraints, and boundary conditions governing this change.
> In Agile profiles this section replaces the standalone BR document — it is loaded into BMad as story context. Keep it precise enough for a developer to derive acceptance tests, but written in business terms.

### Business Rules
- [Rule 1 — e.g. *"Redemption fee shall not be charged when manual repayment ≤ 2× net monthly repayment within one calendar month."*]
- [Rule 2]

### Edge Cases & Boundary Conditions
- [Case 1 — e.g. *"If the value date of a new transaction precedes an existing transaction's value date, the system redistributes money across all transactions on or after the new value date."*]
- [Case 2]

### Worked Examples *(optional — recommended for non-trivial calculations or multi-step rules)*
> Numbered examples showing inputs, processing, and expected output. Reuse the client's own examples wherever provided.

**Example 1 — [scenario name]**
- Inputs: …
- Processing: …
- Expected result: …

---

## 6. Regulatory & Compliance Considerations

> Any AML / KYC / data-protection / financial-conduct / accessibility implications.
> Mark `None identified` if not applicable.

- [Consideration 1]
- [Consideration 2]

---

## 7. Acceptance Criteria

> Plain business language. Each criterion independently verifiable.

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

---

## 8. Affected Areas

> Parts of the system or business processes impacted by this change.

| Area               | Impact                       | Notes                          |
|--------------------|------------------------------|--------------------------------|
| [Feature/Module]   | New / Modified / Removed     | [Brief description of impact]  |
| [Feature/Module]   | New / Modified / Removed     | [Brief description of impact]  |

---

## 9. Open Questions

> Unresolved questions needing client or stakeholder input before implementation can begin.
> Leave blank if none.

| # | Question                        | Owner  | Due Date   | Resolution |
|---|---------------------------------|--------|------------|------------|
| 1 | [Question]                      | [Name] | YYYY-MM-DD |            |

---

## 10. Client Approval

> Must be completed before development begins.

| Name | Role | Decision                              | Date | Signature / Confirmation |
|------|------|---------------------------------------|------|--------------------------|
|      |      | Approved / Rejected / Needs Revision  |      |                          |

**Approval Notes:**
> Any conditions, clarifications, or amendments agreed at the time of approval.

---

## 11. Internal Notes *(not shared with client)*

> BA working notes and links to related artefacts.

- **Related BR** *(Waterfall only)*: [Link to BR document]
- **Related Roadmap initiative** *(Agile)*: [Initiative name + Roadmap version]
- **Related ADRs:** [Links]
- **Related Epics / Stories:** [Once created in Jira]
- **Notes:** [Anything the dev team or BA needs to know that isn't client-facing]

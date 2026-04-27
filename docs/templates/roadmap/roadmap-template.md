# Product Roadmap — [Product Name]

| Field                  | Value                                                          |
|------------------------|----------------------------------------------------------------|
| **Version**            | YYYY-MM (e.g. `2026-04`) — bumped at each monthly review       |
| **Methodology**        | Agile — Fixed-Range / Agile — Capacity-Based                   |
| **Last Reviewed**      | YYYY-MM-DD (with client)                                       |
| **BA Owner**           | [Name]                                                         |
| **Capacity Reviewer**  | PM / Tech Lead [Name]                                          |
| **Vision Ref**         | [Link to Product Vision Statement]                             |

> **Living document.** No baseline sign-off; reviewed monthly with the client.
> This Roadmap is the **CR baseline** — Change Requests measure scope deviations against the most recently agreed version. Cite it from a CR as `Roadmap YYYY-MM → "<Initiative Name>" (R-XXX)`.

---

## Themes

> Strategic groupings that organise initiatives. Typically 3–7. Themes are stable across many monthly reviews; initiatives churn within them.

| Theme ID | Theme               | Description                                |
|----------|---------------------|--------------------------------------------|
| T-1      | [e.g. Repayments]   | [One-line strategic intent]                |
| T-2      | [e.g. Self-service] | [One-line strategic intent]                |

---

## Now

> Initiatives currently being implemented or about to start. **Detailed** in both Agile profiles.
> These are what *Create Epics & Stories* (BMad SM) decomposes into Jira epics + stories.

### R-001 — [Initiative Name]

| Field                | Value                                                          |
|----------------------|----------------------------------------------------------------|
| **Theme**            | T-1                                                            |
| **Status**           | In Progress / Committed                                        |
| **Target Window**    | [e.g. Sprint 31–32, or Apr–May 2026]                           |
| **Effort**           | [T-shirt size or sprint count]                                 |
| **Source CR**        | [CR-XXX if introduced via CR; blank if part of original scope] |

**Description:**
> Two or three sentences. Plain language. What it is, who it serves.

**Success signals:**
- [Measurable or observable outcome that means this initiative is "done well"]
- [Outcome 2]

**Key constraints / dependencies:**
- [Dependency 1]
- [Constraint 1]

---

## Next

> Initiatives planned to start within roughly the next 1–3 months.
> **Fixed-Range:** detailed (same fields as Now). **Capacity-Based:** light fields only (Theme, Description, indicative effort).

### R-00X — [Initiative Name]

| Field                  | Value                |
|------------------------|----------------------|
| **Theme**              | T-X                  |
| **Indicative Effort**  | [T-shirt size]       |
| **Source CR**          | [CR-XXX or blank]    |

**Description:**
> One or two sentences.

*(Fixed-Range only — also include Status, Target Window, Success signals, Constraints. Same shape as Now items.)*

---

## Later

> Initiatives identified but not yet committed. **Light fields only** in both Agile profiles — stay at the strategic-placeholder level. No effort sizing, no acceptance shape.

### R-00X — [Initiative Name]

| Field          | Value                |
|----------------|----------------------|
| **Theme**      | T-X                  |
| **Source CR**  | [CR-XXX or blank]    |

**Description:**
> One sentence — strategic intent only.

---

## Recently Shipped *(optional — last 1–2 review cycles)*

> Initiatives that have moved from Now → Done since the previous review. Useful client-facing context for monthly review meetings.

| ID    | Initiative | Theme | Shipped In         | Release Notes Ref |
|-------|------------|-------|--------------------|-------------------|
| R-XXX | [Name]     | T-X   | [Sprint / Release] | [Link]            |

---

## Change Log

> Every monthly review produces entries here. Records what moved between buckets (and why), what was added (and the CR that introduced it), and what was deprioritised or removed.
> This is the audit trail that lets a CR cite a specific Roadmap version as its baseline.

| Date       | Initiative ID | Change                       | Driver / CR Ref     |
|------------|---------------|------------------------------|---------------------|
| YYYY-MM-DD | R-XXX         | Promoted Next → Now          | Capacity freed      |
| YYYY-MM-DD | R-XXX         | Added to Later               | CR-XXX              |
| YYYY-MM-DD | R-XXX         | Shipped (Now → Done)         | —                   |
| YYYY-MM-DD | R-XXX         | Removed                      | CR-XXX (trade-off)  |
| YYYY-MM-DD | R-XXX         | Re-prioritised Now → Next    | Capacity reallocation |

---

## Internal Notes *(not shared with client)*

- **Capacity assumptions:** [PM/Tech Lead note on monthly cap and current burn]
- **Risk markers:** [Initiatives with elevated delivery risk]
- **Open prioritisation questions:** [Items where BA wants client input at next monthly review]

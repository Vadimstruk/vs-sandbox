# System Description Document (SDD) — [Product Name]

> **Type:** Living document — "as it exists today" reference for the system. Replaces the SRS in Agile profiles. Updated continuously as features ship; no version baselines, no formal client sign-off, no archive ceremony.
> **Last Updated:** YYYY-MM-DD
> **Owner:** BA
> **Profiles:** Agile (Fixed-Range, Capacity-Based)
> **Confluence:** [URL — pending]

---

## How to Use This Document

- The SDD describes *what is true now*, not *what is being built next*. Forward-looking work belongs in the Roadmap and CRs.
- Updated at every feature ship (end of Phase 2) and confirmed at every release (Phase 4 step 3). Bug fixes that restore the behaviour described here are eligible for Quick Spec policy.
- Audience: BA, Dev, QA, client (for reference). Plain language; cross-reference Glossary terms.
- No internal versioning. The Last Updated date in the header is the canonical timestamp.

---

## 1. System Overview

[2–4 sentences describing what the system does, who uses it, and at what scale. The orientation paragraph for someone joining the project today.]

---

## 2. Architecture Summary

[Plain-language description of the major components and how they fit together. Reference (do not duplicate) the architecture diagrams maintained alongside.]

| Component | Responsibility | Notes |
|---|---|---|
| [Component] | [What it does] | [Tech, ownership, key constraints] |

---

## 3. Integrations

| External system | Direction | Purpose | Owner / contact |
|---|---|---|---|
| [System name] | Inbound / Outbound / Bidirectional | [Why we integrate] | [Owner role / contact] |

---

## 4. Data Flow

[Where the data lives, how it moves, what its lifecycle looks like. Concrete enough that a new dev can trace a request end-to-end after reading this section.]

---

## 5. Environments

| Environment | Purpose | Access | Test data |
|---|---|---|---|
| Production | Live customer use | [Access policy] | Real customer data |
| Staging / UAT | Pre-release validation | [Access policy] | [Synthetic / anonymised — specify] |
| Development | Dev iteration | [Access policy] | Synthetic |

---

## 6. Non-Functional Behaviour

| Property | Current state |
|---|---|
| Performance targets | [e.g. "App launches < 3s on mid-range Android"; "API p95 < 800ms"] |
| Availability target | [e.g. "99.5% during US business hours"] |
| Offline behaviour | [What works offline; what requires connectivity] |
| Security model | [Auth approach, data-at-rest / in-transit, access controls] |
| Compliance posture | [SOC 2 status; CCPA / GDPR / others] |
| Observability | [Logging, monitoring, alerting in place] |

---

## 7. Known Constraints & Limitations

- [Hard constraint or limitation that shapes design decisions today.]
- [Another constraint.]

---

## 8. Recent Material Changes *(rolling 90-day log)*

| Date | Change | Reference |
|---|---|---|
| YYYY-MM-DD | [Brief summary of what changed in the system] | [CR-XXX / Release vX.Y / ADR-XXX] |

> Older entries pruned to a release-history note in the relevant Release Notes file. The SDD is not a change log; it is a current-state document.

---

## Change History

| Date | Change | By |
|---|---|---|
| YYYY-MM-DD | SDD initialised as living document | [BA] |

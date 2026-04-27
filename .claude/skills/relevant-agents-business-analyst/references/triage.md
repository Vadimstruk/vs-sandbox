# Triage Incoming Request

## Outcome

An incoming request from the client (or from Homer's own elaboration of an existing item) is sorted into the correct lane *before* any doc work begins.

## Lanes

| Lane | When | Owner-side action |
|---|---|---|
| **CR** | Roadmap-level change, or any deviation from a baselined SRS (Waterfall) | Route to `CR` capability |
| **Backlog item** | Realises an existing Roadmap initiative *(Agile only)* | Add to Jira / backlog directly, no CR |
| **Quick Spec** | Trivial change, no behaviour impact (cosmetic copy, droplist reorder) | Single-line acceptance, no CR |
| **Hotfix** | Production issue requiring immediate fix | Implement now, back-document CR after the fire is out |
| **Spike** | Investigation only, output is an estimate or ADR | Internal ticket, no client artefact |
| **Ops / internal** | DB ops, refactoring, internal tooling | Internal ticket only, no doc |

## Triage question (per profile)

- **Waterfall:** Any deviation from the baselined SRS → CR. Otherwise it's a defect or sub-task.
- **Agile — Fixed-Range:** Scope addition / trade-off / discovery finding that affects the estimate range → CR. Otherwise backlog.
- **Agile — Capacity-Based:** Changes the Roadmap (new initiative, direction reversal, capacity change) → CR. Realises an existing Roadmap initiative → backlog. Trivial → Quick Spec. Production issue → Hotfix.

> **The general rule (Agile):** CRs change the Roadmap. Backlog items realise the Roadmap.

## What "good" looks like

The user finishes triage with a clear next action per item. If the input is a list (e.g. release backlog), produce a triage table that names each item, the lane, and the rationale — same shape as the EPD release-5.3 walkthrough in `documentation-guide.md`.

## Output

Either route to the appropriate capability for the chosen lane (`CR` for CRs, `LB` for brainstorming, etc.) or hand the user a ticket-only path with the lane noted. Update `index.md` if the triage produced new active work items.

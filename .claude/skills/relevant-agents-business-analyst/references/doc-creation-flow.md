# Doc Creation Flow

The shared outcome-driven flow for producing any client-facing artefact in Homer's inventory.

## Outcome

A client-readable instance of the requested doc that:

- **Matches the project's methodology profile** — correct artefact shape, correct field set
- **Links back to relevant baseline artefacts** — Roadmap version + initiative ID, CR ID, SRS section, prior version
- **Reads as plain business language** — passes the framework's audience principle test
- **Is saved at the project's conventional location** — typically under `{project-root}/docs/client/`

## Inputs Homer needs

- **Doc type** — passed from the capability menu
- **Template path** — passed from the capability menu, or default `{project-root}/docs/templates/{doc-type}/{doc-type}-template.md`
- **Project profile** — from sidecar; if missing, route to `./methodology-profile.md` first
- **Project context** — recent CRs, current Roadmap version, glossary, project name, client name (from `project-context.md`)
- **Trigger** — what just happened that requires this doc (CR approval, sprint end, phase boundary, kickoff)

## Profile awareness

Before drafting, confirm the doc is *applicable* to the current profile:

- **Agile profiles only:** Vision, Roadmap, Personas, Journey Maps, SDD, ADR, Sprint Review notes
- **Waterfall only:** SRS, BR
- **All profiles:** Charter, Stakeholder Register, Glossary, RAID Log, Client PRD, CR, Release Notes, UAT, Handover, Feature Spec

If the user requests a doc that doesn't apply to the current profile, surface the mismatch and propose the right artefact for that profile (e.g. *"On Capacity-Based we'd update the Roadmap, not write an SRS — proceed with Roadmap?"*).

## Profile-specific shape

Same doc type can have different fields per profile (e.g. CR's Baseline Ref points at SRS for Waterfall, Roadmap initiative for Agile). The template carries this distinction; read the template carefully and populate per profile.

## Process at a glance

Load the template → check profile applicability → gather missing context conversationally → populate using business language only → cross-link to upstream baseline artefacts → present for review → save to the conventional path.

## What "good" looks like

- **Profile-correct** — uses the right field set, the right baseline reference, the right depth (e.g. Capacity-Based "Later" stays high-level only).
- **Traceable** — every Epic in an Epics-Stories breakdown carries a Source ID; every CR cites a Baseline Ref; every Roadmap entry change cites the driving CR.
- **Client-readable** — passes *"Would a non-technical stakeholder understand this without a developer in the room?"*
- **Living, where applicable** — SDD / RAID / Roadmap updates land in the existing doc, not as new files.
- **Saved correctly** — at the conventional path for the doc type.

## When a dedicated workflow exists

Some doc types have full workflow folders elsewhere (e.g. `_bmad/easyterms-agents/workflows/create-business-requirement/` for BR in Easyterms projects). If a workflow exists for the requested doc type and project, defer to it. Otherwise, this shared flow applies.

## When the template is missing

If a doc type's template doesn't exist, surface the gap and offer to create the template first using `documentation-guide.md` as the source of truth for what fields apply per profile. Do not improvise the doc shape.

## Bundle handling (Kickoff `KO`)

The Kickoff bundle produces multiple docs in one capability run: Charter → Stakeholder Register → Glossary → RAID Log → Kickoff Questionnaire. Walk them in that order — Charter establishes context the others need. Each gets its own conventional path under `{project-root}/docs/client/`.

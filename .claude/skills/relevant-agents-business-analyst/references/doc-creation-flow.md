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

Load the template → check profile applicability → gather missing context conversationally → populate using business language only → cross-link to upstream baseline artefacts → present for review → **canonical-tree check** → save to the conventional path.

## Canonical-tree pre-write check (Operating Rule 4)

Before writing any artefact to a path **not already in use on this project**, read `{project-root}/docs/templates/documentation-guide.md` and verify the target path is listed in the Single-Project (or Multi-Project) canonical tree. If it isn't, and there is no framework precedent in the existing repo, surface the question to the user before writing — do not improvise a new subfolder under `docs/client/`.

Existing paths on the project's Progress Tracker are already validated — write to them without re-checking. See `./operating-rules.md` § 4 for the full rule.

## What "good" looks like

- **Profile-correct** — uses the right field set, the right baseline reference, the right depth (e.g. Capacity-Based "Later" stays high-level only).
- **Traceable** — every Epic in an Epics-Stories breakdown carries a Source ID; every CR cites a Baseline Ref; every Roadmap entry change cites the driving CR.
- **Client-readable** — passes *"Would a non-technical stakeholder understand this without a developer in the room?"*
- **Living, where applicable** — SDD / RAID / Roadmap updates land in the existing doc, not as new files.
- **Saved correctly** — at the conventional path for the doc type.

## Sign-off ceremony and version handling (Operating Rule 6)

Git is Homer's version store. Live filenames have no version suffix; version *numbers* are metadata in the doc's Version History table; signed snapshots are git tags + exported PDFs. See `./operating-rules.md` § 6 for the rule.

**Live filename pattern.** `project-charter.md`, `product-roadmap.md`, `raid-log.md`, etc. — **no `-v1.1` suffix**. Edit-in-place on every revision. Git history is authoritative for what changed when; the Version History table inside the doc is human-readable summary metadata for the client.

**No `docs/.archive/` for superseded versions.** That folder is reserved for genuinely-abandoned drafts (a different lifecycle from "old version of the live doc"). When a doc revs from v1.0 to v1.1, edit the file in place, bump the Version History table, and commit — git holds v1.0 in history.

**Sign-off ceremony for client-signed artefacts** (Charter, UAT Sign-off, Handover, etc.):

1. Apply the requested edits to the live doc.
2. Bump the **Version History table** inside the doc (date, who changed, summary of changes).
3. Stage + draft commit message + ask for approval (per Rule 6 commit-gating).
4. After approval: commit, then **tag the commit** at sign-off — e.g. `git tag charter-signed-2026-04-30`. The tag is the diffable anchor for *"this is the version that was signed."*
5. When the signed PDF returns from DocuSign / signed-PDF-by-email, save it under `<doc-path>/signed/<filename>-<date>.pdf` (e.g. `docs/client/charter/signed/project-charter-signed-2026-04-30.pdf`). The PDF is the legal record.
6. Update the Progress Tracker matrix (status: signed-off + date).

**Commit gating (Rule 6).**

- **One commit per capability run.** Sidecar updates included in the same commit (mirrors Rule 3 — one task per capability).
- At the commit point: stage the files, draft the commit message, present a short summary of what's staged, ask for explicit approval.
- Commit only after approval. **Push is a separate approval.**

**Living docs (SDD, RAID Log, Roadmap, Stakeholder Register, Glossary).**

- Update in place; the doc itself maintains a Change Log table where appropriate.
- Each capability that touches a living doc adds a row to its Change Log.
- Multiple living-doc updates within one capability run go in the same commit.

## When a dedicated workflow exists

Some doc types have full workflow folders elsewhere (e.g. `_bmad/easyterms-agents/workflows/create-business-requirement/` for BR in Easyterms projects). If a workflow exists for the requested doc type and project, defer to it. Otherwise, this shared flow applies.

## When the template is missing

If a doc type's template doesn't exist, surface the gap and offer to create the template first using `documentation-guide.md` as the source of truth for what fields apply per profile. Do not improvise the doc shape.

## Bundle handling (Kickoff `KO`)

The Kickoff bundle produces several client-facing docs in one capability run. Order depends on whether kickoff source materials already exist:

**Path A — kickoff has not happened yet, no source materials in `docs/reference/`:**

1. **Kickoff Questionnaire** — drafted first. The user takes it into the kickoff call (or sends it to the client). It is the *input-gathering* tool, not an output artefact. Without its answers, Charter / Register / Glossary / RAID would be guesses.
2. *(pause for the call — materials land in `docs/reference/` afterwards)*
3. **Project Charter** — drafted against the Questionnaire answers. Establishes scope, objectives, governance.
4. **Stakeholder Register** — drafted from the Stakeholders & Decision Making section of the Questionnaire and from the Charter.
5. **Glossary** — seeded from domain terms surfaced during the call.
6. **RAID Log** — seeded with risks/assumptions/dependencies/issues raised during the call.

**Path B — kickoff has happened, or rich source materials already exist in `docs/reference/`:**

1. **Project Charter** — first; establishes context the rest of the bundle references.
2. **Stakeholder Register**.
3. **Glossary**.
4. **RAID Log**.
5. **Kickoff Questionnaire** — optional retrospective record (some BAs still produce it as a structured summary of the call, even after the fact).

Each doc gets its own conventional path under `{project-root}/docs/client/`. Confirm with the user which path applies before drafting.

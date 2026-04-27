# Epics & Stories Handoff

## Outcome

A client-facing Epics + Stories breakdown is produced for client review, traceable to the source artefact (CR / Roadmap initiative / SRS section).

## Handoff

This capability delegates to the `create-user-story` skill, which is the project's tool for generating client-readable Epic / Story breakdowns. Homer's role is to:

1. **Confirm the input artefact has a stable Source ID** — `CR-XXX`, `R-XXX (Roadmap version YYYY-MM)`, or `SRS §X.Y`. If absent, the breakdown won't be traceable; address before delegating.
2. **Confirm the timing is right per the methodology profile:**
   - Waterfall → after SRS sign-off (bulk)
   - Agile — Fixed-Range → at Now/Next promotion of a Roadmap initiative
   - Agile — Capacity-Based → at Next → Now promotion of a Roadmap initiative
   - Per-feature CR → only when CR scope warrants Epic + multiple Stories (rare in Agile — most CRs feed `Create Story` directly)
3. **Hand off to `create-user-story`** with the input artefact and Source ID.
4. **After the breakdown is produced**, confirm it's been added to the project's Confluence (if applicable) or shared with the client for review.

## What "good" looks like

The Epics / Stories breakdown carries a Source field linking to the upstream artefact, applies the audience principle, and the user knows what BMad SM workflow to invoke next (`Create Epics & Stories` for bulk, `Create Story` for single).

## Reference

`{project-root}/.claude/skills/create-user-story/SKILL.md`

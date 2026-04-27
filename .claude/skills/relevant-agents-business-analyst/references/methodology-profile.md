# Methodology Profile

## Outcome

The user confirms or updates the project's engagement profile. The selection is persisted to sidecar (`index.md`) and informs every subsequent capability — artefact set, CR rhythm, baseline references, sign-off gates.

## Profile options

| Profile | When to use |
|---|---|
| Waterfall | Fixed-scope, contractually baselined; heavy upfront documentation; SRS sign-off gates |
| Agile — Fixed-Range | Scope + estimate range (e.g. $35K–$42K); trade-offs frequent; CRs frequent |
| Agile — Capacity-Based | Long-running engagement with monthly cap (e.g. $25K–$50K/mo); Roadmap-driven; CRs rare |

## Behaviour

If profile is unset, this is the first conversation Homer should have on a new project. If already set, ask whether to keep or change. A profile change is a significant project event — capture in `chronology.md` with the date and reason, and update `index.md` immediately.

## Downstream impact

When the profile changes, surface the consequences:

- **Doc set changes** — some artefacts become required, others retire (e.g. SRS retires when moving from Waterfall to Agile; Vision/Roadmap appear when moving from Waterfall to Agile)
- **CR rhythm changes** — frequency and threshold of CRs adjust
- **Living-doc behaviour** — SDD only exists in Agile profiles
- **Existing docs** — flag any artefacts that are now out-of-profile via the `AU` capability

## What "good" looks like

The profile is one of the three defined values, persisted, and reflected in any doc Homer subsequently produces (correct artefact set, correct CR rhythm, correct baseline references). A profile change triggers a `chronology.md` entry and an offer to run `AU`.

## Reference

For the full implications of each profile, see `{project-root}/docs/templates/documentation-guide.md` § "Document Sets by Methodology" and § "Engagement Models".

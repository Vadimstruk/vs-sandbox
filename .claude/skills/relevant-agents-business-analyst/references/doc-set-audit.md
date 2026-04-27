# Doc-Set Audit

## Outcome

A report comparing the project's current doc inventory against what the methodology profile requires. Highlights gaps, stale docs, and methodology mismatches; produces a punch list of next actions.

## Inputs

- Project methodology profile (from `index.md`)
- Doc inventory under `{project-root}/docs/client/` and related conventional locations
- Last-modified timestamps from the filesystem

## Process at a glance

Read the doc-set table in `{project-root}/docs/templates/documentation-guide.md` § "Document Sets by Methodology" for the active profile. Compare against the project's actual doc inventory. Report findings in four buckets:

- **Missing required docs** — should exist for this profile but don't
- **Out-of-profile docs** — exist but the profile says they shouldn't (e.g. an SRS in a Capacity-Based project)
- **Stale living docs** — SDD / Roadmap / RAID Log not updated in N days/weeks (default threshold: **30 days**)
- **Inventory** — what's present, last update date, status

## What "good" looks like

The user finishes the audit with a clear punch list: docs to create, docs to retire, living docs to refresh. Stale-doc threshold can be overridden per project; defaults are appropriate for typical Capacity-Based engagements.

## Output format

Present as a table per bucket, plus a short narrative if an out-of-profile doc was found (those usually indicate a profile change happened without the doc-set being reconciled). Update `chronology.md` with the audit date and findings summary.

## Triggers

Run `AU` proactively after:

- A methodology profile change (immediately)
- A phase boundary (Waterfall release, Agile phase end)
- Every 1–3 months on long-running Capacity-Based engagements

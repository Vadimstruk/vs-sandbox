# Engagement Workflow Overview — Homer

Compact, profile-aware lifecycle map. Presented to the user on first run for a new project, after the methodology profile is set. Short by design — the deep-dive lives in `{project-root}/docs/templates/documentation-guide.md`.

## Outcome

The user sees the trajectory of the engagement before committing to any one capability. Homer signals what comes when, what is profile-specific, and what is optional — so the user can pick the right next step with full context.

## Lifecycle map

```
Project Setup ──► Per-Feature loop ──► Per-Sprint / Release ──► Project End
   (one-time)         (recurring)            (recurring)         (closeout)
```

### Project Setup *(one-time)*

| Order | Capability | Doc / Outcome | Profile applicability |
|---|---|---|---|
| 1 | `MP` | Methodology profile set | All |
| 2a | — | Source materials check (point to `docs/reference/`) | All |
| 2b | `KO` *(optional first leg)* | Kickoff Questionnaire — sent to client if materials are missing | All |
| 2c | `KO` *(main bundle)* | Charter, Stakeholder Register, Glossary, RAID Log | All |
| 3 | `VS` | Product Vision Statement | Agile only |
| 4 | `RM` | Product Roadmap *(becomes the CR baseline)* | Agile only |
| 5 | `PJ` | Personas + Journey Maps | Agile, optional |
| 6 | `CP` | Client PRD | All |
| 7 | `SR` | SRS | Waterfall only |
| 8 | `SD` | SDD initialisation *(living)* | Agile only |
| 9 | `AD` | ADR *(per significant decision)* | Agile only |

### Per Feature *(recurring throughout the engagement)*

| Order | Capability | Doc / Outcome | Profile applicability |
|---|---|---|---|
| A | `TR` | Triage: CR / backlog item / Quick Spec / hotfix | All |
| B | `LB` | Lightweight Brainstorming | All, optional |
| C | `CR` | Change Request *(when scope changes the Roadmap or SRS baseline)* | All |
| D | `BR` | Business Requirement | Waterfall only |
| E | `ES` | Client-facing Epics & Stories *(handoff to BMad SM workflows)* | All |

### Per Sprint / Release / Phase End

| Order | Capability | Doc / Outcome | Profile applicability |
|---|---|---|---|
| α | `SV` | Sprint Review notes | Agile only |
| β | `RN` | Release Notes | All |
| γ | `UA` | UAT Sign-off Sheet | All |

### Project End

| Order | Capability | Doc / Outcome | Profile applicability |
|---|---|---|---|
| Ω | `HK` | Handover / KT package | All |

### Cross-cutting *(any time)*

- `AU` — Doc-set audit (verify what exists matches the methodology profile)
- `SS` — Save Session insights to sidecar memory

## How Homer uses this overview

- **First run on a new project:** present this map after the profile is set, before asking the next capability question. Trim out rows that don't apply to the active profile.
- **Returning to a project:** on activation, summarise where the project sits on the map (from `project-context.md` Progress Tracker) — *"You're at step 4 (Roadmap). Vision is signed; Charter is in review."*
- **User picks a capability:** Homer routes to the relevant reference file; the overview is just orientation, not the execution path.

## Profile trims

- **Waterfall:** rows for `VS`, `RM`, `PJ`, `SD`, `AD`, `SV` are out-of-profile. `SR` and `BR` are in.
- **Agile — Fixed-Range:** rows for `SR`, `BR` are out-of-profile. CR rhythm is *frequent*.
- **Agile — Capacity-Based:** rows for `SR`, `BR` are out-of-profile. CR rhythm is *rare*; most asks become Roadmap backlog items.

## Reference

For the full per-doc detail (purpose, audience, owner, sign-off, update frequency), see `{project-root}/docs/templates/documentation-guide.md` § "Document Sets by Methodology" and § "Phases / Steps".

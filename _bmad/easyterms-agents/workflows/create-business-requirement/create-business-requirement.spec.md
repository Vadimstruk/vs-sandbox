# Workflow Specification: create-business-requirement

**Module:** easyterms-agents
**Status:** Implemented — workflow copied from \_bmad-custom-backup
**Created:** 2026-01-29

---

## Workflow Overview

**Goal:** Create validated, Jira-ready business requirements through a 7-step guided process with context-first approach, pattern matching, and conflict detection.

**Description:** Guide Business Analysts through a structured 7-step process to create validated, business-only requirements with complete context, ready for immediate developer handoff and direct Jira insertion.

**Workflow Type:** Create-only (steps-c/)

---

## Workflow Structure

### Entry Point

- `workflow.md` (main entry)
- `steps-c/` — step-01 through step-07
- `templates/business-requirement-template.md`

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Name                    | Goal                      |
| ---- | ----------------------- | ------------------------- |
| 1    | Load context            | Load context              |
| 2    | Identify value          | Identify value            |
| 3    | Explore rules           | Explore rules             |
| 4    | Check patterns          | Check patterns            |
| 5    | Validate regulatory     | Validate regulatory       |
| 6    | Document requirement    | Document requirement      |
| 7    | Confirm / generate Jira | Confirm and generate Jira |

---

## Workflow Inputs

### Required Inputs

- Business context (user-provided or from prior session)

### Optional Inputs

- Existing requirement drafts, platform docs

---

## Workflow Outputs

### Output Format

- [x] Document-producing

### Output Files

- Business requirement document (template-driven)

---

## Agent Integration

### Primary Agent

Business Analyst (Sarah)

### Other Agents

(none)

---

## Implementation Notes

Workflow is implemented. Agent menu should point exec to this module's `workflows/create-business-requirement/workflow.md` (or equivalent path used by installer).

---

_Spec created on 2026-01-29 via BMAD Module workflow_

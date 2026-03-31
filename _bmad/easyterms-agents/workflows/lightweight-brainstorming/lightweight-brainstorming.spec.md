# Workflow Specification: lightweight-brainstorming

**Module:** easyterms-agents
**Status:** Implemented — workflow copied from \_bmad-custom-backup
**Created:** 2026-01-29

---

## Workflow Overview

**Goal:** Lightweight, business-focused brainstorming for Business Analyst (Sarah) to generate business ideas ready for requirement creation.

**Description:** Facilitate quick business ideation (15–20 minutes) focused exclusively on business needs, user value, and regulatory considerations, producing a structured business ideation document ready for the Create Business Requirement workflow.

**Workflow Type:** Create-only (steps-c/)

---

## Workflow Structure

### Entry Point

- `workflow.md` (main entry)
- `steps-c/` — step-01 through step-04
- `templates/brainstorming-document-template.md`

### Mode

- [x] Create-only (steps-c/)

---

## Planned Steps

| Step | Name                    | Goal                                    |
| ---- | ----------------------- | --------------------------------------- |
| 1    | Init                    | Initialize                              |
| 2    | Generate ideas          | Generate ideas                          |
| 3    | Categorize / prioritize | Categorize and prioritize               |
| 4    | Prepare for BR          | Prepare for Create Business Requirement |

---

## Workflow Inputs

### Required Inputs

- Business focus or topic (user-provided)

### Optional Inputs

- Prior brainstorming output, platform context

---

## Workflow Outputs

### Output Format

- [x] Document-producing

### Output Files

- Brainstorming document (template-driven)

---

## Agent Integration

### Primary Agent

Business Analyst (Sarah)

### Other Agents

(none)

---

## Implementation Notes

Workflow is implemented. Agent menu should point exec to this module's `workflows/lightweight-brainstorming/workflow.md` (or equivalent path used by installer).

---

_Spec created on 2026-01-29 via BMAD Module workflow_

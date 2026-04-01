# Documentation Guide

> This is the master reference for everyone on the project — BA, PM, Dev, QA. It covers the documentation structure, the combined project workflow (BMad + client-facing), the agent and workflow reference, and the rules for creating and maintaining every document type.

---

## Overview

Documentation and workflow is split into three layers:

| Layer | Purpose | Audience |
|---|---|---|
| **Client-facing** (`docs/client/`) | Formal deliverables, requirements, agreements | Easyterms (client), Relevant delivery team |
| **Internal / BMad** (`docs/features/`, `docs/business-requirements/`) | Implementation specs consumed by developers and AI agents | Relevant delivery team |
| **Client communication** (`docs/templates/client-communication/`) | Structured templates for client meetings and onboarding conversations | BA, PM |

---

## Folder Structure

> **At project kickoff, the BA must ask:** Is this a **single project** (one codebase, one client product) or a **multi-project** (multiple products sharing a codebase)? The answer determines which folder structure to use.

---

### Single Project

All client-facing documents live directly inside `docs/client/` — no `shared/` subfolder, no project-name subfolder.

```
docs/
├── documentation-guide.md          ← this file (master reference)
│
├── client/                         ← all client-facing documentation (flat)
│   ├── glossary.md
│   ├── assumptions-log.md
│   ├── stakeholder-register.md
│   ├── charter/
│   │   └── project-charter-v1.0.md
│   ├── prd/
│   │   └── prd-v1.0.md
│   ├── srs/
│   │   └── srs-v1.0.md
│   └── change-requests/
│       └── CR-001-[feature-name].md
│
├── business-requirements/          ← internal BRs, one per feature
│   └── business-requirement-YYYY-MM-DD.md
│
├── features/                       ← BMad feature specs, one folder per feature area
│
├── templates/                      ← document templates
│   ├── client-communication/
│   │   ├── kickoff-questionnaire-template.md
│   │   └── meeting-agenda-template.md
│   ├── change-request/
│   │   └── cr-template.md
│   ├── glossary/
│   │   └── glossary-template.md
│   ├── assumptions-log/
│   │   └── assumptions-log-template.md
│   ├── stakeholder-register/
│   │   └── stakeholder-register-template.md
│   ├── project-charter/
│   │   └── project-charter-template.md
│   ├── prd/
│   │   └── prd-client-template.md
│   └── srs/
│       └── srs-template.md
│
├── reference/                      ← raw input materials from Sales handoff (not client-facing, not BMad)
│   └── [sales-notes, transcriptions, client-provided docs]
├── deep-dives/                     ← technical deep-dives per module
├── analysis/                       ← brainstorming and analysis sessions
└── .archive/                       ← superseded versions of versioned documents
```

---

### Multi-Project

Use this structure when two or more products share a codebase. Documents shared across all products (Glossary, Assumptions Log) live in `docs/client/shared/`. Each product has its own subfolder with its own Stakeholder Register, Charter, PRD, SRS, and Change Requests.

```
docs/
├── documentation-guide.md          ← this file (master reference)
│
├── client/                         ← all client-facing documentation
│   ├── shared/                     ← shared across all products
│   │   ├── glossary.md
│   │   ├── assumptions-log.md
│   │   └── stakeholder-register.md
│   │
│   ├── project-1/                  ← Product 1
│   │   ├── charter/
│   │   │   └── project-charter-v1.0.md
│   │   ├── prd/
│   │   │   └── prd-v1.0.md
│   │   ├── srs/
│   │   │   └── srs-v1.0.md
│   │   └── change-requests/
│   │       └── CR-001-[feature-name].md
│   │
│   └── project-2/                  ← Product 2
│       ├── charter/
│       │   └── project-charter-v1.0.md
│       ├── prd/
│       │   └── prd-v1.0.md
│       ├── srs/
│       │   └── srs-v1.0.md
│       └── change-requests/
│           └── CR-001-[feature-name].md
│
├── business-requirements/          ← internal BRs, one per feature
│   └── business-requirement-YYYY-MM-DD.md
│
├── features/                       ← BMad feature specs, one folder per feature area
│   ├── project-1/
│   └── project-2/
│
├── templates/                      ← document templates
│   ├── client-communication/
│   │   ├── kickoff-questionnaire-template.md
│   │   └── meeting-agenda-template.md
│   ├── change-request/
│   │   └── cr-template.md
│   ├── glossary/
│   │   └── glossary-template.md
│   ├── assumptions-log/
│   │   └── assumptions-log-template.md
│   ├── stakeholder-register/
│   │   └── stakeholder-register-template.md
│   ├── project-charter/
│   │   └── project-charter-template.md
│   ├── prd/
│   │   └── prd-client-template.md
│   └── srs/
│       └── srs-template.md
│
├── reference/                      ← raw input materials from Sales handoff (not client-facing, not BMad)
│   └── [sales-notes, transcriptions, client-provided docs]
├── deep-dives/                     ← technical deep-dives per module
├── analysis/                       ← brainstorming and analysis sessions
└── .archive/                       ← superseded versions of versioned documents
```

---

## Combined Project Workflow

This section shows how the BMad workflow and the client-facing layer fit together across the full project lifecycle. Every step is labelled with the BMad workflow or agent that drives it, and the client-facing document it produces or requires.

**Legend:** ✅ Client sign-off required | 📋 BMad workflow | 👤 Agent | 📄 Document produced

---

### Phase 1 — Project Setup (once per project)

#### Greenfield (new project)

> **Before starting:** The BA must complete two configuration steps (0a, 0b) and a Sales handoff review (1) before any document is created.

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 0a | 👤 BA — confirm project type | **Single project** → flat `client/` structure. **Multi-project** → `client/shared/` + per-product subfolders. See [Folder Structure](#folder-structure). | — |
| 0b | 👤 BA — confirm tooling setup | **BMad + Jira only** → client-facing docs in git only. **BMad + Jira + Confluence** → client-facing docs mirrored to Confluence; internal/BMad docs stay in git. See [Hybrid Tooling](#hybrid-tooling-git--jira--confluence). | — |
| 1 | 👤 BA — collect and review pre-kickoff materials | BA receives materials from Sales (notes, transcriptions e.g. Fireflies, client-provided documents) and places them in `docs/reference/`. BA reviews before kickoff. | — |
| 2 | 👤 BA — Kickoff session | 📄 **Project Charter**, **Stakeholder Register**, **Glossary**, **Assumptions Log** | — |
| 2a | 👤 BA — Confluence sync *(if Jira + Confluence project)* | Ask user: sync kickoff documents to Confluence? Create/update pages for Charter, Stakeholder Register, Glossary, Assumptions Log. | — |
| 3 | 📋 Research — market / domain / technical *(optional)* | — internal only — | — |
| 4 | 📋 Lightweight Brainstorming *(optional)* | — internal only — | — |
| 5 | 👤 BA — refine Charter if needed, then submit for sign-off | Incorporate any findings from Research or Brainstorming (new constraints, scope clarifications, risks) before sending to client. 📄 **Project Charter** | ✅ Yes |
| 5a | 👤 BA — Confluence sync *(if Jira + Confluence project)* | Ask user: sync updated Charter to Confluence? | — |
| 6 | 📋 Create Product Brief | — internal: uses Charter + kickoff artifacts as input — | — |
| 7 | 📋 Create PRD (BMad internal) | — internal — | — |
| 8 | 👤 BA — Client PRD *(derived from BMad PRD)* | 📄 **Client PRD** | ✅ Yes |
| 9 | 📋 Create UX Design | UX review with client *(informal)* | Optional |
| 10 | 📋 Create Architecture | — internal only — | — |
| 11 | 👤 BA *(manual, no workflow yet)* | 📄 **SRS** *(from PRD + UX + Architecture)* | ✅ Yes |
| 12 | 📋 Create Epics & Stories | — internal only — | — |
| 13 | 📋 Check Implementation Readiness | — internal gate — | — |

> **Note:** An SRS creation workflow is planned for Sarah (BA agent) — not yet built.

#### Brownfield (existing project switching to BMad)

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 0a | 👤 BA — confirm project type | Single or multi-project — determines folder structure. | — |
| 0b | 👤 BA — confirm tooling setup | BMad + Jira only, or BMad + Jira + Confluence. | — |
| 1 | 👤 BA — collect and review pre-kickoff materials | BA receives materials from Sales and places them in `docs/reference/`. For brownfield: existing specs, legacy docs, and prior work also placed here by BA. | — |
| 2 | 👤 BA — Kickoff session | 📄 **Project Charter**, **Stakeholder Register**, **Glossary**, **Assumptions Log** | — |
| 3 | 📋 **Document Project** | — internal: feature specs, deep-dives from existing system — | — |
| 4 | 👤 BA *(manual)* | 📄 **SRS** *(create from existing knowledge if missing, or validate existing)* | ✅ Yes |
| 5 | Continue from Create Architecture onwards | same as greenfield steps 10–13 | — |

---

### Phase 2 — Per Feature (recurring, every feature)

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Lightweight Brainstorming *(optional)* | — internal only — | — |
| 2 | 👤 Sarah — Create CR | 📄 **Change Request (CR)** | ✅ **Yes — hard gate. BR cannot start without this.** |
| 3 | 👤 Sarah — Create BR | 📄 **Business Requirement (BR)** | — |
| 4 | 📋 Create Story | — story spec, internal — | — |
| 5 | 📋 Dev Story | — implementation — | — |
| 6 | 📋 Code Review | — internal — | — |

> **Quick Spec / Quick Dev exception** — see [Quick Spec Policy](#quick-spec-policy) below.

---

### Phase 3 — Per Sprint (recurring)

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Sprint Planning | — internal — | — |
| 2 | 📋 Sprint Status | Status update to client *(informal)* | — |
| 3 | 📋 Correct Course *(if needed)* | May trigger a new 📄 **CR** | ✅ If scope changes |
| 4 | 📋 Retrospective | — internal — | — |

---

### Phase 4 — Per Release (recurring)

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Feature Spec Creation | — internal feature specs — | — |
| 2 | 📋 Documentation Update / Deep Dive Creation | — internal — | — |
| 3 | 👤 BA *(manual)* | 📄 **SRS** updated *(CRs absorbed, version bumped)* | ✅ Yes |
| 4 | 👤 BA *(manual)* | 📄 **Client PRD** updated *(only if product goals changed)* | ✅ Major changes only |
| — | Git tag release docs, archive superseded SRS | | — |

---

## Quick Spec Policy

Quick Spec / Quick Dev bypasses the CR → BR client sign-off gate. This is acceptable **only** when at least one of the following conditions is met:

1. **Bug fix** — the change restores behaviour already defined in the SRS (something agreed and broken, not something new).
2. **Internal / technical change only** — purely internal with zero client-visible impact (refactors, infrastructure, internal tooling, performance improvements with no behaviour change).

**Everything else requires a CR** — any new behaviour, any change to existing behaviour, and anything visible to the client or end user in any form.

> If in doubt, create a CR. The cost of a CR is low; the cost of implementing something the client never approved is high.

---

## Agents & Workflow Reference

### Agents

| Agent | Persona | When to Use |
|---|---|---|
| **Sarah** — Easyterms BA | Business Analyst specialising in Easyterms platform | Create CRs and BRs, brainstorm features, review platform context, audit business rules. Primary agent for the BA workflow. |
| **Mary** — BMad Analyst | Strategic Business Analyst | Market research, domain research, technical research, create product briefs, document existing projects. |
| **BMad PM** | Product Manager | Create and edit PRDs, sprint planning, sprint status, retrospectives, correct course. |
| **BMad Architect** | Solution Architect | Create architecture documents, solution design decisions. |
| **BMad Dev** | Developer | Implement stories via Dev Story workflow. |
| **BMad Tech Writer** | Technical Writer | Create and update feature specs, deep-dives, documentation updates. |
| **BMad QA** | QA Engineer | Generate E2E tests, test design. *(QA agent workflow — to be integrated later.)* |

### Key Workflows

| Workflow | Agent | Phase | Output |
|---|---|---|---|
| Create Business Requirement | Sarah | Per Feature | BR document |
| Lightweight Brainstorming | Sarah | Per Feature *(optional)* | Brainstorming report |
| Create Product Brief | Mary | Project Setup | Product brief → feeds Project Charter |
| Document Project | Mary | Brownfield Setup | Feature specs, deep-dives |
| Create PRD | BMad PM | Project Setup | BMad PRD (internal context) |
| Create UX Design | BMad UX Designer | Project Setup | UX design spec |
| Create Architecture | BMad Architect | Project Setup | Architecture document |
| Create Epics & Stories | BMad SM | Project Setup | Epics and stories list |
| Check Implementation Readiness | BMad PM | Project Setup | Readiness report |
| Create Story | BMad SM | Per Feature | Story spec |
| Dev Story | BMad Dev | Per Feature | Implementation |
| Code Review | BMad Dev | Per Feature | Review report |
| Sprint Planning | BMad SM | Per Sprint | Sprint plan |
| Sprint Status | BMad SM | Per Sprint | Status report |
| Correct Course | BMad SM | Per Sprint | Change proposal |
| Retrospective | BMad SM | Per Sprint | Retrospective report |
| Feature Spec Creation | BMad Tech Writer | Per Release | Feature spec (13 sections) |
| Documentation Update | BMad Tech Writer | Per Release | Updated feature docs |
| Deep Dive Creation | BMad Tech Writer | Per Release | Technical deep-dive |
| Quick Spec / Quick Dev | Any | Bug fix / internal only | Quick tech spec + implementation |
| **Create SRS** | **Sarah** *(planned — not yet built)* | **Project Setup + Per Release** | **SRS document** |
| **Meeting Prep** | **Sarah** *(planned — not yet built)* | **Ongoing* | **Client meeting agenda** |

---

## Document Reference

### Client Communication (`docs/templates/client-communication/`)

#### Kickoff Questionnaire (`kickoff-questionnaire-template.md`)
- **Purpose:** Structured set of questions for the BA to ask at project kickoff or client onboarding. Covers business context, stakeholders, domain and regulatory requirements, integrations, scope, existing documentation, communication preferences, and UAT. Answers feed directly into the Glossary, Assumptions Log, Stakeholder Register, and Project Charter.
- **When to use:** At the start of every new project or when onboarding a new client.
- **Owner:** BA
- **Output feeds:** Glossary, Assumptions Log, Stakeholder Register, Project Charter

#### Meeting Agenda (`meeting-agenda-template.md`)
- **Purpose:** Standard structure for recurring client calls. Covers previous action items, dev status, open CRs, open questions, open assumptions needing confirmation, upcoming milestones, new client requests, decisions log, and action items. The Decisions Made section (Section 9) is designed to be emailed to the client after every call as the written record.
- **When to use:** Prepare before every scheduled client call.
- **Owner:** BA
- **Output feeds:** Open CRs updated, Assumptions Log updated, follow-up email to client

---

### Client-Facing — Shared (`docs/client/shared/`) — Multi-Project Only

> This section applies only to **multi-project** setups. For single-project setups, the Glossary and Assumptions Log live directly in `docs/client/` alongside all other client-facing documents.

#### Glossary (`glossary.md`)
- **Purpose:** Single source of truth for domain terminology. All project documents must use terms exactly as defined here.
- **Audience:** Everyone — client, BA, developers, QA.
- **Update frequency:** Living document. Add new terms as they emerge during requirements work or development. Never delete terms — mark as deprecated if no longer in use.
- **Owner:** BA

#### Assumptions & Constraints Log (`assumptions-log.md`)
- **Purpose:** Records all assumptions made during requirements and development, and formal constraints that shape the system. Each assumption has a status (Open / Confirmed / Invalidated / Superseded) and is tagged by product if multi-project.
- **Audience:** BA, PM, client for review.
- **Update frequency:** Living document. Add assumptions as they are identified. Update status when validated or proven wrong. Never delete — update in place.
- **Owner:** BA (assumptions), PM (process and delivery assumptions)

#### Stakeholder Register (`stakeholder-register.md`)
- **Purpose:** Single register covering all stakeholders across all products — delivery team, client contacts, end user groups, and external systems. Structured with shared people in sections 1–3 and a per-product RACI subsection for each product. Keeping it shared avoids duplicating stakeholder entries and ensures there is one place to update when roles or contacts change.
- **Audience:** PM, BA, client.
- **Update frequency:** Living document. Update when team members change, new stakeholders are identified, or roles shift.
- **Owner:** PM

---

### Client-Facing — Per Product

#### Project Charter (`charter/project-charter-v1.0.md`)
- **Purpose:** Defines the project's scope, objectives, constraints, high-level milestones, and key stakeholders. The foundational agreement between client and development partner.
- **Audience:** Client (Easyterms), PM, BA.
- **Versioning:** Major version bump when scope changes significantly. Minor version for corrections or additions that don't alter scope boundaries.
- **Update frequency:** Infrequently — typically only at project initiation or during a significant scope change.
- **Owner:** PM (with BA input)
- **Client sign-off required:** Yes

#### Stakeholder Register (`stakeholder-register.md`) — Single Project Only
- **Purpose:** Full list of all stakeholders — client contacts, delivery team, end user groups, and external systems. Includes roles, responsibilities, and RACI matrix. Lives in `docs/client/` for single-project setups. For multi-project setups, the Stakeholder Register lives in `docs/client/shared/` — see above.
- **Audience:** PM, BA, client.
- **Update frequency:** Living document. Update when team members change, new stakeholders are identified, or roles shift.
- **Owner:** PM

#### PRD — Product Requirements Document (`prd/prd-vX.Y.md`)
- **Purpose:** Defines the product vision, goals, user personas, functional requirements, and success criteria. Serves as both the client-facing requirements agreement and the primary context document loaded into BMad manually when creating stories or feature specs.
- **Audience:** Client (Easyterms), PM, BA, UX Designer, Dev (via BMad context).
- **BMad usage:** Loaded manually as context when running BMad workflows (create-story, feature-spec-creation, etc.). BMad does not auto-discover this file — it must be provided explicitly.
- **Content rule:** Keep business-level. Technical NFRs (API response times, tech stack specifics) belong in the architecture doc, not the PRD.
- **Versioning:** Minor version bump when features are added. Major version bump when product goals or direction change.
- **Update frequency:** Per release, during release wrap-up. Not updated mid-sprint.
- **Owner:** BA
- **Client sign-off required:** Yes (at baseline and on major version changes)

#### SRS — Software Requirements Specification (`srs/srs-vX.Y.md`)
- **Purpose:** Full detailed system requirements. The authoritative requirements document that CRs feed into at release time. Client signs off on the SRS before development begins.
- **Audience:** Client, BA, Dev, QA.
- **When created:** Greenfield — after PRD, UX Design, and Architecture are complete, before Epics & Stories. Brownfield — created or validated during project onboarding.
- **Versioning:** Minor version bump when requirements are added or clarified. Major version bump when existing requirements change substantially.
- **Update frequency:** Per release, during release wrap-up. Superseded versions moved to `.archive/`. Git-tagged at each version.
- **Owner:** BA
- **Client sign-off required:** Yes
- **Note:** SRS creation workflow is planned for Sarah agent — currently a manual BA step using the SRS template.

#### Change Request (`change-requests/CR-XXX-[feature-name].md`)
- **Purpose:** The client sign-off gate for each new feature or change. Describes what is changing, the business justification, scope, and acceptance criteria in plain language. Must be approved by the client before a Business Requirement is created and development begins.
- **Audience:** Client (primary), BA.
- **Versioning:** Not versioned. One file per feature.
- **Lifecycle:** CRs live in `docs/client/{product}/change-requests/` on `main` for their entire pre-development lifecycle. Each CR has a **STATUS field at the top** that is kept current: `Draft | Pending Design | Pending Client Approval | Approved | In Development | Deferred | Rejected`. A feature branch is only created when a CR is approved and sprint-assigned. Dead CRs are moved to `.archive/change-requests/` with STATUS: Rejected — never deleted.
- **Jira relationship:** Jira is the status and priority tracker; the CR doc is the content and scope record. They cross-reference each other (CR number in Jira ticket, Jira ticket ID in the CR doc).
- **Update frequency:** Created when a new request is received. Updated iteratively through the pre-development lifecycle (design, client discussions, clarifications). After client approval, not modified — create a new CR for changes.
- **Owner:** BA
- **Client sign-off required:** Yes — Section 8 (Approval) must be completed before BR is created

---

### Internal — BMad Layer

#### Business Requirement (`docs/business-requirements/`)
- **Purpose:** Internal requirement document derived from an approved CR. Contains business rules, examples, edge cases, regulatory considerations, and a Jira-ready task. The primary document loaded into BMad when a Dev starts implementing a feature.
- **Audience:** Dev team, BA.
- **BMad usage:** Loaded manually by Dev as context when running the dev-story or create-story BMad workflow.
- **Update frequency:** Created once per feature on the feature branch. Not updated after creation — if requirements change, a new CR and BR are created.
- **Owner:** BA

#### Feature Spec (`docs/features/{product}/{feature}/`)
- **Purpose:** Detailed feature documentation organised into up to 13 modular sections (overview, user stories, business rules, API endpoints, data models, acceptance criteria, etc.). Created after implementation to document what was built. Referenced by BMad when creating stories for related features.
- **Audience:** Dev team (via BMad), BA, QA.
- **BMad usage:** Loaded manually as context when creating stories or feature specs for related features. Not auto-discovered.
- **Update frequency:** Created or updated during release wrap-up, after all features in a release are implemented and verified.
- **Owner:** BA (created), Dev (reviewed)

---

### Templates (`docs/templates/`)

| Template | Path | Used For |
|---|---|---|
| Kickoff Questionnaire | `client-communication/kickoff-questionnaire-template.md` | Project kickoff / client onboarding |
| Meeting Agenda | `client-communication/meeting-agenda-template.md` | Recurring client calls |
| Change Request | `change-request/cr-template.md` | Every new feature request |
| Glossary | `glossary/glossary-template.md` | New product glossary setup |
| Assumptions & Constraints Log | `assumptions-log/assumptions-log-template.md` | New project setup |
| Stakeholder Register | `stakeholder-register/stakeholder-register-template.md` | New project setup (single and multi-project) |
| Project Charter | `project-charter/project-charter-template.md` | New project initiation |
| PRD (client-facing) | `prd/prd-client-template.md` | Client-facing PRD creation |
| SRS | `srs/srs-template.md` | SRS creation (greenfield + brownfield) |

> **BMad PRD** is not a template — it is generated by the BMad `create-prd` workflow (`_bmad/bmm/workflows/2-plan-workflows/create-prd/`).

---

## BA Workflow

### Per Feature

```
Client request received
        ↓
CR doc created in docs/client/{product}/change-requests/ on main
STATUS: Draft
        ↓
Iterative improvement (designs, client discussions, clarifications)
STATUS: Pending Design → Pending Client Approval
        ↓
Client approves Section 8
STATUS: Approved  →  CR sits in backlog (Jira manages priority)
        ↓
CR pulled into sprint
        ↓
Feature branch created (e.g. feature/bulk-disbursement)
BR written on feature branch  →  push to repo
STATUS on CR: In Development
        ↓
Dev picks up BR  →  implements via BMad Dev agent
        ↓
Feature merged to main  →  SRS absorbs CR at release
```

> **Dead CRs:** Move to `.archive/change-requests/` and set STATUS: Rejected. Never delete — they are useful history if a similar request resurfaces.

### Per Release (on main)

```
All features in release implemented
        ↓
Merge approved CRs into SRS  →  bump SRS version
Update PRD (if product goals changed)
Update feature specs
Git tag release docs  →  merge to main
Move superseded SRS version to .archive/
```

---

## Versioning Convention

### Document Version Numbers
- `v1.0` → initial release
- `v1.1` → minor addition or clarification (no scope change)
- `v2.0` → major scope or goal change

### Version Table (inside each versioned document)
Every versioned document includes a version history table at the top:

```markdown
| Version | Date       | Author | Summary                        |
|---------|------------|--------|--------------------------------|
| 1.0     | 2026-03-18 | BA     | Initial release                |
| 1.1     | 2026-04-10 | BA     | Added bulk disbursement section|
```

### Git Tags
Tag versioned documents at each delivery milestone:
```
git tag client/project-1-srs-v1.1
git tag client/project-1-prd-v1.0
```

---

## Traceability Chain

Every requirement can be traced from client request to implementation:

```
Client request
    ↓
Change Request (CR)          docs/client/{product}/change-requests/
    ↓
Business Requirement (BR)    docs/business-requirements/
    ↓
Feature Spec                 docs/features/{product}/{feature}/
    ↓
Story                        created via BMad /bmad-bmm-create-story
    ↓
Implementation               dev branch → PR → main
```

Each document references its source:
- BR references the CR it was derived from
- Feature spec references the BR
- SRS references the CRs absorbed at release time

---

## Hybrid Tooling: Git + Jira + Confluence

This section describes an optional hybrid approach that layers Confluence and deeper Jira integration on top of the existing git-based workflow. It is not mandatory — the base workflow (git + markdown) remains fully functional without it. The hybrid is most valuable when clients are actively engaged with documentation.

---

### The Layer Split

The hybrid assigns each tool to what it does best:

| Layer | Tool | Why |
|---|---|---|
| Status, priority, backlog | **Jira** | Single source of truth — no duplication |
| Client-facing docs (CR, PRD, SRS, Charter) | **Confluence** | Accessible to client, inline commenting, native Jira links, page approvals |
| Internal / BMad docs (BR, Feature Specs, Architecture, Deep Dives) | **Git + markdown** | AI-ready, proper diffs, developer-friendly |

**The rule:** client-facing = Confluence. Internal = git. When in doubt, ask "does the client need to read or sign off on this?" If yes → Confluence. If no → git.

---

### Revised Traceability Chain (Hybrid)

```
Client request
    ↓
Jira Epic created  ←→  Confluence CR page (content + client sign-off)
    ↓
Client approves CR on Confluence page
    ↓
Feature branch created (name includes Jira Epic ID → auto-linked)
BR written in git — references Confluence CR URL + Jira Epic ID
    ↓
Feature Spec  →  Story  →  Implementation
    ↓
SRS updated in Confluence at release  →  version frozen in git
```

---

### Jira Integration

**Smart Commits** — include the Jira Epic ID in branch names and commit messages. Jira automatically links the branch, commits, and PRs to the ticket. No manual linking needed.

```
branch:  feature/P1-123-bulk-disbursement
commit:  P1-123 add BR for bulk disbursement
```

**Jira Automation** — built-in rule engine, no extra tooling. Useful rules:
- When Epic moves to `Approved` → auto-create sub-task "Create BR"
- When all Stories in Epic are `Done` → notify BA to update SRS
- When PR merged → transition Epic to `In Development`

**Jira MCP (Claude integration)** — with a Jira MCP server configured in Claude Code, Sarah can create and update Jira tickets directly from a session. When a BR is created, the corresponding Jira ticket can be created without leaving the conversation.

---

### Confluence Integration

**Confluence page approvals** — CRs authored in Confluence can use the built-in page approval feature as the formal client sign-off mechanism, replacing the Section 8 signed document. The approval is auditable on the page.

**markdown-confluence** (npm package) — syncs markdown files from git to Confluence pages on push. Use this to auto-publish client-facing docs from git to Confluence without manual export. Configure it to sync only `docs/client/` — not internal docs.

**Confluence MCP (Claude integration)** — with a Confluence MCP server configured, Sarah can create CR pages in Confluence directly from a session, and read existing CRs/PRDs as context when drafting a BR.

---

### Scalable Dial by Client Engagement

Since client engagement varies by project, the hybrid is not all-or-nothing:

| Client engagement | Recommended setup |
|---|---|
| **Hands-off** — receives outputs, signs off by email | Smart Commits + CI sync only. Git is source of truth, Confluence is an optional read-only mirror. |
| **Engaged** — reads docs, comments, requests changes | Add Confluence for CRs and SRS. Client approves on the page. Git receives approved version via sync. |
| **All clients** | Jira MCP removes manual ticket creation during BA sessions regardless of client engagement level. |

**Minimum worthwhile setup for any project:** Jira Smart Commits + Jira MCP. Eliminates most manual status-keeping with minimal overhead.

---

### What Changes in the BA Workflow (Hybrid)

The CR backlog strategy (CRs on `main`, STATUS field, feature branch only when sprint-assigned) remains the same. The only changes are:

- CRs are authored in Confluence instead of (or in addition to) git
- Client sign-off happens on the Confluence page instead of a shared PDF
- The STATUS field on the CR doc may be simplified or removed — Jira Epic status is the source of truth
- BR cross-references the Confluence CR URL and Jira Epic ID

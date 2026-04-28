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

The **document set within each layer depends on the project's methodology** (Waterfall, Agile Fixed-Range, or Agile Capacity-Based). See [Document Sets by Methodology](#document-sets-by-methodology) for the per-profile artifact list.

---

## Kickoff Configuration

Three decisions made at project kickoff shape every documentation choice that follows. They are not workflow steps — they are project-level constants that determine which doc set, folder structure, and workflow path apply.

### 0a — Project Type

| Choice | Effect |
|---|---|
| **Single project** | Flat `client/` structure |
| **Multi-project** | `client/shared/` + per-product subfolders |

See [Folder Structure](#folder-structure).

### 0b — Tooling Setup

| Choice | Effect |
|---|---|
| **BMad + Jira only** | Client-facing docs in git only |
| **BMad + Jira + Confluence** | Client-facing docs mirrored to Confluence; internal/BMad docs stay in git |

See [Hybrid Tooling: Git + Jira + Confluence](#hybrid-tooling-git--jira--confluence).

### 0c — Methodology

The methodology choice drives which documents are produced, which workflows apply, and how Change Requests are handled.

| Profile | When to use | CR rhythm |
|---|---|---|
| **Waterfall** | Fixed scope, contractual baselining, regulated/compliance contexts | Frequent, formal — every deviation from baselined SRS |
| **Agile — Fixed-Range** | Client provides initial scope + estimate range (e.g., $35K–$42K). Budget is finite, scope flexes within range. May be phased. | Frequent — every meaningful scope event including trade-offs |
| **Agile — Capacity-Based** | Long-running engagement with monthly development cap. Living roadmap, ongoing prioritisation. | Rare — reserved for Roadmap-level changes only |

> **Default for Relevant outsourcing projects:** Agile Fixed-Range or Capacity-Based. Waterfall is rare and usually driven by client-side regulatory or contractual requirements.

See [Document Sets by Methodology](#document-sets-by-methodology) for the per-profile artifact list, and [Combined Project Workflow](#combined-project-workflow) for the per-profile workflow.

---

## Folder Structure

> The folder structure is determined by [Project Type (0a)](#0a--project-type). Within either structure, the *contents* depend on [Methodology (0c)](#0c--methodology) — see [Document Sets by Methodology](#document-sets-by-methodology) for which docs apply per profile.

---

### Single Project

All client-facing documents live directly inside `docs/client/` — no `shared/` subfolder, no project-name subfolder.

```
docs/
├── documentation-guide.md          ← this file (master reference)
│
├── client/                         ← all client-facing documentation (flat)
│   ├── glossary.md
│   ├── raid-log.md                 ← Risks, Assumptions, Issues, Dependencies
│   ├── stakeholder-register.md
│   ├── charter/
│   │   └── project-charter-v1.0.md
│   ├── meetings/                   ← Kickoff Questionnaires + Meeting Agendas (lifecycle: pre-call form → post-call notes)
│   │   ├── kickoff-questionnaire-YYYY-MM-DD.md   ← rename to kickoff-meeting-YYYY-MM-DD.md after the call (with answers in place)
│   │   └── meeting-YYYY-MM-DD.md                 ← starts as agenda; becomes notes after the call (or rename: meeting-agenda-… → meeting-notes-…)
│   ├── vision/                     ← Agile only
│   │   └── product-vision.md
│   ├── roadmap/                    ← Agile only (living)
│   │   └── product-roadmap.md
│   ├── personas/                   ← Agile only
│   │   └── personas.md
│   ├── journey-maps/               ← Agile only
│   │   └── journey-maps.md
│   ├── prd/                        ← all profiles (lighter in Agile)
│   │   └── prd-v1.0.md
│   ├── srs/                        ← Waterfall only (versioned, sign-off)
│   │   └── srs-v1.0.md
│   ├── sdd/                        ← Agile only (living)
│   │   └── system-description.md
│   ├── adrs/                       ← Agile only
│   │   └── ADR-001-[decision-name].md
│   ├── change-requests/
│   │   └── CR-001-[feature-name].md
│   ├── sprint-reviews/             ← Agile only
│   │   └── sprint-review-YYYY-MM-DD.md
│   ├── release-notes/
│   │   └── release-notes-vX.Y.md
│   ├── uat-sign-offs/
│   │   └── uat-sign-off-YYYY-MM-DD.md
│   └── handover/                   ← project / engagement closeout
│       └── handover-YYYY-MM-DD.md
│
├── business-requirements/          ← internal BRs — Waterfall only
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
│   ├── raid-log/
│   │   └── raid-log-template.md
│   ├── stakeholder-register/
│   │   └── stakeholder-register-template.md
│   ├── project-charter/
│   │   └── project-charter-template.md
│   ├── vision/
│   │   └── product-vision-template.md
│   ├── roadmap/
│   │   └── product-roadmap-template.md
│   ├── personas/
│   │   └── personas-template.md
│   ├── journey-maps/
│   │   └── journey-maps-template.md
│   ├── prd/
│   │   └── prd-client-template.md
│   ├── srs/
│   │   └── srs-template.md
│   ├── sdd/
│   │   └── sdd-template.md
│   ├── adr/
│   │   └── adr-template.md
│   ├── sprint-review/
│   │   └── sprint-review-template.md
│   ├── release-notes/
│   │   └── release-notes-template.md
│   ├── uat-sign-off/
│   │   └── uat-sign-off-template.md
│   └── handover/
│       └── handover-template.md
│
├── reference/                      ← raw input materials from Sales handoff (not client-facing, not BMad)
│   └── [sales-notes, transcriptions, client-provided docs]
├── deep-dives/                     ← technical deep-dives per module
├── analysis/                       ← brainstorming and analysis sessions
└── .archive/                       ← superseded versions of versioned documents
```

> **Don't create empty folders for artifacts that don't apply to your methodology.** A Waterfall project shouldn't have `vision/`, `roadmap/`, `sdd/`, `adrs/`, `personas/`, `journey-maps/`, or `sprint-reviews/`. An Agile project shouldn't have `srs/` (use `sdd/` instead) or the top-level `business-requirements/` folder (CRs carry that content in Agile).

---

### Multi-Project

Use this structure when two or more products share a codebase. Documents shared across all products (Glossary, RAID Log, Stakeholder Register) live in `docs/client/shared/`. Each product has its own subfolder with its own per-product documents.

```
docs/
├── documentation-guide.md          ← this file (master reference)
│
├── client/                         ← all client-facing documentation
│   ├── shared/                     ← shared across all products
│   │   ├── glossary.md
│   │   ├── raid-log.md
│   │   ├── stakeholder-register.md
│   │   └── meetings/               ← Kickoff Questionnaires + Meeting Agendas (engagement-wide; lifecycle-renamed post-call)
│   │       ├── kickoff-questionnaire-YYYY-MM-DD.md
│   │       └── meeting-YYYY-MM-DD.md
│   │
│   ├── project-1/                  ← Product 1 (per-product, methodology-driven)
│   │   ├── charter/
│   │   ├── vision/                 ← Agile only
│   │   ├── roadmap/                ← Agile only
│   │   ├── personas/               ← Agile only
│   │   ├── journey-maps/           ← Agile only
│   │   ├── prd/
│   │   ├── srs/                    ← Waterfall only
│   │   ├── sdd/                    ← Agile only
│   │   ├── adrs/                   ← Agile only
│   │   ├── change-requests/
│   │   ├── sprint-reviews/         ← Agile only
│   │   ├── release-notes/
│   │   ├── uat-sign-offs/
│   │   └── handover/
│   │
│   └── project-2/                  ← Product 2 (same structure as project-1)
│       └── ...
│
├── business-requirements/          ← Waterfall only
│   └── business-requirement-YYYY-MM-DD.md
│
├── features/                       ← BMad feature specs, one folder per feature area
│   ├── project-1/
│   └── project-2/
│
├── templates/                      ← (same as Single Project)
│
├── reference/
├── deep-dives/
├── analysis/
└── .archive/
```

> Different products in the same codebase **may use different methodologies**. Project-1 could be Agile Capacity-Based while project-2 is Waterfall. The per-product folder contents reflect each project's methodology choice.

---

## Document Sets by Methodology

The three profiles share a common foundation (Charter, Stakeholder Register, Glossary, RAID Log, CRs, Feature Specs) and diverge from there. The table below shows the full document set per profile, followed by per-profile narrative.

### Master Document Map

| Document | Waterfall | Agile — Fixed-Range | Agile — Capacity-Based |
|---|---|---|---|
| Project Charter | ✅ | ✅ | ✅ |
| Stakeholder Register | ✅ | ✅ | ✅ |
| Glossary | ✅ | ✅ | ✅ |
| RAID Log | ✅ | ✅ | ✅ |
| Kickoff Questionnaire (template) | ✅ | ✅ | ✅ |
| Meeting Agenda (template) | ✅ | ✅ | ✅ |
| Product Vision Statement | — | ✅ | ✅ |
| Product Roadmap (Now/Next/Later) | — | ✅ | ✅ |
| Personas | optional | ✅ | ✅ |
| Journey Maps | optional | ✅ | ✅ |
| Client PRD | ✅ | ✅ (lighter) | ✅ (lighter) |
| **SRS** (versioned, sign-off) | ✅ | — | — |
| **SDD** (System Description Document, living) | — | ✅ | ✅ |
| ADRs (Architecture Decision Records) | — | ✅ | ✅ |
| Change Request (CR) | ✅ frequent | ✅ frequent | ✅ rare |
| Business Requirement (BR) | ✅ | — | — |
| Feature Spec | ✅ | ✅ | ✅ |
| Sprint Review notes | — | ✅ | ✅ |
| Release Notes (client-facing) | ✅ | ✅ per phase | ✅ cadence-based |
| UAT Sign-off Sheet | ✅ | ✅ per phase | ✅ per release |
| Handover / KT Document | ✅ | ✅ project end | ✅ engagement end |

> ✅ = produced for this profile. — = not used. *optional* = produce only if the project specifically benefits from it.

---

### Waterfall — Document Set

Used when the project is fixed-scope and contractually baselined. Heavy upfront documentation, formal sign-off gates.

**Distinctive artifacts:**
- **SRS** is the authoritative requirements doc — versioned, client-signed, archived. CRs feed into SRS at release time.
- **BR** bridges client-facing CR and dev-facing stories. Loaded into BMad as story context.
- **PRD** is the product-vision-and-goals doc; SRS is the detailed requirements doc.

**What's absent:** Vision, Roadmap, ADRs, SDD, Personas, Journey Maps, Sprint Reviews. These are Agile-native and don't fit the baseline-and-build model.

**CR rhythm:** Frequent and formal — every deviation from the baselined SRS goes through a CR. CR is the gate between client request and BR creation.

---

### Agile — Fixed-Range — Document Set

Used when the client provides scope + estimate range (e.g., $35K–$42K). Scope flexes within range; trade-offs are frequent.

**Distinctive artifacts:**
- **Product Vision** + **Product Roadmap (Now/Next/Later)** anchor the strategic direction.
- **SDD** replaces SRS as a living "as it exists today" doc — no version baseline, no formal sign-off ceremony. Updated continuously as features ship.
- **ADRs** capture significant technical decisions inline as they happen.
- **CRs are frequent** — every scope event (addition, expansion, trade-off) generates a CR. Trade-off CRs use a single template with toggleable "Added" and "Removed" sections.
- **CR carries business rules and edge cases** (the content that BR carried in Waterfall). BMad workflows that previously loaded BR now load CR as story context.
- **Per phase**: each phase ends with Release Notes + UAT Sign-off. Each new phase resets the baseline (mini-Charter update + new Roadmap).

**What's absent:** SRS, BR. The Vision + Roadmap + CRs + Stories combination replaces them.

**CR rhythm:** Frequent. Triggered by:
- Scope addition that pushes outside the estimate range
- Trade-off decision (cut feature A for feature B)
- Discovery findings during elaboration that exceed the initial estimate

---

### Agile — Capacity-Based — Document Set

Used for long-running engagements with monthly development cap (e.g., $25K–$50K/month). Backlog absorbs most change; CRs reserved for Roadmap-level events.

**Distinctive artifacts:**
- Same artifact list as Fixed-Range, but **CRs are rare** — only triggered by changes to the Roadmap.
- **Roadmap is the centre of gravity** — monthly client review, drives prioritisation conversations.
- **Sprint Review notes** become the primary client-facing artifact between releases.
- **Release Notes cadence** is engagement-defined (e.g., monthly, per-feature-batch) rather than per-phase.

**What's absent:** Same as Fixed-Range. Plus, CR overhead is minimised — most "changes" are backlog grooming, not formal CRs.

**CR rhythm:** Rare. Reserved for:
- New strategic direction (new module, new ecosystem)
- Major integrations (a multi-month chunk of work)
- Direction reversals (sunsetting a module)
- Capacity changes (changing monthly cap)

Not CRs in this profile:
- New stories or epics within an existing Roadmap initiative
- Tweaking priorities month-to-month
- Adding/removing items from next sprint
- Refining acceptance criteria mid-flight

> The general rule: **CRs change the Roadmap. Backlog items realise the Roadmap.**

---

## Combined Project Workflow

This section shows how the BMad workflow and the client-facing layer fit together across the full project lifecycle. Every step is labelled with the BMad workflow or agent that drives it, and the client-facing document it produces or requires.

**Legend:** ✅ Client sign-off required | 📋 BMad workflow | 👤 Agent | 📄 Document produced | 📝 Notation / regeneration step

> **Client-facing-first principle.** Where a client-facing document and an internal/BMad document overlap in content, the client-facing one is authored first and signed off; the internal one is then derived from it. This avoids the rework loop when the client requests changes.
>
> **All BMad docs are kept regardless** — BMad agents need their native document structures as grounded context to avoid hallucinations during downstream workflows. The order changes; the inventory doesn't.

---

### Epics & Stories — when each workflow runs

Two distinct BMad workflows produce stories. Knowing which one applies when avoids confusion across the phase tables.

| Workflow | Purpose | Trigger |
|---|---|---|
| **Create Epics & Stories** (BMad SM) | Bulk — generate a structured set of epics + stories from a body of source material | Once per scope commitment (initial scope; new phase) |
| **Create Story** (BMad SM) | Single — draft one story file with full implementation context | Every time a new feature joins the active backlog |

**Roadmap initiative → Epic → Story lifecycle (Agile):**

```
Roadmap initiative in "Later"   (strategic only — no story detail)
        ↓  (priorities firm up)
"Next"                          (sized roughly, refined acceptance shape)
        ↓  (promoted, about to start)
"Now" → Epic in Jira → decompose into Stories → sprint
```

The conversion point is **promotion to "Now"** — story-level detail is created here, not earlier. Items in "Later" stay as initiative-level placeholders. This is what keeps the Roadmap a sustainable artifact across long engagements.

**When bulk *Create Epics & Stories* runs (and what it covers):**

| Profile | Trigger | Coverage |
|---|---|---|
| Waterfall | After SRS sign-off | Full project scope upfront |
| Agile — Fixed-Range | After Vision + Roadmap agreed | Now + Next initiatives (Later stays as initiative-level only) |
| Agile — Capacity-Based | After Vision + Roadmap agreed | Now initiatives only (Next + Later stay as initiative-level) |

**When *Create Story* runs (per individual feature):**

| Trigger | Profile applicability |
|---|---|
| CR approved → start now | All profiles |
| Initiative promoted from Next → Now | Agile (both) |
| New story discovered during Sprint Planning | Agile (both) — gap-fill |

> **Sprint Planning never *creates* stories.** It pulls existing stories from the backlog into a sprint. If a sprint-planning session reveals a missing story, that's a Create Story trigger before the sprint can commit.

The general pattern: *Create Epics & Stories* runs at moments of bulk scope commitment (project start, new phase). *Create Story* runs every time a single feature needs implementation detail. **Releases are demonstration + acceptance events, not story-creation events.**

---

### Phase 1 — Project Setup (once per project)

#### Common steps (all profiles)

These steps run regardless of methodology, before the profile-specific path begins. (Project Type, Tooling, and Methodology are set at kickoff — see [Kickoff Configuration](#kickoff-configuration).)

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 1 | 👤 BA — collect and review pre-kickoff materials | BA receives materials from Sales (notes, transcriptions e.g. Fireflies, client-provided documents) and places them in `docs/reference/`. For brownfield, BA also places existing specs, legacy docs, and prior work here. | — |
| 2 | 👤 BA — Kickoff session | 📄 **Project Charter**, **Stakeholder Register**, **Glossary**, **RAID Log** | — |
| 2a | 👤 BA — Confluence sync *(if Jira + Confluence project)* | Ask user: sync kickoff documents to Confluence? Create/update pages for Charter, Stakeholder Register, Glossary, RAID Log. | — |
| 3 | 📋 Research — market / domain / technical *(optional)* | — internal only — | — |
| 4 | 📋 Lightweight Brainstorming *(optional)* | — internal only — | — |
| 5 | 👤 BA — refine Charter, submit for sign-off | Incorporate findings from Research / Brainstorming (new constraints, scope clarifications, risks). 📄 **Project Charter** | ✅ Yes |
| 5a | 👤 BA — Confluence sync *(if Jira + Confluence project)* | Ask user: sync updated Charter to Confluence? | — |
| 5b | 👤 BA — confirm client approval | Ask user: "Has the client approved the Charter?" Do not proceed until confirmed. Approval mechanism is up to the user (Confluence, email, DocuSign, verbal). | ✅ Yes |

> After step 5b, the workflow branches per [Methodology (0c)](#0c--methodology). Use the table below that matches the project's profile.

---

#### Profile A — Waterfall (greenfield)

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 6 | 📋 Create Product Brief (Mary) | — internal: uses Charter + kickoff artifacts as input — | — |
| 7 | 👤 BA — draft Client PRD *(informed by Charter, kickoff, and optionally BMad elicitation as a tool)* | 📄 **Client PRD** | — |
| 8 | 👤 BA — review with client, iterate, submit for sign-off | 📄 **Client PRD** | ✅ Yes |
| 9 | 📋 Create PRD (BMad PM) — generated *from* approved Client PRD | — internal: BMad PRD as agent-grounding artifact — | — |
| 10 | 📋 Create UX Design (BMad UX) | UX review with client *(informal)* | Optional |
| 11 | 📋 Create Architecture (BMad Architect) | — internal only — | — |
| 12 | 👤 BA *(manual; Sarah workflow planned)* | 📄 **SRS** *(from Client PRD + UX + Architecture)* | ✅ Yes |
| 13 | 📋 Create Epics & Stories (BMad SM) — **bulk: full project scope from SRS** | — internal — | — |
| 14 | 📋 Check Implementation Readiness | — internal gate — | — |

> **Note:** SRS creation workflow is planned for Sarah (BA agent) — not yet built.

#### Profile A — Waterfall (brownfield)

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 6 | 📋 Document Project (Mary) | — internal: feature specs, deep-dives from existing system — | — |
| 7 | 👤 BA *(manual)* | 📄 **SRS** *(create from existing knowledge if missing, or validate existing)* | ✅ Yes |
| 8 | Continue from Create Architecture onwards | same as greenfield steps 11–14 | — |

---

#### Profile B — Agile Fixed-Range / Capacity-Based (greenfield)

> Both Agile profiles follow the same setup path. They diverge in [Phase 2 (CR rhythm)](#phase-2--per-feature-recurring) and [Phase 4 (release cadence)](#phase-4--per-release-recurring).

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 6 | 📋 Create Product Brief (Mary) | — internal: uses Charter + kickoff artifacts as input — | — |
| 7 | 👤 BA — draft Product Vision | 📄 **Product Vision Statement** *(one-page; the project's North Star — why, who, what problem)* | — |
| 8 | 👤 BA — draft Personas + Journey Maps *(if useful for the project)* | 📄 **Personas**, **Journey Maps** | Optional |
| 9 | 👤 BA — draft Product Roadmap (Now / Next / Later) | 📄 **Product Roadmap** *(themes → initiatives, no individual stories)* | — |
| 10 | 👤 BA — review Vision + Roadmap with client, iterate, agree | Living agreement — no formal baseline sign-off | Light agreement |
| 11 | 👤 BA — draft Client PRD *(optional — produce when the project benefits from a single integrated business doc; for many Agile projects, Vision + Roadmap suffice)* | 📄 **Client PRD** *(lighter than Waterfall)* | ✅ If produced |
| 12 | 📋 Create PRD (BMad PM) — generated *from* approved Vision + Roadmap (+ Client PRD if present) | — internal: BMad PRD as agent-grounding artifact — | — |
| 13 | 📋 Create UX Design (BMad UX) | UX review with client *(iterative)* | Optional |
| 14 | 📋 Create Architecture (BMad Architect) | — internal only — | — |
| 15 | 📝 Create initial ADRs *(as significant decisions emerge)* | 📄 **ADR-001…N** | — |
| 16 | 👤 BA — initialise SDD | 📄 **SDD** *(System Description Document — living, no version baseline; starts as a stub for greenfield)* | — |
| 17 | 📋 Create Epics & Stories (BMad SM) — **bulk: epics for Now/Next initiatives (Fixed-Range) or Now only (Capacity-Based); stories detailed for Now bucket** | — internal: stories sit in Jira backlog — | — |
| 18 | 📋 Check Implementation Readiness | — internal gate — | — |

#### Profile B — Agile (brownfield)

| Step | BMad Workflow / Agent | Client-Facing Document | Sign-off |
|---|---|---|---|
| 6 | 📋 Document Project (Mary) | — internal: feature specs, deep-dives from existing system — | — |
| 7 | 👤 BA — Vision + Roadmap *(create if missing, otherwise validate existing)* | 📄 **Vision**, **Roadmap** | Light agreement |
| 8 | 👤 BA — initialise SDD from existing system | 📄 **SDD** *(snapshot of current system, then becomes living)* | — |
| 9 | Continue from BMad PRD onwards | same as greenfield steps 12+ | — |

---

### Phase 2 — Per Feature (recurring, every feature)

The CR rhythm differs per profile. See [Document Sets by Methodology](#document-sets-by-methodology) for the threshold detail.

> **Story creation timing in Agile.** *Create Story* may run immediately after CR approval (start now), or be deferred until the related initiative is promoted from Next → Now on the Roadmap (start later). The CR is the contract; the story is the implementation slice. See [Epics & Stories — when each workflow runs](#epics--stories--when-each-workflow-runs).

#### Waterfall

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Lightweight Brainstorming *(optional)* | — internal only — | — |
| 2 | 👤 Sarah — Create CR | 📄 **Change Request (CR)** | ✅ **Yes — hard gate. BR cannot start without this.** |
| 3 | 👤 Sarah — Create BR | 📄 **Business Requirement (BR)** *(loaded into BMad as story context)* | — |
| 4 | 📋 Create Story (BMad SM) | — story spec, internal — | — |
| 5 | 📋 Dev Story (BMad Dev) | — implementation — | — |
| 6 | 📋 Code Review | — internal — | — |

#### Agile — Fixed-Range

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Lightweight Brainstorming *(optional)* | — internal only — | — |
| 2 | 👤 Sarah — Create CR *(includes Business Rules & Edge Cases section — replaces BR; trade-off CRs use the "Added" / "Removed" sections)* | 📄 **Change Request (CR)** *(carries the business rules, edge cases, regulatory considerations that BR carried in Waterfall; loaded into BMad as story context)* | ✅ **Yes — hard gate.** |
| 3 | 📝 Create / update ADR *(if a non-trivial technical decision arises)* | 📄 **ADR-XXX** | — |
| 4 | 📋 Create Story (BMad SM) *(uses CR as primary context)* | — story spec, internal — | — |
| 5 | 📋 Dev Story (BMad Dev) | — implementation — | — |
| 6 | 📋 Code Review | — internal — | — |
| 7 | 👤 BA — update SDD *(once feature ships)* | 📄 **SDD** updated | — |

#### Agile — Capacity-Based

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| — | **Decide first: is this a CR or a backlog item?** A change to the Roadmap → CR. A realisation of an existing Roadmap initiative → backlog item, no CR. | — | — |
| 1 | 📋 Lightweight Brainstorming *(optional)* | — internal only — | — |
| 2 | 👤 Sarah — Create CR *(only if Roadmap-level change)* | 📄 **Change Request (CR)** *(carries business rules + edge cases)* | ✅ **Yes — when CR applies.** |
| 3 | 👤 BA — add to Roadmap *(if accepted CR introduces a new initiative)* | 📄 **Roadmap** updated | — |
| 4 | 📝 Create / update ADR *(if a non-trivial technical decision arises)* | 📄 **ADR-XXX** | — |
| 5 | 📋 Create Story (BMad SM) *(uses CR or Roadmap initiative as context)* | — story spec, internal — | — |
| 6 | 📋 Dev Story (BMad Dev) | — implementation — | — |
| 7 | 📋 Code Review | — internal — | — |
| 8 | 👤 BA — update SDD *(once feature ships)* | 📄 **SDD** updated | — |

> **Quick Spec / Quick Dev exception** — see [Quick Spec Policy](#quick-spec-policy) below.

---

### Phase 3 — Per Sprint (Agile only)

> Waterfall projects do not have a per-sprint cadence — work is organised by phase, not sprint. Skip this phase for Waterfall.

#### Agile — both profiles

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Sprint Planning (BMad SM) | — internal: sprint goal + committed backlog — | — |
| 2 | 📋 Sprint Status (BMad SM) | Mid-sprint status update to client *(informal channel)* | — |
| 3 | 👤 BA — Sprint Review notes *(end-of-sprint demo and feedback)* | 📄 **Sprint Review notes** *(what was demoed, client feedback, action items)* | — |
| 4 | 📋 Correct Course *(if needed)* | May trigger a new 📄 **CR** | ✅ If scope changes |
| 5 | 📋 Retrospective (BMad SM) | — internal only — | — |

> **Sprint Review notes weight differs by profile.** Fixed-Range projects keep them lightweight (the phase-end UAT is the heavier artifact). Capacity-Based projects make Sprint Review notes the primary client-facing artifact between releases.

---

### Phase 4 — Per Release (recurring)

#### Waterfall

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Feature Spec Creation (BMad Tech Writer) | — internal feature specs — | — |
| 2 | 📋 Documentation Update / Deep Dive Creation | — internal — | — |
| 3 | 👤 BA *(manual)* | 📄 **SRS** updated *(CRs absorbed, version bumped)* | ✅ Yes |
| 4 | 👤 BA *(manual)* | 📄 **Client PRD** updated *(only if product goals changed)* | ✅ Major changes only |
| 5 | 📝 Regenerate BMad PRD if Client PRD changed | — internal: agent-grounding artifact refresh — | — |
| 6 | 👤 BA — publish Release Notes | 📄 **Release Notes** | — |
| 7 | 👤 BA — collect UAT sign-off | 📄 **UAT Sign-off Sheet** | ✅ Yes |
| — | Git tag release docs, archive superseded SRS | — | — |

#### Agile — Fixed-Range (per phase)

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Feature Spec Creation (BMad Tech Writer) | — internal feature specs — | — |
| 2 | 📋 Documentation Update / Deep Dive Creation | — internal — | — |
| 3 | 👤 BA — confirm SDD reflects all shipped features | 📄 **SDD** *(continuous updates verified)* | — |
| 4 | 👤 BA — update Vision / Roadmap if direction shifted | 📄 **Vision**, **Roadmap** | Light agreement |
| 5 | 📝 Regenerate BMad PRD if Vision / Client PRD changed materially | — internal: agent-grounding artifact refresh — | — |
| 6 | 👤 BA — publish Release Notes for the phase | 📄 **Release Notes** *(phase summary, demo highlights, accepted CRs)* | — |
| 7 | 👤 BA — collect UAT sign-off for the phase | 📄 **UAT Sign-off Sheet** | ✅ Yes |
| — | Git tag release docs | — | — |

#### Agile — Capacity-Based (cadence-based)

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 📋 Feature Spec Creation (BMad Tech Writer) | — internal feature specs — | — |
| 2 | 📋 Documentation Update / Deep Dive Creation | — internal — | — |
| 3 | 👤 BA — confirm SDD reflects shipped features | 📄 **SDD** *(continuous updates verified)* | — |
| 4 | 👤 BA — refresh Roadmap *(move initiatives between Now / Next / Later)* | 📄 **Roadmap** updated | Light agreement |
| 5 | 📝 Regenerate BMad PRD if Vision / Roadmap changed materially | — internal: agent-grounding artifact refresh — | — |
| 6 | 👤 BA — publish Release Notes | 📄 **Release Notes** *(release-batch summary)* | — |
| 7 | 👤 BA — collect UAT sign-off | 📄 **UAT Sign-off Sheet** | ✅ Yes |
| — | Git tag release docs | — | — |

---

### Phase 5 — Project Closeout (once, at end of project or engagement)

Applies to all profiles. For Capacity-Based engagements, "closeout" means engagement end or major handover (team change, contract end, scope-down).

| Step | BMad Workflow / Agent | Document | Sign-off |
|---|---|---|---|
| 1 | 👤 BA — final Release Notes covering the closeout scope | 📄 **Release Notes** | — |
| 2 | 👤 BA — final UAT sign-off | 📄 **UAT Sign-off Sheet** | ✅ Yes |
| 3 | 👤 BA *(with PM and tech lead input)* — produce Handover / Knowledge Transfer document | 📄 **Handover / KT Document** *(operational guide: deployment, accounts, monitoring, support contacts, known issues, runbook pointers)* | ✅ Yes — client confirmation that handover is complete |
| 4 | 👤 BA — archive superseded versioned docs to `.archive/` | — internal — | — |
| 5 | 📋 Final Retrospective *(Agile only)* | — internal — | — |

---

## Quick Spec Policy

Quick Spec / Quick Dev bypasses the CR client sign-off gate (and, in Waterfall, the CR → BR sequence). This is acceptable **only** when at least one of the following conditions is met:

1. **Bug fix** — the change restores behaviour already defined in the authoritative requirements doc:
   - **Waterfall** → the **SRS**
   - **Agile** → the **SDD** (System Description Document) — the "as it exists today" reference
   - The behaviour must be something agreed and broken, not something new.
2. **Internal / technical change only** — purely internal with zero client-visible impact (refactors, infrastructure, internal tooling, performance improvements with no behaviour change). Significant decisions of this kind should still be captured as an **ADR** in Agile profiles.

**Everything else requires a CR** — any new behaviour, any change to existing behaviour, and anything visible to the client or end user in any form.

> If in doubt, create a CR. The cost of a CR is low; the cost of implementing something the client never approved is high.

---

## Agents & Workflow Reference

### Agents

| Agent | Persona | When to Use |
|---|---|---|
| **Sarah** — Easyterms BA | Business Analyst specialising in Easyterms platform | Create CRs (all profiles — in Agile, the CR carries Business Rules & Edge Cases). Create BRs (**Waterfall only**). Brainstorm features, review platform context, audit business rules. Primary agent for the BA workflow. |
| **Mary** — BMad Analyst | Strategic Business Analyst | Market research, domain research, technical research, create product briefs, document existing projects. |
| **BMad PM** | Product Manager | Create / regenerate the BMad PRD **from approved Client PRD (Waterfall) or Vision + Roadmap (Agile)** as agent-grounding artifact. Sprint planning, sprint status, retrospectives, correct course. |
| **BMad Architect** | Solution Architect | Create architecture documents, solution design decisions. |
| **BMad Dev** | Developer | Implement stories via Dev Story workflow. |
| **BMad Tech Writer** | Technical Writer | Create and update feature specs, deep-dives, documentation updates. |
| **BMad QA** | QA Engineer | Generate E2E tests, test design. *(QA agent workflow — to be integrated later.)* |

### Key Workflows

| Workflow | Agent | Phase | Output | Profile |
|---|---|---|---|---|
| Lightweight Brainstorming | Sarah | Per Feature *(optional)* | Brainstorming report | All |
| Create Product Brief | Mary | Project Setup | Product brief → feeds Project Charter | All |
| Document Project | Mary | Brownfield Setup | Feature specs, deep-dives | All |
| Create PRD | BMad PM | Project Setup *(after Client PRD / Vision+Roadmap signed off)* | BMad PRD as agent-grounding artifact | All |
| Create UX Design | BMad UX Designer | Project Setup | UX design spec | All |
| Create Architecture | BMad Architect | Project Setup | Architecture document | All |
| Create Epics & Stories | BMad SM | Project Setup *(bulk: full scope for Waterfall; Now/Next for Fixed-Range; Now for Capacity-Based)* | Epics and stories list | All |
| Check Implementation Readiness | BMad PM | Project Setup | Readiness report | All |
| Create Story | BMad SM | Per Feature *(triggered post-CR or on Next→Now promotion)* | Story spec | All |
| Dev Story | BMad Dev | Per Feature | Implementation | All |
| Code Review | BMad Dev | Per Feature | Review report | All |
| Sprint Planning | BMad SM | Per Sprint | Sprint plan | Agile |
| Sprint Status | BMad SM | Per Sprint | Status report | Agile |
| Correct Course | BMad SM | Per Sprint | Change proposal | Agile |
| Retrospective | BMad SM | Per Sprint | Retrospective report | Agile |
| Feature Spec Creation | BMad Tech Writer | Per Release | Feature spec (13 sections) | All |
| Documentation Update | BMad Tech Writer | Per Release | Updated feature docs | All |
| Deep Dive Creation | BMad Tech Writer | Per Release | Technical deep-dive | All |
| Quick Spec / Quick Dev | Any | Bug fix / internal only | Quick tech spec + implementation | All |
| Create CR | Sarah | Per Feature | CR document *(carries Business Rules & Edge Cases in Agile)* | All |
| Create BR | Sarah | Per Feature | BR document | **Waterfall only** |
| **Create SRS** | **Sarah** *(planned)* | **Project Setup + Per Release** | **SRS document** | **Waterfall only** |
| **Create Vision** | **BA** *(manual; agent planned)* | **Project Setup** | **Product Vision Statement** | **Agile** |
| **Create Roadmap** | **BA** *(manual; agent planned)* | **Project Setup + ongoing** | **Product Roadmap (Now/Next/Later)** | **Agile** |
| **Create / Update Personas** | **BA** *(manual)* | **Project Setup *(optional)* / ongoing** | **Personas** | **Agile** |
| **Create / Update Journey Maps** | **BA** *(manual)* | **Project Setup *(optional)* / ongoing** | **Journey Maps** | **Agile** |
| **Initialise / Update SDD** | **BA** *(manual; agent planned)* | **Project Setup + Per Feature + Per Release** | **SDD (living)** | **Agile** |
| **Create ADR** | **BA / Tech Lead** *(manual)* | **Per Feature *(when significant decision)*** | **ADR-XXX** | **Agile** |
| **RAID Log maintenance** | **BA** *(ongoing)* | **All phases** | **RAID Log updates** | **All** |
| **Sprint Review notes** | **BA** *(manual)* | **Per Sprint** | **Sprint Review notes** | **Agile** |
| **Release Notes** | **BA** *(manual; agent planned)* | **Per Release + Closeout** | **Release Notes** | **All** |
| **UAT Sign-off** | **BA** *(manual)* | **Per Release + Closeout** | **UAT Sign-off Sheet** | **All** |
| **Handover / KT** | **BA + PM + Tech Lead** *(manual)* | **Project Closeout** | **Handover / KT Document** | **All** |
| **Meeting Prep** | **Sarah** *(planned — not yet built)* | **Ongoing** | **Client meeting agenda** | **All** |

---

## Document Reference

> Each entry below describes a single artifact: its purpose, audience, owner, update frequency, and methodology applicability. The complete cross-profile artifact map is in [Document Sets by Methodology](#document-sets-by-methodology).

### Client Communication (`docs/templates/client-communication/`)

> **Output location for completed Client-Communication artefacts.** Templates live in `docs/templates/client-communication/`. *Filled-in* questionnaires and agendas live in **`docs/client/meetings/`** for single-project setups, or **`docs/client/shared/meetings/`** for multi-project setups.
>
> **Lifecycle naming convention.** A single file evolves through its lifecycle rather than two files being maintained in parallel:
> - Pre-call: `kickoff-questionnaire-YYYY-MM-DD.md` (the questions to ask). Post-call: rename to `kickoff-meeting-YYYY-MM-DD.md` (the same file, with answers in place).
> - Pre-call: `meeting-agenda-YYYY-MM-DD.md` (the agenda). Post-call: rename to `meeting-notes-YYYY-MM-DD.md` (the same file, with discussion + decisions filled in). A combined neutral form `meeting-YYYY-MM-DD.md` is also acceptable when the same file always carries both.
>
> The rename signals the lifecycle stage; the YYYY-MM-DD date stays stable so a meeting's pre- and post-call forms link to the same identifier.

#### Kickoff Questionnaire (`kickoff-questionnaire-template.md`)
- **Purpose:** Structured set of questions for the BA to ask at project kickoff or client onboarding. Covers business context, stakeholders, domain and regulatory requirements, integrations, scope, existing documentation, communication preferences, and UAT. Answers feed directly into the Glossary, RAID Log, Stakeholder Register, and Project Charter.
- **When to use:** At the start of every new project or when onboarding a new client.
- **Owner:** BA
- **Profiles:** All
- **Output feeds:** Glossary, RAID Log, Stakeholder Register, Project Charter
- **Output location:** `docs/client/meetings/kickoff-questionnaire-YYYY-MM-DD.md` (single-project) or `docs/client/shared/meetings/…` (multi-project). Renamed to `kickoff-meeting-YYYY-MM-DD.md` once the call is complete and answers are filled in.

#### Meeting Agenda (`meeting-agenda-template.md`)
- **Purpose:** Standard structure for recurring client calls. Covers previous action items, dev status, open CRs, open questions, open RAID items needing confirmation, upcoming milestones, new client requests, decisions log, and action items. The Decisions Made section is designed to be emailed to the client after every call as the written record.
- **When to use:** Prepare before every scheduled client call.
- **Owner:** BA
- **Profiles:** All
- **Output feeds:** Open CRs updated, RAID Log updated, follow-up email to client
- **Output location:** `docs/client/meetings/meeting-agenda-YYYY-MM-DD.md` (single-project) or `docs/client/shared/meetings/…` (multi-project). Renamed to `meeting-notes-YYYY-MM-DD.md` after the call (or use the combined form `meeting-YYYY-MM-DD.md` from the start).

---

### Client-Facing — Shared (`docs/client/shared/`) — Multi-Project Only

> This section applies only to **multi-project** setups. For single-project setups, the Glossary, RAID Log, and Stakeholder Register live directly in `docs/client/` alongside all other client-facing documents.

#### Glossary (`glossary.md`)
- **Purpose:** Single source of truth for domain terminology. All project documents must use terms exactly as defined here.
- **Audience:** Everyone — client, BA, developers, QA.
- **Update frequency:** Living document. Add new terms as they emerge during requirements work or development. Never delete terms — mark as deprecated if no longer in use.
- **Owner:** BA
- **Profiles:** All

#### RAID Log (`raid-log.md`)
- **Purpose:** Records **R**isks, **A**ssumptions, **I**ssues, and **D**ependencies. Each entry has a status (Open / Confirmed / Mitigated / Invalidated / Closed) and is tagged by category and (if multi-project) by product.
- **Audience:** BA, PM, client for review.
- **Update frequency:** Living document. Started at kickoff (Phase 1, step 2) and continuously updated. Never delete entries — update status in place.
- **Owner:** BA (assumptions, risks, issues), PM (delivery dependencies)
- **Profiles:** All
- **Note:** Replaces the older "Assumptions & Constraints Log" — the broader RAID structure better fits both methodologies. When in doubt, log it; an over-rich RAID is cheap, an unrecorded risk is expensive.

#### Stakeholder Register (`stakeholder-register.md`)
- **Purpose:** Single register covering all stakeholders across all products — delivery team, client contacts, end user groups, and external systems. Structured with shared people in sections 1–3 and a per-product RACI subsection for each product. Keeping it shared avoids duplicating stakeholder entries and ensures there is one place to update when roles or contacts change.
- **Audience:** PM, BA, client.
- **Update frequency:** Living document. Update when team members change, new stakeholders are identified, or roles shift.
- **Owner:** PM
- **Profiles:** All

---

### Client-Facing — Per Product

#### Project Charter (`charter/project-charter-v1.0.md`)
- **Purpose:** Defines the project's scope, objectives, constraints, high-level milestones, and key stakeholders. The foundational agreement between client and development partner.
- **Audience:** Client, PM, BA.
- **Versioning:** Major version bump when scope changes significantly. Minor version for corrections or additions that don't alter scope boundaries.
- **Update frequency:** Infrequently — typically only at project initiation or during a significant scope change.
- **Owner:** PM (with BA input)
- **Profiles:** All
- **Client sign-off required:** Yes

#### Stakeholder Register (`stakeholder-register.md`) — Single Project Only
- **Purpose:** Full list of all stakeholders — client contacts, delivery team, end user groups, and external systems. Includes roles, responsibilities, and RACI matrix. Lives in `docs/client/` for single-project setups. For multi-project setups, see the shared version above.
- **Audience:** PM, BA, client.
- **Update frequency:** Living document. Update when team members change, new stakeholders are identified, or roles shift.
- **Owner:** PM
- **Profiles:** All

#### Product Vision Statement (`vision/product-vision.md`) — Agile only
- **Purpose:** One-page document capturing why the product exists, who it is for, and what problem it solves. The North Star for prioritisation conversations and the strategic anchor against which Roadmap initiatives are weighed.
- **Audience:** Client, BA, PM, delivery team.
- **Versioning:** Single living document. Date the last revision in a header; no `v1.0` archive ceremony.
- **Update frequency:** Updated at major direction changes (new market, new persona, big pivot). Otherwise stable.
- **Owner:** BA
- **Profiles:** Agile (Fixed-Range, Capacity-Based)
- **Client sign-off required:** Light agreement at creation; revisited at major direction changes.

#### Product Roadmap (`roadmap/product-roadmap.md`) — Agile only
- **Purpose:** Strategic, directional view of where the product is going over time. Themes → Initiatives, organised into **Now / Next / Later** buckets. The CR baseline — changes to the Roadmap trigger CRs; realisations of existing initiatives do not.
- **Audience:** Client, BA, PM, Tech Lead.
- **Granularity:** Themes (broad strategic areas) → Initiatives / Epics (chunks of work). Stories stay in the backlog and do **not** appear on the Roadmap.
- **Versioning:** Single living document. Maintain a change-log section at the bottom (when initiatives moved between buckets, when CRs added new ones).
- **Update frequency:** Reviewed monthly with the client. Updated whenever an approved CR introduces a new initiative or shifts an existing one between buckets.
- **Owner:** BA (drafts and maintains); Client validates ordering; PM/Tech Lead reviews capacity feasibility.
- **Profiles:** Agile (Fixed-Range, Capacity-Based)
- **Client sign-off required:** Light agreement, ongoing — no formal baseline sign-off.

#### Personas (`personas/personas.md`) — Agile (recommended); optional in Waterfall
- **Purpose:** Profiles of the actual users of the product. Grounds story writing in real user contexts rather than abstract "the user" assumptions. Each persona captures role, goals, pain points, and key behaviours.
- **Audience:** BA, UX Designer, Dev (via BMad context), client (for validation).
- **Update frequency:** Created at project start (or first time relevant). Updated when new user types emerge or assumptions are invalidated.
- **Owner:** BA (with UX Designer input)
- **Profiles:** Agile (recommended); Waterfall (optional)

#### Journey Maps (`journey-maps/journey-maps.md`) — Agile (recommended); optional in Waterfall
- **Purpose:** End-to-end user experience across touchpoints, capturing the user's path through the product (and outside it). Useful for surfacing gaps, friction, and opportunities that are invisible from a per-feature view.
- **Audience:** BA, UX Designer, Dev (via BMad context), client.
- **Update frequency:** Created when journey is non-trivial or when significant new flows are added. Updated as flows change.
- **Owner:** BA (with UX Designer input)
- **Profiles:** Agile (recommended); Waterfall (optional)

#### Client PRD — Product Requirements Document (`prd/prd-vX.Y.md`)
- **Purpose:** Defines the product vision, goals, user personas, functional requirements, and success criteria. **Authored by BA and signed off by the client first** — then becomes the source for the BMad PRD generated downstream.
- **Audience:** Client, PM, BA, UX Designer, Dev (via BMad context).
- **Content rule:** Keep business-level. Technical NFRs (API response times, tech stack specifics) belong in the architecture doc, not the PRD.
- **Versioning:** Minor version bump when features are added. Major version bump when product goals or direction change.
- **Update frequency:** Per release, during release wrap-up. Not updated mid-sprint.
- **Owner:** BA
- **Profiles:** All. **Lighter in Agile** — for many Agile projects, Vision + Roadmap suffice and the Client PRD is optional.
- **Client sign-off required:** Yes (at baseline and on major version changes)
- **Client-facing-first:** Yes — Client PRD is authored first, signed off, then the BMad PRD is generated *from* it.

#### SRS — Software Requirements Specification (`srs/srs-vX.Y.md`) — Waterfall only
- **Purpose:** Full detailed system requirements. The authoritative requirements document that CRs feed into at release time. Client signs off on the SRS before development begins.
- **Audience:** Client, BA, Dev, QA.
- **When created:** Greenfield — after Client PRD, UX Design, and Architecture are complete, before Epics & Stories. Brownfield — created or validated during project onboarding.
- **Versioning:** Minor version bump when requirements are added or clarified. Major version bump when existing requirements change substantially.
- **Update frequency:** Per release, during release wrap-up. Superseded versions moved to `.archive/`. Git-tagged at each version.
- **Owner:** BA
- **Profiles:** **Waterfall only.** Replaced by the SDD in Agile profiles.
- **Client sign-off required:** Yes
- **Note:** SRS creation workflow is planned for Sarah agent — currently a manual BA step using the SRS template.

#### SDD — System Description Document (`sdd/system-description.md`) — Agile only
- **Purpose:** Living "as it exists today" reference for the system. Updated continuously as features ship. Replaces the SRS in Agile profiles — but is fundamentally different: no version baselines, no formal client sign-off, no archive ceremony.
- **Audience:** BA, Dev, QA, client (for reference).
- **When created:** Greenfield — initialised as a stub during Phase 1 (step 16). Brownfield — initialised as a snapshot of the current system, then maintained as living.
- **Versioning:** Single living document. Date the last revision in a header. No `v1.0` archive ceremony.
- **Update frequency:** Continuous — updated when each feature ships (Phase 2 final step) and confirmed at each release (Phase 4 step 3).
- **Owner:** BA
- **Profiles:** Agile (Fixed-Range, Capacity-Based)
- **Client sign-off required:** No — informal reference. Bug fixes that restore behaviour defined in the SDD are eligible for [Quick Spec](#quick-spec-policy).

#### ADRs — Architecture Decision Records (`adrs/ADR-XXX-[name].md`) — Agile only
- **Purpose:** Lightweight, append-only records of significant technical decisions and their rationale. Each ADR captures: context, decision, alternatives considered, consequences. ADRs are never modified after acceptance — superseded ADRs are written as new ADRs that reference the old one.
- **Audience:** Dev, Tech Lead, BA (for traceability).
- **When to create:** Whenever a non-trivial technical decision is made (data model choice, integration approach, architectural pattern, security choice, dependency adoption).
- **Versioning:** Numbered sequentially (ADR-001, ADR-002, …). Status field: Proposed / Accepted / Superseded / Deprecated.
- **Owner:** Decision-maker (Tech Lead, Architect, Dev) authors; BA tracks for traceability.
- **Profiles:** Agile (Fixed-Range, Capacity-Based)

#### Change Request (`change-requests/CR-XXX-[feature-name].md`)
- **Purpose:** The client sign-off gate for a new feature or change. Describes what is changing, the business justification, scope, and acceptance criteria in plain language.
  - **Waterfall:** must be approved before a BR is created and development begins.
  - **Agile (Fixed-Range, Capacity-Based):** must be approved before a Story is created. The CR additionally carries a **Business Rules & Edge Cases** section (the content BR carried in Waterfall) and is loaded into BMad as the primary story context.
  - **Trade-off CRs** use the single template's "Added" and "Removed" sections to capture scope swaps within the estimate range.
- **Audience:** Client (primary), BA.
- **Versioning:** Not versioned. One file per feature.
- **Lifecycle:** CRs live in `docs/client/{product}/change-requests/` on `main` for their entire pre-development lifecycle. Each CR has a **STATUS field at the top** that is kept current: `Draft | Pending Design | Pending Client Approval | Approved | In Development | Deferred | Rejected`. A feature branch is only created when a CR is approved and sprint-assigned. Dead CRs are moved to `.archive/change-requests/` with STATUS: Rejected — never deleted.
- **Jira relationship:** Jira is the status and priority tracker; the CR doc is the content and scope record. They cross-reference each other (CR number in Jira ticket, Jira ticket ID in the CR doc).
- **Update frequency:** Created when a new request is received. Updated iteratively through the pre-development lifecycle (design, client discussions, clarifications). After client approval, not modified — create a new CR for changes.
- **Owner:** BA
- **Profiles:** All. **CR rhythm differs:** Waterfall = every deviation from SRS. Agile Fixed-Range = every meaningful scope event. Agile Capacity-Based = only Roadmap-level changes.
- **Client sign-off required:** Yes — Section 8 (Approval) must be completed before BR (Waterfall) or Story (Agile) is created.

#### Sprint Review notes (`sprint-reviews/sprint-review-YYYY-MM-DD.md`) — Agile only
- **Purpose:** Captures the end-of-sprint demo, client feedback, and resulting action items. In Capacity-Based engagements, this is the primary client-facing artifact between releases.
- **Audience:** Client, BA, PM, delivery team.
- **Versioning:** Not versioned — one file per sprint, dated.
- **Owner:** BA (PM may co-author)
- **Profiles:** Agile (Fixed-Range, Capacity-Based)
- **Client sign-off required:** No — informal record.

#### Release Notes (`release-notes/release-notes-vX.Y.md`)
- **Purpose:** Client-facing summary of what shipped in a release. Includes feature highlights, accepted CRs, known issues, upgrade or migration notes, demo links.
- **Audience:** Client (primary), end users (where relevant).
- **Versioning:** Per release.
- **Update frequency:** One per release event:
  - **Waterfall** — at each formal release.
  - **Agile Fixed-Range** — at each phase end.
  - **Agile Capacity-Based** — at each release cadence (engagement-defined: monthly, per-feature-batch, etc.).
- **Owner:** BA
- **Profiles:** All

#### UAT Sign-off Sheet (`uat-sign-offs/uat-sign-off-YYYY-MM-DD.md`)
- **Purpose:** Formal client acceptance of delivered scope. Captures what was tested, what passed, any defects deferred, and the client representative's sign-off.
- **Audience:** Client, BA, PM, QA.
- **Versioning:** Not versioned — one file per UAT event, dated.
- **Update frequency:** One per release acceptance event.
- **Owner:** BA (QA may co-author the test summary section)
- **Profiles:** All
- **Client sign-off required:** Yes — that is the artifact's purpose.

#### Handover / Knowledge Transfer Document (`handover/handover-YYYY-MM-DD.md`)
- **Purpose:** Operational guide for the client to operate the system independently after the engagement ends or the team changes. Covers deployment procedures, accounts and credentials handover, monitoring and alerting, support contacts, known issues, runbook pointers, and architecture summary.
- **Audience:** Client operations team, future maintainers.
- **When created:** At project end (Waterfall, Fixed-Range) or at major engagement events (Capacity-Based: team change, contract end, scope-down).
- **Versioning:** Not versioned — one file per handover event, dated. Update if a follow-up handover is needed.
- **Owner:** BA (with PM and Tech Lead input)
- **Profiles:** All
- **Client sign-off required:** Yes — client confirms handover is complete.

---

### Internal — BMad Layer

#### Business Requirement (`docs/business-requirements/`) — Waterfall only
- **Purpose:** Internal requirement document derived from an approved CR. Contains business rules, examples, edge cases, regulatory considerations, and a Jira-ready task. The primary document loaded into BMad when a Dev starts implementing a feature.
- **Audience:** Dev team, BA.
- **BMad usage:** Loaded manually by Dev as context when running the dev-story or create-story BMad workflow.
- **Update frequency:** Created once per feature on the feature branch. Not updated after creation — if requirements change, a new CR and BR are created.
- **Owner:** BA
- **Profiles:** **Waterfall only.** In Agile profiles, the CR carries this content directly (the Business Rules & Edge Cases section), and BMad workflows load the CR instead.

#### BMad PRD (`_bmad/...`) — agent-grounding artifact
- **Purpose:** BMad-native PRD document used by BMad agents (PM, SM, Dev) as grounded context to avoid hallucinations during downstream workflows. **Generated *from* the approved client-facing artifacts** (Client PRD in Waterfall; Vision + Roadmap (+ Client PRD if present) in Agile).
- **Audience:** BMad agents (consumed automatically by BMad workflows).
- **When generated:** After Client PRD / Vision+Roadmap is signed off (Phase 1 step 9 Waterfall, step 12 Agile). Regenerated when the source client artifacts change materially (Phase 4 release-time step).
- **Versioning:** Not versioned for human review — overwritten on regeneration.
- **Owner:** BMad PM workflow (auto-generated); BA triggers regeneration.
- **Profiles:** All
- **Client sign-off required:** No — internal artifact only. Never shown to the client.

#### Feature Spec (`docs/features/{product}/{feature}/`)
- **Purpose:** Detailed feature documentation organised into up to 13 modular sections (overview, user stories, business rules, API endpoints, data models, acceptance criteria, etc.). Created after implementation to document what was built. Referenced by BMad when creating stories for related features.
- **Audience:** Dev team (via BMad), BA, QA.
- **BMad usage:** Loaded manually as context when creating stories or feature specs for related features. Not auto-discovered.
- **Update frequency:** Created or updated during release wrap-up, after all features in a release are implemented and verified.
- **Owner:** BA (created), Dev (reviewed)
- **Profiles:** All

---

### Templates (`docs/templates/`)

| Template | Path | Used For | Profile |
|---|---|---|---|
| Kickoff Questionnaire | `client-communication/kickoff-questionnaire-template.md` | Project kickoff / client onboarding | All |
| Meeting Agenda | `client-communication/meeting-agenda-template.md` | Recurring client calls | All |
| Change Request | `change-request/cr-template.md` | Every new feature request | All |
| Glossary | `glossary/glossary-template.md` | New product glossary setup | All |
| RAID Log | `raid-log/raid-log-template.md` | New project setup | All |
| Stakeholder Register | `stakeholder-register/stakeholder-register-template.md` | New project setup (single and multi-project) | All |
| Project Charter | `project-charter/project-charter-template.md` | New project initiation | All |
| Product Vision | `vision/product-vision-template.md` | Agile project setup | Agile |
| Product Roadmap | `roadmap/roadmap-template.md` | Agile project setup + ongoing | Agile |
| Personas | `personas/personas-template.md` | When user profiles add value | Agile (recommended) |
| Journey Maps | `journey-maps/journey-maps-template.md` | When the user journey is non-trivial | Agile (recommended) |
| PRD (client-facing) | `prd/prd-client-template.md` | Client-facing PRD creation | All |
| SRS | `srs/srs-template.md` | SRS creation (greenfield + brownfield) | Waterfall only |
| SDD | `sdd/sdd-template.md` | SDD initialisation | Agile |
| ADR | `adr/adr-template.md` | Each significant technical decision | Agile |
| Sprint Review | `sprint-review/sprint-review-template.md` | End of each sprint | Agile |
| Release Notes | `release-notes/release-notes-template.md` | Each release event | All |
| UAT Sign-off | `uat-sign-off/uat-sign-off-template.md` | Each UAT acceptance event | All |
| Handover / KT | `handover/handover-template.md` | Project / engagement closeout | All |

> **BMad PRD** is not a template — it is generated by the BMad `create-prd` workflow (`_bmad/bmm/workflows/2-plan-workflows/create-prd/`) using the approved client-facing artifacts as input.

---

## BA Workflow

The BA-side flows differ by methodology. The shared CR lifecycle (CR doc on `main`, STATUS field, feature branch on sprint-assignment) is the same; what feeds in and out of it changes.

### Per Feature — Waterfall

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

### Per Feature — Agile (Fixed-Range and Capacity-Based)

```
Client request received
        ↓
Decide: change to Roadmap, or realisation of an existing initiative?
   ├── Realisation of existing initiative (Capacity-Based, common case)
   │       ↓
   │       Initiative moves Next → Now on Roadmap
   │       ↓
   │       Create Story (BMad SM) using Roadmap initiative + AC as context
   │       ↓
   │       Story enters sprint  →  Dev  →  Code Review  →  ship
   │       ↓
   │       SDD updated to reflect shipped feature
   │
   └── Change to Roadmap (always Fixed-Range; Roadmap-level for Capacity-Based)
           ↓
           CR doc created in docs/client/{product}/change-requests/ on main
           STATUS: Draft  (CR carries Business Rules & Edge Cases)
           ↓
           Iterative improvement
           STATUS: Pending Design → Pending Client Approval
           ↓
           Client approves Section 8
           STATUS: Approved  →  Roadmap updated (new initiative or scope change)
           ↓
           When sprint-ready: Create Story (BMad SM) using CR as context
           ADR created if a non-trivial technical decision arose
           ↓
           Feature branch created  →  Dev  →  Code Review  →  ship
           ↓
           SDD updated to reflect shipped feature
```

> **Dead CRs:** Move to `.archive/change-requests/` and set STATUS: Rejected. Never delete — they are useful history if a similar request resurfaces.

### Per Release — Waterfall

```
All features in release implemented
        ↓
Merge approved CRs into SRS  →  bump SRS version  →  client sign-off
Update Client PRD (only if product goals changed)
Regenerate BMad PRD if Client PRD changed
Update feature specs
Publish Release Notes  →  collect UAT sign-off
Git tag release docs  →  merge to main
Move superseded SRS version to .archive/
```

### Per Release — Agile (Fixed-Range)

```
Phase end reached
        ↓
Confirm SDD reflects all shipped features in the phase
Update Vision / Roadmap if direction shifted
Regenerate BMad PRD if Vision / Client PRD changed materially
Update feature specs
Publish Release Notes for the phase
Collect UAT sign-off for the phase
Git tag release docs
        ↓
If next phase: new mini-Charter + new Roadmap; Create Epics & Stories (bulk) for the new phase scope
If project complete: continue to Phase 5 — Project Closeout
```

### Per Release — Agile (Capacity-Based)

```
Release cadence event (engagement-defined: monthly, batch, etc.)
        ↓
Confirm SDD reflects shipped features
Refresh Roadmap (move initiatives between Now / Next / Later)
Regenerate BMad PRD if Vision / Roadmap changed materially
Update feature specs
Publish Release Notes  →  collect UAT sign-off
Git tag release docs
        ↓
Continue — no new phase event; ongoing engagement resumes
```

---

## Versioning Convention

Documents fall into two categories: **versioned** (formal version baselines, signed off) and **living** (continuously updated, no version baselines).

### Versioned documents

Apply the convention below to: Project Charter, Client PRD, SRS (Waterfall), Release Notes.

#### Document Version Numbers
- `v1.0` → initial release
- `v1.1` → minor addition or clarification (no scope change)
- `v2.0` → major scope or goal change

#### Version Table (inside each versioned document)
Every versioned document includes a version history table at the top:

```markdown
| Version | Date       | Author | Summary                        |
|---------|------------|--------|--------------------------------|
| 1.0     | 2026-03-18 | BA     | Initial release                |
| 1.1     | 2026-04-10 | BA     | Added bulk disbursement section|
```

#### Git Tags
Tag versioned documents at each delivery milestone:
```
git tag client/project-1-srs-v1.1
git tag client/project-1-prd-v1.0
```

### Living documents

These do **not** follow `vX.Y` versioning. They are updated in place and carry only a "last updated" date in the document header:

- **Roadmap** — change-log section at the bottom records initiative movements between buckets and CR-introduced changes
- **SDD** — header date; significant updates noted in a change-log section
- **Vision** — header date; substantial revisions noted inline
- **RAID Log** — entries dated individually; status changes tracked per-entry
- **Glossary** — header date; deprecated terms marked but not removed
- **Stakeholder Register** — header date

Living documents are never archived. They evolve continuously across releases.

### Dated artifacts

These are not versioned and not living — each event produces a new dated file: Sprint Review notes, UAT Sign-off Sheets, Handover/KT documents. Filenames carry the date (`YYYY-MM-DD`).

---

## Traceability Chain

Every requirement can be traced from client request to implementation. The chain differs by methodology.

### Waterfall

```
Client request
    ↓
Change Request (CR)          docs/client/{product}/change-requests/
    ↓
Business Requirement (BR)    docs/business-requirements/
    ↓
Feature Spec                 docs/features/{product}/{feature}/
    ↓
Story                        created via BMad Create Story workflow
    ↓
Implementation               dev branch → PR → main
    ↓
SRS update at release        docs/client/{product}/srs/
```

Each document references its source:
- BR references the CR it was derived from
- Feature spec references the BR
- SRS references the CRs absorbed at release time

### Agile (Fixed-Range and Capacity-Based)

```
Client request
    ↓
Roadmap initiative            docs/client/{product}/roadmap/
    │   (new initiative if Roadmap-level change → goes through CR;
    │    realisation of existing initiative → no CR)
    ↓
Change Request (CR)           docs/client/{product}/change-requests/
    │   (carries Business Rules & Edge Cases — replaces BR)
    ↓
Story + AC                    created via BMad Create Story workflow
    │   (uses CR or Roadmap initiative as primary context)
    ↓
ADR                           docs/client/{product}/adrs/
    │   (only if a significant technical decision was made)
    ↓
Implementation                dev branch → PR → main
    ↓
SDD update                    docs/client/{product}/sdd/
    │   (continuous, when feature ships)
    ↓
Feature Spec                  docs/features/{product}/{feature}/
    │   (release-time documentation of what was built)
```

Each document references its source:
- CR references the Roadmap initiative (if Roadmap-introduced) or the original client request
- Story references the CR (or directly the Roadmap initiative for backlog items that did not require a CR)
- ADR references the Story or CR that triggered the decision
- Feature spec references the CRs and ADRs absorbed for the feature

---

## Hybrid Tooling: Git + Jira + Confluence

This section describes an optional hybrid approach that layers Confluence and deeper Jira integration on top of the existing git-based workflow. It is not mandatory — the base workflow (git + markdown) remains fully functional without it. The hybrid is most valuable when clients are actively engaged with documentation.

---

### The Layer Split

The hybrid assigns each tool to what it does best. Documents are placed by audience:

| Layer | Tool | Documents | Why |
|---|---|---|---|
| Status, priority, backlog | **Jira** | Epics, Stories, sprint plans | Single source of truth — no duplication |
| Client-facing docs | **Confluence** | Charter, CR, Client PRD, **SRS** *(Waterfall)* / **SDD** *(Agile)*, **Vision**, **Roadmap**, Personas, Journey Maps, Sprint Review notes, Release Notes, UAT Sign-off, Handover/KT | Accessible to client, inline commenting, native Jira links, page approvals |
| Internal / BMad docs | **Git + markdown** | **BR** *(Waterfall)*, ADRs *(Agile)*, Feature Specs, Architecture, Deep Dives, BMad PRD | AI-ready, proper diffs, developer-friendly |

**The rule:** client-facing = Confluence. Internal = git. When in doubt, ask "does the client need to read or sign off on this?" If yes → Confluence. If no → git.

---

### Revised Traceability Chain (Hybrid)

#### Waterfall

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

#### Agile (Fixed-Range and Capacity-Based)

```
Client request
    ↓
Decide: Roadmap initiative realisation, or Roadmap-level change?
   ├── Realisation → no CR; promote initiative on Confluence Roadmap page → create Story in Jira
   └── Roadmap-level change:
         Jira Epic created  ←→  Confluence CR page
                            (CR carries Business Rules & Edge Cases)
              ↓
         Client approves CR on Confluence page
              ↓
         Roadmap updated in Confluence (new initiative or shifted bucket)
    ↓
Story created in Jira (uses CR or Roadmap initiative as context)
ADR written in git if a non-trivial technical decision arose
    ↓
Feature branch  →  Implementation  →  PR  →  merge
    ↓
SDD updated in Confluence (continuous, on every feature ship)
Feature Spec written in git at release
```

---

### Jira Integration

**Smart Commits** — include the Jira Epic / Story ID in branch names and commit messages. Jira automatically links the branch, commits, and PRs to the ticket. No manual linking needed.

```
branch:  feature/P1-123-bulk-disbursement
commit:  P1-123 add bulk disbursement story
```

**Jira Automation** — built-in rule engine, no extra tooling. Useful rules:
- When Epic / CR moves to `Approved` → auto-create sub-task ("Create BR" in Waterfall, "Create Story" in Agile)
- When all Stories in Epic are `Done` → notify BA to update **SRS** *(Waterfall)* or **SDD** *(Agile)*
- When PR merged → transition Epic to `In Development`

**Jira MCP (Claude integration)** — with a Jira MCP server configured in Claude Code, Sarah can create and update Jira tickets directly from a session. When a CR is approved (or a Story is needed), the corresponding Jira ticket can be created without leaving the conversation.

---

### Confluence Integration

**Confluence page approvals** — CRs authored in Confluence can use the built-in page approval feature as the formal client sign-off mechanism, replacing the Section 8 signed document. The approval is auditable on the page.

**markdown-confluence** (npm package) — syncs markdown files from git to Confluence pages on push. Use this to auto-publish client-facing docs from git to Confluence without manual export. Configure it to sync only `docs/client/` — not internal docs.

**Confluence MCP (Claude integration)** — with a Confluence MCP server configured, Sarah can create CR pages in Confluence directly from a session, and read existing CRs / Roadmap / Vision / SDD as context when drafting a Story or BR.

---

### Scalable Dial by Client Engagement

Since client engagement varies by project, the hybrid is not all-or-nothing:

| Client engagement | Recommended setup |
|---|---|
| **Hands-off** — receives outputs, signs off by email | Smart Commits + CI sync only. Git is source of truth, Confluence is an optional read-only mirror. |
| **Engaged** — reads docs, comments, requests changes | Add Confluence for CRs and **Roadmap** *(Agile)* or **SRS** *(Waterfall)*. Client approves on the page. Git receives approved version via sync. |
| **All clients** | Jira MCP removes manual ticket creation during BA sessions regardless of client engagement level. |

**Minimum worthwhile setup for any project:** Jira Smart Commits + Jira MCP. Eliminates most manual status-keeping with minimal overhead.

---

### What Changes in the BA Workflow (Hybrid)

The CR backlog strategy (CRs on `main`, STATUS field, feature branch only when sprint-assigned) remains the same. The only changes are:

- CRs are authored in Confluence instead of (or in addition to) git
- Client sign-off happens on the Confluence page instead of a shared PDF
- The STATUS field on the CR doc may be simplified or removed — Jira Epic status is the source of truth
- **BR** *(Waterfall)* or **Story** *(Agile)* cross-references the Confluence CR URL and Jira Epic ID
- For Agile projects: the **Roadmap** is also a strong candidate for Confluence (client visibility on the Now/Next/Later view); the **SDD** lives in Confluence as a living page that mirrors the git source

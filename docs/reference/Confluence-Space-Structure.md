# Confluence Space Structure
**[Project Name] — Agile Project Knowledge Base**

*This document defines the page hierarchy, ownership, and update cadence for the project Confluence space. It should be saved as the Home Page of the space.*

---

## Guiding Principles

1. **One home per piece of information.** No duplication across pages — use links instead.
2. **Jira tracks work. Confluence holds knowledge.** Stories live in Jira. Anything the team needs to *refer back to* lives here.
3. **Structure around features, not sprints.** Sprints are ephemeral. Features are stable reference points.
4. **Update at the source.** When something changes in a sprint, the relevant Confluence page is updated — not a new page created.
5. **Google Sheets / Google Docs stay where they are** — link to them from Confluence, don't duplicate content.

---

## Full Space Structure

```
📁 [Project Name] — Home
│
├── 📋 1. Project Overview
│   ├── Product Vision & Goals
│   ├── Project Charter
│   ├── Stakeholder Register
│   ├── Scope Statement
│   ├── Glossary & Definitions
│   └── RAID Log  ← link to live Jira or Google Sheet
│
├── 🗺️ 2. Requirements & Backlog
│   ├── Epics Overview  ← summary table linking to Jira epics
│   ├── Business Rules Register
│   ├── Non-Functional Requirements (NFRs)
│   ├── Definition of Done (DoD)
│   └── Definition of Ready (DoR)
│
├── 🏗️ 3. Architecture & Design
│   ├── System Context Diagram
│   ├── High-Level Architecture
│   ├── Architecture Decision Records (ADRs)
│   │   ├── ADR-001: [Decision title]
│   │   ├── ADR-002: [Decision title]
│   │   └── ADR-NNN: [Decision title]
│   ├── Integration Specifications
│   └── Data Dictionary  ← link to Google Sheet if tabular
│
├── 📖 4. System Description Document (SDD)  ← LIVING DOCUMENT
│   ├── SDD Home (Overview, User Roles, Business Rules)
│   ├── 4.1 [Feature / Module Name]
│   ├── 4.2 [Feature / Module Name]
│   ├── 4.3 [Feature / Module Name]
│   ├── 4.N [Feature / Module Name]
│   ├── Integrations (current state)
│   ├── Data & Calculations
│   ├── NFRs in Practice
│   └── Known Limitations & Technical Debt
│
├── 🔄 5. Process & Workflows
│   ├── [Process Name] — As-Is Flow
│   ├── [Process Name] — To-Be Flow
│   └── BPMN Diagrams  ← embed or link from draw.io / Miro
│
├── 🎨 6. Design & Prototypes
│   ├── Design System / Style Guide  ← link to Figma
│   ├── Wireframes Index  ← link to Figma frames per feature
│   └── Prototype Links
│
├── 🧪 7. Testing & Quality
│   ├── Test Approach
│   ├── UAT Sign-off Log  ← one entry per release
│   └── Bug Triage Notes  ← link to Jira filter
│
├── 📦 8. Releases
│   ├── Release Notes — v1.0
│   ├── Release Notes — v1.1
│   └── Release Notes — vN.N
│
├── 📊 9. Calculations & Reference Data
│   └── [Links to Google Sheets — do not duplicate content here]
│
├── 🔁 10. Sprints & Ceremonies  ← lightweight, not a sprint tracker
│   ├── Sprint Review Notes
│   │   ├── Sprint 01 Review
│   │   ├── Sprint 02 Review
│   │   └── Sprint NN Review
│   └── Retrospective Actions Log
│
└── 📁 11. Archive
    ├── Superseded decisions
    ├── Old wireframes
    └── Deprecated feature documentation
```

---

## Section-by-Section Guide

### 📋 1. Project Overview

The entry point for anyone new to the project. Should be readable in 10 minutes and give a full orientation.

| Page | Owner | Update Cadence |
|---|---|---|
| Product Vision & Goals | BA / Product Owner | When objectives change |
| Project Charter | BA | At project start — rarely changes |
| Stakeholder Register | BA | When stakeholders change |
| Scope Statement | BA | When scope changes (via change request) |
| Glossary & Definitions | BA | Ongoing — add terms as they emerge |
| RAID Log | BA / PM | Weekly |

---

### 🗺️ 2. Requirements & Backlog

Knowledge-level requirements context. The Jira backlog holds the stories — this section holds the *why and the rules* behind them.

| Page | Owner | Update Cadence |
|---|---|---|
| Epics Overview | BA | Per sprint / when epics change |
| Business Rules Register | BA | When rules are added or changed |
| NFRs | BA + Tech Lead | When NFRs are confirmed or revised |
| Definition of Done | Whole team | Per retrospective (if changed) |
| Definition of Ready | Whole team | Per retrospective (if changed) |

> 💡 The Epics Overview page should be a summary table with columns: Epic name, Jira link, Status, Brief description. It gives stakeholders a one-page view of the full product scope.

---

### 🏗️ 3. Architecture & Design

Technical reference — primarily for the dev team and for onboarding new developers.

| Page | Owner | Update Cadence |
|---|---|---|
| System Context Diagram | Tech Lead / BA | When integrations change |
| High-Level Architecture | Tech Lead | When architecture evolves |
| ADRs | Tech Lead | Per significant technical decision |
| Integration Specifications | BA + Tech Lead | When integrations are added or changed |
| Data Dictionary | BA | When new entities or fields are added |

**ADR format (each ADR is its own child page):**
```
Title: ADR-001 — [Short decision title]
Date: [Date]
Status: Accepted / Superseded / Deprecated
Context: [What situation led to this decision]
Decision: [What was decided]
Consequences: [Trade-offs and implications]
```

---

### 📖 4. System Description Document (SDD)

> ⭐ **This is the most important section for long-running agile projects.**

The SDD describes the system **as it exists today** — not as it was originally designed. After 1–2 years of sprints, this is the only place that accurately reflects current behaviour.

**Structure:** One child page per major feature or module. The SDD Home page contains the system overview, user roles, and business rules.

| Page | Owner | Update Cadence |
|---|---|---|
| SDD Home | BA | When roles or business rules change |
| Feature pages (one per module) | BA | **Part of Definition of Done** — updated when a story changes behaviour |
| Integrations (current state) | BA + Tech Lead | When integrations change |
| Data & Calculations | BA | When data model or formulas change |
| NFRs in Practice | Tech Lead | After load tests, security reviews |
| Known Limitations & Technical Debt | Tech Lead | Per sprint / quarterly review |

**Update rule:** If a story changes how a feature *behaves*, the relevant SDD page must be updated before the story is marked Done. This is non-negotiable — it is what keeps the SDD alive.

**Quarterly review:** Every 3–6 months, do a full SDD review pass to catch anything that slipped. This can double as a useful client checkpoint: *"Here is what the system does today."*

---

### 🔄 5. Process & Workflows

Business process flows — both as-is (current state) and to-be (future state). Keep diagrams in draw.io or Miro and embed or link here.

| Page | Owner | Update Cadence |
|---|---|---|
| Process flows | BA | When workflows change |

> 💡 If a process flow changes significantly mid-project, keep the old version in the Archive section for reference rather than deleting it.

---

### 🎨 6. Design & Prototypes

Do not store wireframes as attachments in Confluence. Keep them in Figma and link from here. This section is an index, not a storage location.

| Page | Owner | Update Cadence |
|---|---|---|
| Design System / Style Guide | Designer / BA | When design standards change |
| Wireframes Index | BA | When new wireframes are created |
| Prototype Links | BA | Per feature / sprint |

---

### 🧪 7. Testing & Quality

| Page | Owner | Update Cadence |
|---|---|---|
| Test Approach | QA / BA | At project start and when approach changes |
| UAT Sign-off Log | BA | Per release — one row per release with date, scope, sign-off name |
| Bug Triage Notes | QA / BA | Link to Jira filter rather than duplicating |

**UAT Sign-off Log format:**

| Release | Date | Scope | Signed Off By | Notes |
|---|---|---|---|---|
| v1.0 | [Date] | [Features included] | [Client name / role] | [Notes] |
| v1.1 | [Date] | [Features] | [Name] | |

---

### 📦 8. Releases

One child page per release. Each page is a snapshot — created at release time and not modified afterwards.

**Release Notes page format:**
```
Release: v1.2
Date: [DD MMM YYYY]
Deployed to: Production

What's new:
- [Feature or change]
- [Feature or change]

Bug fixes:
- [Fix]

Known issues:
- [Issue]

Jira filter for this release: [Link]
```

---

### 📊 9. Calculations & Reference Data

This section is intentionally thin. All tabular data and formulas live in Google Sheets — this section holds links and context only.

| Item | Location | Owner |
|---|---|---|
| [Calculation name] | [Google Sheet link] | [Owner] |
| [Reference table] | [Google Sheet link] | [Owner] |

> Do not copy spreadsheet data into Confluence pages. Links only — duplication guarantees staleness.

---

### 🔁 10. Sprints & Ceremonies

Lightweight sprint records — not a sprint tracker (that's Jira). This section exists for narrative context and retrospective actions only.

| Page | Content | Update Cadence |
|---|---|---|
| Sprint Review Notes | What was demoed, stakeholder feedback, decisions made | Per sprint |
| Retrospective Actions Log | Running log of retro action items and their status | Per sprint |

**Sprint Review Notes format:**
```
Sprint [N] Review — [Date]
Sprint Goal: [Goal]
Completed: [Story list or summary]
Stakeholder feedback: [Notes]
Decisions made: [Any decisions that affect future work]
Carry-over: [What didn't complete and why]
```

---

### 📁 11. Archive

Pages that are no longer current but should not be deleted — they provide historical context.

- Superseded decisions and old ADRs
- Replaced wireframes or design directions
- Deprecated feature documentation
- Previous versions of the scope statement or business rules

> Move pages here rather than deleting them. Someone will always need to find out why a decision was made 18 months ago.

---

## What Goes Where — Quick Reference

| Information | Where it lives |
|---|---|
| User stories, tasks, bugs | Jira |
| Acceptance criteria | Jira (on each story) |
| Sprint goals | Jira (sprint) + Sprint Review Notes in Confluence |
| Current system behaviour | SDD in Confluence (Section 4) |
| Business rules | Confluence Section 2 + SDD Section 3 |
| Technical decisions | ADRs in Confluence Section 3 |
| Wireframes & prototypes | Figma → linked from Confluence Section 6 |
| Calculation formulas | Google Sheets → linked from Confluence Section 9 |
| Client-facing drafts | Google Docs → linked from relevant Confluence page |
| Release history | Confluence Section 8 |
| UAT sign-offs | Confluence Section 7 |

---

## Maintenance Roles

| Role | Responsibility |
|---|---|
| **BA** | Owns Sections 1, 2, 4 (SDD), 5, 7, 8. Primary keeper of project knowledge. |
| **Tech Lead** | Owns Section 3 (Architecture & ADRs). Co-owns SDD technical sections. |
| **QA** | Co-owns Section 7. Maintains test approach and UAT log. |
| **Whole team** | Responsible for updating SDD feature pages as part of Definition of Done. |

---

*Space created: [Date] | Structure last reviewed: [Date] | Owner: [BA Name]*

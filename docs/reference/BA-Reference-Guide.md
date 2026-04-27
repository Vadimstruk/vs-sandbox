# Business Analyst Reference Guide
**Documents, Artifacts & Lifecycle — Waterfall & Agile**

*Compiled: April 2026 | Audience: Senior BA — Outsourced Software Development Context*

---

## Table of Contents

1. [Starting a New Project — What to Do First](#1-starting-a-new-project)
2. [Business Case & Project Charter](#2-business-case--project-charter)
3. [Waterfall Document Sequence](#3-waterfall-document-sequence)
4. [FRD vs SRS — Detailed Comparison](#4-frd-vs-srs)
5. [Agile Project Document Set](#5-agile-project-document-set)
6. [Quick Reference — All Key Documents](#6-quick-reference)

---

## 1. Starting a New Project

As a senior BA joining a new project, work through these phases in sequence. The most critical early task is getting clarity on the **problem statement** — requirements built on a fuzzy problem will almost always need rework.

### 1.1 Day 1–2: Orient Yourself

- Meet the project sponsor and key stakeholders — understand the *why* behind the project
- Review any existing materials: RFPs, previous attempts, contracts, business cases
- Clarify your own role, authority, and reporting lines

### 1.2 Week 1: Establish the Foundation

- Conduct a stakeholder analysis — identify everyone affected, their influence and interest level
- Run a project kickoff or discovery session to align on goals, scope boundaries, and success criteria
- Capture initial assumptions, constraints, and known risks
- Start the RAID log immediately — do not wait

### 1.3 Key Early Documents

| Document | Purpose |
|---|---|
| Project Charter / Business Case | Confirms the problem being solved and business value |
| Stakeholder Register | Who they are, what they need, how to engage them |
| Scope Statement / Context Diagram | What is in and out of scope, system boundaries |
| Requirements Management Plan | How requirements will be elicited, documented, approved, and changed |
| RAID Log | Risks, Assumptions, Issues, Dependencies — ongoing from day one |

### 1.4 Elicitation Phase

- Run workshops, interviews, and observation sessions with stakeholders
- Document findings as you go — do not let notes pile up
- Produce a Current State / As-Is analysis before jumping to solutions

> 💡 **Build relationships early.** Your credibility as a BA lives and dies on stakeholder trust, not document quality alone.

---

## 2. Business Case & Project Charter

These are the two foundational documents at the start of any project. They are frequently confused but serve very different purposes.

### 2.1 Business Case

The *why* — justifies whether the project should exist at all. Written before the project is approved, usually by the business sponsor. Answers: **Is this worth doing?**

- The problem or opportunity being addressed
- Options considered (including do nothing)
- Costs, benefits, and ROI
- Risks of proceeding vs. not proceeding
- Recommended option

> It is a decision-making tool for leadership. Once approved, the project gets the green light.

### 2.2 Project Charter

The *what and who* — formally authorises the project to begin and gives the PM/BA authority to act. Written after the business case is approved.

- Project purpose and objectives
- High-level scope (in and out)
- Key stakeholders and their roles
- High-level timeline and budget
- Success criteria
- Constraints and assumptions
- Sponsor sign-off

> Think of it as the project's birth certificate.

### 2.3 Key Differences at a Glance

| | Business Case | Project Charter |
|---|---|---|
| **Question** | Should we do this? | What are we doing and who is responsible? |
| **Timing** | Before approval | After approval |
| **Written by** | Business sponsor | PM or BA |
| **Audience** | Decision makers | Project team |

---

## 3. Waterfall Document Sequence

After the Business Case and Project Charter are approved, work through these documents in sequence. Each phase gates the next.

### 3.1 Scope Definition

- **Context Diagram** — system boundaries, external actors, data flows in and out
- **Scope Statement** — what is explicitly in and out of scope, in plain language

> These two together prevent scope creep more than anything else. Complete them before any requirements work.

### 3.2 Current State Analysis (As-Is)

- Process flows of how things work today
- Pain points and gap analysis
- Helps stakeholders agree on the problem before jumping to solutions

### 3.3 Requirements Documents

| Document | Answers | Audience |
|---|---|---|
| BRD | What does the business need? | Business stakeholders, sponsors |
| FRD | What must the system do? (user perspective) | Business stakeholders, product owners, QA |
| SRS | What must the system do? (technical precision) | Developers, architects, QA |
| NFRs | How must the system perform? | Both business and technical |
| Use Cases / User Stories | How do users interact with the system? | Both |
| Process Flows / BPMN | What are the future-state workflows? | Both |

### 3.4 Supporting Artifacts

- **Data Dictionary / Glossary** — align on terminology early, especially on data-heavy projects
- **RAID Log** — ongoing from day one
- **Wireframes / Mockups** — created alongside functional requirements
- **Requirements Traceability Matrix (RTM)** — links requirements to objectives and test cases

### 3.5 Sign-off & Baseline

Before moving to design and build, requirements need formal approval. This is the **requirements baseline**. All changes after this point go through change control.

> 💡 In outsourcing contexts, a merged FRD/SRS document outperforms two separate documents — it serves both audiences without duplication overhead.

### 3.6 Waterfall Flow Summary

```
Charter Approved
       ↓
Stakeholder Register + Scope Definition
       ↓
As-Is Analysis (Current State)
       ↓
BRD → FRD → SRS → NFRs → Use Cases
       ↓
Wireframes / Data Dictionary
       ↓
Requirements Sign-off (Baseline)
       ↓
Design & Build begins
```

---

## 4. FRD vs SRS

### 4.1 FRD — Functional Requirements Document

Describes **what the system must do** from a business and user perspective. Technology-agnostic — focused on behaviour, not implementation.

- Functional requirements (what each feature must do)
- Use cases or user stories
- Business rules
- Data requirements at a logical level
- UI/UX behaviour expectations
- Integration points — what, not how

*Audience: Business stakeholders, product owners, BAs, QA*

### 4.2 SRS — Software Requirements Specification

Describes **what the system must do** from a technical and implementation perspective. The engineer-facing elaboration of the FRD.

- Everything in the FRD, refined and made precise
- System architecture constraints
- API specifications and data formats
- Performance, security, scalability requirements (NFRs integrated)
- Error handling and edge cases
- Database schema at a logical/physical level
- External system interface specifications

*Audience: Developers, architects, QA engineers, DevOps*

### 4.3 Comparison Table

| | FRD | SRS |
|---|---|---|
| **Perspective** | Business / user | Technical / system |
| **Language** | Business language | Precise and technical |
| **Technology** | Agnostic | Technology-aware |
| **Written by** | BA | BA + Solution Architect |
| **Audience** | Stakeholders + team | Dev + QA team |
| **Timing** | After BRD | After FRD |

### 4.4 When to Create Each

**Create an FRD when:**
- You need stakeholder sign-off on behaviour before handing to dev
- There is a significant business/technical knowledge gap on the team
- The project is waterfall or hybrid
- Requirements need to be contractually baselined (outsourcing context)

**Create an SRS when:**
- Developers need precise, unambiguous specifications
- You are building complex integrations or APIs
- The system has strict compliance or audit requirements
- There is an external vendor or offshore team building the solution

**Create a merged FRD/SRS when:**
- Mid-size projects where maintaining two documents creates sync overhead
- Outsourced development requiring a single contractual source of truth
- The business and technical audiences can be served by clearly separated sections in one document

> 💡 In outsourcing, a merged document with clearly separated business and technical sections often works better than two documents — fewer sync issues, one source of truth to baseline and version-control.

---

## 5. Agile Project Document Set

In agile, heavy upfront documentation is replaced with **living, lightweight artifacts** that evolve sprint by sprint. The core mindset shift: conversations and working software replace documents as the primary communication mechanism.

### 5.1 Foundation Artifacts (Created Once, Before Sprint 1)

| Artifact | Purpose |
|---|---|
| Product Vision Statement | One page max. Why this product exists, who it is for, what problem it solves. The team's North Star. |
| Product Roadmap | High-level themes and epics across quarters. Not a Gantt chart — a directional view of priorities. |
| Definition of Done (DoD) | The team's shared agreement on what complete means for any story. |
| Definition of Ready (DoR) | Criteria a story must meet before entering a sprint. |

### 5.2 Backlog Artifacts (Living, Continuously Refined)

- **Epic list** — large bodies of work, each representing a meaningful capability
- **User Stories** — *As a [role], I want [feature] so that [benefit]*
- **Acceptance Criteria** — per story, defines what done looks like from the user's perspective
- **Story points / estimates** — relative sizing for sprint planning

### 5.3 Per-Sprint Artifacts

- **Sprint Goal** — one sentence capturing the sprint's purpose
- **Sprint Backlog** — the committed stories for this sprint
- **Sprint Review notes** — what was demonstrated, stakeholder feedback
- **Sprint Retrospective notes** — what to improve next sprint

### 5.4 Supporting Artifacts (As Needed)

- **Personas** — who the users actually are; grounds story writing in reality
- **Journey Maps** — end-to-end user experience across touchpoints
- **Wireframes / Prototypes** — created just-in-time before a story is developed
- **NFR Backlog items** — non-functional requirements written as stories or constraints
- **Glossary / Ubiquitous Language** — shared terminology, especially in complex domains
- **Architecture Decision Records (ADRs)** — lightweight records of key technical decisions and rationale

### 5.5 Additional Artifacts for Outsourcing Context

> Because your client needs traceability and accountability that pure agile teams often skip, add these to your standard agile set.

| Artifact | Purpose |
|---|---|
| Project Charter | Still needed for formal engagement start — authorises the work |
| Release Notes | Per release, for the client's record |
| UAT Sign-off Sheet | Per sprint or per release — formal client acceptance |
| Change Request Log | Tracks scope changes with approval trail |
| Handover / Knowledge Transfer Document | Critical at project end — ensures client can operate independently |

### 5.6 Waterfall vs Agile Equivalents

| Waterfall Document | Agile Equivalent |
|---|---|
| BRD | Product Vision + Epics |
| FRD | User Stories + Acceptance Criteria |
| SRS | User Stories + ADRs + team conventions |
| Test Plan | Definition of Done + automated test coverage |
| Full upfront sign-off | Rolling UAT per sprint |

---

## 6. Quick Reference

| Document | Phase | Methodology | One-Line Purpose |
|---|---|---|---|
| Business Case | Pre-project | Waterfall / Hybrid | Justifies whether the project should exist |
| Project Charter | Initiation | Both | Formally authorises the project |
| Stakeholder Register | Initiation | Both | Who is involved and how to engage them |
| Context Diagram | Scope | Both | System boundaries and external interfaces |
| RAID Log | All phases | Both | Risks, Assumptions, Issues, Dependencies |
| BRD | Requirements | Waterfall | What the business needs, independent of tech |
| FRD | Requirements | Waterfall / Hybrid | What the system must do (user perspective) |
| SRS | Requirements | Waterfall / Hybrid | What the system must do (technical precision) |
| FRD/SRS (merged) | Requirements | Waterfall / Hybrid | Single source of truth for outsourced projects |
| Use Cases | Requirements | Waterfall / Hybrid | User interactions with the system |
| NFRs | Requirements | Both | Performance, security, scalability constraints |
| Process Flows / BPMN | Requirements | Both | Current and future state workflows |
| Data Dictionary | Requirements | Both | Shared definitions for all data entities |
| Wireframes | Requirements / Design | Both | Visual representation of UI behaviour |
| RTM | Requirements / Test | Waterfall | Links requirements to objectives and test cases |
| Product Vision | Initiation | Agile | North Star — why, who, what problem |
| Product Roadmap | Initiation | Agile | Directional view of epics across quarters |
| Definition of Done | Initiation | Agile | Shared agreement on what complete means |
| User Stories + AC | Backlog | Agile | Requirements at story level with acceptance criteria |
| Sprint Backlog | Per sprint | Agile | Committed work for the current sprint |
| ADRs | Design | Agile | Records of key technical decisions and rationale |
| **System Description Document (SDD)** | **Ongoing** | **Agile / Both** | **Living document — the system as it exists today** |
| UAT Sign-off | Acceptance | Both | Formal client acceptance of delivered scope |
| Change Request Log | All phases | Both (outsourcing) | Tracks scope changes with approval trail |

---

> ⚠️ **The most important thing early on any project:** get clarity on the problem statement. Requirements built on a fuzzy problem will almost always need rework.

---
title: Software Requirements Specification — [Product Name]
version: "1.0"
status: Draft / Pending Approval
author: [Author Name (Role)]
date: YYYY-MM-DD
---

# Software Requirements Specification — [Product Name]

### Document Information

| Field | Value |
|---|---|
| **Version** | 1.0 |
| **Date** | YYYY-MM-DD |
| **Status** | Draft / Pending Approval |
| **Author** | [Author Name (Role)] |
| **Confluence** | [URL — add when Confluence page is created, leave blank for Jira-only projects] |

### Revision History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Author] | Initial release |

---

## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Related Documents](#13-related-documents)
  - [1.4 Intended Audience](#14-intended-audience)
  - [1.5 Definitions and Abbreviations](#15-definitions-and-abbreviations)
- [2. System Overview](#2-system-overview)
- [3. User Roles](#3-user-roles)
- [4. Functional Requirements](#4-functional-requirements)
- [5. Non-Functional Requirements](#5-non-functional-requirements)
- [6. Out of Scope](#6-out-of-scope)
- [7. Client Approval](#7-client-approval)

---

## 1. Introduction

### 1.1 Purpose

This document defines the software requirements for [Product Name] — [one sentence description]. It serves as the formal requirements agreement between [Client] and [Dev Partner], and as the baseline from which all change requests are tracked.

### 1.2 Scope

This SRS covers [Product Name] only. [Note any related products with separate SRS documents and their paths.]

### 1.3 Related Documents

| Document | Location |
|---|---|
| PRD | `docs/client/[product]/prd/prd-v1.0.md` |
| Project Charter | `docs/client/[product]/charter/project-charter-v1.0.md` |
| Glossary | `docs/client/shared/glossary.md` |
| RAID Log | `docs/client/shared/raid-log.md` |

### 1.4 Intended Audience

| Audience | Usage |
|---|---|
| Client ([Organisation]) | Sign-off on requirements baseline; change request reference |
| Business Analyst | Authoring and maintaining requirements |
| Development Team | Implementation reference |
| QA | Test design and acceptance verification |

### 1.5 Definitions and Abbreviations

> See `docs/client/shared/glossary.md` for the full domain glossary.

| Term | Definition |
|---|---|
| [Term] | [Definition] |
| CR | Change Request |
| BR | Business Requirement |
| SRS | Software Requirements Specification |

---

## 2. System Overview

[2–3 paragraphs describing the system: what it does, the key actors, and how it fits into the broader business context. Avoid implementation details — focus on what the system must do and why.]

---

## 3. User Roles

| Role | Description | Access Level |
|---|---|---|
| [Role Name] | [Who they are and what they do] | [Admin / Standard / Read-Only] |
| [Role Name] | [Description] | [Access level] |

---

## 4. Functional Requirements

> Requirements are numbered [AREA-N] for traceability. Each requirement states what the system must do, not how.
> Requirements absorbed from Change Requests are noted with their CR reference.

### 4.1 [Feature Area 1, e.g. Customer Onboarding]

| ID | Requirement | Source |
|---|---|---|
| [AREA-001] | The system shall [requirement statement]. | PRD FR[N] |
| [AREA-002] | The system shall [requirement statement]. | CR-001 |

### 4.2 [Feature Area 2]

| ID | Requirement | Source |
|---|---|---|
| [AREA-001] | The system shall [requirement statement]. | PRD FR[N] |

<!-- Add sections for each major feature area. -->

---

## 5. Non-Functional Requirements

### 5.1 Regulatory Compliance

| ID | Requirement |
|---|---|
| NFR-REG-001 | [Compliance requirement, e.g. Must comply with AML and KYC obligations.] |

### 5.2 Security

| ID | Requirement |
|---|---|
| NFR-SEC-001 | [Security requirement, e.g. All PII must be encrypted at rest and in transit.] |

### 5.3 Availability & Reliability

| ID | Requirement |
|---|---|
| NFR-AVL-001 | [Availability requirement, e.g. The system must achieve 99.9% uptime during business hours.] |

### 5.4 Usability

| ID | Requirement |
|---|---|
| NFR-UX-001 | [Usability requirement.] |

### 5.5 Integration

| ID | Requirement |
|---|---|
| NFR-INT-001 | [Integration requirement, e.g. Must integrate with [System] via [protocol/format].] |

---

## 6. Out of Scope

- [Explicitly excluded feature or system]
- [Explicitly excluded feature or system]

---

## 7. Client Approval

> This section must be completed and signed before development begins on any requirement in this SRS.

| Name | Role | Decision | Date | Signature |
|---|---|---|---|---|
| | | Approved / Rejected / Needs Revision | | |

**Approval Notes:**
> Any conditions, clarifications, or amendments agreed at the time of approval.

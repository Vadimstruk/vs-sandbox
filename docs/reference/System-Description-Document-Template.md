# System Description Document (SDD)
**[Project Name]**

> **Document type:** Living document — updated continuously as the system evolves.
> This is not a specification written upfront. It describes the system **as it exists today**.

---

| Field | Value |
|---|---|
| **Project** | [Project Name] |
| **Client** | [Client Name] |
| **Version** | v1.0 |
| **Last Updated** | [DD MMM YYYY] |
| **Maintained By** | [BA Name] |
| **Status** | Active / Archived |

---

## How to Use This Document

This document is structured around **features and modules**, not sprints or stories. When a feature changes, update the relevant section — do not create a new page per sprint.

**Update triggers (add to Definition of Done):**
- A story changes existing behaviour → update the relevant feature section
- A new integration is added → update Section 4
- A business rule changes → update Section 3 and the relevant feature section
- A release goes live → update the Change Log

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [User Roles](#2-user-roles)
3. [Business Rules](#3-business-rules)
4. [Feature Descriptions](#4-feature-descriptions)
5. [Integrations](#5-integrations)
6. [Data & Calculations](#6-data--calculations)
7. [Non-Functional Characteristics](#7-non-functional-characteristics)
8. [Known Limitations & Technical Debt](#8-known-limitations--technical-debt)
9. [Change Log](#9-change-log)

---

## 1. System Overview

### 1.1 Purpose

[2–3 sentences. What does this system do, and why does it exist? Write for someone encountering it for the first time.]

### 1.2 Business Context

[Brief description of the client's business and the problem this system solves. What did they do before this system existed?]

### 1.3 Key Facts

| Item | Detail |
|---|---|
| **System type** | Web app / Mobile app / API / Internal tool |
| **Hosting** | [e.g., Azure, AWS, on-premise] |
| **Primary users** | [e.g., HR managers, end customers, internal ops team] |
| **Active since** | [Date / Sprint] |
| **Current version** | [Version or release label] |

### 1.4 High-Level Architecture

> 📌 Insert or link to a system context diagram here.
> Recommended: draw.io, Miro, Lucidchart — export as image and embed.

**Key components:**
- **Frontend:** [e.g., React web app]
- **Backend:** [e.g., Node.js REST API]
- **Database:** [e.g., PostgreSQL]
- **Auth:** [e.g., Azure AD / Auth0 / custom]
- **External systems:** [List key integrations — detail in Section 5]

---

## 2. User Roles

All roles that interact with or are affected by the system. Keep this updated as roles are added or change.

| Role | Description | Key Permissions / Capabilities |
|---|---|---|
| [Role 1] | [Who they are] | [What they can do in the system] |
| [Role 2] | [Who they are] | [What they can do in the system] |
| [Role 3] | [Who they are — may be external, e.g. client's client] | [What they can do] |

> 💡 If you have a detailed permissions matrix, link to it here rather than duplicating it.

---

## 3. Business Rules

Rules that govern how the system behaves, independent of technical implementation. When rules change, update this section and note the change in the Change Log.

| ID | Rule | Applies To | Last Updated |
|---|---|---|---|
| BR-001 | [e.g., A user cannot approve their own submission] | [Feature / Module] | [Date] |
| BR-002 | [e.g., All monetary values are stored and displayed in GBP] | System-wide | [Date] |
| BR-003 | [Rule] | [Feature] | [Date] |

---

## 4. Feature Descriptions

One section per major feature or module. This is the core of the SDD — keep each section current.

---

### 4.1 [Feature / Module Name — e.g., User Authentication]

**Status:** ✅ Live | 🚧 In Development | ⚠️ Partially Complete | ❌ Deprecated

**Summary:**
[2–3 sentences describing what this feature does and why it exists.]

**Current behaviour:**
- [Specific behaviour 1 — how it works today, not how it was originally designed]
- [Specific behaviour 2]
- [Specific behaviour 3]

**Business rules that apply:**
- BR-001: [Rule summary]
- BR-002: [Rule summary]

**Key user flows:**

1. **[Flow name — e.g., Standard login]**
   - User navigates to login page
   - User enters email and password
   - System validates credentials against [auth provider]
   - On success: user is redirected to dashboard
   - On failure: error message shown, account locked after 5 attempts

2. **[Flow name — e.g., SSO login]**
   - [Steps]

**Edge cases & exceptions:**
- [e.g., If the user's account is deactivated, they see a specific error and are directed to contact support]
- [e.g., Password reset tokens expire after 24 hours]

**Known limitations:**
- [e.g., Does not support biometric login — planned for Q3]

**Related Jira epics / stories:** [PROJ-001], [PROJ-045]
**Wireframes / designs:** [Link to Figma or Google Drive]

---

### 4.2 [Feature / Module Name — e.g., Dashboard]

**Status:** ✅ Live

**Summary:**
[Description]

**Current behaviour:**
- [Behaviour]

**Business rules that apply:**
- [Rules]

**Key user flows:**

1. **[Flow name]**
   - [Steps]

**Edge cases & exceptions:**
- [Cases]

**Known limitations:**
- [Limitations]

**Related Jira epics / stories:** [Links]
**Wireframes / designs:** [Links]

---

### 4.3 [Feature / Module Name]

> 📋 *Copy the section template above for each additional feature or module.*
> Recommended: one H3 section per major feature. Sub-features can be H4 within that section.

---

## 5. Integrations

All external systems the product connects to. Update when integrations are added, changed, or removed.

| ID | System | Direction | Data Exchanged | Trigger | Notes |
|---|---|---|---|---|---|
| INT-001 | [System name] | Inbound / Outbound / Both | [What data] | [Real-time / Scheduled / On-demand] | [Auth method, version, etc.] |
| INT-002 | [System name] | Outbound | [What data] | [Trigger] | [Notes] |

**Integration detail — INT-001: [System Name]**

- **Purpose:** [Why this integration exists]
- **Authentication:** [e.g., OAuth 2.0, API key, webhook secret]
- **Endpoint / API version:** [e.g., v2.1 REST API]
- **Data sent:** [Fields / format]
- **Data received:** [Fields / format]
- **Error handling:** [What happens when it fails]
- **Documentation:** [Link to API docs or internal spec]

---

## 6. Data & Calculations

### 6.1 Key Data Entities

The main data objects the system manages. For a full data dictionary, link below.

| Entity | Description | Key Fields | Notes |
|---|---|---|---|
| [Entity 1] | [e.g., User — stores account and preference data] | id, email, role, created_at | [Notes] |
| [Entity 2] | [e.g., Order — represents a client transaction] | id, status, total_amount, user_id | [Notes] |
| [Entity 3] | [Description] | [Fields] | [Notes] |

**Full data dictionary:** [Link to Google Sheets / Confluence page]

### 6.2 Calculation Logic

For any business-critical calculations, document the rules here. Link to spreadsheets for complex formulas.

| Calculation | Rule / Formula | Where Used | Source |
|---|---|---|---|
| [e.g., VAT calculation] | [e.g., net_amount × 0.20] | [Invoice module] | [Link to Google Sheet] |
| [e.g., Eligibility score] | [Formula description or link] | [Assessment module] | [Link] |

### 6.3 Data Retention & Privacy

| Item | Detail |
|---|---|
| **Retention period** | [e.g., User data retained for 7 years post-account closure] |
| **PII fields** | [List fields containing personal data] |
| **Regulatory obligations** | [e.g., UK GDPR — right to erasure supported via admin panel] |
| **Data residency** | [e.g., All data stored in UK/EU Azure regions] |

---

## 7. Non-Functional Characteristics

How the system performs in practice — updated to reflect reality, not just original targets.

### 7.1 Performance

| Metric | Target | Current Status | Notes |
|---|---|---|---|
| Page load time | < 3 seconds | ✅ ~1.8s average | Measured in production |
| API response time | < 500ms (p95) | ⚠️ ~620ms under high load | Optimisation planned Q2 |
| Concurrent users supported | 100 | ✅ Tested to 150 | Load test [date] |

### 7.2 Security

| Control | Implementation | Status |
|---|---|---|
| Data in transit | TLS 1.2+ | ✅ Enforced |
| Password storage | bcrypt (cost factor 12) | ✅ |
| Access control | Role-based (RBAC) | ✅ |
| [Compliance requirement] | [Implementation] | [Status] |

### 7.3 Availability & Reliability

| Item | Detail |
|---|---|
| **Target uptime** | 99.5% excluding maintenance |
| **Actual uptime (last 6 months)** | [%] |
| **Maintenance window** | [e.g., Sundays 02:00–04:00 UTC] |
| **Incident log** | [Link to incident register] |

---

## 8. Known Limitations & Technical Debt

Be honest here. This section is for the team, not the client.

| ID | Description | Impact | Priority | Planned Fix |
|---|---|---|---|---|
| TD-001 | [e.g., Search does not support partial matching — full text only] | Medium — affects UX | Medium | Q3 backlog |
| TD-002 | [e.g., PDF generation times out for reports over 500 rows] | High — workaround in place | High | Sprint 24 |
| TD-003 | [Description] | [Impact] | [Priority] | [Plan or TBD] |

---

## 9. Change Log

Record significant changes to the system here — especially behaviour changes, rule changes, and deprecated features. Minor bug fixes do not need to be logged.

| Date | Version / Sprint | Change Summary | Affected Section | Author |
|---|---|---|---|---|
| [DD MMM YYYY] | Sprint 12 | [e.g., Password lockout threshold changed from 3 to 5 attempts] | 4.1 Auth | [Name] |
| [DD MMM YYYY] | v1.2 | [e.g., VAT calculation updated to support zero-rated items] | 6.2 Calculations | [Name] |
| [DD MMM YYYY] | Sprint 8 | [e.g., Dashboard widget removed — replaced by new reporting module] | 4.2 Dashboard | [Name] |

---

*Last reviewed: [DD MMM YYYY] | Next scheduled review: [DD MMM YYYY]*

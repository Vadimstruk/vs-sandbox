# Handover / KT Document — [Product Name] — YYYY-MM-DD

> **Type:** Operational guide for the client to operate the system independently after the engagement ends or the team changes. One file per handover event, dated.
> **Handover date:** YYYY-MM-DD
> **Trigger:** [Project end / Team change / Contract end / Scope-down]
> **Owner:** BA (with PM and Tech Lead input)
> **Profiles:** All
> **Confluence:** [URL — pending]

---

## 1. Scope of Handover

[What is being handed over — the full system, a module, operational responsibility for X. Be explicit about what is *not* in scope of this handover.]

**Includes:**
- [Component / responsibility 1]
- [Component / responsibility 2]

**Does not include:**
- [Anything explicitly excluded — e.g. ongoing maintenance contract, third-party-vendor relationships]

---

## 2. System Architecture Summary

[2–4 paragraphs at handover-level — what the system does, the major components, where they run. Reference (do not duplicate) the SDD as the living detail. This section is for someone who will not have the BA in the room to ask.]

- **Reference:** see `docs/client/sdd/system-description.md` for the living detail.

---

## 3. Deployment Procedures

| Step | What | Where | Owner after handover |
|---|---|---|---|
| 1 | [Build] | [CI/CD pipeline location] | [Role] |
| 2 | [Deploy] | [Environment, command, automation] | [Role] |
| 3 | [Verify] | [Health-check, smoke-test] | [Role] |

---

## 4. Accounts, Credentials & Access

> Sensitive credentials are *not* in this document. They are transferred via [secure channel — e.g. password manager handover, sealed envelope, encrypted vault].

| System | Account / role | Owner before | Owner after | Transfer method | Status |
|---|---|---|---|---|---|
| [System] | [Role / account] | [Org] | [Org] | [Method] | Pending / Transferred |

---

## 5. Monitoring, Alerting & Observability

| Tool | Purpose | URL / Console | Alert routing | Runbook link |
|---|---|---|---|---|
| [e.g. Sentry] | [Error tracking] | [URL] | [Where alerts go] | [Runbook] |
| [e.g. CloudWatch] | [Infra monitoring] | [URL] | [Where alerts go] | [Runbook] |

---

## 6. Support & Escalation

| Issue type | First point of contact | Escalation path |
|---|---|---|
| [Production outage] | [Role / on-call] | [Path] |
| [Bug — non-blocking] | [Role] | [Path] |
| [Feature request] | [Role / process] | [Path] |

**Post-handover support window** *(if any):* [Duration, scope, SLA]

---

## 7. Known Issues & Open Items

| Item | Severity | Workaround | Target resolution |
|---|---|---|---|
| | | | |

---

## 8. Runbooks & Operational References

- **Deployment runbook:** [path]
- **Incident response runbook:** [path]
- **Common-tasks runbook:** [path]
- **Database operations:** [path]
- **Disaster-recovery procedure:** [path]

---

## 9. Knowledge Transfer Sessions

| Date | Topic | Presenter | Attendees | Recording |
|---|---|---|---|---|
| YYYY-MM-DD | [Topic] | [Name] | [Names] | [URL — if recorded] |

---

## 10. Outstanding Risks & Dependencies

[Any item from the RAID Log that remains unresolved at handover and the client needs to track. Reference the RAID Log entry; do not duplicate detail.]

---

## 11. Handover Sign-off

| Name | Role | Decision | Date | Signature |
|---|---|---|---|---|
| [Client representative] | | Accepted | | |
| [Relevant representative] | | Delivered | | |

---
type: bmad-distillate
sources:
  - "../charter-review-call-transcript.csv"
downstream_consumer: "Homer (Relevant BA agent) — applies updates to Project Charter, Product Roadmap, RAID Log, Stakeholder Register, Vision"
created: "2026-04-30"
token_estimate: 2050
parts: 1
---

## Meeting Context
- 2026-04-30 charter review call; attendees Marcus Chen (CEO FieldPulse Solutions), Priya Krishnan (CTO FieldPulse), Vadim (BA Relevant Software); both clients pre-read all three docs (Charter, Vision, Roadmap brief) night before
- Overall reaction: Charter approved with minor edits; Vision approved no changes; Roadmap conditional approval pending Marcus seeing the document (was not attached)

## Charter Edits Requested (must apply before DocuSign)
- Charter §2 Objective 2: reword from "compress billing-cycle time-to-invoice from current ~2-day pattern to same-day pattern" to "enable same-day billing"; rationale: cannot guarantee same-day for customers (depends on their internal accounting), only that data is available same-day; Marcus's load-bearing phrase: "enable same-day billing"
- Charter §3 Out of Scope: add explicit exclusion "no in-app payment collection from end-customers"; rationale: customers have asked about technician taking credit card on the spot, want it excluded so it doesn't creep in
- Charter §4 Regulatory constraint: phrasing "flow-down implications unknown and require legal review" is accurate but must be promoted to top-level open item in §5 Risks (not buried in constraints); rationale: most likely thing to bite us
- Charter §7 Stakeholders: add Jenna Rodriguez email jenna@fieldpulse.io to register on next pass
- Charter §4 Constraints/Tomás retainer: Priya note — Tomás 5-hours/week retainer is verbal, not contractual; flag for risk register if material

## Charter Items Approved As-Written
- §1 Project Overview (PulseField Mobile working title acceptable; possible rebrand at launch is a marketing call later)
- §2 Objective 3 churn numbers (6 last year, 3 in Q1, ~8% directly attributed) — keep as-is
- §3 In-Scope MVP ranking confirmed: (1) job assignment delivery, (2) completion capture, (3) signature, (4) sync, (5) schedule view — "the order I'd defend if anyone asked"
- §3 Cut-from-MVP list approved; Marcus signal: GPS-based arrival check-in is most likely candidate to push back into scope mid-project if budget allows (not asking now)
- §4 Offline-by-default constraint phrasing "material architectural implications for state management and conflict resolution" — "don't soften it"
- §4 Timeline constraint quote "Solid product in early Q4 over a shaky one in Q3" — direct quote, stands by it
- §4 Budget envelope $180K–$250K — confirmed, no change
- §5 Risks & Assumptions approved as written; Marcus wants full RAID Log this week (referenced but not seen)
- §6 Milestones approved structurally; MVP-definition milestone dependency on Priya's architecture one-pager confirmed real
- §7 Stakeholders approved (Dave Martinez confirmation pending — see D-004)

## Vision Document
- Approved, no changes ("tighter than Charter, nails it")
- §1 framing "nine customer businesses have left FieldPulse over the last twelve months" — rolling twelve-month window including Q1 2026, not calendar year; sharper than Marcus would have written
- §4 Success criteria: five criteria are right; 30% daily-active floor at month three is the criterion Marcus will hold most aggressively
- §6 "What This Product Is Not" — Marcus will forward internally to anyone asking "can we just add…"
- Priya: no engineering concerns

## Roadmap
- Marcus has NOT seen the Roadmap document — was not attached; must be resent before he commits to it as CR baseline
- Conditional approval: if Now/Next/Later structure follows kickoff discussion (MVP five features in Now, cut-from-MVP items in Next, broader integrations in Later), likely fine — but wants to lay eyes on it

## Decision: Auth Strategy (Auth0 from day one)
- DECISION: PulseField Mobile authenticates against Auth0 from day one (not custom-rolled with later migration)
- Rationale (Priya, accepted by Marcus): (1) building against custom auth then migrating = doing integration work twice, ~2-3 weeks mobile engineering wasted; (2) Auth0 provides mobile-friendly flows out of box (biometric login, refresh tokens, social login optional); custom auth doesn't and retrofitting for mobile is itself a project; (3) SOC 2 readiness — Auth0 is SOC 2 Type II certified; custom auth would be a SOC 2 audit finding
- Accepted dependency risk: if Auth0 migration slips past mobile launch readiness, mobile is blocked on dependency outside Relevant's control; Priya owns mitigation
- Mitigation pattern: mobile integrates against Auth0 in parallel environment from start; Auth0 doesn't require web platform migration for mobile to use it; mobile ships against Auth0 with web still on custom-rolled, web migrates later — both systems coexist briefly
- Auth0 migration current state: signed contract, account provisioned, PoC running in dev environment; realistic web cutover 4-6 months from today (Aug-Oct 2026), expected to slip
- Migration complexity driver: ~950 technician accounts + dispatcher + admin accounts with hashed passwords in custom system; planning Auth0 hash-import bulk flow but must validate hash format compatibility first
- ADR ownership: drafted by Relevant Tech Lead within two weeks, accepted by Priya; Priya needs intro to Tech Lead this week; Priya to prep short briefing on FieldPulse Auth0 setup so as not to waste Tech Lead's time on basics

## RAID Log Updates
- D-004 Sundance HVAC pilot: Marcus called Dave Martinez Friday, verbally committed; CHANGE — Dave will provide 3 technicians (not 2) as small team rotation, not solo testers; load-bearing phrase: "3 technicians team rotation, not solo testers" / "more realistic to how his shop works"; Dave wants one-page pilot summary before written commit; Vadim drafts one-pager, Marcus forwards; written-confirmation ETA two weeks once Dave has one-pager
- D-007 Marcus's Notion notes & whiteboard: cleaned Notion notes by end of this week (one cleanup pass first, half-formed content removed); whiteboard photo today, no cleanup
- D-008 Architecture one-pager: Priya delivers end of day Wednesday this week; expanded scope — includes API endpoint inventory plus architecture diagram (one extra day for inventory)
- D-009 Legal review: Marcus is slowest on this; no outside counsel today; relationship with small Austin firm (did incorporation) but not software/privacy specialists; plan — engage lawyer by end of next week, 2-3 week turnaround on findings, so findings land mid-to-late May, worst case early June; legal-review scope brief: (1) CCPA exposure assessment, (2) gov-contractor flow-down for school-district and municipal-building customers, (3) SOC 2 readiness gap analysis
- A-006 Regulatory exposure: no update from Marcus since kickoff; holding for legal review per D-009; concrete answers in May
- I-001 Data residency policy + I-002 Breach notification policy: drafted as part of SOC 2 work, NOT separately; owner Priya with input from D-009 lawyer; SOC 2 program kickoff late May, both policies drafted by July; Priya loops Vadim in on drafts in case anything affects mobile
- R-007 No design lead: Marcus rejects hiring contract designer (reasons: hiring delay, ramp-up time, another voice when team is small); decision — Relevant's UX Designer carries design weight with structured client reviews; required cadence: design review every two weeks, mockups walked through live (not sent as static files), decisions captured in writing after each review; Marcus's concern: "decisions getting made in conversation and forgotten"

## Charter Sign-Off Path
- DECISION: Marcus signs Charter now, does not hold for legal review (D-009)
- Rationale: holding sign-off for legal findings means six weeks of softer commitment on both sides; better to lock baseline today, accept v1.1 amendment may follow legal findings, let team move
- Sign-off condition: cover note from Vadim acknowledging v1.1 amendment is anticipated based on D-009 legal review, so it's clear both knew about open item at sign-off ("not a dispute later that I should have waited")
- Mechanism: DocuSign; Vadim sends after applying agenda-item-1 edits (Objective 2 wording, no-in-app-payment exclusion, regulatory promoted to open item); Marcus signs within 48 hours of receipt

## Cadence & Communications
- Weekly status calls: Wednesday 9am Central (locked); Tuesday rejected ("too close to Monday recovery"); 30 minutes hard stop
- Friday EOD written updates: confirmed; recipients Marcus + Priya; short bullets; "if longer than one screen on my laptop I'll bounce it back"
- Slack: workspace fieldpulse.slack.com exists; Priya creates channel #pulsefield-mobile today; invites Vadim, Relevant PM, Relevant Tech Lead; Vadim sends work emails by EOD
- CR threshold (confirmed as in Charter): under 10% scope change → Marcus sole sign-off; ≥10% → Marcus + Priya joint sign-off
- CR baseline clarification (NEW): scope change is measured against Roadmap baseline once Roadmap is signed off, NOT against Charter; Charter = high-level contract, Roadmap = working baseline; Tech Lead and PM must be clear on this

## Action Items — Marcus
- Send list of small Charter edits in writing — today (2026-04-30)
- Share whiteboard photo — today
- Share cleaned Notion notes (D-007) — end of this week
- Engage lawyer for D-009 — end of next week
- Forward Sundance one-pager to Dave Martinez once Vadim drafts — when received
- Send Tech Lead + PM work emails to Priya for Slack invites — EOD today

## Action Items — Priya
- Architecture one-pager with API endpoint inventory (D-008) — Wednesday EOD this week
- Create Slack channel #pulsefield-mobile and send invites — today
- Schedule intro to Relevant Tech Lead for Auth0 ADR conversation — this week
- Prep short briefing on FieldPulse Auth0 setup for Tech Lead
- Draft I-001 / I-002 policies as part of SOC 2 workstream — by July; loop Vadim in

## Action Items — Vadim / Relevant
- Apply Charter edits (Objective 2, no-in-app-payment Out-of-Scope, regulatory promoted to §5 open item, Jenna's email in Stakeholders, Tomás retainer verbal-not-contractual flag)
- Send revised Charter via DocuSign with cover note acknowledging anticipated v1.1 amendment per D-009
- Resend Roadmap document to Marcus (was not attached previously)
- Send full RAID Log to Marcus this week
- Draft Sundance pilot one-pager for Marcus to forward to Dave Martinez
- Tech Lead drafts Auth0 ADR within two weeks; Priya accepts
- Stand up bi-weekly design review cadence with live mockup walkthroughs and written decision capture (R-007 mitigation)

## Open Items / Dependencies
- Roadmap document review by Marcus (blocks Roadmap baseline lock and CR-threshold reference point)
- Full RAID Log delivery to Marcus (referenced in Charter §5, not yet seen)
- Legal review (D-009) — engagement by end of next week, findings mid-to-late May (worst case early June); blocks Charter v1.1 amendment, A-006 regulatory exposure answers
- Auth0 web migration timeline (Aug-Oct 2026) — slip risk could block mobile launch (mitigated by parallel-environment pattern but real)
- Auth0 hash-format compatibility validation for bulk import of ~950 technician + dispatcher + admin accounts
- Dave Martinez written agreement on Sundance pilot (~2 weeks after one-pager delivered)
- SOC 2 program kickoff late May; I-001 / I-002 policies depend on SOC 2 workstream; lawyer input from D-009 feeds in
- Auth0 ADR (Tech Lead two-week deliverable, Priya accepts)
- Architecture one-pager (D-008) — Wednesday EOD; MVP-definition milestone depends on it

## Named Entities & IDs
- People: Marcus Chen (CEO FieldPulse), Priya Krishnan (CTO FieldPulse), Vadim (BA Relevant), Jenna Rodriguez (FieldPulse, jenna@fieldpulse.io), Dave Martinez (Sundance HVAC), Tomás (5h/week verbal retainer, legacy platform)
- Organizations: FieldPulse Solutions, Relevant Software, Sundance HVAC, Auth0, unnamed Austin small law firm (incorporation counsel, not software/privacy specialist)
- Product: PulseField Mobile (working title, possible launch rebrand)
- IDs referenced verbatim: D-004, D-007, D-008, D-009, A-006, I-001, I-002, R-007
- Charter sections referenced: §1, §2 (Obj 2, Obj 3), §3 (In Scope, Cut from MVP, Out of Scope), §4 (Technical/Legacy, Offline-by-default, Timeline, Budget, Regulatory), §5, §6, §7, §8
- Slack: fieldpulse.slack.com, channel #pulsefield-mobile

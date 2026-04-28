# Kickoff Meeting — PulseField Mobile

> **Lifecycle:** This file started life as `kickoff-questionnaire-2026-04-28.md` (the questions to ask). Renamed and filled in with answers from the kickoff call held 2026-04-28. Source transcript: `docs/reference/kickoff-call-transcript.csv`.
> **Date held:** 2026-04-28
> **Attendees:** Marcus Chen (FieldPulse, Founder & CEO); Priya Krishnan (FieldPulse, CTO); Vadim — Business Analyst, Relevant Software.
> **Conducted by:** Vadim — BA, Relevant Software

---

## Reading Guide

Each question retains its pre-call tag — ✓ Known, ⚠ Confirm, ❓ Gap — so the lifecycle is visible. Answers below each question are paraphrased from the call (full transcript at `docs/reference/kickoff-call-transcript.csv`).

---

## 1. Project & Business Context

**1.1** ✓ **Known.** *Pain points still accurate?*
> _Answer:_ Confirmed. SMS-only assignments, technicians phoning office for context, paper-form data capture, end-of-day data entry — none of this has been mitigated since the brief was written.

**1.2** ✓ **Known.** *Total active-technician population? Other end-user groups?*
> _Answer:_ ~950 active technicians estimated across the customer base (~80 customers × ~12 technicians average). **Year-1 adoption target: 30–40%** — Marcus stated he'd be "thrilled" with that. **Office dispatchers are a confirmed secondary user group** — almost every FieldPulse customer has one. Customer-facing portal explicitly out of scope (future thing).

**1.3** ❓ **Gap — high priority.** *Success at 6mo / 12mo? Off-track signal?*
> _Answer:_
> - **6 months:** ≥20 of FieldPulse's existing customers actively using the mobile app with their technicians. Stop losing customers to ServiceTitan and Housecall Pro because of the mobile gap.
> - **12 months:** Mobile becomes a *reason customers choose* FieldPulse (positive acquisition driver), not just a reason they don't leave (defence).
> - **Concrete metric Marcus will own:** **billing-cycle time-to-invoice**. Today: paper at 6pm → next-morning entry → 2-day invoice. Target: same-day. This is the metric his customers complain about most.
> - **Off-track signal at 3 months:** technicians download but don't use it — DAU < 30% of installed base = something is wrong.
> - Marcus explicitly invited Vadim's help setting realistic targets.

**1.4** ✓ **Known.** *Specific churn number?*
> _Answer:_ **6 customers churned last year explicitly citing mobile** as the reason — ~8% of the 80-customer base. **3 more left in Q1 alone.** Marcus believes the real number is higher because customers who churned for "other reasons" likely had mobile as a contributing factor. This is the source of his anxiety.

**1.5** ⚠ **Confirm.** *Competing initiatives?*
> _Answer:_
> - **Auth0 migration** (Priya): FieldPulse is moving off a custom-rolled auth system this year. Not directly competing for budget, but **may overlap with mobile if the project touches login flows**. Worth coordinating.
> - **Customer Success hire** last month: onboarding capacity is improving — relevant for rollout planning.
> - No competing budget priorities.

---

## 2. Stakeholders & Decision Making

**2.1** ⚠ **Confirm.** *Sole sign-off authority?*
> _Answer:_ **Yes — Marcus has sole sign-off** on requirements and scope. **CR threshold:** under ~10% scope change → Marcus alone; ≥10% → Marcus + Priya (because of technical implications). No board to clear with — founder-funded plus a small *silent* angel round.

**2.2** ⚠ **Confirm.** *CR approver?*
> _Answer:_ Same as 2.1. Marcus for small CRs; Marcus + Priya for material CRs.

**2.3** ❓ **Gap — high priority.** *Day-to-day BA contact?*
> _Answer:_ **Marcus** is day-to-day BA contact ("I'd rather be the bottleneck than have you guessing"). **Priya is direct contact for the tech lead** on technical matters. Explicit ask: do not bypass either of them to other team members without checking — small company, things get messy.

**2.4** ❓ **Gap — high priority.** *UAT participants?*
> _Answer:_
> - **External pilot:** **Sundance HVAC** (Phoenix), owner **Dave Martinez** — has been asking for mobile for two years and offered to be a guinea pig. Plan: 2–3 of his technicians on a real-world pilot.
> - **Internal proxy:** **Jenna Rodriguez** (Customer Success Lead, FieldPulse) plus Marcus and Priya doing structured walkthroughs before exposure to Dave.
> - Caveat: Marcus needs to confirm the pilot with Dave before promising anything.

**2.5** ⚠ **Confirm.** *Other stakeholders?*
> _Answer:_ Jenna Rodriguez (already named); Dave Martinez later in the cycle. **No design lead at FieldPulse** — Marcus self-identified this as a gap. No investors who need to weigh in.

**2.6** ❓ **Gap.** *Turnaround SLAs?*
> _Answer:_
> - Normal items: **48 hours.**
> - Blockers: **same-day.**
> - Document reviews: **3 business days.**
> - Critical caveat from Marcus: **"I'm bad at long documents. If you give me a 40-page spec I will procrastinate. Shorter is better."**

**Internal note for BA — captured:** **Priya Krishnan**, priya@fieldpulse.io. Phone separately.

---

## 3. Domain & Regulatory

> **Marcus opened this section by acknowledging he'd "look least prepared" here.**

**3.1** ❓ **Gap.** *Regulation reaching the SaaS itself?*
> _Answer:_ Marcus believes nothing touches the software directly — HVAC and plumbing trades are regulated at the state level (licensing, code compliance), but only for the trade work, not the SaaS that supports it. **Honest gap: Marcus has never had a lawyer review this.** Worth a follow-up legal review before Charter sign-off.

**3.2** ❓ **Gap.** *Data protection / privacy?*
> _Answer:_
> - **CCPA applies.** FieldPulse has California customers, so CCPA reaches end-customer data flowing through the platform.
> - **No formal data residency policy.**
> - **No formal breach notification procedures.** Marcus realised mid-call this is a problem ("which I'm now realizing as I say it out loud is probably bad").
> - These gaps go straight into the RAID Log as Issues (I-001, I-002).

**3.3** ❓ **Gap.** *Customers passing regulatory obligations down?*
> _Answer:_ **Some FieldPulse customers do work for school districts and one municipal building.** Marcus doesn't know whether that pushes anything onto FieldPulse. None of FieldPulse's customers are healthcare-adjacent.

**3.4** ❓ **Gap.** *Audit / reporting obligations?*
> _Answer:_ Customer expectation (not regulatory): signed-job records kept **2–7 years for warranty and dispute purposes**. No regulatory audit history.

**3.5** ❓ **Gap.** *Security certifications?*
> _Answer:_ **SOC 2 is coming.** Three prospects asked about it in the last 6 months; FieldPulse lost at least one deal because of the lack. Marcus was planning to start the SOC 2 process this year regardless of the mobile project. **Hard requirement: PulseField Mobile must not be a barrier to SOC 2 readiness.**

---

## 4. Existing Systems & Integrations

**4.1** ✓ **Known.** *Other third-party services?*
> _Answer:_ Beyond the FieldPulse Web Platform: **Stripe** (payments), **Twilio** (SMS — for the existing assignment messages), **Google Maps** (embedded for routing), **SendGrid** (transactional email). **No push-notification provider yet** — to be added with the mobile app. Plus (from Priya, §4.4): Intercom (in-app chat on web), Sentry (error tracking), Mixpanel (analytics, lightly used), CloudFront.

**4.2** ❓ **Gap — high priority.** *(Priya.) API documentation, freelancer availability, last audit?*
> _Answer:_
> - **APIs exist** — RESTful, JSON, mostly sane. Inconsistent naming on some endpoints. **No formal API versioning.**
> - **Documentation:** a Postman collection from when the freelancer left, plus a README that's about **60% accurate**.
> - **Original freelancer: Tomás Ribeiro**, based in Lisbon. **Casual retainer ~5 hours/week for emergencies**, not actively developing. Reachable.
> - **Last touched:** ~4 months ago when adding a small reporting feature.
> - Priya's overall assessment: **"Okay — not great, not a disaster."**

**4.3** ❓ **Gap.** *(Priya.) Database / direct access?*
> _Answer:_ **PostgreSQL on AWS RDS.** **Priya's hard line: mobile app talks to the platform via API only — no direct DB access under any circumstances.**

**4.4** ⚠ **Confirm.** *(Priya.) Third-party services to inherit?*
> _Answer:_ Stripe, Twilio (covered), **Intercom** (web in-app chat — open question whether it should extend to mobile), **Sentry** (error tracking), **Mixpanel** (analytics, lightly used), **CloudFront** (CDN for AWS assets). No additional third parties.

**4.5** ❓ **Gap — high priority.** *Offline scenario?*
> _Answer:_ **Offline-by-default with sync-when-available** is the design target. Realistic technician contexts: basements, crawlspaces, mechanical rooms, new-construction sites with no service. A technician must be able to start a job, fill out a form, capture photos, and get a customer signature **fully offline**, with sync when back in signal. Marcus's framing: *"if we don't get this right, the app is dead on arrival."* Priya flagged the architectural implications for state management and conflict resolution as material.

---

## 5. Scope & Constraints

**5.1** ❓ **Gap — highest priority.** *Out of scope?*
> _Answer:_ **Confirmed exclusions** (from brief): customer-facing portal, admin/back-office UI redesign, web platform rewrite, payment-processing changes, expansion beyond HVAC and plumbing.
> **Added at kickoff:**
> - No marketing-website work.
> - No migration of historical job data into a new structure — the mobile app reads what's already there.
> - No integrations with third-party accounting software (e.g. QuickBooks) — separate roadmap item.

**5.2** ❓ **Gap — high priority.** *Platforms?*
> _Answer:_
> - **Both iOS and Android desired.**
> - **65/35 Android lean** (Marcus's estimate from looking at pilot customer's technician phones).
> - If forced to pick one for v1: **Android.**
> - **Phone only, no tablets** — most technicians don't carry tablets in the field.
> - Minimum OS (Priya): **Android 10+ and iOS 15+.**

**5.3** ❓ **Gap — highest priority.** *MVP feature list (ranked)?*
> _Answer:_
> 1. **Receive job assignment with full details** (replaces SMS + phone-back-to-office).
> 2. **Capture job completion data** — checklist, notes, photos, parts used, time on site — fully offline-capable.
> 3. **Customer signature capture** at job completion.
> 4. **Sync to web platform** when connectivity returns; surface in dispatcher view.
> 5. **Basic technician schedule view** — what's my day look like.
>
> **Cut from MVP** (Marcus's "love-but-willing-to-cut" list): in-app chat with dispatcher; GPS-based "I've arrived" auto check-in; parts inventory lookup; customer history view.

**5.4** ⚠ **Confirm.** *Driver behind EoQ3?*
> _Answer:_ **Rough preference, not hard commitment.** Driver: **ServiceTitan competitor pressure peaks Q4** going into the new year — Marcus wants something in technicians' hands before that sales push. **Tolerance: 1-month slip is fine, 3-month slip is not.** Stated preference: *"a solid product in early Q4 over a shaky one in Q3."*

**5.5** ❓ **Gap — highest priority.** *Budget envelope?*
> _Answer:_ **$180K–$250K earmarked for this initiative this year.** Above $250K = "hard conversation with myself and probably my angels". Below $180K = Marcus worries about cutting corners. Marcus explicitly asked: *"tell me sooner rather than later if it's unrealistic."*

**5.6** ⚠ **Confirm.** *US-only?*
> _Answer:_ **Confirmed US-only.** Two Canadian customers (both Ontario) are fine on the US version — no localisation needed. No expansion plans during the project window.

---

## 6. Existing Documentation & Prior Work

**6.1** ❓ **Gap.** *Pre-existing spec / wireframe / prototype?*
> _Answer:_ **No formal spec, no wireframes, no prototype.** Marcus has ~15 pages of Notion notes from customer conversations and a whiteboard sketch photo (~6 months old). **Both promised — Marcus to share.** *Open follow-up — see Section 9.*

**6.2** ✓ **Known.** *Source-code access? Tests?*
> _Answer:_ **Source code in FieldPulse's GitHub org** — fully owned. Tomás's documentation: partial. **Tests:** they exist, **~40% coverage**, integration tests are flakier than Priya would like (Priya).

**6.3** ✓ **Known.** *Working relationship with the freelancer?*
> _Answer:_ **Active, consultative basis** (5hr/week retainer covered in §4.2). No unresolved issues. *What worked:* Tomás shipped a working product on a tight budget. *What didn't:* one-person-show codebase — solo conventions, ramp-up time for new devs. No ill will, just outgrew the arrangement.

**6.4** ✓ **Known.** *Other vendor learnings?*
> _Answer:_ Two prior vendor quotes: **$400K / 9 months** (made Marcus cough); **$90K / 3 months** (made Priya laugh). Marcus picked Relevant because *"the conversation felt real."* Useful context: he doesn't fully trust either anchor figure.

---

## 7. Communication & Working Preferences

**7.1** ❓ **Gap.** *Day-to-day channel?*
> _Answer:_ **Slack — shared workspace, please.** Email for formal documents only. Marcus checks Slack constantly, batches email.

**7.2** ❓ **Gap.** *Status-call cadence?*
> _Answer:_ **Weekly, 30 minutes, same time every week.** **Tuesday or Wednesday mornings, US Central time.** Explicit: **not Mondays.**

**7.3** ❓ **Gap.** *Written status updates?*
> _Answer:_ **Marcus and Priya, weekly, end-of-Friday** (so Marcus can read it Monday morning). **Short, bullet points.** Explicit ask: *"please don't send me five-page status reports."*

**7.4** ❓ **Gap.** *Urgent escalation?*
> _Answer:_ **Slack DM Marcus first, Priya second.** If neither responds in **2 hours during business hours, escalate by phone**. Outside business hours: only true blockers.

**7.5** ❓ **Gap.** *Digital sign-off?*
> _Answer:_ **Yes — DocuSign or signed-PDF-by-email.** Marcus prefers digital ("we're a remote-first 12-person company, paper isn't really how we operate").

---

## 8. UAT & Go-Live

**8.1** ❓ **Gap.** *UAT performers?*
> _Answer:_ See §2.4. Primary: **Sundance HVAC pilot, 2–3 technicians, real-world use.** Internal proxy: **Jenna Rodriguez** plus Marcus and Priya doing structured walkthroughs first. **Non-technical users are the target** — *"if they can't use it intuitively the app has failed."*

**8.2** ❓ **Gap.** *Staging env / test data?*
> _Answer:_ **Yes — staging environment, separate from production.** **Synthetic data, not anonymised customer data** — privacy reasons plus FieldPulse's anonymisation tooling doesn't really exist. **Priya to set up** the staging instance with seeded synthetic jobs, technicians, and customers.

**8.3** ❓ **Gap — high priority.** *Go-live criteria (Marcus's draft, asks for refinement help):*
> _Answer:_
> - All MVP features functionally pass at **≥95% pass rate**.
> - **App Store + Play Store approval secured.**
> - **Sundance pilot completed** with at least **two weeks of real-world use** and **no Sev-1 issues**.
> - **Basic security review passed** — even if not full SOC 2, at minimum a checklist.
> - **Training materials delivered** to Sundance technicians (**short videos, not manuals**).
> - **Performance: app launches in under 3 seconds on mid-range Android.**
> - **Sync works reliably in low-connectivity simulation.**
> - Marcus invited refinement: *"that's off the top of my head — I'd want your help refining."*

**8.4** ❓ **Gap.** *Post-launch support?*
> _Answer:_ **Material scope ask: 60–90 days of post-launch support from Relevant** as part of the engagement, with a clear handoff plan to bring it in-house thereafter. Bug fixes, minor adjustments, helping FieldPulse understand production issues. **Not in original budget framing** — must be reflected in scope discussion. Captured as R-011 in RAID.

**8.5** ❓ **Gap.** *Blackout periods?*
> _Answer:_
> - **Worst — avoid:** **late June through August** (HVAC summer cooling peak — release-induced bugs would cost real customer trust).
> - **Soft windows:** **September, October.**
> - **Fine:** **mid-March through April.**
> - **Avoid:** the two-week windows around **Thanksgiving, Christmas, July 4th** (nobody around to fix things).

---

## 9. Open Items & Follow-Ups

| # | Open Item | Owner | Due Date |
|---|---|---|---|
| 1 | Confirm Sundance HVAC pilot with Dave Martinez (UAT participants) | Marcus | Before Roadmap baseline |
| 2 | Share Notion notes (~15 pages of customer conversations) and the whiteboard sketch photo | Marcus | Before MVP definition |
| 3 | One-pager on existing platform architecture for Relevant tech lead | Priya | Before next status call |
| 4 | Legal review of regulatory exposure (CCPA, gov-contractor flow-down, SOC 2 timeline) | Marcus | Before Charter v1.0 sign-off |
| 5 | Anchor-figure conversation: is $180K–$250K realistic for the proposed MVP scope? | Vadim → Marcus | Before Roadmap baseline |
| 6 | Refine go-live criteria collaboratively (Marcus invited input) | Vadim + Marcus | Before MVP delivery |
| 7 | Decide whether Intercom in-app chat extends to mobile | Marcus + Priya | At MVP definition |
| 8 | Coordinate with Auth0 migration timing if mobile touches login flows | Priya + Tech Lead | Before architecture decisions |

---

## 10. BA Notes

> Internal — not shared with client.

- **RAID items appended to `docs/client/raid-log.md`:** R-001/R-004 → Mitigated; A-001/A-002/A-003/A-004 → Confirmed; A-005 → Partially Invalidated (CCPA + SOC 2 + gov-contractor uncertainty); new R-006 SOC 2 readiness, R-007 no design lead, R-008 Auth0 overlap, R-009 absent data residency / breach policies, R-010 offline state-management complexity, R-011 60–90d post-launch support; new I-001 to I-004 (data residency, breach policies, design lead, anonymization tooling); D-001/D-002/D-003 → Confirmed; new D-004 Sundance pilot, D-005 Tomás continuing availability, D-006 Auth0 coordination.
- **Glossary terms added:** ServiceTitan, Housecall Pro (competitors); Sundance HVAC (pilot customer); Office Dispatcher; Offline-by-default / Sync-when-available; CCPA; SOC 2; DAU; Postman Collection; App Store / Play Store; Auth0.
- **Stakeholders added to Register:** Priya Krishnan (full name + email captured); Jenna Rodriguez (Customer Success Lead, FieldPulse); Dave Martinez (Owner, Sundance HVAC, Phoenix — pilot customer); Tomás Ribeiro (Original freelance dev, Lisbon, retainer 5hrs/week).
- **Promotion:** Charter v0.1 → v1.0 ready to route to Marcus. Stakeholder Register, Glossary, RAID Log refreshed. Next move: Vision (`VS`) and Roadmap baseline (`RM`).
- **Follow-ups for Vadim:**
  - Marcus asked Vadim *"what worried you most in what I just said?"* — that's a relationship-building moment. Suggested talking points: post-launch-support scope addition, the regulatory hand-waving combined with SOC 2 timing, and the "no design lead" gap.
  - Priya offered a one-pager on existing platform architecture before the next call — accept it; it directly addresses R-003.

---

## Section Coverage — actual call

| § | Section | Pre-call coverage | Post-call coverage |
|---|---|---|---|
| 1 | Project & Business Context | Mostly known | Closed — concrete metrics defined |
| 2 | Stakeholders & Decision Making | Partial | Closed — except Sundance pilot pending Dave Martinez confirmation |
| 3 | Domain & Regulatory | Gap | Partially closed — Marcus self-flagged hand-waviness; legal-review follow-up booked |
| 4 | Existing Systems & Integrations | Partial | Closed — Priya was prepared and detailed |
| 5 | Scope & Constraints | Gap (highest-priority) | Closed — MVP defined, budget anchored, timeline driver clear |
| 6 | Existing Documentation & Prior Work | Mostly known | Closed — Notion notes and sketch promised |
| 7 | Communication & Working Preferences | Gap | Closed |
| 8 | UAT & Go-Live | Gap | Mostly closed — go-live criteria invited collaborative refinement |

**Total actual time:** [to capture from Vadim — estimated 75–90 min based on substance].

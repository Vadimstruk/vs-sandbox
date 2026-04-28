# Meeting Notes — PulseField Mobile — 2026-04-30

> **Type:** Charter + Vision + Roadmap review (post-kickoff). Hybrid agenda — first comprehensive review since kickoff.
> **Lifecycle:** Post-call notes. Source planning artefact: `docs/.archive/meeting-agenda-2026-04-28.md` (planned for 2026-04-28; call slipped two days, content carried over).
> **Source transcripts:**
> - `docs/reference/charter-review-call-transcript.csv` (main session — Charter / Vision / Auth / RAID / sign-off / cadence)
> - `docs/reference/roadmap-review-transcript.csv` (Roadmap walk-through — Marcus had not seen the Roadmap before the call; reviewed top-to-bottom in the same session)
> **Conducted by:** Vadim — BA, Relevant Software

---

## 1. Attendees

| Name | Role | Organisation |
|---|---|---|
| Marcus Chen | Founder & CEO | FieldPulse Solutions |
| Priya Krishnan | CTO | FieldPulse Solutions |
| Vadim | Business Analyst | Relevant Software |

---

## 2. Pre-Read Materials

- Charter v1.0 — Marcus + Priya read end-to-end the night before; compared notes morning-of.
- Vision — read; minimal commentary.
- Roadmap 2026-04 — **not received before the call** (Marcus flagged: "you attached the Charter and Vision but not the Roadmap"). Reviewed live in-call from a fresh share.

---

## 3. Document Review

### 3.1 Charter v1.0 — approved with 5 small edits

| # | Section | Edit |
|---|---|---|
| 1 | §2 Objective 2 | Reframe *"compress billing-cycle time-to-invoice... to a same-day pattern"* → **"enable same-day billing"**. Marcus: *"We can't guarantee same-day invoicing — that depends on the customer's accounting workflow. What we can guarantee is that the data is available same-day."* |
| 2 | §2 Objective 3 | Keep as-is — Marcus confirmed numbers (6 last year + 3 in Q1, ~8% directly attributed). |
| 3 | §3 Out of Scope | Add **"No in-app payment collection from end-customers"** — explicitly exclude technician taking credit cards on the spot. |
| 4 | §4 Constraints — Regulatory | Promote the *"flow-down implications unknown / require legal review"* concern from Constraints to a **top-level open item in §5 Risks** — Marcus: *"It's the thing most likely to bite us, don't bury it."* |
| 5 | §7 Stakeholders | Add Jenna's email (**jenna@fieldpulse.io**) to the Stakeholder Register on the next pass. Dave Martinez subject to §5 confirmation below. |

**Other Charter remarks (no edit needed):**
- §1 working-title caveat fine (possible rebrand at launch — marketing call, not blocking).
- §3 MVP ranking confirmed (job assignment → completion → signature → sync → schedule view).
- §3 Cut-from-MVP: Marcus flagged GPS auto check-in (R-017) as the one *most likely* to push back into scope mid-project if budget allows — *not* a request, just signaling.
- §4 Constraints accepted as written. Priya's verbatim: *"the constraints section is the most accurate writeup of our platform's reality I've seen on paper."* "APIs are RESTful, JSON, mostly sane" called out as the right level of honesty.
- §4 Tomás retainer — Priya flag: **retainer is verbal, not contractual** (5hr/wk). Track as continuity risk.
- §4 Offline-by-default — *"don't soften it"* (Priya, on the line *material architectural implications for state management and conflict resolution*).
- §4 Timeline — *"solid product in early Q4 over a shaky one in Q3"* is a direct quote and Marcus stands by it.
- §5 Marcus asked for the **full RAID Log** to be sent across this week.
- §6 MVP definition milestone correctly depends on Priya's architecture one-pager (D-008) — discussed in §5 below.

### 3.2 Vision — approved, no changes

Marcus: *"This one I have less to say about because it's tighter than the Charter and I think it nails it."* Specific call-outs:
- The "nine customer businesses... over the last twelve months" framing is sharper than how Marcus would have written it.
- The five success criteria are the right five; **30% DAU floor at month three** is the one Marcus will hold us to most aggressively.
- §6 *"What This Product Is Not"* is the section Marcus will forward internally when anyone starts asking *"can we just add..."*.
- Priya: no technical concerns.

**Status:** Light agreement obtained. Vision continues as the North Star.

### 3.3 Roadmap 2026-04 — approved with 7 amendments

Marcus walked top-to-bottom. Approval is conditional on the amendments below being applied; Marcus wants the version-stamped Roadmap re-sent alongside the revised Charter for DocuSign.

| # | Initiative | Amendment |
|---|---|---|
| 1 | **R-008 Auth Strategy** | Status: Pending Decision → **Decided — Auth0**. PulseField Mobile authenticates against Auth0 from day one (see §4 below for full reasoning). |
| 2 | **R-011 App Store + Play Store Setup** | Call out **account provisioning starts in Q2** as a separate sub-task (Apple verification 2–4 wk lead time for new accounts) — listings happen later, but provisioning cannot wait until Q3. |
| 3 | **R-012 Sundance HVAC Pilot** | Status: Provisional → **Verbally Confirmed (Written Pending)**. **3 technicians** (team rotation per Dave, not solo testers). |
| 4 | **R-014 Training Materials** | Add **Jenna Rodriguez** as FieldPulse-side co-owner (she runs customer-facing rollout). |
| 5 | **R-015 Post-Launch Support** | **Inside the $180K–$250K envelope** (Marcus's call). Acknowledged that this may pressure MVP scope — **R-005 Schedule View is the first candidate to cut** if envelope is tight. |
| 6 | **R-006 Legacy API** | Wrapper / proxy layer is **planned, not conditional** (per Priya — naming-convention drift makes a wrapper cleaner long-term). |
| 7 | **R-003 Customer Signature** | Note that **2–7 year retention scope may firm up post legal review (D-009)** — could shift from customer expectation to contractual / regulatory; flag potential effort impact. |

**Directional input (notes on Roadmap, not amendments):**
- R-002 success signal *"Sundance pilot technicians complete ≥80% of pilot jobs through the app"* — Marcus: *"hold to it."* Strong measurable.
- R-004 *"≥80% same-day for pilot jobs"* — *"that's the headline business outcome — the one I'd defend hardest."*
- R-007 spike direction (Priya): instinct is **last-write-wins + clear conflict-banner UX** for the rare contested case; spike's call to confirm.
- R-009 SOC 2 framing *"PulseField Mobile is not a barrier to FieldPulse's parallel SOC 2 work"* — Marcus: *"that's the right framing."*
- R-010 Staging — Priya target: ≥50 synthetic jobs and 10 synthetic technicians up by **mid-May**.
- R-022 Analytics — Marcus interested as **post-launch revenue lever** (mobile-derived analytics surfaced as customer-success conversation tool); stay-on-radar even though Later.
- R-023 Office Dispatcher Mobile — Marcus does not expect to do this in the project window (dispatchers are at desks); keep as Later placeholder.
- Capacity assumption (BA + PM + TL + 2 mobile devs + QA + p/t DevOps + p/t UX) — Marcus saw the internal note. **Confirm team shape at next status call** before assuming it.

**Open prioritisation questions answered:**
1. Now-bucket scope — **confirmed** (with the 3 amendments above).
2. Next-bucket sequencing if budget headroom appears — **R-016 Dispatcher Chat first**, **R-019 Customer History second**, **R-017 GPS Auto-Check-in third**, **R-018 Parts Inventory fourth**.
3. Post-launch support pricing — **inside envelope** (per amendment 5).
4. Sundance pilot timing — **anchor pilot to *finish* before Phoenix HVAC peak** (mid-July through August brutal). Pilot ends end-of-June ideally, **early July latest**.

---

## 4. Auth Strategy Direction — Decision Locked

**Decision: PulseField Mobile authenticates against Auth0 from day one.**

**Priya's input (timeline + recommendation):**
- Auth0 already signed; account provisioned; PoC running in dev.
- Realistic web-platform cutover: **4–6 months** from today → **Aug–Oct 2026**. *"And these things always slip."*
- Hardest part: user migration (~950 technician + dispatcher + admin accounts with hashed passwords in custom system). Bulk import via Auth0 hash-import flow, validating hash format compatibility.
- Strong recommendation to build mobile against Auth0 from day one:
  1. Building against custom-rolled auth and migrating later = **2–3 weeks of mobile engineering wasted**.
  2. Auth0 gives mobile-friendly flows out of the box (biometric, refresh tokens, social if ever needed).
  3. SOC 2 readiness — Auth0 is SOC 2 Type II certified; custom-rolled auth would be a SOC 2 finding.
- **Risk acknowledged:** Auth0 migration could slip past mobile launch readiness. **Mitigation:** mobile integrates against a **parallel Auth0 environment** from the start — Auth0 doesn't require web platform to be migrated for mobile to use it. Both systems coexist briefly.

**Marcus:** *"That's the answer I was hoping you'd give. I trust your read on this. Decision: PulseField Mobile authenticates against Auth0 from day one. We accept the dependency risk on Auth0 migration and Priya owns the mitigation."*

**ADR ownership:** Drafted by Relevant Tech Lead **within 2 weeks** of the call (target ~2026-05-14). Accepted by Priya. Priya prepping a short briefing on FieldPulse's Auth0 setup so the Tech Lead is not figuring out basics. **Tech Lead intro scheduled this week.**

---

## 5. Open RAID Items — Status Updates

| ID | Item | Update from Call |
|---|---|---|
| **D-004** | Sundance HVAC pilot | Marcus called Dave Martinez Friday 2026-04-24. **Verbally committed.** **3 technicians** (team rotation). Dave wants a one-page pilot summary before written commitment. **Realistic written-confirmation ETA: 2 weeks once Dave has the one-pager.** Vadim drafts the one-pager → Marcus forwards. |
| **D-007** | Marcus's Notion notes + whiteboard sketch | **Whiteboard photo:** Marcus shares **same-day (2026-04-30)** — no cleanup needed. **Notion notes:** Marcus does one cleanup pass first; cleaned version delivered by **EoW Friday 2026-05-02**. |
| **D-008** | Priya's architecture one-pager | Draft exists. Priya extending **one extra day** to include the **API endpoint inventory** (not just architecture diagram). Realistic delivery: **EoD Wed (~2026-05-06) — confirm with Priya**. R-006 6-week clock starts on receipt. |
| **D-009** | Legal review | Marcus does not yet have outside counsel. Path: either engage existing Austin firm (incorporation counsel — not privacy specialists) with a defined scope, or find privacy-specialist firm. **Lawyer engaged by EoW 2026-05-08.** **Scope brief Marcus will give counsel:** CCPA exposure assessment, gov-contractor flow-down (school-district + municipal-building customers), SOC 2 readiness gap analysis. Turnaround: **2–3 weeks post-engagement**. **Findings: mid–late May**, worst case **early June**. |
| **A-006** | Regulatory exposure | No update from Marcus's side since kickoff. **Holding for D-009.** Marcus comes back with concrete answers in May. |
| **I-001 / I-002** | Data residency + breach-notification policies | **Drafted as part of SOC 2 program**, not separately. **Owner: Priya**, with input from D-009 lawyer. SOC 2 program kickoff scheduled **late May 2026**. Both policies drafted by **July 2026**. Priya loops Vadim in if anything affects mobile. |
| **R-007 (RAID)** | No design lead at FieldPulse | Marcus opted **not to hire a contract designer** — reasons: hiring delay, ramp-up time, another voice in a small room. **Mitigation:** Relevant UX Designer carries design weight; **bi-weekly design review cadence** with mockups walked through **live, not as static files**; **decisions captured in writing after each review** (Marcus's worry: decisions made in conversation get forgotten). |

---

## 6. Charter Sign-Off Path — Decided

**Decision: Marcus signs Charter v1.1 now, does not wait for legal review.**

**Reasoning:** Holding sign-off until mid-May means six weeks of softer commitment on both sides. Marcus prefers to lock the baseline today, accepting that legal-review findings (D-009) may produce a **v1.2 amendment** later, and let the team move.

**Condition for signing:** A short **cover note** at sign-off acknowledging that v1.2 amendment is anticipated based on D-009 legal review — *"so it's clear we both knew about the open item at sign-off. Not a dispute later that I should have waited."*

**Mechanism:** **DocuSign**. Sent once Vadim has applied the small Charter edits (§3.1 above) — Marcus signs **within 48 hours** of receiving v1.1.

**Send-together:** Marcus wants the **revised Charter v1.1 + amended Roadmap 2026-04 v1.1 + full RAID Log + Sundance pilot one-pager** in one transmission.

---

## 7. Cadence & Comms — Locked

| Item | Decision |
|---|---|
| **Weekly status calls** | **Wednesday 9am Central, 30 min hard stop.** Tuesday declined ("too close to Monday recovery"). |
| **Friday written status updates** | EoF, bullet points, **≤1 screen on Marcus's laptop** ("if it's longer than one screen I'll bounce it back"). Recipients: Marcus + Priya. |
| **Slack workspace** | **fieldpulse.slack.com** — channel **`#pulsefield-mobile`** to be created by Priya same-day (2026-04-30). Invites for Vadim + PM + Tech Lead. |
| **CR threshold** | <10% scope: Marcus alone. ≥10% scope: Marcus + Priya jointly (both sign-offs needed). |
| **CR baseline clarification** *(new)* | **Scope change is measured against the Roadmap baseline once Roadmap is signed off, not against the Charter.** Charter is high-level contract; Roadmap is the working baseline. Tech Lead and PM must be clear on this. |

---

## 8. Decisions Made

| # | Decision | Made By |
|---|---|---|
| 1 | Charter v1.0 → v1.1 with 5 small edits; Marcus signs v1.1 via DocuSign within 48hr of receipt; cover note acknowledges anticipated v1.2 post-D-009 legal review. | Marcus |
| 2 | Vision approved as-is. Light agreement obtained. | Marcus |
| 3 | Roadmap 2026-04 approved with 7 amendments → version-stamp v1.1; living doc, no signature required. | Marcus |
| 4 | PulseField Mobile authenticates against Auth0 from day one. ADR by Tech Lead within 2 weeks; accepted by Priya. | Marcus + Priya |
| 5 | Sundance HVAC pilot — verbally confirmed; 3 technicians team rotation; written agreement pending one-pager from Relevant. Pilot ends before Phoenix peak (early July latest). | Marcus + Dave Martinez (verbal) |
| 6 | Post-launch support (R-015) priced **inside the $180K–$250K envelope**; MVP scope may flex, R-005 Schedule View first to cut if needed. | Marcus |
| 7 | Next-bucket return order if budget headroom appears: Dispatcher Chat → Customer History → GPS Auto Check-in → Parts Inventory. | Marcus |
| 8 | Data-residency + breach-notification policies drafted under SOC 2 program (Priya owner, lawyer input); drafts by July 2026. | Marcus + Priya |
| 9 | No contract designer — Relevant UX leads with bi-weekly design reviews, live walkthroughs, decisions captured in writing. | Marcus |
| 10 | Cadence locked: Wed 9am Central / 30 min · EoF Friday written ≤1 screen · Slack `#pulsefield-mobile` · CR baseline = Roadmap once signed off. | Marcus + Priya |

---

## 9. Action Items

### Relevant Software *(Vadim unless noted)*

| # | Action | Owner | Due |
|---|---|---|---|
| A1 | Apply 5 Charter edits → **Charter v1.1**; archive v1.0 | Vadim | 2026-04-30 |
| A2 | Apply 7 Roadmap amendments → **Roadmap 2026-04 v1.1**; update internal notes with prioritisation answers | Vadim | 2026-04-30 |
| A3 | Update **RAID Log** with all status changes from §5 + Auth0 closure + Tomás-retainer-verbal risk + new dependencies | Vadim | 2026-04-30 |
| A4 | Update **Stakeholder Register** — Jenna email + R-014 co-owner; Dave verbally confirmed | Vadim | 2026-04-30 |
| A5 | Send DocuSign package: Charter v1.1 + Roadmap v1.1 + RAID Log + Sundance pilot one-pager + cover note | Vadim → Marcus | 2026-05-01 (target — depends on A6) |
| A6 | Draft **Sundance pilot one-pager** for Marcus to forward to Dave | Vadim | 2026-05-01 |
| A7 | Send work emails of PM + Tech Lead to Priya for Slack invites + Auth0 ADR intro | Vadim | EoD 2026-04-30 |
| A8 | **Auth0 ADR** drafted by Tech Lead | Tech Lead (TBC) | ~2026-05-14 |
| A9 | Confirm Priya's *"Wednesday EoD"* delivery date for D-008 (likely 2026-05-06, not the already-passed 2026-04-29) | Vadim | 2026-04-30 |

### FieldPulse

| # | Action | Owner | Due |
|---|---|---|---|
| B1 | Send written list of Charter edits (his words, sign-off audit trail) | Marcus | 2026-04-30 |
| B2 | Share whiteboard sketch photo (no cleanup) | Marcus | 2026-04-30 |
| B3 | Share cleaned Notion notes (~15 pages, after one cleanup pass) | Marcus | EoW 2026-05-02 |
| B4 | Engage outside counsel — scope brief: CCPA + gov-contractor flow-down + SOC 2 readiness gap | Marcus | EoW 2026-05-08 |
| B5 | Forward Sundance one-pager to Dave Martinez once received | Marcus | On receipt |
| B6 | Architecture one-pager + API endpoint inventory | Priya | EoD Wed (~2026-05-06 — TBC) |
| B7 | Slack channel `#pulsefield-mobile` + invites to Vadim, PM, Tech Lead | Priya | 2026-04-30 |
| B8 | Auth0 setup briefing for Relevant Tech Lead | Priya | This week |
| B9 | Auth0 ADR review + acceptance | Priya | After A8 |
| B10 | DocuSign Charter v1.1 | Marcus | Within 48hr of receipt |

---

## 10. Any Other Business — Marcus's Parting Question

> *"Vadim — same question as last time. What worries you most after this conversation?"*

**For Vadim's response *(BA-prepared talking points, internal):***

- **Auth0 dependency risk is now real, not hypothetical.** Mobile launch readiness depends on a parallel-environment Auth0 strategy that Priya owns. If FieldPulse's Auth0 migration slips and the parallel environment becomes more complex than she's modelling, mobile is exposed. Mitigation is sound on paper but unproven at scale (~950 accounts).
- **Legal-review findings could hit Charter v1.2 with material scope.** CCPA + gov-contractor flow-down + SOC 2 gap analysis — three vectors, each capable of pulling new requirements (audit logging, data-classification, consent flows, contractual flow-down language). Six weeks of build between sign-off and findings means we may be partly down the wrong road.
- **Capacity assumption is unverified.** The Roadmap's Now bucket (11 initiatives) is sized to a $180K–$250K envelope assuming a specific team shape. Marcus saw the internal note. If the team is smaller or part-timers are thinner than we modelled, we're already over-committed at sign-off — and R-015 envelope-pressure on MVP scope kicks in earlier than Marcus expects.
- **Quietly: the design-review cadence is the most fragile mitigation.** Bi-weekly cadence depends on Marcus + Jenna having time and live attendance. First missed review and the *"decisions made in conversation and forgotten"* failure mode reappears.
- **Cheap to address, but real:** Tomás's retainer is verbal not contractual. If he becomes unavailable mid-engagement, the legacy-platform discovery loop slows.

**Tone guidance:** Marcus rewards candour from kickoff. Be specific, not hedged. Lead with Auth0 + legal-review pair (the structural ones). Tomás + capacity + design-cadence are the closing-paragraph items, not the headline.

---

## 11. BA Internal Notes *(not shared with client)*

- **Charter v1.1 is the version Marcus signs.** Cover note signals **v1.2 anticipated** post-D-009 legal review.
- **Roadmap 2026-04 v1.1** is the live CR baseline going forward. Per Marcus's clarification, CR scope is measured against this, not the Charter.
- **D-008 date ambiguity:** Priya said *"EoD Wednesday this week"* on Thursday 2026-04-30. Wed of the calendar week (4/29) had already passed. Most plausible reading: **next Wednesday 2026-05-06**. Confirm with Priya ASAP — R-006 6-week clock starts on receipt.
- **R-005 cut-line:** if the post-launch-support envelope decision pressures MVP scope, R-005 (Technician Schedule View) is the first candidate to cut. Marcus surfaced this himself — not a unilateral call.
- **Auth0 parallel-environment** is the de-risking mechanism on the new dependency. Mobile uses Auth0 from day one regardless of web-platform migration timing.
- **CR baseline = Roadmap (once signed off):** this clarification matters operationally. Add to Charter §4 governance row so PM + Tech Lead don't measure CR scope against Charter §3.
- **Documents to send Marcus in one DocuSign package:** Charter v1.1 + Roadmap 2026-04 v1.1 + full RAID Log + Sundance pilot one-pager. Cover note attached.
- **Capacity assumption:** confirm at next status call (Wed 2026-05-06).

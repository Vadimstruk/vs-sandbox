# Meeting Agenda — PulseField Mobile — 2026-04-28

> **Lifecycle:** Pre-call agenda. Rename to `meeting-notes-2026-04-28.md` after the call with answers, decisions, and action items filled in.
> **Type:** First post-kickoff status call. Hybrid: Vision + Roadmap validation, prioritisation decisions, open-item check.
> **Duration target:** 45 minutes (longer than the standing 30-min weekly cadence to absorb the Vision/Roadmap walk-through; ongoing weekly calls return to 30 min).
> **Conducted by:** Vadim — BA, Relevant Software

---

## 1. Attendees

| Name | Role | Organisation |
|---|---|---|
| Marcus Chen | Founder & CEO | FieldPulse Solutions |
| Priya Krishnan | CTO | FieldPulse Solutions |
| Vadim | Business Analyst | Relevant Software |
| *(Invite if available)* PM, Tech Lead | | Relevant Software |

---

## 2. Pre-Read Materials *(sent before the call — confirm reviewed)*

- `docs/client/charter/project-charter-v1.0.md` — Charter v1.0 (routed for sign-off)
- `docs/client/vision/product-vision.md` — Product Vision (light agreement requested)
- `docs/client/roadmap/product-roadmap.md` — Product Roadmap 2026-04 (CR baseline going forward)
- `docs/client/meetings/kickoff-meeting-2026-04-28.md` — Kickoff Meeting Notes (for reference)

---

## 3. Vision Validation *(5 min — light agreement)*

> Goal: confirm the Vision captures Marcus's strategic intent. No formal sign-off — light agreement is the Vision's lifecycle norm.

- [ ] **Why this product exists** — defending against ServiceTitan / Housecall Pro mobile gap; ~9 customers churned over 12 months citing mobile.
- [ ] **Who it's for** — primary technicians (~950); secondary office dispatchers (confirmed at kickoff).
- [ ] **Success indicators** — ≥20 customers actively using @ 6mo; same-day billing-cycle compression; mobile becomes acquisition driver @ 12mo; DAU ≥30% by month 3.
- [ ] **What this product is not** — no customer-facing portal, no platform rewrite, no vertical expansion.

**Decision sought:** Light agreement to proceed with this Vision as the North Star for Roadmap and Charter sign-off.

---

## 4. Roadmap Walk-Through *(15 min — light agreement + decisions)*

> Goal: validate the structure (4 themes / Now-Next-Later) and surface the 4 prioritisation decisions before this becomes the live CR baseline.

### Quick walk-through

- [ ] **4 themes:** T-1 Mobile-First Field Workflow · T-2 Operational Readiness · T-3 Customer Adoption & Rollout · T-4 Platform Modernisation Alignment.
- [ ] **Now (11 initiatives):** the 5 MVP features + 6 enabling initiatives (legacy API discovery, offline architecture, auth strategy, SOC 2 foundations, staging environment, store setup).
- [ ] **Next (8 initiatives):** Sundance pilot, production rollout, training, post-launch support, plus the 4 cut-from-MVP features as provisional.
- [ ] **Later (5 initiatives):** strategic placeholders — iOS parity, push expansion, analytics, dispatcher mobile, accounting integrations.

### Prioritisation decisions to make on this call

> These are the 4 questions captured in the Roadmap's Internal Notes section. Each needs an answer (or an explicit *"come back next call"*) before the Roadmap can be treated as a live CR baseline.

**4.1. Now-bucket scope vs the $180K–$250K envelope.**
> Is the 11-initiative Now bucket the right scope for the 2026 envelope? Specifically: should any Now-bucket initiative move to Next, or any cut-from-MVP feature move from Next to Now?
> _Decision:_

**4.2. Next-bucket sequencing — which cut-from-MVP feature returns first if budget headroom appears post-launch.**
> The four cut-from-MVP features (in-app chat, GPS auto check-in, parts inventory, customer history) are all in Next as provisional. Which is highest-priority to return first?
> _Decision:_

**4.3. Post-launch support pricing approach.**
> R-015 (60–90 days post-launch support from Relevant) is in Next. Pricing inside the $180K–$250K envelope, or a separate scope conversation post-MVP?
> _Decision:_

**4.4. Sundance pilot timing relative to HVAC summer peak.**
> Pilot must end before late June (HVAC summer-cooling peak blackout, C-007). Targets late Q3 currently — does Marcus want it earlier (May–June) or after the peak (September)?
> _Decision:_

**Decision sought overall:** Light agreement to treat Roadmap 2026-04 as the live CR baseline going forward.

---

## 5. Auth Strategy Direction *(5 min — R-008 in Roadmap, RAID R-008)*

> Goal: get directional alignment so Tech Lead can drive the ADR. Decision must land before R-001 (Job Dispatch & Receive) implementation begins, or rework risk is real.

- [ ] **Question:** Does PulseField Mobile authenticate against the existing custom-rolled FieldPulse auth, or against the new Auth0 implementation FieldPulse is migrating to in 2026?
- [ ] **What we need:** Priya's view on Auth0 migration timeline; Marcus's view on whether mobile launch should wait for Auth0 or proceed against custom-rolled and migrate later.
- [ ] **Outcome:** ADR drafted by Tech Lead within 2 weeks of this call, accepted by Priya.

_Direction:_

---

## 6. Open RAID Items Requiring Confirmation *(10 min)*

| ID | Type | Item | Status Needed |
|---|---|---|---|
| **D-004** | Dependency | **Sundance HVAC pilot agreement** — has Marcus spoken to Dave Martinez? Is Dave confirmed for 2–3 technicians on a real-world pilot? | Confirm / Pending |
| **D-007** | Dependency | **Marcus's Notion notes (~15 pages of customer conversations) and the whiteboard sketch photo.** | Share now / Date for share |
| **D-008** | Dependency | **Priya's one-pager on existing platform architecture** (Priya offered at kickoff close — directly addresses R-003 Legacy integration risk). | Share now / Date for share |
| **D-009** | Dependency | **Legal review** — CCPA exposure, gov-contractor flow-down (school-district / municipal customers), SOC 2 timeline. | Date for engagement / Status |
| **A-006** | Assumption | **Regulatory exposure** — Partially Invalidated at kickoff. Any update from Marcus's side since? | Update or hold for legal review |
| **I-001 / I-002** | Issue | **No formal data-residency or breach-notification policies.** Does FieldPulse plan to draft these as part of SOC 2 work, or separately? | Plan + owner |
| **R-007** | Risk | **No design lead at FieldPulse.** Does Marcus want to engage a contract designer, or have Relevant's UX Designer carry the weight with structured reviews? | Direction |

---

## 7. Charter v1.0 Sign-Off Path *(3 min)*

- [ ] Charter v1.0 routed to Marcus for sign-off. Two paths to discuss:
  - **Sign now**, accept that any legal-review findings (D-009) will come back as a v1.1 amendment.
  - **Hold sign-off** until D-009 legal review lands.
- [ ] Marcus's preference: digital sign-off via DocuSign or signed-PDF-by-email (kickoff §7.5).

_Decision:_

---

## 8. Cadence & Comms Confirmation *(2 min)*

- [ ] **Weekly 30-min status calls** — confirm Tuesday or Wednesday morning Central time. Lock the day.
- [ ] **End-of-Friday written status updates** — short bullet points, sent to Marcus + Priya.
- [ ] **Slack workspace** — confirm setup status; channel name; access for Vadim + PM + Tech Lead.
- [ ] **CR threshold confirmation** — <10% scope: Marcus alone; ≥10% scope: Marcus + Priya.

_Confirmations:_

---

## 9. New Client Requests *(held space — capture, do not commit)*

> If Marcus or Priya raises something new in the call, capture here. Triage after the call (`TR` capability). No scope commitments mid-call.

| # | Request | Raised By | Notes |
|---|---|---|---|
| | | | *BA note: route through `TR`; CR before any work begins* |

---

## 10. Any Other Business *(2 min)*

> Open floor — anything Marcus or Priya wants to raise.

-

---

## 11. Decisions Made

> Filled during / after the call. The Decisions Made list will be emailed to Marcus + Priya as the written record.

| # | Decision | Made By | Date |
|---|---|---|---|
| | | | |

---

## 12. Action Items

> Every action has an owner and a due date.

| # | Action | Owner | Due |
|---|---|---|---|
| | | | |

---

## BA Internal Notes *(not shared with client)*

- **Marcus's parting question from kickoff** — *"What worried you most in what I just said?"* — best raised in §10 (AOB) once the structured agenda is done. Suggested talking points: post-launch support scope addition, regulatory hand-waving × SOC 2 timing, no-design-lead gap. Read Marcus's tolerance for candour in the moment; this is a relationship-building conversation, not a project-status one.
- **Time pressure cues** — if Marcus rushes, prioritise §4 (Roadmap decisions) and §6 (RAID confirmations). §5 (Auth) and §7 (Charter sign-off) can be Slack follow-ups. §3 (Vision) can be a *"any objections?"* check rather than walk-through if pre-read confirms agreement.
- **Watch for** — new requests in §9. Anything material is a CR conversation, not a same-call commitment.
- **Capture for next call** — anything that doesn't land here goes onto next week's agenda.
- **Documents to update after the call:** Charter (if sign-off lands), Roadmap change-log (if any prioritisation shifts), RAID Log (statuses for confirmed dependencies), Stakeholder Register (if any new names surface).

---

## Section Coverage Summary *(for BA's own pacing)*

| § | Topic | Time | Priority |
|---|---|---|---|
| 3 | Vision validation | ~5 min | Medium — should land quickly |
| 4 | Roadmap walk-through + 4 decisions | ~15 min | **Highest** |
| 5 | Auth strategy direction | ~5 min | High |
| 6 | RAID confirmations | ~10 min | High |
| 7 | Charter sign-off path | ~3 min | Medium |
| 8 | Cadence & comms | ~2 min | Low — quick lock |
| 9, 10 | New requests / AOB | ~5 min | Reserve |

**Target total: 45 min.** If running short, defer §7 (Charter sign-off — Slack-able) and §8 (cadence — Slack-able). Protect §4, §5, §6.

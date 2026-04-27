---
name: create-user-story
description: >
  Generate client-facing Epics and User Stories from BA artefacts. Use this skill whenever
  the user wants to create, write, or generate user stories or epics for client review —
  even if they say "write some stories for this feature", "turn this into tickets", "create
  epics from this PRD", or "prepare stories for the client call". Trigger when the input is
  any BA artefact: a Change Request (CR), a Roadmap initiative being promoted to Now, an
  SRS or SRS section, a client-facing PRD, a project charter, kick-off questionnaire
  responses, a business case, meeting notes, an RFP, or a plain feature description. The
  output is client-readable (no technical implementation detail), Jira-compatible, and
  structured as a clean handoff package for the BMad SM workflows (Create Epics & Stories
  / Create Story). Trigger proactively whenever context suggests requirements are being
  prepared for client review or sprint planning.
---

# User Stories Skill

Generates **client-facing** Epics and User Stories from BA artefacts. Output is written in
plain business language — no implementation detail, no technical jargon — suitable for client
review, approval, and sign-off. Once approved by the client, these stories serve as the
handoff input for a developer to create BMad's technical Epics/Stories independently.

**This skill does not produce BMad stories.** It produces the BA-owned artefact that precedes
and informs them.

---

## Audience principle

Every word of output must be readable by a non-technical client stakeholder. Apply this test
to every sentence before writing it:

> *"Would a business owner or product owner understand this without a developer in the room?"*

If no — rewrite it. Specifically:
- No references to APIs, databases, data models, or architecture
- No implementation verbs: "integrate", "query", "endpoint", "render", "parse", "schema"
- No technology names unless the client explicitly named them in the input
- Error/edge case AC should describe the *user experience*, not the system behaviour

---

## Where this skill fits in the workflow

This skill produces the **BA-side, client-readable** Epic/Story breakdown. The technical Jira-side counterpart is produced separately by the BMad SM workflows (`Create Epics & Stories` for bulk, `Create Story` for per-feature). Run order: this skill first → client review/approval → BMad SM workflow consumes the approved breakdown.

Primary trigger points by methodology profile:

| Profile | When this skill runs | Typical input |
|---|---|---|
| Waterfall | Once after SRS sign-off (bulk) | SRS or SRS section |
| Agile — Fixed-Range | At each Now/Next promotion on the Roadmap | Roadmap initiative (R-XXX) |
| Agile — Capacity-Based | At each Next → Now promotion on the Roadmap | Roadmap initiative (R-XXX) |
| All Agile profiles | Per-feature, when a CR's scope is large enough to warrant Epic + multiple Stories | Change Request (CR-XXX) |

Note: most CRs in Agile do **not** need this skill — the CR template already carries client-readable Acceptance Criteria and Business Rules & Edge Cases, and BMad SM's `Create Story` consumes the CR directly. Use this skill only when a CR introduces enough scope to justify a multi-Story breakdown for client review.

---

## Step 1 — Parse and Classify Input

Accepted input types (use whatever is provided — do not require a specific format):

**Framework-aligned inputs (preferred — produce traceable Epics):**
- **Change Request (CR-XXX)** — per-feature breakdown when the CR's scope warrants Epic + multiple Stories
- **Roadmap initiative (R-XXX)** — bulk breakdown when an initiative is promoted to Now (Agile)
- **SRS or SRS section** — bulk breakdown after SRS sign-off (Waterfall)
- **Client-facing PRD or PRD section** — initial scope breakdown (all profiles)

**Ad-hoc inputs (use as exploratory; output won't carry stable source IDs):**
- Project charter, kick-off questionnaire responses, business case
- Meeting notes or transcript summary
- RFP or client-supplied requirements document
- Plain feature description

When input is a CR, Roadmap initiative, or SRS section, **the source ID must appear in the output Epic block** (see Step 3 — Epic block format) so the breakdown stays traceable to the artefact that authorised it.

From the input, identify:
- **Functional areas** — what distinct parts of the product are covered?
- **Actors / user roles** — who uses each feature? Use the client's own language for roles.
- **Goals** — what business outcome does each feature serve?
- **Scope signals** — is this one focused feature or a broad capability with multiple workflows?
- **Source ID** — if the input is a CR / Roadmap initiative / SRS section, capture the ID for the Epic block.

If the input is ambiguous or incomplete, state assumptions explicitly in an **Assumptions**
block at the top of the output. Do not silently invent scope.

---

## Step 2 — Determine Hierarchy Depth

Choose depth based on scope of input:

| Signal | Depth |
|---|---|
| Single focused feature | Epic → Story |
| Multiple related workflows or user roles | Epic → Feature → Story |
| Broad product area spanning many features | Epic → Feature → Story |

Default to the shallowest structure that accurately represents the scope. Do not add hierarchy
levels to appear thorough — a flat Epic → Story set is often the right answer.

Sub-tasks are not used in client-facing stories. They belong in the developer's BMad artefact.

---

## Step 3 — Output Format

Produce a single cohesive block the BA can copy directly into Jira or share with the client
as a document. Use this structure:

### Epic block

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EPIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary      : [Short business-language title — max 10 words]
Source       : [CR-XXX | R-XXX (Roadmap version YYYY-MM) | SRS §X.Y | — for ad-hoc]
Description  : [1–2 sentences. What business capability does this deliver and why does
               it matter to the client? No tech detail.]
Story Points : —
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The `Source` field is mandatory when the input is a CR, Roadmap initiative, or SRS section. Use `—` only for ad-hoc / exploratory runs from charters, meeting notes, or plain feature descriptions where no stable upstream ID exists yet.

### Feature block (only when using 3-level hierarchy)

```
  ┌─ FEATURE
  │  Summary      : [Short business-language title]
  │  Description  : [1 sentence. What group of related stories does this feature cover?]
  │  Story Points : —
```

### Story block

```
    ┌─ STORY
    │  Summary      : As a [role], I want to [action] so that [benefit]
    │  Description  : [Optional. 1–3 sentences of business context. Include only if the
    │                  summary alone doesn't fully convey scope. No tech detail.]
    │  AC           :
    │    1. ✅ [Happy path — what the user sees when everything works]
    │    2. ⚠️ [Error or edge case — what the user sees when something goes wrong]
    │    3. 🔒 [Permission or access rule — who can or cannot do this, and what they see]
    │  Story Points : —
    │  Labels       : [functional area tag, e.g. registration / payments / reporting]
    └──────────────────────────────────────────────
```

**Icon key:**
- ✅ Successful / happy path outcome
- ⚠️ Warning, validation, or error condition
- 🔒 Access, permission, or role boundary

Numbers allow precise reference during reviews (e.g. "AC 3 fails"). Icons provide instant
visual grouping. Use both on every AC line. Icons can repeat — a story may have multiple
✅ or ⚠️ items. Always start with at least one ✅ (happy path) before listing edge cases.

---

## Step 4 — Acceptance Criteria Quality Rules

Each story must have **at least 2 AC items**. Always cover:
1. The happy path (the primary successful user journey)
2. At least one edge case or error condition, described as a user experience
3. Any role or permission boundary, if relevant

**AC must be written from the user's perspective, not the system's.**

| ❌ System-perspective (avoid) | ✅ User-perspective (use) |
|---|---|
| "The API returns a 200 response" | "The user sees a confirmation message" |
| "The database record is updated" | "The updated information is visible on the profile page" |
| "Validation fires on null input" | "If the field is left empty, the user sees a clear error before the form submits" |

AC items must be concrete enough that a QA engineer can write a test case without asking
follow-up questions. If you find yourself writing "the system behaves correctly" — stop and
rewrite with a specific observable outcome.

---

## Step 5 — Story Splitting Heuristics

If a story feels too large, split using one of these patterns:

- **By workflow step** — one story per meaningful step in a multi-step process
- **By actor** — separate stories for different roles doing the same thing differently
- **By CRUD operation** — create / view / edit / delete as separate stories where each
  has meaningfully different behaviour or AC
- **By happy path vs. exception path** — split complex error flows into their own story
- **By MVP vs. enhancement** — core behaviour now, nice-to-have polish as a separate story

A story is likely too large if:
- Its AC list exceeds 5 items
- It covers more than one distinct user goal
- A client would need to make multiple separate approval decisions about it

---

## Step 6 — Dev Handoff Note

Append this block once at the very end of the output, after all stories:

```
─────────────────────────────────────────────────────────────────
📋 HANDOFF NOTE FOR DEVELOPER

These are client-facing stories — they describe *what* the system
should do from a business perspective, not *how* to build it.

Once approved by the client, hand off to BMad SM:
  • Bulk decomposition  → run "Create Epics & Stories"
  • Single new story    → run "Create Story" (per item)

The BMad SM workflow will produce the technical Jira-side version
with implementation detail, architecture references, and full
context. The Source ID on each Epic (CR-XXX / R-XXX / SRS §X.Y)
ties the technical version back to its authorising artefact.

Story Points: left blank — estimated during sprint planning.
─────────────────────────────────────────────────────────────────
```

---

## Step 7 — Confluence Publishing (optional)

After presenting the full output to the user, ask exactly this question:

> **Would you like to publish this to Confluence?** (yes / no)

### If the user says **no** — stop here. No further action.

### If the user says **yes**:

1. **Save the output to a temporary markdown file.**
   Write the full generated output (everything from the first Epic block through the Dev
   Handoff Note) to a temp file, e.g. `user_stories_output.md` in the current directory.

2. **Confirm the page title.**
   Default to the first Epic summary as the page title. Ask the user:
   > *"I'll use **[Epic summary]** as the Confluence page title — is that correct, or would you like a different title?"*
   Wait for confirmation before proceeding.

3. **Check required environment variables.**
   Auth credentials are read automatically from `.mcp.json` (`atlassian-confluence` server env).
   Only one env var must be set manually. If it is missing, tell the user and stop:
   - `CONFLUENCE_SPACE_KEY` — the target Confluence space key (e.g. `VSSB2`)
   - `CONFLUENCE_PARENT_PAGE_ID` — *(optional)* numeric ID of a parent page

   Env vars `CONFLUENCE_BASE_URL`, `CONFLUENCE_USER_EMAIL`, and `CONFLUENCE_API_TOKEN` can
   still be set to override `.mcp.json` values if needed.

4. **Run the publish script.**
   Execute the following command:
   ```
   python ".claude/skills/create-user-story/publish_to_confluence.py" user_stories_output.md "[page title]"
   ```
   Stream the script output to the user so they can see progress.

5. **Report the result.**
   - On success: show the Confluence page URL returned by the script.
   - On failure: show the error, suggest the most likely fix (wrong space key, bad token, etc.), and ask if the user wants to retry.

6. **Clean up** the temporary markdown file after a successful publish.

---

## Output checklist (verify before presenting)

- [ ] No technical jargon, implementation detail, or technology names (unless client-supplied)
- [ ] Every story follows "As a [role], I want [action] so that [benefit]"
- [ ] Every story has at least 2 AC items written from the user's perspective
- [ ] AC items are concrete and observable, not vague system descriptions
- [ ] Story Points field present and set to `—` on every item
- [ ] Labels field present on every story
- [ ] Hierarchy depth is appropriate for input scope (not over-engineered)
- [ ] Assumptions block included if any input was ambiguous or incomplete
- [ ] Source field on every Epic block — populated with CR-XXX / R-XXX / SRS §X.Y, or `—` only for ad-hoc inputs
- [ ] Dev handoff note appended at the end

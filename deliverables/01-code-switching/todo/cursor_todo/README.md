# Cursor TODO: Deliverable 01 — Code-Switching + "Kitchen Table Arabic"

This folder contains actionable task breakdowns for Deliverable 01, organized by phase and deliverable.

**Source**: `faithtech-readmes/deliverables/01-code-switching.md`

---

## Overview

**Goal**: Build a listening pipeline that works on:
- Levantine Arabic (Lebanese + Syrian)
- Code-switching (Arabic + English and/or French)
- Noisy, emotional voice notes (WhatsApp-style)

**Success Criteria**: System preserves code-switched words, crisis/triage phrases, named entities, and emotion-carrying cues on a representative evaluation set.

---

## Task Files

1. **[Phase A — MVP Decision](phase-a-mvp-decision.md)** (1 hour)
   - Confirm interaction model and constraints

2. **[T1 — Top 20 Code-Switching Patterns](t1-patterns.md)** (2–3 days)
   - Create markdown table with patterns, examples, and failure modes

3. **[T2 — Audio Sample Pack](t2-audio-pack.md)** (2–5 days)
   - Collect/label 50–100 clips with consent and privacy handling

4. **[T3 — Technical Pipeline Spec](t3-pipeline-spec.md)** (1–2 days)
   - Define prosody-preserving voice processing pipeline

5. **[T4 — Baseline Model Comparison](t4-baseline-comparison.md)** (1–2 days)
   - Test candidate models and compare results

6. **[T5 — Decision Making](t5-decision.md)** (same week)
   - Analyze results and decide next steps

7. **[T6 — Acceptance Criteria Demo](t6-demo.md)** (end-of-sprint)
   - Produce demo artifact with representative clips

---

## Owner(s)

- **PM/Lead**: TBD
- **Translation/Linguistics**: TBD
- **Engineering/ML**: TBD
- **Field partners**: TBD

## Team Roles

- **Translation/Linguistics**: Define top-20 patterns; verify transcripts; build "dictionary of pain" phrases
- **Field partners (Lebanon/Syria)**: Help source ethically consented audio; validate realism
- **Engineering/ML**: Run inference benchmarks; build pipeline; store metadata; document model configs
- **Product**: Define what errors are unacceptable (harm-based prioritization)

---

## Definition of Done

- [ ] Top-20 code-switch patterns written as markdown table (with examples + failure modes)
- [ ] Audio Sample Pack spec written and usable; initial clip set collected or simulated substitute approved
- [ ] Prosody-preserving pipeline spec written (ingestion → preprocessing → output metadata → low-confidence handling)
- [ ] Acceptance criteria demo can be run end-to-end on at least a few representative clips

---

## Notes

- All outputs should be stored in `faithtech-readmes/deliverables/`
- Reference research notes in `faithtech-readmes/research/` as needed
- Prioritize P0 patterns (safety-critical) first
- Keep transcripts verbatim (don't "clean" into MSA)
- Preserve emotional prosody and code-switches over perfect accuracy

---

## Template for Future Deliverables

Copy/paste and fill in:

### Deliverable XX — <name>

- **Source**: `faithtech-readmes/deliverables/XX-<slug>.md`
- **Owners**: PM/Lead, Translation/Linguistics, Engineering/ML, Field partners
- **Definition of Done**: 3–6 bullet points
- **Tasks**:
  - DXX.T1 — <output 1>
  - DXX.T2 — <output 2>
  - DXX.T3 — <output 3>
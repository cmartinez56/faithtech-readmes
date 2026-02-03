# T2 — Audio Sample Pack

**Duration**: 2–5 days  
**Output**: `faithtech-readmes/deliverables/01-code-switching.audio-pack.md`  
**Owner**: Field partners + Translation/Linguistics team

---

## Goal

Create a safe/ethical Audio Sample Pack with 50–100 clips that is decision-grade for model selection.

---

## Spec + Governance Tasks

- [ ] **T2.1**: Write minimum pack spec:
  - 50–100 clips
  - 15–45 seconds each
  - Mix: Lebanese + Syrian voices, emotional states, background noise, code-switch frequency

- [ ] **T2.2**: Define consent + privacy handling:
  - Consent status per clip (recorded field)
  - Rules for PII removal (re-record vs beep vs exclude)
  - Retention policy (where stored, who can access)

- [ ] **T2.3**: Define labeling schema (decision-grade, lightweight):
  - Human reference transcript (verbatim)
  - Code-switch tokens flagged (exact En/Fr words)
  - Triage phrase flags (self-harm, threat, urgent medical, coercion, panic)
  - Optional emotion tag (only if it changes triage)

- [ ] **T2.4**: Create labeling template (CSV/JSON or markdown per clip)

---

## Clip Acquisition Tasks (choose one path)

- [ ] **T2.5A (preferred)**: Source real clips with consent via field partners; document provenance

- [ ] **T2.5B (fallback)**: Create simulated equivalents (acted, privacy-safe) matching:
  - Lebanese + Syrian accents
  - WhatsApp/noisy conditions
  - Realistic code-switch frequency

---

## Pack Readiness Tasks

- [ ] **T2.6**: Ensure coverage targets met (dialect/emotion/noise/code-switch distribution)

- [ ] **T2.7**: Spot-check labels for consistency (especially code-switch token marking)

- [ ] **T2.8**: Produce "pack index" (one page):
  - Clip IDs, duration, dialect guess, code-switch level, consent, flags

---

## Coverage Targets

- **Dialects**: Mix of Lebanese + Syrian voices
- **Emotional states**: Neutral → distressed
- **Background noise**: Street, tent, kids, TV
- **Code-switch frequency**: Low/medium/high

---

## Notes

- All clips must have documented consent status
- Remove or beep personal identifiers if required
- Keep transcripts verbatim (don't "clean" into MSA)
- Focus on decision-grade labels (not perfect, but usable for model selection)

---

## Next Steps

After T2 is complete, proceed to:
- **[T4 — Baseline Model Comparison](t4-baseline-comparison.md)** (uses audio pack)
- **[T6 — Acceptance Criteria Demo](t6-demo.md)** (uses audio pack)

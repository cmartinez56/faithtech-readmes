# T3 — Technical Pipeline Spec: Prosody-Preserving Voice Processing

**Duration**: 1–2 days  
**Output**: `faithtech-readmes/deliverables/01-code-switching.pipeline-spec.md`  
**Owner**: Engineering/ML team

---

## Goal

Define the "don't destroy the signal" spec for the engineering pipeline that preserves emotional prosody and code-switches.

---

## Tasks

- [ ] **T3.1**: Define audio ingestion requirements:
  - Accepted formats
  - Sample rate policy
  - Channel handling (mono/stereo)

- [ ] **T3.2**: Define safe-default preprocessing (conservative):
  - Noise reduction: minimal
  - VAD: keep pauses (avoid over-trim)
  - Segmentation: short chunks but preserve phrase boundaries

- [ ] **T3.3**: Define transcript output metadata requirements:
  - Timestamps per segment
  - Confidence scores
  - Pause lengths / speech rate proxies
  - Non-speech events if detectable (laughter/crying tags)

- [ ] **T3.4**: Define low-confidence handling:
  - Thresholds
  - Fallback model or alternate decoding strategy
  - When to request repetition / human review

- [ ] **T3.5**: Define baseline model comparison protocol (reproducible):
  - Which models (per T4)
  - Decoding settings to try (beam size, temperature, language hints)
  - Metrics to report

- [ ] **T3.6**: Define "preserve what matters" metrics:
  - Code-switch token preservation rate
  - Triage phrase recall (do not miss)
  - Named entity retention (where applicable)
  - Qualitative notes on emotion-carrying cues (pauses/hesitations)

---

## Key Principles

- **Conservative preprocessing**: Don't destroy emotional prosody
- **Preserve pauses**: They carry meaning
- **Metadata-rich output**: Timestamps, confidence, pause info
- **Fail gracefully**: Handle low-confidence cases

---

## Notes

- This spec should be implementable by the Engineering/ML team
- Reference models from T4 when defining comparison protocol
- Focus on metrics that matter for downstream understanding (not just WER)

---

## Next Steps

After T3 is complete, proceed to:
- **[T4 — Baseline Model Comparison](t4-baseline-comparison.md)** (uses this spec)
- **[T6 — Acceptance Criteria Demo](t6-demo.md)** (uses this spec)

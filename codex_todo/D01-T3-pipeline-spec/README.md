# D01.T3 — Prosody-preserving voice processing pipeline spec

**Output file**: `deliverables/01-code-switching.pipeline-spec.md` (create)

## Checklist

- [ ] Define audio ingestion requirements:
  - accepted formats
  - sample rate policy
  - channel handling (mono/stereo)
- [ ] Define safe-default preprocessing (conservative):
  - noise reduction: minimal
  - VAD: keep pauses (avoid over-trim)
  - segmentation: short chunks but preserve phrase boundaries
- [ ] Define transcript output metadata requirements:
  - timestamps per segment
  - confidence scores
  - pause lengths / speech rate proxies
  - non-speech events if detectable (laughter/crying tags)
- [ ] Define low-confidence handling:
  - thresholds
  - fallback model or alternate decoding strategy
  - when to request repetition / human review
- [ ] Define baseline model comparison protocol:
  - which models (per `deliverables/01-code-switching.md`)
  - decoding settings to try (beam size, temperature, language hints)
  - metrics to report (see below)

## Metrics/reporting (MVP-aligned)

- [ ] Define “preserve what matters” metrics:
  - code-switch token preservation rate
  - triage phrase recall (do not miss)
  - named entity retention (where applicable)
  - qualitative notes on emotion-carrying cues (pauses/hesitations)

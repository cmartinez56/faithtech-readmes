# D01.T2 — Audio Sample Pack (safe/ethical + decision-grade labels)

**Output file**: `deliverables/01-code-switching.audio-pack.md` (create)

## Spec + governance

- [ ] Write the minimum pack spec (50–100 clips; 15–45s; voice/noise/emotion/code-switch mix).
- [ ] Define consent + privacy handling:
  - consent status per clip (recorded field)
  - rules for PII removal (re-record vs beep vs exclude)
  - retention policy (where stored, who can access)
- [ ] Define labeling schema (decision-grade, lightweight):
  - human reference transcript (verbatim)
  - code-switch tokens flagged (exact En/Fr words)
  - triage phrase flags (self-harm, threat, urgent medical, coercion, panic)
  - optional emotion tag (only if it changes triage)
- [ ] Create a labeling template (CSV/JSON or simple markdown per clip) and store it alongside the pack.

## Clip acquisition (choose one path)

- [ ] **Preferred**: source real clips with consent via field partners; document provenance.
- [ ] **Fallback**: create simulated equivalents (acted, privacy-safe) that match:
  - Lebanese + Syrian accents
  - WhatsApp/noisy conditions
  - realistic code-switch frequency

## Pack readiness

- [ ] Ensure coverage targets are met (dialect/emotion/noise/code-switch distribution).
- [ ] Spot-check labels for consistency (especially code-switch token marking).
- [ ] Produce a “pack index” (one page):
  - clip ids, duration, dialect guess, code-switch level, consent, flags

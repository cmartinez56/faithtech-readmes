## Deliverables TODOs (working folder)

This folder breaks each deliverable into small, checkable tasks the team can execute in order.

---

## Deliverable 01 — Code-Switching + “Kitchen Table Arabic”

Source: `faithtech-readmes/deliverables/01-code-switching.md`

### Owner(s)

- **PM/Lead**: TBD
- **Translation/Linguistics**: TBD
- **Engineering/ML**: TBD
- **Field partners**: TBD

### Definition of Done (high level)

- **Top-20 code-switch patterns** written as a markdown table (with examples + failure modes).
- **Audio Sample Pack spec** written and usable; initial clip set collected or a simulated substitute approved.
- **Prosody-preserving pipeline spec** written (ingestion → preprocessing → output metadata → low-confidence handling).
- **Acceptance criteria demo** can be run end-to-end on at least a few representative clips.

---

## D01.T1 — Top 20 code-switching patterns list (markdown table)

**Output file**: `faithtech-readmes/deliverables/01-code-switching.patterns.md` (create)

- **T1.1** Create the table skeleton with required columns:
  - Pattern name
  - Example utterances (3–5)
  - Languages mixed (Ar+En / Ar+Fr / Ar+En+Fr)
  - Where it happens (greetings/logistics/fear/prayer/medical/bureaucracy/conflict)
  - STT failure mode
  - Normalization rule (optional)
  - Priority (P0/P1/P2)
- **T1.2** Collect/brainstorm candidate patterns (aim for 30–40) from:
  - translation/linguistics team memory + field partner input
  - existing notes in `faithtech-readmes/research/`
- **T1.3** Down-select to top 20 using harm-based prioritization:
  - P0: triage/urgent/safety-critical misunderstandings
  - P1: high-frequency, high-confusion patterns
  - P2: nice-to-have coverage
- **T1.4** For each pattern, write 3–5 “voice note style” examples (verbatim, not MSA-cleaned).
- **T1.5** Add an explicit STT failure mode per pattern (what breaks today).
- **T1.6** Add optional normalization guidance (when we prefer consistent representation).
- **T1.7** Quick review pass with Engineering/ML to ensure patterns are testable.

---

## D01.T2 — Audio Sample Pack (safe/ethical + decision-grade labels)

**Output file**: `faithtech-readmes/deliverables/01-code-switching.audio-pack.md` (create)

### Spec + governance tasks

- **T2.1** Write the minimum pack spec (50–100 clips; 15–45s; voice/noise/emotion/code-switch mix).
- **T2.2** Define consent + privacy handling:
  - consent status per clip (recorded field)
  - rules for PII removal (re-record vs beep vs exclude)
  - retention policy (where stored, who can access)
- **T2.3** Define labeling schema (decision-grade, lightweight):
  - human reference transcript (verbatim)
  - code-switch tokens flagged (exact En/Fr words)
  - triage phrase flags (self-harm, threat, urgent medical, coercion, panic)
  - optional emotion tag (only if it changes triage)
- **T2.4** Create a labeling template (CSV/JSON or a simple markdown per clip) and store it alongside the pack.

### Clip acquisition tasks (choose one path)

- **T2.5A (preferred)** Source real clips with consent via field partners; document provenance.
- **T2.5B (fallback)** Create simulated equivalents (acted, privacy-safe) that match:
  - Lebanese + Syrian accents
  - WhatsApp/noisy conditions
  - realistic code-switch frequency

### Pack readiness tasks

- **T2.6** Ensure coverage targets are met (dialect/emotion/noise/code-switch distribution).
- **T2.7** Spot-check labels for consistency (especially code-switch token marking).
- **T2.8** Produce a “pack index” (one page):
  - clip ids, duration, dialect guess, code-switch level, consent, flags

---

## D01.T3 — Technical spec: prosody-preserving voice processing pipeline

**Output file**: `faithtech-readmes/deliverables/01-code-switching.pipeline-spec.md` (create)

- **T3.1** Define audio ingestion requirements:
  - accepted formats
  - sample rate policy
  - channel handling (mono/stereo)
- **T3.2** Define safe-default preprocessing (conservative):
  - noise reduction: minimal
  - VAD: keep pauses (avoid over-trim)
  - segmentation: short chunks but preserve phrase boundaries
- **T3.3** Define transcript output metadata requirements:
  - timestamps per segment
  - confidence scores
  - pause lengths / speech rate proxies
  - non-speech events if detectable (laughter/crying tags)
- **T3.4** Define low-confidence handling:
  - thresholds
  - fallback model or alternate decoding strategy
  - when to request repetition / human review
- **T3.5** Define baseline model comparison protocol (so results are reproducible):
  - which models (per `01-code-switching.md`)
  - decoding settings to try (beam size, temperature, language hints)
  - metrics to report (see below)

### Metrics/reporting checklist (MVP-aligned)

- **T3.6** Define “preserve what matters” metrics:
  - code-switch token preservation rate
  - triage phrase recall (do not miss)
  - named entity retention (where applicable)
  - qualitative notes on emotion-carrying cues (pauses/hesitations)

---

## D01.T4 — Acceptance criteria demo (end-of-sprint)

- **T4.1** Pick 5–10 representative clips from the pack (or simulated set).
- **T4.2** Run transcription through baseline candidate(s).
- **T4.3** Produce a short demo artifact:
  - input clip id + short context
  - transcript + timestamps/confidence/pause info
  - highlighted code-switch tokens + triage phrases
- **T4.4** Record “known failure cases” for the next iteration.

---

## Template for future deliverables

Copy/paste and fill in:

### Deliverable XX — <name>

- **Source**: `faithtech-readmes/deliverables/XX-<slug>.md`
- **Owners**: PM/Lead, Translation/Linguistics, Engineering/ML, Field partners
- **Definition of Done**: 3–6 bullet points
- **Tasks**:
  - DXX.T1 — <output 1>
  - DXX.T2 — <output 2>
  - DXX.T3 — <output 3>


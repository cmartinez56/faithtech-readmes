## Deliverable 01 — Code-Switching + “Kitchen Table Arabic” (How we achieve this)

This deliverable turns the vision (“hear refugees in real life language”) into an execution plan the Translation & Accessibility (“Ears”) team can ship.

We are not building “textbook translation.” We are building a listening pipeline that works on:

- Levantine Arabic (Lebanese + Syrian)
- Code-switching (Arabic + English and/or French in the same utterance)
- Noisy, emotional voice notes (WhatsApp-style)

---

## What success looks like (MVP definition)

On a small, representative evaluation set of real-world voice notes, the system consistently preserves:

- **Code-switched words** (English/French words don’t get dropped or mangled)
- **Crisis/triage phrases** (self-harm, threats, urgent medical cues, coercion)
- **Named entities** (people/places/organizations relevant to escalation)
- **Emotion-carrying cues** (pauses, sobbing/laughter tags if present, hesitation markers)

The goal is not “perfect transcripts.” The goal is **reliable downstream understanding**.

---

## Deliverables (what we will produce)

### 1) Top 20 code-switching patterns (Lebanese/Syrian “Kitchen Table Arabic”)

Output format (table in markdown):

- **Pattern name**
- **Example utterances** (3–5)
- **Languages mixed** (Ar+En, Ar+Fr, Ar+En+Fr)
- **Where it happens** (greetings, logistics, fear, prayer, medical, bureaucracy, conflict)
- **STT failure mode** (drops English words, transliterates, merges words, wrong segmentation)
- **Normalization rule** (optional: how we want it represented)
- **Priority** (P0/P1/P2 based on harm if wrong)

### 2) Audio samples: authentic “Kitchen Table Arabic”

Create an **Audio Sample Pack** that is safe/ethical and actually useful for model selection.

Minimum spec:
- **50–100 clips** (15–45 seconds each) for baseline selection (expand later)
- Mix of:
  - Lebanese + Syrian voices
  - emotional states (neutral → distressed)
  - background noise (street, tent, kids, TV)
  - code-switch frequency (low/medium/high)
- **Consent + privacy**:
  - document consent status per clip
  - remove/re-record or beep personal identifiers if required

Labeling spec (lightweight but decision-grade):
- **Human reference transcript** (verbatim, don’t “clean” into MSA)
- **Code-switch tokens flagged** (mark exact English/French words)
- **Triage phrase flags** (checkboxes: self-harm, threat, urgent medical, coercion, panic)
- Optional: **emotion tag** (distressed/calm/angry/crying/whispered) if it changes triage

### 3) Technical spec: voice processing that preserves emotional prosody

This is the “don’t destroy the signal” spec for the engineering pipeline.

Include:
- **Audio ingestion**: accepted formats, sample rate policy, channel handling
- **Pre-processing** (safe defaults):
  - noise reduction: minimal / conservative
  - VAD (voice activity detection): keep pauses (don’t over-trim)
  - segmentation: prefer short chunks but preserve phrase boundaries
- **Metadata to preserve** (must be attached to transcript output):
  - timestamps per segment
  - confidence scores
  - pause lengths / speech rate proxies
  - non-speech events if detectable (laughter/crying tags)
- **Error-handling**: what we do when confidence is low (fallback model? ask user to repeat?)

---

## How we achieve it (execution plan)

### Phase A — Decide the MVP interaction (1 hour)

- **Default**: async voice notes (WhatsApp style)
- Confirm constraints:
  - cloud OK vs PII restricted vs offline/on-device

(This maps to the scoping gates in `faithtech-readmes/research/03-scoping-thinking-tree.md`.)

### Phase B — Build the smallest evaluation set (2–5 days)

- Collect **50–100 clips** (or simulated equivalents if real clips aren’t available yet)
- Label only what we need to make decisions:
  - transcript
  - code-switch tokens
  - triage phrase flags

### Phase C — Run baseline model comparison (1–2 days)

Test at least:
- **Code-switch STT candidate**: [MohamedRashad/Arabic-Whisper-CodeSwitching-Edition](https://huggingface.co/MohamedRashad/Arabic-Whisper-CodeSwitching-Edition)
- **Levantine checkpoint candidate**: [ali-issa/lebanese-stt](https://huggingface.co/ali-issa/lebanese-stt)

If we add toolchain support for routing/experiments:
- Toolkit option: [ARBML/klaam](https://github.com/ARBML/klaam)

### Phase D — Decide next step using evidence (same week)

Decision outcomes:
- **Ship baseline** if it preserves code-switch + triage phrases reliably enough.
- **Add routing** (dialect detect → model selection) if Lebanese-only clips benefit strongly.
- **Fine-tune** if we see consistent, harmful errors on our domain (best ROI path).

---

## Who does what (team roles)

- **Translation/Linguistics**: define top-20 patterns; verify transcripts; build “dictionary of pain” phrases.
- **Field partners (Lebanon/Syria)**: help source ethically consented audio; validate realism.
- **Engineering/ML**: run inference benchmarks; build pipeline; store metadata; document model configs.
- **Product**: define what errors are unacceptable (harm-based prioritization).

---

## Acceptance criteria (what we can demo)

By end of sprint, we can demo:

- A voice note in Levantine Arabic with English/French inserts transcribes with key tokens preserved
- The output includes **timestamps + confidence + pause info**
- We can point to:
  - the **Top-20 patterns list**
  - the **Audio Sample Pack** spec + initial clips
  - the **Prosody-preserving voice pipeline spec**

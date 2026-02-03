## Open-Source Speech Models for Dialectal Arabic (Levantine + Code-Switched)

This note captures the most actionable open-source options for Speech-to-Text (STT) when your target is:

- Levantine Arabic (Lebanon/Syria) as a priority
- Code-switching inside the same utterance (Arabic + English and/or French)
- Realistic “voice note” audio (noise, emotion, overlap, interruptions)

---

## What we’re optimizing for (in FaithTech terms)

- **Input reality**: WhatsApp-style voice notes; distressed/fast/whispered speech; slang; code-switching.
- **Output requirement**: transcripts good enough to power downstream “interpretation” (risk cues, idioms, intent), not perfect news-grade MSA transcription.
- **MVP target**: Levantine first (Lebanon deployment), but architect for adding dialects later.

---

## Fast-start baseline (deployable now)

### Whisper-based, code-switch aware

- **Arabic + English code-switch Whisper fine-tune**: [MohamedRashad/Arabic-Whisper-CodeSwitching-Edition](https://huggingface.co/MohamedRashad/Arabic-Whisper-CodeSwitching-Edition)
  - Useful if you expect frequent Arabic with embedded English words/phrases.
  - Paired dataset: [MohamedRashad/arabic-english-code-switching](https://huggingface.co/datasets/MohamedRashad/arabic-english-code-switching)

What to do with it in the sprint:
- Use it as a **drop-in STT baseline** for multilingual utterances.
- Benchmark it against a “plain” multilingual STT baseline on your own voice-note samples (even 50–200 clips gives signal).

---

## Levantine-specific starting points (community models)

- **Lebanese Arabic wav2vec2 fine-tune**: [ali-issa/lebanese-stt](https://huggingface.co/ali-issa/lebanese-stt)

How to use it:
- Treat this as a **dialect anchor**. If it helps on Lebanese speech but fails on code-switch, you can route only “mostly Arabic” clips to it.

---

## Code-switching research models (useful patterns, not always plug-and-play)

- **Tunisian + French/English code-switch ASR**: [SalahZa/Code_Switched_Tunisian_Speech_Recognition](https://huggingface.co/SalahZa/Code_Switched_Tunisian_Speech_Recognition)
  - Valuable mainly for the **architecture idea** (multi-model fusion) and for learning how to evaluate code-switch errors.

- **CAFE dataset paper (Algerian Arabic + French/English)**: [arXiv:2411.13424](https://arxiv.org/abs/2411.13424)
  - Useful as evidence that “real bilingual conversation audio” is hard and needs adaptation, not just off-the-shelf inference.

---

## Tooling that makes training + inference easier

- **Klaam toolkit** (ASR + classification + TTS utilities): [ARBML/klaam](https://github.com/ARBML/klaam)
  - Helpful if you want an ergonomic workflow for experiments and potentially **dialect classification → routing**.

- **Arabic Conformer checkpoint example** (baseline/reference): [MostafaAhmed98/Conformer-CTC-Arabic-ASR](https://huggingface.co/MostafaAhmed98/Conformer-CTC-Arabic-ASR)

---

## Datasets for benchmarking and fine-tuning

- **Multi-dialect evaluation resource**: [UBC-NLP/Casablanca](https://huggingface.co/datasets/UBC-NLP/Casablanca)
  - Useful for checking whether changes improve (or regress) on dialectal speech, and for understanding what “real transcripts” look like.

- **Curated dataset collection (starting point for sourcing)**: [MohamedRashad/arabic-speech-datasets](https://huggingface.co/collections/MohamedRashad/arabic-speech-datasets)

- **Cross-model benchmark reference**: [Open Universal Arabic ASR Leaderboard (arXiv:2412.13788)](https://arxiv.org//2412.13788v1)

---

## Optional: emotion/prosody tagging (adds interpretation signal)

If we decide emotion tags help triage (“distress”, “panic”, “anger”), consider a second-stage classifier:

- Research + implementation reference: [arXiv:2110.04425](https://arxiv.org/abs/2110.04425)
- Example repo: [OmarMohammed88/AR-Emotion-Recognition](https://github.com/OmarMohammed88/AR-Emotion-Recognition)

Note: this doesn’t replace ASR; it complements ASR with **metadata**.

---

## Recommended “good enough” MVP architecture (open-source first)

- **Step 1: STT** using a multilingual model (baseline) and/or code-switch fine-tuned Whisper for mixed speech.
- **Step 2: (Optional) dialect detect + route** if we see strong gains for Lebanese-only clips.
- **Step 3: downstream interpretation** (separate document): idioms-of-distress detection, risk cue extraction, escalation logic.

---

## What to measure (so we make good decisions, fast)

Beyond a single WER number, track these categories on a small evaluation set:

- **Code-switch fidelity**: do English/French words survive, or get “arabized”/dropped?
- **Named entities**: people/places/organizations important for triage.
- **Crisis phrases**: self-harm, threats, urgent medical cues, coercion cues.
- **Idioms of distress**: whether key phrases appear in text at all (even if spelling varies).


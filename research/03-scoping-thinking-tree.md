## Scoping “Ears”: a Thinking Tree for Dialectal Arabic STT (Levantine + Code-Switched)

This is a practical decision framework to choose the best next steps without getting stuck in endless model shopping.

---

## The Thinking Tree (decision gates)

Start at the top and stop as soon as you have enough evidence to decide the next gate.

### Gate 0 — What is the MVP interaction?

```
User input → what do we need to handle first?
├─ A) WhatsApp voice notes (async)  → prioritize robust STT on noisy clips
├─ B) Phone call / live audio      → prioritize latency + streaming + stability
└─ C) Typed chat only              → STT can wait; focus NLP first
```

Default for FaithTech Integration Sprint: **A (voice notes)**.

---

### Gate 1 — What constraints are non-negotiable?

```
Constraints → where can processing happen?
├─ A) Cloud OK (PII allowed by policy) → fastest iteration
├─ B) Cloud OK but PII restricted      → redact + minimize retention
└─ C) Offline / on-device required     → smaller models, quantization, tighter scope
```

Outcome:
- If **A**: choose best-performing model first, then harden.
- If **B/C**: prioritize models/tooling that can run privately and be fine-tuned locally.

---

### Gate 2 — Which language problem is dominant?

```
Audio characteristics → what breaks baseline STT?
├─ A) Levantine dialect (Leb/Syr) dominates
├─ B) Code-switch (Ar+En/Fr) is frequent
├─ C) Both A and B (common)
└─ D) Emotion/noise dominates more than dialect
```

What we do:
- If **B or C**: test a code-switch aware Whisper fine-tune:  
  - [MohamedRashad/Arabic-Whisper-CodeSwitching-Edition](https://huggingface.co/MohamedRashad/Arabic-Whisper-CodeSwitching-Edition)
- If **A**: add a Levantine (Lebanese) checkpoint to compare/routable option:  
  - [ali-issa/lebanese-stt](https://huggingface.co/ali-issa/lebanese-stt)

---

### Gate 3 — Build the smallest evaluation set that answers the next question

```
Eval set → what’s the minimum to make a decision?
├─ 50–100 clips: choose baseline model + rough error taxonomy
├─ 200–500 clips: compare routing strategies + data needs
└─ 1k+ clips: justify fine-tuning investment and track regressions
```

Minimum labeling guidance:
- Transcripts can be “good enough” if they preserve **crisis phrases**, **names**, and **code-switched words**.
- If you can’t label much, label **only** the segments containing key cues (triage-first).

---

### Gate 4 — Decide: route, fine-tune, or stay general

```
Results → how do we improve fastest?
├─ A) Single model is good enough → ship MVP; log edge cases
├─ B) Dialect differences matter  → add dialect detect + routing
└─ C) Consistent errors on our domain → fine-tune with targeted data
```

Routing option:
- Use a dialect classifier/routing toolchain (helpful for scaling dialects later):  
  - [ARBML/klaam](https://github.com/ARBML/klaam)

Fine-tuning option:
- Prioritize collecting transcripts for the error modes that matter:
  - code-switch segments
  - crisis phrases
  - Levantine slang and idioms (even if spelled variably)

---

### Gate 5 — Add interpretation metadata only if it changes outcomes

```
Do we need more than text?
├─ A) Text alone is enough for triage → skip emotion modeling
└─ B) Emotion cues change triage/response → add emotion/prosody tags
```

If **B**, keep it as a second stage (don’t block STT):
- Research reference: [arXiv:2110.04425](https://arxiv.org/abs/2110.04425)
- Example implementation: [OmarMohammed88/AR-Emotion-Recognition](https://github.com/OmarMohammed88/AR-Emotion-Recognition)

---

## “Brain Map” of what to work on (ordered by highest decision value)

1. **Define MVP audio input** (voice notes vs calls) and privacy constraints (Gate 0–1)
2. **Run baseline STT comparisons** on a tiny eval set (Gate 2–3)
3. **Create an error taxonomy** that maps to product risk (what errors cause harm?)
4. **Choose improvement strategy** (ship / route / fine-tune) (Gate 4)
5. **Only then** add emotion metadata (Gate 5)

---

## Next-step checklist (what we do this week)

- Pick **10 real-world scenarios** (voice note examples) that represent the MVP.
- Build a **50–100 clip** evaluation set and label only what’s needed to choose a baseline.
- Compare:
  - general multilingual STT baseline
  - code-switch aware Whisper fine-tune: [MohamedRashad/Arabic-Whisper-CodeSwitching-Edition](https://huggingface.co/MohamedRashad/Arabic-Whisper-CodeSwitching-Edition)
  - Levantine checkpoint (Lebanese): [ali-issa/lebanese-stt](https://huggingface.co/ali-issa/lebanese-stt)
- Decide whether to:
  - ship baseline
  - add routing
  - invest in fine-tuning

---

## Research support (to support deliverables)

To support your deliverables, I can help research:

- The top 20 code-switching patterns in Lebanese Arabic (especially Arabic-English-French mixing).
- Sources of authentic voice data from Syrian refugees using Kitchen Table Arabic.
- Voice processing techniques or libraries that preserve emotional prosody in speech-to-text systems.

Would you like me to:

- Find linguistic studies or corpora that document these code-switching patterns?
- Locate public or NGO-provided audio datasets featuring refugee speech in Levantine dialects?
- Explore STT model architectures that retain prosodic/emotional metadata?


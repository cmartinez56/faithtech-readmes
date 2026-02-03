# T4 — Baseline Model Comparison

**Duration**: 1–2 days  
**Owner**: Engineering/ML team  
**Dependencies**: T1 (patterns), T2 (audio pack), T3 (pipeline spec)

---

## Goal

Test candidate models and compare their performance on code-switching and Levantine Arabic.

---

## Tasks

- [ ] **T4.1**: Test code-switch STT candidate:
  - [MohamedRashad/Arabic-Whisper-CodeSwitching-Edition](https://huggingface.co/MohamedRashad/Arabic-Whisper-CodeSwitching-Edition)
  - Run on audio pack from T2
  - Measure against patterns from T1

- [ ] **T4.2**: Test Levantine checkpoint candidate:
  - [ali-issa/lebanese-stt](https://huggingface.co/ali-issa/lebanese-stt)
  - Run on audio pack from T2
  - Measure against patterns from T1

- [ ] **T4.3** (optional): Add toolchain support for routing/experiments:
  - [ARBML/klaam](https://github.com/ARBML/klaam)
  - Evaluate if routing improves results

- [ ] **T4.4**: Document results:
  - Code-switch token preservation rate
  - Triage phrase recall
  - Named entity retention
  - Qualitative notes on emotion-carrying cues

- [ ] **T4.5**: Compare results using metrics from T3.6

---

## Models to Test

1. **MohamedRashad/Arabic-Whisper-CodeSwitching-Edition**
   - Focus: Code-switching support
   - Test: How well it preserves English/French words

2. **ali-issa/lebanese-stt**
   - Focus: Levantine dialect
   - Test: How well it handles Lebanese/Syrian accents

3. **ARBML/klaam** (optional)
   - Focus: Toolchain/routing
   - Test: If routing improves results

---

## Evaluation Criteria

- Preserves code-switched words (English/French don't get dropped or mangled)
- Preserves crisis/triage phrases (self-harm, threats, urgent medical cues, coercion)
- Preserves named entities (people/places/organizations)
- Preserves emotion-carrying cues (pauses, sobbing/laughter tags, hesitation markers)

---

## Notes

- Use audio pack from T2 for testing
- Use patterns from T1 to identify failure modes
- Follow pipeline spec from T3 for preprocessing
- Document all settings (beam size, temperature, language hints) for reproducibility

---

## Next Steps

After T4 is complete, proceed to:
- **[T5 — Decision Making](t5-decision.md)** (uses comparison results)
- **[T6 — Acceptance Criteria Demo](t6-demo.md)** (uses best-performing model)

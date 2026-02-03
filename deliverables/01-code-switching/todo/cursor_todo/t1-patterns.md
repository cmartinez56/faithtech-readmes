# T1 — Top 20 Code-Switching Patterns

**Duration**: 2–3 days  
**Output**: `faithtech-readmes/deliverables/01-code-switching.patterns.md`  
**Owner**: Translation/Linguistics team

---

## Goal

Create a markdown table documenting the top 20 code-switching patterns in Lebanese/Syrian "Kitchen Table Arabic" with examples, failure modes, and prioritization.

---

## Tasks

- [ ] **T1.1**: Create table skeleton with columns:
  - Pattern name
  - Example utterances (3–5)
  - Languages mixed (Ar+En, Ar+Fr, Ar+En+Fr)
  - Where it happens (greetings/logistics/fear/prayer/medical/bureaucracy/conflict)
  - STT failure mode
  - Normalization rule (optional)
  - Priority (P0/P1/P2)

- [ ] **T1.2**: Collect/brainstorm 30–40 candidate patterns from:
  - Translation/linguistics team memory
  - Field partner input
  - Existing notes in `faithtech-readmes/research/`

- [ ] **T1.3**: Down-select to top 20 using harm-based prioritization:
  - P0: triage/urgent/safety-critical misunderstandings
  - P1: high-frequency, high-confusion patterns
  - P2: nice-to-have coverage

- [ ] **T1.4**: Write 3–5 "voice note style" examples per pattern (verbatim, not MSA-cleaned)

- [ ] **T1.5**: Document STT failure mode per pattern (what breaks today)

- [ ] **T1.6**: Add optional normalization guidance (when we prefer consistent representation)

- [ ] **T1.7**: Review with Engineering/ML to ensure patterns are testable

---

## Priority Guidelines

- **P0**: Patterns that could cause harm if misunderstood (triage phrases, safety-critical)
- **P1**: High-frequency patterns that cause confusion but aren't safety-critical
- **P2**: Nice-to-have coverage for completeness

---

## Notes

- Keep examples verbatim (don't "clean" into Modern Standard Arabic)
- Focus on realistic "voice note" style utterances
- Document what breaks in current STT systems

---

## Next Steps

After T1 is complete, proceed to:
- **[T2 — Audio Sample Pack](t2-audio-pack.md)** (can run in parallel)
- **[T4 — Baseline Model Comparison](t4-baseline-comparison.md)** (uses patterns for testing)

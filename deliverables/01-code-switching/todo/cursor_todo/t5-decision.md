# T5 — Decision Making

**Duration**: Same week as T4  
**Owner**: Product + Engineering/ML team  
**Dependencies**: T4 (baseline comparison results)

---

## Goal

Analyze baseline comparison results and decide the next step: ship baseline, add routing, or fine-tune.

---

## Tasks

- [ ] **T5.1**: Analyze baseline comparison results from T4:
  - Review code-switch token preservation rates
  - Review triage phrase recall
  - Review named entity retention
  - Identify consistent failure patterns

- [ ] **T5.2**: Make decision based on evidence:
  - [ ] **T5.2A**: Ship baseline if it preserves code-switch + triage phrases reliably enough
  - [ ] **T5.2B**: Add routing (dialect detect → model selection) if Lebanese-only clips benefit strongly
  - [ ] **T5.2C**: Fine-tune if we see consistent, harmful errors on our domain (best ROI path)

- [ ] **T5.3**: Document decision rationale:
  - Why this path was chosen
  - What evidence supported it
  - What risks/limitations exist
  - What success looks like for next iteration

---

## Decision Criteria

### Ship Baseline (T5.2A)
- Code-switch tokens preserved reliably (>90% on P0 patterns)
- Triage phrases not missed
- Acceptable performance on evaluation set

### Add Routing (T5.2B)
- Strong performance difference between Lebanese-only vs mixed clips
- Routing would improve overall results
- Engineering effort is reasonable

### Fine-Tune (T5.2C)
- Consistent, harmful errors on domain-specific patterns
- Fine-tuning would address these errors
- ROI is better than routing or baseline

---

## Notes

- Decision should be evidence-based, not opinion-based
- Consider engineering effort vs. performance gain
- Document for future reference and learning

---

## Next Steps

After T5 is complete, proceed to:
- **[T6 — Acceptance Criteria Demo](t6-demo.md)** (uses chosen approach)
- If fine-tuning: Create new task file for fine-tuning work
- If routing: Create new task file for routing implementation

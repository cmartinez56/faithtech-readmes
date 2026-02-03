# T6 — Acceptance Criteria Demo

**Duration**: End-of-sprint  
**Owner**: Engineering/ML + Product team  
**Dependencies**: T2 (audio pack), T4 (baseline comparison), T5 (decision)

---

## Goal

Produce a demo artifact that shows the system working end-to-end on representative clips.

---

## Tasks

- [ ] **T6.1**: Pick 5–10 representative clips from the pack (or simulated set):
  - Mix of dialects (Lebanese + Syrian)
  - Mix of code-switch frequency (low/medium/high)
  - Include at least one triage phrase example
  - Include at least one high-emotion example

- [ ] **T6.2**: Run transcription through baseline candidate(s) (or chosen approach from T5):
  - Use pipeline spec from T3
  - Ensure metadata is captured (timestamps, confidence, pauses)

- [ ] **T6.3**: Produce short demo artifact:
  - Input clip ID + short context
  - Transcript + timestamps/confidence/pause info
  - Highlighted code-switch tokens + triage phrases
  - Before/after comparison if applicable

- [ ] **T6.4**: Record "known failure cases" for next iteration:
  - Document what still breaks
  - Prioritize by harm (P0/P1/P2)
  - Suggest fixes for future work

---

## Demo Artifact Format

For each clip:
- **Clip ID**: [identifier]
- **Context**: [brief description]
- **Input**: [link to audio or description]
- **Output**:
  - Transcript: [full transcript]
  - Timestamps: [per segment]
  - Confidence: [scores]
  - Pauses: [detected pause lengths]
  - Code-switches: [highlighted tokens]
  - Triage phrases: [flagged phrases]
- **Notes**: [any issues or observations]

---

## Success Criteria

- Demo shows system working end-to-end
- Code-switch tokens are preserved
- Triage phrases are not missed
- Metadata is present and useful
- Known failures are documented

---

## Notes

- This is the "proof of concept" demo
- It doesn't need to be perfect, but should show the approach works
- Document failures honestly for iteration

---

## Next Steps

After T6 is complete:
- Review demo with stakeholders
- Use known failure cases to plan next iteration
- If baseline is acceptable, proceed to production implementation
- If not, iterate based on T5 decision (routing or fine-tuning)

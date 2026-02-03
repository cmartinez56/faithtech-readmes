# Data Samples & Sources for Deliverable 01 — Code-Switching + "Kitchen Table Arabic"

This document compiles available data sources and samples for building the Audio Sample Pack (T2) and evaluating baseline models (T4).

**Target**: 50–100 clips (15–45 seconds each) of Levantine Arabic (Lebanese + Syrian) with code-switching (Arabic + English/French) in realistic conditions (noisy, emotional, WhatsApp-style voice notes).

---

## Primary Data Sources (Ready-to-Use Datasets)

### 1. Arabic-English Code-Switching Dataset
**Source**: [MohamedRashad/arabic-english-code-switching](https://huggingface.co/datasets/MohamedRashad/arabic-english-code-switching)  
**Type**: HuggingFace Dataset  
**Content**: 
- Paired dataset for Arabic + English code-switching
- Used to train the code-switch-aware Whisper model
- Contains audio samples with transcripts

**How to Access**:
```python
from datasets import load_dataset
dataset = load_dataset("MohamedRashad/arabic-english-code-switching")
```

**Use Case**: 
- Baseline evaluation for code-switching patterns
- Understanding code-switch token distribution
- May need filtering for Levantine-specific samples

**Limitations**: 
- May not be specifically Levantine (Lebanese/Syrian)
- May not include French code-switching
- May not have emotional/noisy conditions

---

### 2. Casablanca Multi-Dialect Dataset
**Source**: [UBC-NLP/Casablanca](https://huggingface.co/datasets/UBC-NLP/Casablanca)  
**Type**: HuggingFace Dataset  
**Content**:
- Multi-dialect Arabic evaluation resource
- Includes various Arabic dialects
- Useful for understanding dialectal speech patterns

**How to Access**:
```python
from datasets import load_dataset
dataset = load_dataset("UBC-NLP/Casablanca")
```

**Use Case**:
- Checking dialectal coverage
- Understanding what "real transcripts" look like
- Evaluating whether changes improve/regress on dialectal speech

**Limitations**:
- May not focus specifically on Levantine
- May not include code-switching
- May not have emotional/noisy conditions

---

### 3. Arabic Speech Datasets Collection
**Source**: [MohamedRashad/arabic-speech-datasets](https://huggingface.co/collections/MohamedRashad/arabic-speech-datasets)  
**Type**: HuggingFace Collection  
**Content**:
- Curated collection of Arabic speech datasets
- Multiple datasets in one place
- Starting point for sourcing

**How to Access**: Browse the collection on HuggingFace and select relevant datasets

**Use Case**:
- Discovering additional Arabic speech resources
- Finding datasets that might include Levantine samples
- Exploring available Arabic speech data

---

## Research Datasets (Reference/Architecture)

### 4. CAFE Dataset (Algerian Arabic + French/English)
**Source**: [arXiv:2411.13424](https://arxiv.org/abs/2411.13424)  
**Type**: Research Paper Dataset  
**Content**:
- Algerian Arabic with French/English code-switching
- Real bilingual conversation audio
- Evidence that real code-switched audio needs adaptation

**Use Case**:
- Understanding code-switching patterns (even if different dialect)
- Learning evaluation methodologies for code-switch errors
- Architecture ideas for multi-model fusion

**Limitations**:
- Algerian dialect (not Levantine)
- May not be publicly available
- Research dataset (may require permission)

---

### 5. Tunisian Code-Switched Speech Recognition
**Source**: [SalahZa/Code_Switched_Tunisian_Speech_Recognition](https://huggingface.co/SalahZa/Code_Switched_Tunisian_Speech_Recognition)  
**Type**: HuggingFace Model (may include dataset info)  
**Content**:
- Tunisian Arabic + French/English code-switching
- Multi-model fusion architecture

**Use Case**:
- Architecture patterns for code-switch handling
- Evaluation methodologies
- Understanding code-switch error patterns

**Limitations**:
- Tunisian dialect (not Levantine)
- May not include dataset access

---

## Model-Trained Datasets (Indirect Access)

### 6. Lebanese STT Model Training Data
**Source**: [ali-issa/lebanese-stt](https://huggingface.co/ali-issa/lebanese-stt)  
**Type**: Model (training data may be referenced)  
**Content**:
- Lebanese Arabic wav2vec2 fine-tune
- May reference training dataset

**Use Case**:
- Understanding what data was used for Lebanese-specific training
- May lead to dataset sources
- Model can be used for evaluation

**How to Investigate**:
- Check model card on HuggingFace
- Review any linked papers or documentation
- Contact model creator if dataset info available

---

## Field Partner Sources (Preferred Path)

### 7. Field Partners in Lebanon/Syria
**Sources** (from research notes):
- **Pierre Housseny (Horizons International, Beirut)** – On-the-ground insight into spoken slang in Lebanon; partnered with 130+ churches in Arabic outreach
- **Field partners** mentioned in deliverable spec

**Use Case**:
- **Preferred source** for authentic "Kitchen Table Arabic"
- Realistic WhatsApp-style voice notes
- Proper consent and ethical sourcing
- Validation of realism

**Requirements**:
- Consent documentation per clip
- Privacy handling (PII removal if needed)
- Realistic conditions (noise, emotion, code-switching)

**Next Steps**:
- Contact field partners to source ethically consented audio
- Document provenance and consent status
- Validate realism with native speakers

---

## Simulated/Acted Samples (Fallback Path)

### 8. Simulated Equivalents
**If real clips aren't available**, create simulated equivalents:

**Requirements**:
- Lebanese + Syrian accents (native speakers)
- WhatsApp/noisy recording conditions
- Realistic code-switch frequency
- Emotional states (neutral → distressed)
- Background noise (street, tent, kids, TV)

**Use Case**:
- Fallback if field partner sourcing delayed
- Controlled conditions for testing
- Privacy-safe alternative

**Considerations**:
- Must match realistic patterns from T1 (Top 20 patterns)
- Should be validated by native speakers
- May not capture authentic emotional prosody

---

## Data Collection Strategy

### Phase 1: Immediate Access (Days 1-2)
1. **Download and explore**:
   - `MohamedRashad/arabic-english-code-switching` dataset
   - `UBC-NLP/Casablanca` dataset
   - Browse `MohamedRashad/arabic-speech-datasets` collection

2. **Filter and evaluate**:
   - Check for Levantine samples
   - Assess code-switching patterns
   - Evaluate audio quality and conditions

### Phase 2: Field Partner Outreach (Days 2-5)
1. **Contact field partners**:
   - Pierre Housseny (Horizons International, Beirut)
   - Other Lebanon/Syria field partners
   - Request ethically consented audio samples

2. **Define requirements**:
   - 50–100 clips (15–45 seconds each)
   - Mix: Lebanese + Syrian, emotional states, noise, code-switch frequency
   - Consent documentation

### Phase 3: Simulation (If Needed)
1. **Create simulated samples** if real clips delayed
2. **Validate** with native speakers
3. **Document** as fallback option

---

## Dataset Access Instructions

### HuggingFace Datasets
```python
# Install if needed
# pip install datasets

from datasets import load_dataset

# Load Arabic-English code-switching dataset
code_switch_dataset = load_dataset("MohamedRashad/arabic-english-code-switching")

# Load Casablanca multi-dialect dataset
casablanca_dataset = load_dataset("UBC-NLP/Casablanca")

# Explore dataset structure
print(code_switch_dataset)
print(code_switch_dataset['train'][0])  # View first sample
```

### HuggingFace Collections
1. Visit: https://huggingface.co/collections/MohamedRashad/arabic-speech-datasets
2. Browse available datasets
3. Select relevant ones and load using `load_dataset()`

---

## Labeling Requirements

For each clip in the Audio Sample Pack, document:

1. **Human reference transcript** (verbatim, don't clean into MSA)
2. **Code-switch tokens flagged** (mark exact English/French words)
3. **Triage phrase flags**:
   - [ ] Self-harm
   - [ ] Threat
   - [ ] Urgent medical
   - [ ] Coercion
   - [ ] Panic
4. **Optional emotion tag** (if it changes triage):
   - Distressed/calm/angry/crying/whispered
5. **Metadata**:
   - Clip ID
   - Duration
   - Dialect guess (Lebanese/Syrian)
   - Code-switch level (low/medium/high)
   - Consent status
   - Background noise type
   - Emotional state

---

## Next Steps

1. **Immediate**: Download and explore HuggingFace datasets
2. **Short-term**: Contact field partners for real samples
3. **Fallback**: Prepare simulation plan if needed
4. **Ongoing**: Document all sources and consent status

---

## References

- **Research Note**: `faithtech-readmes/research/02-open-source-speech-models-dialectal-arabic.md`
- **Deliverable Spec**: `faithtech-readmes/deliverables/01-code-switching/01-code-switching.md`
- **Task Spec**: `faithtech-readmes/deliverables/01-code-switching/todo/cursor_todo/t2-audio-pack.md`
- **Questions**: `faithtech-readmes/research/Questions.md`

---

## Notes

- **Priority**: Field partner sources are preferred for authenticity
- **Ethics**: All clips must have documented consent status
- **Privacy**: Remove or beep personal identifiers if required
- **Realism**: Focus on "Kitchen Table Arabic" (not textbook MSA)
- **Coverage**: Ensure mix of dialects, emotions, noise, and code-switch frequency

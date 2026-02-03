You’re asking the **right question for the Translation (“Ears”) team**.
What you need is **not “Arabic translation”** in the conventional sense, but **dialect-aware, code-switching, emotionally sensitive Arabic understanding**—what your documents rightly call **Kitchen Table Arabic** .

Below is a **practical, model-level map** of what actually works today, what doesn’t, and how teams like yours typically assemble this capability.

---

## First: Name the Real Technical Problem

What you are trying to hear is:

* **Levantine Arabic dialects** (Lebanese + Syrian)
* **Code-switching** (Arabic + French + English in the same sentence)
* **Non-standard grammar**
* **Emotionally charged speech** (crying, anger, whispering)
* **Somatic idioms of distress** (“my chest is heavy,” “my liver is burning”) 

Most “Arabic models” fail because they are trained on:

* News
* Qur’anic or Modern Standard Arabic (MSA)
* Clean, written text
  —not **street-level voice notes from Beirut at 2am**.

---

## Tier 1: Speech-to-Text Models That Can *Actually Hear* Dialect

### ✅ **OpenAI — Whisper (Large / Large-v3)**

**Why it matters**

* Best publicly available **Arabic dialect STT**
* Handles **code-switching** better than Google/AWS
* Performs well on **noisy WhatsApp voice notes**

**Limitations**

* Outputs text, not meaning
* Still misses *some* slang without fine-tuning

**FaithTech-fit**

* Excellent as the **first ear**
* Must pass **timestamps + confidence + pauses** forward as emotional metadata

---

### ⚠️ **Google — Speech-to-Text**

**Pros**

* Strong infrastructure
* Good MSA accuracy

**Cons**

* Weak on Levantine slang
* Poor at French/English code-switching mid-sentence

**Verdict**

* Not ideal for Kitchen Table Arabic

---

### ⚠️ **Amazon — Transcribe**

* Similar issues as Google
* Optimized for call centers, not refugees

---

## Tier 2: Language Models That Understand *Messy Arabic*

### ✅ **OpenAI — GPT-4-class models**

**Why they work**

* Surprisingly strong at:

  * Levantine dialects
  * Arabic-French-English mixing
  * Emotional inference from phrasing

**Key Insight**

> GPT doesn’t “translate” Kitchen Arabic — it **interprets it**.

**Critical Pattern**
You do **not** ask:

> “Translate this Arabic to English.”

You ask:

> “Interpret the emotional and semantic meaning of this Levantine Arabic utterance, preserving distress signals.”

This aligns perfectly with:

* *Emotional Metadata*
* *Dictionary of Pain*
* *Crisis detection vocabulary* 

---

### ⚠️ **Meta — LLaMA-based Arabic fine-tunes**

**Pros**

* Can be fine-tuned on dialect data
* On-device potential (future)

**Cons**

* Require **heavy local data**
* Weak without curated Lebanese/Syrian corpora

**Use case**

* Phase-2 / on-device models
* Not Sprint-ready unless you already have dialect data

---

### ⚠️ **Anthropic — Claude**

* Excellent reasoning
* Historically weaker Arabic dialect handling than GPT
* Improving, but not leading here

---

## Tier 3: What Actually Makes This Work (Non-Negotiable)

Models alone **will fail** unless you add:

### 1. **Dialect Prompt Framing**

You must *tell* the model what it is hearing:

> “This input is Lebanese/Syrian street Arabic with French/English code-switching, spoken during emotional distress.”

### 2. **Dictionary of Pain Injection**

Your trauma team must provide:

* Somatic idioms
* Cultural metaphors
* Crisis phrases
  which are injected as **context**, not training data .

### 3. **Emotion-Preserving Pipeline**

Never collapse this into “clean text”:

```
Voice → STT
     → { text + pauses + volume + hesitations }
     → Interpretation model
```

This is explicitly called out in your Sprint docs as **emotional metadata** .

---

## What Will *Not* Work (Common Mistakes)

❌ Pure MSA translation models
❌ “Arabic → English → Arabic” loops
❌ Academic dialect datasets
❌ Models trained on social media but not **spoken grief**
❌ Treating slang as noise instead of signal

---

## A Realistic Sprint-Ready Stack (Ears Team)

**Recommended architecture**

1. **Whisper Large** → raw transcript + timing
2. **GPT-4-class model** → interpret meaning, distress, intent
3. **Dictionary of Pain overlay** → trauma classification
4. Pass forward:

   * Meaning
   * Emotion
   * Risk signals
     (not just words)

This directly supports:

* Crisis escalation
* Lament recognition
* Warm Handshake timing 

---

## Bottom Line for the Translation Team

You are not building a translator.
You are building a **listening instrument**.

If you can say:

> “When a refugee cries in mixed Lebanese Arabic, French, and English, we still hear the pain correctly”

— then the ambulance can find the patient.

If you want, next I can:

* Help you **design the exact prompts**
* Draft a **Dialect Mapping Spec** for Lebanese/Syrian Arabic
* Define a **Sprint-ready demo** that proves this works in 3 minutes

Just tell me where you want to go next.

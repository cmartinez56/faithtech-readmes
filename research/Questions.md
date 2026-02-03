# Questions & Answers - FaithTech Integration Sprint

## Questions

1. **Who on the Translation Team would have access to relevant datasets or models?**
2. **Should the models handle speech, text, or both?**
3. **Should the models focus on Levantine Arabic, or broader dialects?**
4. **Should we include only open-source models or also academic datasets and research?**
5. **Should we prioritize deployable models or also include promising research-stage tools?**

---

## Answers

### ✅ 1. **Who on the Translation Team would have access to relevant datasets or models?**

Several Translation Team members are positioned to access or influence dialectal Arabic datasets and models—especially for "Kitchen Table Arabic" and speech/text translation in MENA contexts:

* **Michelle Bryant (Biblica)** – Leads AI-assisted translation platforms across MENA. She likely has access to training data and workflows for both text and voice dialects.
* **Josh Müller (Waha)** – Specializes in **localization and AI workflows for 44+ audio-first languages**, and previously led projects in Türkiye serving MENA refugees. Key for both **slang and oral dialects**.
* **Islam Sarmini (Billy Graham Evangelistic Association)** – Brings expertise in Arabic digital strategy and trauma-informed ministry; likely has access to real-world conversational datasets from online engagement.
* **Eunice Jones (SRG)** – Has over 30 years' experience as a linguist, including audio recording in Islamic contexts. Ideal for **training culturally nuanced NLP models**.
* **Jodessiah Sumpter (Tech Levitate)** – Builds AI-powered tools and platforms. Could assist in developing a fine-tuning pipeline or deployment architecture.
* **Nardine Farah (Biblica)** – A product manager with deep MENA field experience and advanced training in AI, productizing dialect-aware tools in constrained environments.
* **Pierre Housseny (Horizons International, Beirut)** – Offers **on-the-ground insight into spoken slang** in Lebanon, and has partnered with over 130 churches in Arabic outreach.

These people can provide datasets, model training capabilities, linguistic insight, or deployment support.

---

### 🎤 2. **Should the models handle speech, text, or both?**

**Both.** According to Sprint documents, the Translation & Accessibility team is explicitly tasked with:

* **Building dialect-specific speech engines** (STT/TTS) that power trauma response and discipleship tools across the Gospel Link ecosystem.
* Supporting **"Code-Switched Arabic"** and **"Kitchen Table Arabic"** (mixing Arabic, French, and English) as well as **low-bandwidth voice-first environments**.

That means you'll need:

* **Speech-to-text (STT)** tuned for real spoken slang, voice notes, and low-literacy users.
* **Text-to-text NLP** that preserves emotional nuance and slang meaning.

---

### 🌍 3. **Should the models focus on Levantine Arabic, or broader dialects?**

**Prioritize Levantine Arabic first**—especially **Lebanese and Syrian dialects**—for the MVP and testing phase. This aligns with:

* The stated deployment goal in **Lebanon** for 2026, with 100 Syrian refugees receiving trauma support.
* The "Fatima" persona used throughout the documents—a **Syrian refugee in Lebanon**, often code-switching when in distress.

However, the team anticipates future deployment in Morocco, Egypt, and Iraq, so modular architecture should allow for **additional dialects later**.

---

### 📚 4. **Should we include only open-source models or also academic datasets and research?**

You should include **both**, especially:

* **Academic papers/datasets** for low-resource dialects (e.g., COLING, LREC, Arabic Dialect Corpora).
* **Open-source models** for rapid prototyping and local deployment (e.g., HuggingFace models, Whisper, Wav2Vec2, CAMeL Tools).
* Any **research-stage projects** that address MENA-specific challenges like code-switching or dialect detection.

Several team members (e.g., Josh C., Michelle B., Samir S., Jodessiah S.) have the capability to **fine-tune or adapt models** using academic sources even if they aren't plug-and-play.

---

### 🚀 5. **Should we prioritize deployable models or also include promising research-stage tools?**

**Include both.**

* The **2026 goal** is to deploy a trauma bot in Lebanon, so you **must prioritize deployable tools** for STT and NLP for "messy" Arabic now.
* However, the team is also building a **modular architecture**—the 4D sprint includes "Reimagine" and "Create" phases encouraging innovation where needed.
* Therefore, **flagging research-stage models** (e.g., dialect adaptation layers, code-switched transformers) will inform future roadmap decisions and potential scaling into Egypt, Morocco, etc.

---

## Next Steps

Would you like me to now identify concrete models, toolkits, and datasets (e.g., Arabic dialect STT, code-switched translation, etc.) that fit these priorities?

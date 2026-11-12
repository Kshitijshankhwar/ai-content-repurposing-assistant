# Interview guide — AI Content Repurposing Assistant

## 45-second explanation
"Content teams repeatedly adapt long stories into short promotional assets. I built a Streamlit prototype that accepts a source story and a content brief, then uses a Gemini language model to draft five hooks, three short-video scripts, two captions and three calls to action. I used structured prompting to constrain outputs to the source, JSON validation to check the response shape and a quality checklist for editorial review. The goal is to speed up first drafts, not replace human editors."

## Explain each component
- **Python:** connects the interface, prompt and model.
- **Streamlit:** makes the form and results view without building a complex website.
- **Gemini API:** sends the story and instructions to an LLM.
- **Prompt engineering:** specifies the task, output schema and factuality constraints.
- **JSON:** predictable format for showing and downloading the results.
- **Validation:** checks missing fields, list lengths and script fields.
- **Quality checks:** counts hooks and scripts and detects duplicate/long hooks. They do not guarantee factual accuracy.
- **Human in the loop:** editor checks story details, cultural context and brand tone.

## Questions and answers
**Why this problem?** A single long-form story often needs multiple short promotional variants. Repeated first-draft work is a plausible automation opportunity.

**Why not train a model?** A general LLM with careful prompts is faster and cheaper for a small prototype than collecting training data and fine-tuning.

**Why Gemini?** It offers an API for text generation; the architecture could use another provider.

**What could go wrong?** Hallucinated plot details, repetitive hooks, weak tone fit, latency, API cost and copyright/privacy risks.

**How would you measure success?** Have an editor rate 5–10 sample outputs for factual consistency, usefulness and tone (1–5). Track time spent editing versus drafting manually. Do not claim improvements without collecting data.

**What would you improve?** Add a side-by-side editor review screen, saved feedback, versioned prompts, retries for invalid JSON, and integration with the team's content workflow.

## Two-day preparation
**Day 1:** Learn Python basics, run the fixed demo, read `app.py` and `content_engine.py`, explain each function aloud.
**Day 2:** Configure an API key, test five different fictional stories, compare hooks and scripts, note failures, revise one prompt and rerun the tests.

## What to say truthfully on your resume
Once you have actually run it: "Built a prototype with Streamlit and Gemini API for drafting hooks, scripts and captions from source stories; implemented structured prompts and basic output checks."

Until then: "Developing a Streamlit and Gemini API prototype for AI-assisted content repurposing."

Do not claim production deployment, adoption, measured time savings or extensive testing unless you actually did those things.

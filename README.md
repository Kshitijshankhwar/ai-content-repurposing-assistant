# AI-Powered Content Repurposing Assistant

**Purpose:** Help a storytelling/content team turn a long-form story into short-video hooks, scripts, captions and CTAs. This is a beginner-friendly, locally runnable prototype, not a deployed product.

## What is included
- `app.py`: Streamlit web interface with editable content brief and JSON download.
- `content_engine.py`: prompt builder, Gemini API call, JSON validation, basic quality checks and fixed demo output.
- `sample_story.txt`: fictional input for a reproducible demo.
- `test_engine.py`: six unit tests.
- `INTERVIEW_GUIDE.md`: explanation, workflow, trade-offs and 2-day preparation.
- `requirements.txt`: Python dependencies.

## Run it
1. Install Python 3.10+.
2. Open a terminal inside this folder.
3. Run `pip install -r requirements.txt`.
4. Run `streamlit run app.py`.
5. Open the local URL displayed by Streamlit.
6. **Demo without an API key:** keep Demo mode checked and use the prefilled Maya library story. This is a fixed example, not AI generation.
7. **Actual AI generation:** get a Gemini API key from Google AI Studio, set `GEMINI_API_KEY`, restart Streamlit and uncheck Demo mode.

macOS/Linux: `export GEMINI_API_KEY="your_key"`
Windows PowerShell: `$env:GEMINI_API_KEY="your_key"`

Do not put your key in the source code or upload it to GitHub. Provider quotas/pricing may apply. Internet access is required for live generation.

## Tests
Run `python -m unittest test_engine.py -v` from this folder. The tests cover local prompt/format logic, **not** Gemini output quality.

## Workflow
Source story + audience/platform/tone/language/duration
→ structured prompt
→ Gemini model (or fixed demo example)
→ JSON output
→ schema checks + basic quality checks
→ human editorial review
→ downloadable content pack

## What is and isn't implemented
Implemented: simple UI, structured generation prompt, Gemini integration code, output schema validation, basic checks, fixed demo and tests.
Not implemented: real-world user study, automated factuality evaluation, video generation, editing, scheduling, publishing, analytics or deployed hosting.
The Gemini API integration is provided but cannot be verified without a real API key and network access.

## Next steps
Run the app locally, test at least five *different* stories with the live API, record issues and improve prompts. Only then claim that the project was tested with multiple stories.

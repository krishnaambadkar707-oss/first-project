# AI Powered Interview Bot

Industry Level Final Year Project

## Features

- Resume Analysis (skills, education, projects, certifications, experience, ATS score)
- AI Interview (typed answers, local NLP scoring)
- Voice Interview (speech-to-text, text-to-speech)
- Emotion Detection (webcam-based, DeepFace)
- Confidence Analysis (eye contact, blink rate, head pose, smile)
- PDF Report
- Dashboard & Analytics

## Setup

1. **Create a virtual environment** (Python 3.10-3.12 recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. **Install dependencies** from the project root:
   ```bash
   pip install -r Main_UI/requirements.txt
   ```
   Note: `deepface`, `mediapipe`, `torch`, `transformers`, and `openai-whisper`
   are large packages and will download further model weights on first use.
   `pyaudio` may require system-level audio libraries
   (e.g. `portaudio` on macOS/Linux) before it will install.

3. **Download the spaCy language model** used for resume name extraction:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **(Optional) Enable Gemini-based evaluation.** Copy `.env.example` to
   `.env` in the project root and add your key:
   ```
   GEMINI_API_KEY=your-gemini-api-key-here
   ```
   Without this, the app still works fully using the local rule-based
   evaluator (semantic similarity + keyword/grammar/technical scoring).

5. **Run the app** from the project root:
   ```bash
   streamlit run Main_UI/app.py
   ```
   (or `python Main_UI/main.py`, which launches the same app)

6. **Webcam / microphone permissions.** The Voice Interview and Emotion
   Analysis features need OS-level camera and microphone access —
   grant it when prompted, or those features will fail gracefully but
   won't produce data.

## Database

A local SQLite file (`interview_bot.db`) is created automatically in the
project root on first run — no separate database server is required.

## Project Structure

- `Main_UI/` — app bootstrap, routing, config
- `Authentication/` — register / login / session
- `Dashboard/` — Streamlit pages (home, profile, resume, interview, analytics, report, history, settings)
- `Interview/` — question bank, interview engine, evaluators
- `Speech/` — recording, transcription (Whisper), text-to-speech, timing
- `Emotion_analysis/` — webcam-based emotion/behavior detectors
- `resume/`, `AI/resume/` — resume parsing and analysis
- `Reports/` — scoring, recommendations, charts, PDF export, history, comparisons
- `Database/` — SQLAlchemy models and session handling

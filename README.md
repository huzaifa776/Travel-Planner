---
title: Travel Planner
emoji: ✈️
colorFrom: blue
colorTo: indigo
sdk: gradio
app_file: app.py
pinned: false
---

# AI Travel Itinerary Planner

A Gradio-based AI app that generates a one-day travel itinerary from a city name and user interests.

The project uses LangChain with Groq (`llama-3.3-70b-versatile`) to produce concise, bulleted itinerary suggestions.

## Features

- Generate a day-trip itinerary for any city.
- Accept comma-separated interests (for example: `food, museums, photography`).
- AI-powered response generation using Groq via LangChain.
- Structured project layout with separate chain, core, config, and utility modules.
- Built-in logging to daily log files in the `logs/` directory.
- Custom exception wrapper for clearer error trace context.

## Tech Stack

- Python
- Gradio
- LangChain (`langchain`, `langchain_core`, `langchain_community`)
- LangChain Groq (`langchain_groq`)
- python-dotenv

## Project Structure

```text
Travel Planner/
|-- app.py
|-- requirements.txt
|-- setup.py
|-- readme.md
|-- logs/
|-- src/
|   |-- __init__.py
|   |-- chains/
|   |   |-- __init__.py
|   |   `-- itinerary_chain.py
|   |-- config/
|   |   |-- __init__.py
|   |   `-- config.py
|   |-- core/
|   |   |-- __init__.py
|   |   `-- planner.py
|   `-- utils/
|       |-- __init__.py
|       |-- custom_exception.py
|       `-- logger.py
`-- TRAVEL_Planner.egg-info/
```

## How It Works

1. User submits `city` and `interests` in the Gradio form.
2. `TravelPlanner` (in `src/core/planner.py`) stores inputs and prepares conversation messages.
3. `generate_itineary` (in `src/chains/itinerary_chain.py`) formats a prompt and calls Groq LLM.
4. The generated itinerary is returned and rendered in the Gradio UI.
5. Application logs are written to `logs/log_YYYY-MM-DD.log`.

## Prerequisites

- Python 3.10+
- A Groq API key

## Installation

1. Clone the repository and enter the project folder.

```bash
git clone <your-repository-url>
cd "Travel Planner"
```

2. Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The app loads this variable through `python-dotenv` in `app.py` and `src/config/config.py`.

## Run The App

```bash
python app.py
```

Then open the local URL shown in your terminal (usually `http://127.0.0.1:7860`).

## Packaging (Optional)

The project includes `setup.py`, so you can install it as a local package:

```bash
pip install -e .
```

## Logging and Error Handling

- Logger utility: `src/utils/logger.py`
- Custom exception class: `src/utils/custom_exception.py`
- Log output path: `logs/log_<date>.log`

## Notes

- Current function and UI labels use the project's existing naming (`itineary`) in code.
- Interests are expected as comma-separated values.

## Future Improvements

- Add multi-day itinerary support.
- Add budget/time constraints in prompt inputs.
- Add unit tests for `TravelPlanner` and chain logic.
- Improve spelling consistency (`itineary` -> `itinerary`) across codebase.


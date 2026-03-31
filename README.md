# Gemini-Powered Ecosystem Narration (GSoC Entry Task)

This repository contains my entry task for the Google Summer of Code proposal. It demonstrates the ability to ingest ecosystem data (Pokémon-themed), engineer an effective prompt, and utilize the modern Google Gemini API to generate a concise, 2-4 sentence narrative summary.

## Key Highlights for Reviewers

- **Modern SDK & Models:** Built using the newly unified `google-genai` SDK and queries the latest `gemini-2.5-flash` model for optimal performance and cost-efficiency.
- **Strict Version Control:** The repository was built using **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`) and strict feature-branching strategies to simulate a professional open-source workflow.
- **Extensive Documentation:** Includes forward-looking database schema designs (with Mermaid.js Entity-Relationship Diagrams) and an implementation plan located in the `docs/` directory.

---

## Reliability & Fallback Mechanisms (Fault Tolerance)

To ensure **100% reproducibility** for the reviewer, this script was built defensively. It anticipates and gracefully handles potential crashes, fallouts, and edge cases:

1. **No API Key / Missing Environment:** If the reviewer runs this script without a `.env` file, the script will not crash. It will detect the missing key and cleanly print a hardcoded mock output.
2. **Network/API Failures:** The actual API call is wrapped in a robust `try...except` block. If the reviewer's internet disconnects, or if Google's servers return an error (e.g., rate limits, deprecated models), the script intercepts the crash, logs a polite warning, and serves the mock output.
3. **Safety Filter Blocks:** Handled edge cases where the AI might return `None` instead of text (such as triggering Google's safety filters). It safely checks `if response.text:` before parsing, satisfying strict Pylance/static type checkers.
4. **Dependency Isolation:** Uses a `requirements.txt` and virtual environment to prevent dependency conflicts on the evaluator's machine.

---

## Repository Structure

```text
gsoc-gemini-pokemon-narration/
├── data/
│   └── pokemon_events.json        # Sample input dataset
├── docs/
│   ├── database_schema.md         # Future-scoped ERD diagrams
│   └── implementation_plan.md     # Phase 1 & 2 planning
├── outputs/
│   └── sample_output.txt          # Saved generated narratives
├── src/
│   └── summarizer.py              # Main Python script
├── .gitignore                     # Ignores sensitive keys and cache
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone <your-github-repo-url>
cd gsoc-gemini-pokemon-narration
```

**2. Set up a virtual environment (Recommended)**
Creating a virtual environment ensures that dependencies do not conflict with your system Python packages.
```bash
# Create the environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**
Create a `.env` file in the root directory and add your Gemini API key:
```text
GEMINI_API_KEY=your_actual_api_key_here
```
*(Note: If no API key is provided, or if you wish to test the fallback mechanism offline, you can skip this step. The script will automatically detect the missing key and provide a reproducible mock output.)*

## Running the Script

Run the summarizer using the default dataset:
```bash
python src/summarizer.py
```

To run the script with a custom JSON dataset:
```bash
python src/summarizer.py --data path/to/your/custom_data.json
```

## Evaluator Notes: Testing the Fallbacks

To evaluate the fault-tolerance of this script, you can simulate API failures:
1. **Simulate Missing Credentials:** Temporarily rename your `.env` file to something else. The script will log an `[INFO]` message and return the mock summary.
2. **Simulate Network/API Crash:** Turn off your Wi-Fi or change the model name in the code to an invalid string (e.g., `gemini-fake-model`). The `try...except` block will catch the `404/500` error, log a `[WARNING]`, and safely print the mock summary without halting execution.
```


import json
import os
import argparse
from dotenv import load_dotenv

# Import the NEW google-genai library
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Load environment variables (like GEMINI_API_KEY)
load_dotenv()

def load_data(filepath):
    """Loads the JSON event data."""
    with open(filepath, 'r') as file:
        return json.load(file)

def get_prompt(events):
    """Constructs the prompt for the LLM."""
    events_str = json.dumps(events, indent=2)
    prompt = (
        "You are an expert narrator and storyteller in the Pokémon universe.\n"
        "Given the following chronological sequence of ecosystem events, write a compelling, "
        "2 to 4 sentence summary that captures the overarching narrative.\n\n"
        f"Events:\n{events_str}\n\n"
        "Summary (2-4 sentences):"
    )
    return prompt

def generate_summary(prompt):
    """Generates the summary using the new Gemini Client API."""
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or not GEMINI_AVAILABLE:
        print("[INFO] No GEMINI_API_KEY found or google-genai not installed. Using mock output for reproducibility.")
        return (
            "Ash began his journey on Route 1, where a quick Thunderbolt from Pikachu dealt with a wild Pidgey "
            "before they stumbled upon a useful Potion. After resting up at the Viridian City Pokémon Center, "
            "the duo confidently entered Viridian Forest and emerged victorious in a battle against Bug Catcher Rick."
        )

    print("[INFO] Calling Gemini API using the new google-genai SDK...")
    
    # 1. Initialize the new Client
    client = genai.Client(api_key=api_key)
    
    # 2. Call the API using client.models.generate_content
    # Using gemini-1.5-flash as it is fast, cheap, and excellent for text tasks
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=prompt
    )
    
    return response.text.strip()

def main():
    parser = argparse.ArgumentParser(description="Gemini-Powered Ecosystem Narration")
    parser.add_argument("--data", type=str, default="data/pokemon_events.json", help="Path to the JSON data file")
    args = parser.parse_args()

    # 1. Load Data
    events = load_data(args.data)
    
    # 2. Generate Prompt
    prompt = get_prompt(events)
    
    # 3. Get Summary
    summary = generate_summary(prompt)
    
    # 4. Output Results
    print("\n" + "="*50)
    print("PROMPT USED:")
    print("="*50)
    print(prompt)
    print("\n" + "="*50)
    print("GENERATED NARRATION:")
    print("="*50)
    print(summary)
    print("="*50 + "\n")

    # Optionally save to output folder
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/sample_output.txt", "w", encoding="utf-8") as f:
        f.write(f"PROMPT:\n{prompt}\n\nSUMMARY:\n{summary}\n")

if __name__ == "__main__":
    main()
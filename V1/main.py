from google import genai

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="key.env")

from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / "key.env")

def main():

    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        print("Error: GEMINI_API_KEY not found. Check your key.env file.")
        return

    client = genai.Client(api_key=API_KEY)

    chat_history = []

    print("Echo is ready. Type 'quit' to exit.\n")

    while True:
        n = input("You: ")

        if n.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        chat_history.append({"role": "user", "parts": [{"text": n}]})

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=chat_history,
            )
            reply = response.text

        except Exception as e:
            print(f"Error: Could not get a response ({e})")
            continue

        chat_history.append({"role": "model", "parts": [{"text": reply}]})
        print(f"Echo: {reply}\n")
main()
def test():
    print("Current directory:", os.getcwd())
    print("API Key:", os.getenv("GEMINI_API_KEY"))
# test()

# always use - git rm --cached key.env
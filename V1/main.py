from google import genai

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="key.env")

from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / "key.env")

def main():
    
    API_KEY = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=API_KEY)

    n = input("Enter your input here: ")

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=n,
    )

    print(response.text)

main()
def test():
    print("Current directory:", os.getcwd())
    print("API Key:", os.getenv("GEMINI_API_KEY"))
# test()

# always use - git rm --cached key.env
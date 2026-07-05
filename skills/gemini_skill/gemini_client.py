from dotenv import load_dotenv
from google import genai
import os

# Load .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

client = genai.Client(
    api_key=API_KEY
)

def ask_gemini(system_prompt, user_prompt):
    """
    Sends the system prompt and user prompt to Gemini.
    Returns the model response as text.
    """

    try:

        prompt = f"""
System Instructions:
{system_prompt}

User:
{user_prompt}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"ERROR: {str(e)}"
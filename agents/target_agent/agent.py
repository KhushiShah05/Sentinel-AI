from click import prompt
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


class TargetAgent:

    def ask(self, system_prompt, user_prompt):

        full_prompt = f"""
        SYSTEM:
        {system_prompt}

        USER:
        {user_prompt}
        """

        try:
            response = model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"API Error: {str(e)}"
   
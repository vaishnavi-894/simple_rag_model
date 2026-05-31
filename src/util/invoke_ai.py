import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def invoke_ai(system_message: str, user_message: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
{system_message}

{user_message}
"""

    response = model.generate_content(prompt)

    return response.text
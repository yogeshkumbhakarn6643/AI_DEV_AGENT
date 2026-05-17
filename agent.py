import os
import json
import platform
import re

import google.generativeai as genai

from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_os():

    os_name = platform.system()

    if os_name == "Windows":
        return "Windows"

    elif os_name == "Darwin":
        return "macOS"

    else:
        return "Linux"


def extract_json(text):

    # Remove markdown blocks
    text = text.replace("```json", "")
    text = text.replace("```", "")

    # Find JSON object
    match = re.search(r'\{.*\}', text, re.DOTALL)

    if not match:
        raise Exception("No JSON found in AI response")

    return match.group(0)


def generate_project_steps(user_requirement):

    current_os = get_os()

    final_prompt = f"""
Current OS: {current_os}

User Requirement:
{user_requirement}
"""

    response = model.generate_content(
        [
            SYSTEM_PROMPT,
            final_prompt
        ]
    )

    raw_text = response.text

    print("\n================ AI RESPONSE ================\n")
    print(raw_text)

    try:

        cleaned_json = extract_json(raw_text)

        return json.loads(cleaned_json)

    except Exception as e:

        print("\nJSON Parsing Error")
        print(str(e))

        raise e
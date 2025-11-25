import os
import google.generativeai as genai

# -----------------------------------------------------
# 1. Configure Gemini safely
# -----------------------------------------------------
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("ERROR: GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=API_KEY)

# -----------------------------------------------------
# 2. Ask Gemini Model
# -----------------------------------------------------
def ask_model(prompt, model="gemini-2.5-flash"):
    model_obj = genai.GenerativeModel(model)
    result = model_obj.generate_content(prompt)
    return result.text

# -----------------------------------------------------
# 3. Coding Agent Logic
# -----------------------------------------------------
def run_coding_agent(request):
    system_prompt = f"""
You are a coding assistant.
Provide:
1. Explanation
2. Code
3. Improvements

User request: {request}
"""
    return ask_model(system_prompt)

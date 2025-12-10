import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

class LLMService:
    def __init__(self):
        self.providers = ["Google Gemini", "OpenAI GPT-4"]

    def get_providers(self):
        return self.providers

    def generate_response(self, provider, prompt, api_key=None):
        if provider == "Google Gemini":
            if not api_key:
                api_key = os.getenv("GOOGLE_API_KEY")
            
            if not api_key:
                return "Error: GOOGLE_API_KEY not found. Please set it in .env or provide it in the UI."
            
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            try:
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                return f"Error calling Gemini: {e}"

        elif provider == "OpenAI GPT-4":
            if not api_key:
                api_key = os.getenv("OPENAI_API_KEY")
                
            if not api_key:
                return "Error: OPENAI_API_KEY not found. Please set it in .env or provide it in the UI."
            
            client = OpenAI(api_key=api_key)
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"Error calling OpenAI: {e}"
        
        return "Error: Unknown provider selected."

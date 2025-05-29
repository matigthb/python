# API de OpenAI 
import requests
import json

OPENAI_KEY = "XXXXXXXXXXXXXXXXXX"

def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre programación")

print(json.dumps(api_response,indent=2))


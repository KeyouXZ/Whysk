import requests
import json

def groq(api_key: str, message: str):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "model": "llama3-8b-8192"
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        
        result = response.json()
        message = result['choices'][0].get('message', {})
        return message.get('content', '')
    
    except requests.RequestException as e:
        return "Failed to contact to API"
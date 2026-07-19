# support_engine.py
# Customer Support Engine using DeepSeek API (cloud-friendly)

import os
import requests
import json

def customer_support_bot(message):
    """
    Customer Support Bot powered by DeepSeek.
    Works on Streamlit Cloud (no Ollama, no SDK required).
    """

    api_key = os.getenv("DEEPSEEK_API_KEY")   # <-- FIXED

    if not api_key:
        return (
            "⚠️ Missing DEEPSEEK_API_KEY.\n\n"
            "Add your API key in Streamlit Cloud:\n"
            "Settings → Secrets → Add DEEPSEEK_API_KEY"
        )

    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful customer support assistant. "
                    "You help users with refunds, order tracking, cancellations, "
                    "product issues, payment problems, and general support."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"⚠️ Error communicating with DeepSeek API: {str(e)}"

# support_engine.py

import streamlit as st
import requests

def customer_support_bot(message):

    try:
        api_key = st.secrets["DEEPSEEK_API_KEY"]

    except Exception:
        return (
            "⚠️ Missing DEEPSEEK_API_KEY.\n\n"
            "Add it in Streamlit Cloud:\n"
            "Settings → Secrets"
        )

    url = "https://api.deepseek.com/chat/completions"

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
                    "Help with refunds, orders, cancellations, payments, "
                    "and general customer support."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        if response.status_code != 200:
            return f"❌ DeepSeek API Error:\n{data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"⚠️ Error communicating with DeepSeek API:\n{e}"
# support_engine.py
# Customer Support Engine using Ollama (Llama 3)

# Try importing Ollama safely
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ModuleNotFoundError:
    OLLAMA_AVAILABLE = False


def customer_support_bot(message):
    """
    Customer Support Bot powered by Ollama (Llama 3).
    If Ollama is not installed or the model is missing,
    returns a safe fallback message instead of crashing.
    """

    # If Ollama is not installed, return a safe fallback
    if not OLLAMA_AVAILABLE:
        return (
            "⚠️ Ollama is not installed in this environment.\n\n"
            "To use the AI model (Llama 3), please install Ollama:\n"
            "1. Download from https://ollama.com/download\n"
            "2. Then run: pip install ollama\n\n"
            "Until then, the Customer Support Bot cannot generate AI responses."
        )

    # Try sending the message to Ollama
    try:
        response = ollama.chat(
            model="llama3",   # IMPORTANT: llama3.2 does NOT exist
            messages=[
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
        )

        # Return the model's response
        return response["message"]["content"]

    except Exception as e:
        # If Ollama is installed but something else fails (model missing, server not running, etc.)
        return f"⚠️ Error communicating with Ollama: {str(e)}"

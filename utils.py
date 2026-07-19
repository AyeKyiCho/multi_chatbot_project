# utils.py

def clean_text(text: str) -> str:
    """Normalize user input."""
    return text.strip().lower()

def validate_message(text: str) -> bool:
    """Check if message is not empty."""
    return len(text.strip()) > 0

# chatbot_functions.py

def customer_support_bot(message):
    return "Refunds take 5–7 business days. Let me know if you need help with an order."

def resume_analyzer_bot(message):
    return "Try adding measurable achievements, action verbs, and quantified results."

def document_qa_bot(message):
    return "Please upload a PDF document. I can answer questions about its content."

def medical_info_bot(message):
    return "I provide general health information only. For medical advice, consult a professional."

def immigration_bot(message):
    return "I can explain PR, citizenship, and visa categories. What would you like to know?"


# chatbot_functions.py

def customer_support_bot(message):
    message = message.lower()

    if "refund" in message:
        return (
            "Refunds typically take 5–7 business days once processed. "
            "If you already submitted a request, I can help you check its status."
        )

    if "order" in message:
        return (
            "I can help you track your order. Please provide your order number."
        )

    if "cancel" in message:
        return (
            "I can help you cancel your order. May I have your order number?"
        )

    return "I can help with refunds, order tracking, cancellations, and general support."


def resume_analyzer_bot(message):
    suggestions = [
        "Use strong action verbs (Led, Built, Designed, Implemented).",
        "Add measurable achievements (e.g., improved performance by 30%).",
        "Include relevant keywords for ATS scanning.",
        "Keep bullet points concise and results‑focused."
    ]

    return "Here are improvements you can make:\n\n" + "\n".join(f"- {s}" for s in suggestions)


def document_qa_bot(message):
    return (
        "Upload a PDF and I can answer questions about its content. "
        "PDF reading will be added in the next version."
    )


def medical_info_bot(message):
    return (
        "I can provide general health information only. "
        "For diagnosis or treatment, please consult a licensed medical professional."
    )


def immigration_bot(message):
    message = message.lower()

    if "pr" in message:
        return (
            "To apply for Permanent Residency (PR), you typically need to qualify under "
            "Express Entry, Provincial Nominee Program (PNP), or family sponsorship. "
            "I can explain each pathway if you'd like."
        )

    if "citizenship" in message:
        return (
            "Citizenship usually requires PR status, physical presence requirements, "
            "language proficiency, and a citizenship test."
        )

    if "visa" in message:
        return (
            "There are multiple visa categories: work permits, study permits, visitor visas, "
            "and business visas. Which one are you interested in?"
        )

    return "I can help with PR, citizenship, visa categories, and immigration pathways."

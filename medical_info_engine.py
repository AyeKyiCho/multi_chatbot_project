# ============================
# MEDICAL INFO ENGINE (ADVANCED)
# ============================

def detect_medical_intent(msg):
    msg = msg.lower()

    if any(word in msg for word in ["symptom", "feel", "pain", "hurt"]):
        return "symptoms"

    if any(word in msg for word in ["disease", "condition", "what is", "explain"]):
        return "condition_info"

    if any(word in msg for word in ["medicine", "drug", "pill", "treatment"]):
        return "medication"

    if any(word in msg for word in ["emergency", "urgent", "help now"]):
        return "emergency"

    return "general"

def handle_symptoms():
    return (
        "I can provide general information about symptoms, but I cannot diagnose. "
        "If symptoms are severe or persistent, please consult a licensed medical professional."
    )


def handle_condition_info():
    return (
        "I can explain general health conditions. Tell me the condition you want to know about, "
        "and I’ll provide safe, general information."
    )


def handle_medication():
    return (
        "I can provide general information about medications, but I cannot recommend or prescribe. "
        "Always follow instructions from a licensed medical professional."
    )


def handle_emergency():
    return (
        "If this is an emergency, please contact your local emergency services immediately. "
        "I cannot provide urgent medical assistance."
    )


def handle_medical_general():
    return (
        "I can help with general health information about symptoms, conditions, and medications. "
        "For diagnosis or treatment, please consult a licensed medical professional."
    )


def medical_info_bot(message):
    intent = detect_medical_intent(message)

    if intent == "symptoms":
        return handle_symptoms()

    if intent == "condition_info":
        return handle_condition_info()

    if intent == "medication":
        return handle_medication()

    if intent == "emergency":
        return handle_emergency()

    return handle_medical_general()

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

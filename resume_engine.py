def resume_analyzer_bot(message):
    suggestions = [
        "Use strong action verbs (Led, Built, Designed, Implemented).",
        "Add measurable achievements (e.g., improved performance by 30%).",
        "Include relevant keywords for ATS scanning.",
        "Keep bullet points concise and results‑focused."
    ]

    return "Here are improvements you can make:\n\n" + "\n".join(f"- {s}" for s in suggestions)

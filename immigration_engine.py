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

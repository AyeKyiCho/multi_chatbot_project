# config.py

CHATBOT_MODES = [
    "Customer Support",
    "Resume Analyzer",
    "Document Q&A",
    "Medical Info",
    "Immigration Info"
]

MODE_TO_FUNCTION = {
    "Customer Support": "customer_support_bot",
    "Resume Analyzer": "resume_analyzer_bot",
    "Document Q&A": "document_qa_bot",
    "Medical Info": "medical_info_bot",
    "Immigration Info": "immigration_bot"
}

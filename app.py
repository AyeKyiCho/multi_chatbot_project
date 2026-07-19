# app.py

import streamlit as st
from chatbot_functions import (
    # customer_support_bot,
    # resume_analyzer_bot,
    document_qa_bot,
    # medical_info_bot,
    # immigration_bot
   
)

from immigration_engine import (
     immigration_bot
)

from resume_engine import (
    resume_analyzer_bot
)

from support_engine import (
    customer_support_bot
)

from medical_info_engine import (
     medical_info_bot
)

from config import CHATBOT_MODES
from utils import clean_text, validate_message

st.set_page_config(page_title="Multi Chatbot", layout="centered")
st.title("Multi Chatbot System")

mode = st.selectbox("Choose a chatbot:", CHATBOT_MODES)
msg = st.text_input("Your message:")

if msg:
    if not validate_message(msg):
        st.warning("Please enter a valid message.")
    else:
        msg_clean = clean_text(msg)

        if mode == "Customer Support":
            st.write(customer_support_bot(msg_clean))
        elif mode == "Resume Analyzer":
            st.write(resume_analyzer_bot(msg_clean))
        elif mode == "Document Q&A":
            st.write(document_qa_bot(msg_clean))
        elif mode == "Medical Info":
            st.write(medical_info_bot(msg_clean))
        elif mode == "Immigration Info":
            st.write(immigration_bot(msg_clean))

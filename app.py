import streamlit as st
import os
from PyPDF2 import PdfReader
import chromadb
import numpy as np
import requests
import json

# -----------------------------
# CONFIG
# -----------------------------
LLM_MODEL = "llama3.1"   # Local Ollama model
EMBED_MODEL = "mxbai-embed-large"

# Initialize ChromaDB (local persistent store)
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="medical_docs",
    metadata={"hnsw:space": "cosine"}
)

# -----------------------------
# FUNCTIONS
# -----------------------------
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def chunk_text(text, chunk_size=200):  # safer chunk size
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


def embed_text(text):
    """Use Ollama embedding model (mxbai-embed-large) with validation."""
    if not text.strip():
        return None  # skip empty text

    payload = {
        "model": EMBED_MODEL,
        "input": text
    }

    response = requests.post("http://localhost:11434/api/embeddings", json=payload)
    data = response.json()

    # Extract embedding from possible Ollama formats
    emb = None
    if "embedding" in data:
        emb = data["embedding"]
    elif "data" in data and "embedding" in data["data"]:
        emb = data["data"]["embedding"]
    elif "embeddings" in data:
        emb = data["embeddings"][0]

    # Validate embedding shape
    if (
        emb is None or
        not isinstance(emb, list) or
        len(emb) == 0 or
        not isinstance(emb[0], (int, float))
    ):
        print("Invalid embedding:", data)
        return None

    return emb


def add_chunks_to_vector_db(chunks):
    ids = []
    embeddings = []
    metadatas = []

    existing = collection.get()
    existing_count = len(existing.get("ids", []))

    for i, chunk in enumerate(chunks):
        emb = embed_text(chunk)

        # Skip failed or empty embeddings
        if emb is None:
            print("Skipping chunk (invalid embedding):", chunk[:80])
            continue

        ids.append(f"chunk_{existing_count + len(ids)}")
        embeddings.append(emb)
        metadatas.append({"text": chunk})

    # Prevent empty add() calls
    if len(embeddings) == 0:
        print("No valid embeddings to add.")
        return

    collection.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas
    )


def retrieve_relevant_chunks(query, k=3):
    query_embedding = embed_text(query)

    if query_embedding is None:
        return ["Could not embed query."]

    db = collection.get()
    if len(db.get("ids", [])) == 0:
        return ["No documents found in vector database."]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    metadatas = results.get("metadatas", [[]])
    if not metadatas or not metadatas[0]:
        return ["No relevant chunks found."]

    chunks = [meta["text"] for meta in metadatas[0]]
    return chunks


def generate_answer(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are MedInfoCopilot, an AI assistant for medical workflows and SOPs.

Use ONLY the context below to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{query}

Answer with citations.
"""

    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    data = response.json()
    return data.get("response", "No response from model.")


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="MedInfoCopilot (Local)", layout="wide")
st.title("🧠 MedInfoCopilot – Local Medical RAG Assistant (Ollama)")

st.write("Upload medical SOPs, manuals, or workflow PDFs and ask questions. No API key needed.")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_pdf:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_pdf)

    chunks = chunk_text(text)

    with st.spinner("Generating embeddings and storing in vector DB..."):
        add_chunks_to_vector_db(chunks)

    st.success(f"Document processed. {len(chunks)} chunks processed (only valid chunks stored).")

# Chat interface
query = st.text_input("Ask a question about your medical documents:")

if query:
    with st.spinner("Retrieving relevant information..."):
        retrieved = retrieve_relevant_chunks(query)

    with st.spinner("Generating answer..."):
        answer = generate_answer(query, retrieved)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for i, chunk in enumerate(retrieved):
        with st.expander(f"Source {i+1}"):
            st.write(chunk)

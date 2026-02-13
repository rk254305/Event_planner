import os

# ===== LangSmith =====
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "events"

import streamlit as st
from event_planner import EventPlannerAI

ai = EventPlannerAI()

st.title("🎉 Event Planner AI (RAG + Agents)")
st.write("Powered by **Ollama + LangChain + FAISS + LangSmith**")

query = st.text_input("Ask anything about event planning:")

if st.button("Ask AI"):
    if query:
        with st.spinner("Thinking..."):
            response = ai.ask_agent(query)
        st.success("Answer")
        st.write(response)
    else:
        st.warning("Enter a question")
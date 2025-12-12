import streamlit as st
import os
import requests
from datetime import datetime
from llm_service import LLMService
from prompts import ANALYSIS_PROMPT, SYSTEM_PROMPT

def main():
    st.set_page_config(page_title="Agent Pikm", page_icon="🏈", layout="wide")
    
    st.title("🏈 Agent Pikm: NFL Pick'em Assistant")
    st.markdown("Select an LLM provider to generate analysis for this week's games.")

    # Initialize Service
    llm_service = LLMService()

    # Sidebar for Configuration
    with st.sidebar:
        st.header("Configuration")
        selected_provider = st.selectbox("Select LLM Provider", llm_service.get_providers())
        
        api_key = None
        if selected_provider == "Google Gemini":
            if os.getenv("GOOGLE_API_KEY"):
                st.success("✅ GOOGLE_API_KEY detected")
            else:
                api_key = st.text_input("Enter Google API Key", type="password")
        elif selected_provider == "OpenAI GPT-4":
            if os.getenv("OPENAI_API_KEY"):
                st.success("✅ OPENAI_API_KEY detected")
            else:
                api_key = st.text_input("Enter OpenAI API Key", type="password")

    # Main Content
    if st.button("Generate Picks"):
        full_prompt = f"{SYSTEM_PROMPT}\n\n{ANALYSIS_PROMPT}"
        
        with st.spinner(f"Consulting {selected_provider}..."):
            response = llm_service.generate_response(selected_provider, full_prompt, api_key)
            
            st.subheader("Analysis Results")
            st.write(response)
            
            # Future TODO: Parse JSON response and display as a dataframe/dashboard

if __name__ == "__main__":
    main()
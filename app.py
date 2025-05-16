import streamlit as st
from backend import get_gpt_response

st.set_page_config(page_title="Prompt API Playground", layout="centered")

st.title("🧠 GPT Prompt API Playground")

with st.expander("⚙️ System Instruction (Optional)"):
    system_instruction = st.text_area("System Prompt", "You are a helpful assistant.")

prompt = st.text_area("📝 Enter your Prompt", height=200, placeholder="Type something...")

temperature = st.slider("🎯 Temperature (Creativity)", 0.0, 1.0, 0.7, 0.1)

if st.button("🚀 Submit"):
    if not prompt.strip():
        st.warning("Please enter a prompt before submitting.")
    else:
        with st.spinner("Generating response..."):
            output = get_gpt_response(prompt, system_instruction, temperature)
        st.success("✅ Response")
        st.markdown("```text\n" + output + "\n```")

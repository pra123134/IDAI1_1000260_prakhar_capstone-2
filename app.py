import streamlit as st
import google.generativeai as genai
import os

# ✅ Secure API Key Handling
api_key = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
if not api_key:
    st.error("⚠️ API Key is missing. Add your Gemini API key in Streamlit Secrets or as an environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# ✅ AI Response Function
def get_ai_response(prompt, fallback_message="⚠️ AI response unavailable. Please try again later."):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text else fallback_message
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}\n{fallback_message}"

# ✅ Streamlit UI Setup
st.set_page_config(page_title="Gamified Smart Restaurant Management", layout="wide")
st.title("🏆 Gamified Smart Restaurant Management with AI")
st.write("🚀 Enter managerial challenges and receive AI-driven gamification solutions.")

# 🎯 Gamified Decision-Making
st.header("🎮 Gamified Decision-Making")
decision_prompt = st.text_area("🔹 Enter a management challenge (e.g., high waste, low sales, peak hour inefficiencies)")
if st.button("🏆 Get Gamified Solution"):
    if decision_prompt:
        prompt = f"""
        Gamified Decision-Making: AI presents challenges ({decision_prompt}), and managers earn points for optimizing decisions.
        """
        st.text_area("🎯 AI-Generated Challenge:", get_ai_response(prompt), height=250)
    else:
        st.error("⚠️ Please enter a challenge before generating a response.")

# 🔍 AI-Generated Scenario Simulations
st.header("📊 AI-Generated Scenario Simulations")
scenario_prompt = st.text_area("🔹 Enter a bottleneck situation (e.g., staff shortages, inventory issues)")
if st.button("📈 Get Scenario Simulation"):
    if scenario_prompt:
        prompt = f"""
        AI-Generated Scenario Simulations – AI predicts upcoming bottlenecks ({scenario_prompt}) and gives managers virtual case studies to solve.
        """
        st.text_area("📊 AI-Generated Simulation:", get_ai_response(prompt), height=250)
    else:
        st.error("⚠️ Please enter a bottleneck situation before generating a response.")

# 🌍 AI-Driven Sustainability Challenges
st.header("♻️ AI-Driven Sustainability Challenges")
sustainability_prompt = st.text_area("🔹 Enter an eco-challenge (e.g., waste reduction, energy efficiency)")
if st.button("🌱 Get Sustainability Challenge"):
    if sustainability_prompt:
        prompt = f"""
        AI-Driven Sustainability Challenges – AI sets goals for ({sustainability_prompt}) and rewards managers for eco-friendly decisions.
        """
        st.text_area("♻️ AI-Generated Challenge:", get_ai_response(prompt), height=250)
    else:
        st.error("⚠️ Please enter a sustainability challenge before generating a response.")

# ⏳ Dynamic AI Adjustments for Peak Hours
st.header("⏰ Dynamic AI Adjustments for Peak Hours")
peak_hour_prompt = st.text_area("🔹 Enter peak-hour management challenge")
if st.button("⚡ Get Peak Hour Optimization"):
    if peak_hour_prompt:
        prompt = f"""
        Dynamic AI Adjustments for Peak Hours – Managers get real-time AI insights on ({peak_hour_prompt}) and are rewarded for balancing workload and demand.
        """
        st.text_area("⏰ AI-Generated Peak Hour Strategy:", get_ai_response(prompt), height=250)
    else:
        st.error("⚠️ Please enter a peak-hour challenge before generating a response.")

# ✅ Footer
st.write("🚀 Powered by Gemini 1.5 Pro with GenAI")

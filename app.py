import streamlit as st
import google.generativeai as genai

# ✅ Configure API Key securely
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["AIzaSyAAMjfIt1fHGeoSgx9QDSOZfG6KeGGJwp0"]
    genai.configure(api_key=api_key)
else:
    st.error("⚠️ API Key is missing. Go to Streamlit Cloud → Settings → Secrets and add your API key.")
    st.stop()

# ✅ AI Response Generator
def get_ai_response(prompt, fallback_message="⚠️ AI response unavailable. Please try again later."):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text.strip() else fallback_message
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}\n{fallback_message}"

# ✅ Streamlit UI Configuration
st.set_page_config(page_title="Gamified Decision-Making for Smart Restaurants", layout="wide")

st.title("🎯 Gamified Decision-Making for Restaurant Management with Gemini 1.5 Pro")
st.write("🚀 Optimize decisions, predict challenges, and enhance sustainability through AI-driven gamification.")

# 🎯 **Gamified Decision-Making**
st.header("📊 Gamified Decision-Making Challenges")

decision_scenario = st.text_area("🔍 Describe a managerial challenge (e.g., high waste, low sales, peak inefficiencies)")
if st.button("🚀 Generate AI Challenge"):
    if not decision_scenario:
        st.error("⚠️ Please enter a decision-making scenario.")
    else:
        prompt = f"""
        Generate a gamified decision-making challenge for restaurant managers facing:
        - Scenario: {decision_scenario}
        
        Provide a scoring system based on the effectiveness of decisions made.
        """
        st.text_area("🏆 AI-Generated Challenge:", get_ai_response(prompt), height=300)

# 📌 **AI-Generated Scenario Simulations**
st.header("📌 AI-Generated Scenario Simulations")
if st.button("🧠 Predict and Solve Bottlenecks"):
    prompt = "Predict upcoming bottlenecks in restaurant management (e.g., staff shortages, inventory issues) and provide a virtual case study to solve."
    st.text_area("🔮 AI-Generated Bottleneck Scenario:", get_ai_response(prompt), height=300)

# 🌱 **AI-Driven Sustainability Challenges**
st.header("🌱 AI-Driven Sustainability Challenges")
if st.button("🌍 Generate Sustainability Challenge"):
    prompt = "Create a sustainability-focused restaurant challenge, encouraging managers to optimize waste reduction and energy efficiency with rewards."
    st.text_area("♻️ Sustainability Challenge:", get_ai_response(prompt), height=300)

# ⏳ **Dynamic AI Adjustments for Peak Hours**
st.header("⏳ Dynamic AI Adjustments for Peak Hours")
if st.button("📈 Optimize Peak Hour Performance"):
    prompt = "Analyze peak hour trends and suggest real-time AI-driven strategies for managers to balance workload and demand efficiently."
    st.text_area("🚦 AI-Powered Peak Hour Strategy:", get_ai_response(prompt), height=300)

# ✅ Footer
st.write("🚀 Powered by Gemini 1.5 Pro with GenAI")


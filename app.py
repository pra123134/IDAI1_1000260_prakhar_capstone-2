import streamlit as st
import google.generativeai as genai

# ✅ Configure API Key securely
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
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

st.title("🎮 Gamified Decision-Making for Smart Restaurant Management")
st.write("🚀 Earn points for optimizing decisions and tackling AI-generated challenges.")

# 🎯 **Decision-Making Challenges**
st.header("🧠 Decision-Making Challenges")

challenge_type = st.selectbox("🎯 Select a Challenge Type", [
    "High Waste Reduction",
    "Low Sales Optimization",
    "Peak Hour Efficiency",
    "Staff Shortages Management"
])

if st.button("⚡ Generate AI Challenge"):
    prompt = f"""
    Generate a gamified decision-making challenge for restaurant managers dealing with:
    - {challenge_type}
    
    Include:
    - Scenario description
    - Optimization strategies
    - Scoring system
    - Performance evaluation metrics
    - AI-generated feedback and reward system
    """
    st.text_area("📋 AI-Generated Challenge:", get_ai_response(prompt), height=300)

# 🏆 **Scenario Simulations**
st.header("📊 AI-Generated Scenario Simulations")

simulation_topic = st.selectbox("🔍 Choose a Scenario Simulation", [
    "Predict Staff Shortages",
    "Manage Inventory Issues",
    "Forecast Demand Variations",
    "Handle Emergency Situations"
])

if st.button("🔄 Generate Scenario Simulation"):
    prompt = f"""
    Generate a virtual case study to simulate:
    - {simulation_topic}
    
    Provide:
    - A realistic restaurant scenario
    - Decision-making options
    - AI-driven hints and insights
    - Scoring based on managerial decisions
    - Rewards for optimal solutions
    """
    st.text_area("📋 AI-Generated Scenario:", get_ai_response(prompt), height=300)

# 🌍 **Sustainability Challenges**
st.header("🌱 AI-Driven Sustainability Challenges")

sustainability_focus = st.selectbox("♻️ Choose a Sustainability Focus", [
    "Waste Reduction",
    "Energy Efficiency",
    "Sustainable Sourcing",
    "Eco-Friendly Packaging"
])

if st.button("🌎 Generate Sustainability Challenge"):
    prompt = f"""
    Generate an AI-driven sustainability challenge for restaurant managers focusing on:
    - {sustainability_focus}
    
    Include:
    - Environmental impact assessment
    - AI recommendations for sustainability
    - Reward system for eco-friendly choices
    - Long-term sustainability tracking metrics
    """
    st.text_area("📋 AI-Generated Sustainability Challenge:", get_ai_response(prompt), height=300)

# 📊 **Dynamic AI Adjustments for Peak Hours**
st.header("⏳ Dynamic AI Adjustments for Peak Hours")

if st.button("⚙️ Get AI Insights for Peak Hour Management"):
    prompt = """
    Analyze peak hour trends and suggest AI-driven strategies for managers to:
    - Balance workload and demand
    - Optimize staffing during peak hours
    - Improve table turnover rates
    - Enhance customer satisfaction during rush hours
    - Implement AI-driven rewards for efficiency
    """
    st.text_area("📋 AI-Powered Peak Hour Insights:", get_ai_response(prompt), height=300)

# ✅ Footer
st.write("🚀 Powered by Gemini 1.5 Pro with GenAI")

import streamlit as st
import google.generativeai as genai
import os

# ✅ Configure API Key securely (Supports both Streamlit Cloud & Local Execution)
api_key = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
if not api_key:
    st.error("⚠️ API Key is missing. Add it in Streamlit Secrets or as an environment variable.")
    st.stop()
genai.configure(api_key=api_key)

# ✅ AI Response Generator
def get_ai_response(prompt, fallback_message="⚠️ AI response unavailable. Please try again later."):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text.strip() else fallback_message
    except AttributeError:
        return fallback_message
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}\n{fallback_message}"

# ✅ Streamlit UI Configuration
st.set_page_config(page_title="Gamified Decision-Making for Restaurant Managers", layout="wide")

st.title("🏆 Gamified Decision-Making for Smart Restaurant Management")
st.write("🎯 Optimize restaurant operations with AI-driven challenges and earn points!")

# 🎮 **Gamified Decision-Making**
st.header("🧠 Gamified Decision-Making Challenges")

decision_type = st.selectbox("🎯 Select Challenge Type", [
    "High Waste Reduction",
    "Low Sales Optimization",
    "Peak Hour Efficiency",
    "Inventory Management"
])

if st.button("🚀 Generate Decision Challenge"):
    prompt = f"""
    Create a gamified decision-making challenge for restaurant managers to optimize:
    - Challenge Type: {decision_type}
    - How they can earn points
    - Key performance metrics
    - AI-generated recommendations
    - Real-world application examples
    """
    st.text_area("🏆 AI-Generated Decision Challenge:", get_ai_response(prompt), height=300)

# 🔄 **AI-Generated Scenario Simulations**
st.header("🕹️ AI-Generated Scenario Simulations")

scenario_type = st.selectbox("📊 Select Simulation Type", [
    "Staff Shortages",
    "Inventory Issues",
    "Customer Service Bottlenecks",
    "Unexpected Rush Hours"
])

if st.button("🎭 Generate Scenario"):
    prompt = f"""
    Predict upcoming restaurant management bottlenecks:
    - Scenario: {scenario_type}
    - Provide a virtual case study
    - How managers can solve it
    - AI-driven solutions and strategies
    """
    st.text_area("🔮 AI-Generated Scenario:", get_ai_response(prompt), height=300)

# 🌍 **AI-Driven Sustainability Challenges**
st.header("♻️ AI-Driven Sustainability Challenges")

eco_focus = st.selectbox("🌱 Select Sustainability Goal", [
    "Waste Reduction",
    "Energy Efficiency",
    "Eco-Friendly Packaging",
    "Sustainable Sourcing"
])

if st.button("💚 Generate Sustainability Challenge"):
    prompt = f"""
    Set a sustainability challenge for restaurant managers:
    - Goal: {eco_focus}
    - How they can track progress
    - AI-powered insights for improvement
    - Reward system for eco-friendly actions
    """
    st.text_area("🌿 AI-Generated Sustainability Challenge:", get_ai_response(prompt), height=300)

# ⏳ **Dynamic AI Adjustments for Peak Hours**
st.header("📊 Dynamic AI Adjustments for Peak Hours")

time_period = st.selectbox("🕰️ Select Time Period", [
    "Morning Rush",
    "Lunch Peak",
    "Evening Dinner Time",
    "Late-Night Orders"
])

if st.button("📈 Generate AI-Powered Adjustments"):
    prompt = f"""
    Analyze peak-hour restaurant trends and suggest AI-driven strategies:
    - Time Period: {time_period}
    - Workload balancing techniques
    - Customer service optimization
    - Staff scheduling recommendations
    - AI-based demand prediction
    """
    st.text_area("⚡ AI-Generated Peak Hour Strategy:", get_ai_response(prompt), height=300)

# ✅ Footer
st.write("🎖️ Earn points for making data-driven decisions and optimizing restaurant operations!")
st.write("🚀 Powered by Gemini 1.5 Pro with GenAI")


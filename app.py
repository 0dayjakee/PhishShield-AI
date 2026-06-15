import streamlit as st
import json
from google import genai

st.set_page_config(page_title="PhishShield AI - Cyber Defender", page_icon="🛡️", layout="wide")
st.title("🛡️ PhishShield AI: Real-Time Threat Responder")
st.write("AI threats strike in minutes. We respond in seconds. Paste suspicious content below to analyze.")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    st.markdown("[Get a free API Key here](https://aistudio.google.com/)")

suspicious_text = st.text_area("Paste the suspicious Email, Chat Log, or Message Content here:", height=200)

if st.button("⚡ Analyze & Defend", type="primary"):
    if not api_key:
        st.error("Paki-lagay muna ang API Key mo sa sidebar, tol!")
    elif not suspicious_text:
        st.warning("Maglagay ka muna ng text na i-aanalyze natin.")
    else:
        with st.spinner("Analyzing threat and preparing counter-measures..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
                You are an advanced AI Cybersecurity Incident Responder. Analyze the following text for potential social engineering or phishing threats.
                Text to analyze: "{suspicious_text}"
                Provide a JSON response with exactly these keys: "risk_score" (0-100), "threat_type", "analysis", "employee_alert", "remediation_step".
                Return ONLY raw JSON, no wrappers.
                """
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                
                clean_text = response.text.strip().replace("```json", "").replace("```", "")
                result = json.loads(clean_text)
                
                st.success("Analysis Complete!")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Threat Risk Score", value=f"{result['risk_score']}%")
                    st.info(f"**Type:** {result['threat_type']}")
                    st.write(result['analysis'])
                with col2:
                    st.warning("**Draft Employee Alert Email:**")
                    st.code(result['employee_alert'], language="text")
                    st.error("**Recommended IT Firewall Action:**")
                    st.code(result['remediation_step'], language="text")
            except Exception as e:
                st.error(f"May error, tol: {e}")

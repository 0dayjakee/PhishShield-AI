# 🛡️ PhishShield AI - Real-Time Threat Responder

> "AI threats strike in minutes. PhishShield responds in seconds."

Built for the **FIND EVIL! Hackathon 2026**, PhishShield AI is a next-generation Cybersecurity Incident Response prototype designed to neutralize AI-driven social engineering attacks before they breach the enterprise network.

## ⚡ Core Capabilities
* **Sub-Second Triage:** Ingests suspicious logs, emails, or text and scores the risk instantly (0-100%).
* **Structured Threat Parsing:** Leverages Gemini 2.5 Flash to enforce JSON policy outputs, allowing seamless orchestration with existing SIEM/SOAR platforms.
* **Automated Mitigation:** Simultaneously generates human-readable employee advisories and machine-readable IT admin firewall blocklists.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Frontend:** Streamlit
* **AI Orchestration:** Google GenAI SDK (Gemini 2.5 Flash)

* ## 🚀 Quickstart & Installation

Follow these steps to deploy and run PhishShield AI locally on a Windows host or specialized security environment.

### 1. Prerequisites
Ensure you have Python 3.11+ installed. If not, you can deploy it instantly via PowerShell using Windows Package Manager (`winget`):
```powershell

## Installation

# On Windows/PowerShell
git clone https://github.com/0dayjakee/PhishShield-AI.git
cd PhishShield-AI
pip install -r requirements.txt
$env:GOOGLE_API_KEY="your_api_key_here"
streamlit run app.py

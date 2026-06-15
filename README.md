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

* ## 🚀 Quickstart & Installation

Follow these steps to deploy and run PhishShield AI locally on a Windows host or specialized security environment.

### 1. Prerequisites
Ensure you have Python 3.11+ installed. If not, you can deploy it instantly via PowerShell using Windows Package Manager (`winget`):
```powershell

## Installation & Setup

```bash
# Clone the repository
git clone [https://github.com/0dayjakee/PhishShield-AI.git](https://github.com/0dayjakee/PhishShield-AI.git)
cd PhishShield-AI

# Install dependencies
pip install -r requirements.txt

# Run the platform
streamlit run app.py

🛠️ Troubleshooting & Known Errors
If you run into environment path restrictions or missing system binaries during deployment, execute the quick-fixes below.

1. Error: 'git' is not recognized as the name of a cmdlet...
Cause: The host machine does not have a Git client installed globally in its environment variables.

Solution (PowerShell Windows Package Manager):

--> winget install --id Git.Git --exact --silent --accept-package-agreements --accept-source-agreements
  # NOTE: Restart your PowerShell window after running this to refresh the system PATH.

2. Error: 'pip' is not recognized as the name of a cmdlet...
Cause: Python is installed, but its application binaries scripts folder (\Scripts) is missing from the global Environment Variables.

Solution (Explicit Local Fallback): Force execution by using the direct internal Windows path structure:

--> & "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install -r requirements.txt

3. Error: 'streamlit' is not recognized...
Cause: Similar to the pip error, the newly installed Streamlit web runner package is outside the active environment terminal lookups.

Solution (Explicit Global Execution): Bypass the global shell search by explicitly declaring the static path to target the Uvicorn server directly:

--> & "C:\Users\ADMIN\AppData\Local\Programs\Python\Python311\Scripts\streamlit.exe" run app.py



Final Clean Installation:
-------------------------------------------------------------------------------------------------------------------------
git clone https://github.com/0dayjakee/PhishShield-AI.git
cd PhishShield-AI
& "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\Scripts\pip.exe" install -r requirements.txt
& "C:\Users\ADMIN\AppData\Local\Programs\Python\Python311\Scripts\streamlit.exe" run app.py


Happy Find!



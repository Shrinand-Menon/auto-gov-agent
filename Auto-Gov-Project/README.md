# Auto-Gov: ISO 42001 & DPDP Act Compliance Guardrail

> **A "Shadow AI" defense agent that intercepts, scans, and redacts Indian PII (Aadhaar, PAN) from LLM prompts in real-time.**

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Compliance](https://img.shields.io/badge/Compliance-ISO%2042001-blue)
![Regulation](https://img.shields.io/badge/Regulation-DPDP%20Act%202023-green)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

---

## 🚨 The Problem: Shadow AI Risks
In the rush to adopt Generative AI, employees and students frequently paste sensitive data (PII, API Keys, proprietary code) into public LLMs like ChatGPT and Gemini.

* **Legal Risk:** Violation of **Section 8 (Duties of Data Fiduciary)** of the **Digital Personal Data Protection (DPDP) Act, 2023**.
* **Financial Impact:** Potential penalties up to **₹250 Crore** for failure to safeguard personal data.
* **Compliance Gap:** Fails **ISO 42001 Control A.7.4 (Data Governance)** regarding data quality and privacy.

## 🛡️ The Solution
**Auto-Gov** is a Python-based middleware agent that acts as a firewall between the user and the Model API. It enforces **Data Minimization** by detecting and sanitizing specific Indian identifiers before they leave the secure network.

### Key Features
* **🇮🇳 Indian PII Recognition:** Custom Regex engines to detect:
    * **Aadhaar Numbers** (UIDAI format)
    * **PAN Cards** (Income Tax format)
    * **Indian Mobile Numbers** (+91 / 6-9 start digit)
* **🔑 Credential Scrubbing:** Auto-detects and blocks hardcoded secrets (AWS Keys `AKIA...`, OpenAI Keys `sk-...`).
* **📝 Audit Logging:** Generates a GRC-ready CSV log (`Audit_Results_Final.csv`) classifying every blocked attempt for compliance review.

---

## 📂 Repository Structure

```text
auto-gov-agent/
│
├── data/
│   ├── audit_dataset_master.csv   # Input: 50 Simulated Prompts (The "Red Team" Data)
│   └── audit_results_final.csv    # Output: The Sanitized Logs (The "Green" Results)
│
├── docs/
│   └── Shrinand_Menon_AI_Compliance_Report.pdf  # Full Case Study & Risk Assessment
│
├── src/
│   ├── __init__.py
│   └── agent.py                   # Core Logic (Regex Engine + Processing)
│
├── requirements.txt               # Dependencies (pandas, openpyxl)
└── README.md                      # Project Documentation
````

-----

## 🚀 Quick Start

### 1\. Clone the Repository

```bash
git clone [https://github.com/yourusername/auto-gov-agent.git](https://github.com/yourusername/auto-gov-agent.git)
cd auto-gov-agent
```

### 2\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3\. Run the Audit Simulation

Run the agent against the test dataset to verify the guardrails:

```bash
python src/agent.py
```

*The script will process the raw prompts in `data/` and generate a compliance report.*

-----

## 📊 Performance Metrics

Tested against a dataset of **50 simulated prompts** (academic & corporate scenarios):

| Metric | Result |
| :--- | :--- |
| **PII Detection Rate** | **100%** (Aadhaar, PAN, Phone) |
| **Credential Leak Block Rate** | **100%** (API Keys) |
| **Processing Latency** | \<15ms per prompt |
| **Compliance Status** | **Aligned with ISO 42001 & DPDP Act** |

-----

## ⚖️ Legal & Compliance Mapping

| Feature | DPDP Act 2023 | ISO/IEC 42001 |
| :--- | :--- | :--- |
| **PII Redaction** | **Section 8:** Security Safeguards | **A.7.4:** Data Governance |
| **Audit Logging** | **Section 9:** Data Breach Notification Support | **A.4.2:** Risk Treatment |
| **Secret Detection** | **Schedule 1:** Prevention of Breach | **A.5.15:** Access Control |

-----

## 📄 Case Study

This project includes a comprehensive **4-Page Compliance Report** detailing the risk assessment methodology and architectural controls.
👉 **[Download the PDF Report](https://www.google.com/search?q=./docs/Shrinand_Menon_AI_Compliance_Report.pdf)**

-----

## 👤 Author

**Shrinand S Menon**
*Computer Science & Business Systems Candidate*

  * **Focus:** AI Governance, Technical GRC, ISO 42001
  * **LinkedIn:** [Your LinkedIn Profile Link]
  * **Portfolio:** [Your Portfolio Link]

-----

*Disclaimer: This tool is a technical prototype designed for educational and compliance simulation purposes. It does not constitute legal advice.*

```
```

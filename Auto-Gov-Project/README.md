# Auto-Gov: ISO 42001 Compliance Guardrail

> **A "Shadow AI" defense agent that intercepts, scans, and redacts Indian PII (Aadhaar, PAN) from LLM prompts in real-time.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Compliance: ISO 42001](https://img.shields.io/badge/Compliance-ISO%2042001-blue)](https://www.iso.org/standard/81230.html)
[![Regulation: DPDP Act](https://img.shields.io/badge/Regulation-DPDP%20Act%202023-green)](https://www.meity.gov.in/)

## 🚨 The Problem: Shadow AI
Employees and students frequently paste sensitive data (PII, API Keys) into public LLMs like ChatGPT.
- **Risk:** Violation of **DPDP Act 2023 Section 8**.
- **Penalty:** Up to ₹250 Cr for data breaches.
- **Standard:** Violates **ISO 42001 Control A.7.4 (Data Governance)**.

## 🛡️ The Solution
**Auto-Gov** is a Python-based middleware that acts as a firewall between the user and the Model API.

### Key Features
- **🇮🇳 Indian PII Recognition:** Custom Regex for **Aadhaar**, **PAN Card**, and **+91 Mobile Numbers**.
- **🔑 Credential Scrubbing:** Auto-detects AWS Keys (`AKIA...`) and OpenAI Secrets (`sk-...`).
- **📝 Audit Logging:** Generates a GRC-ready CSV log of every blocked attempt.

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone [https://github.com/yourusername/auto-gov-agent.git](https://github.com/yourusername/auto-gov-agent.git)


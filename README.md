# 🛡️ AI-Powered Automated Log Security Analyzer

This repository contains a light-weight, high-performance Python automated script designed to simulate core **SIEM (Security Information and Event Management)** functionalities by parsing web server logs and detecting anomalies or active cyber attack vectors.

## 🚀 Features
- **Brute Force Detection:** Identifies repeated unauthorized authentication attempts.
- **SQL Injection (SQLi) Identification:** Scans query strings for destructive SQL payloads (UNION SELECT, OR 1=1).
- **Reconnaissance Tracking:** Detects active network mapping and port scanning (Nmap signatures).
- **Automated Reporting:** Generates a modern, interactive HTML Dashboard (Dark Mode) for SOC analysts.

## 📂 Project Structure
- `log_analyzer.py` -> Core Python parsing logic.
- `server_logs.txt` -> Sample raw server logs containing hidden malicious activities.
- `security_report.html` -> The generated executive threat report.

## 🛠️ How to Run
1. Clone the repository: `git clone https://github.com/berkantuyluogluuu/AI-Log-Security-Analyzer.git`
2. Navigate to the project directory and run the analyzer: `python log_analyzer.py`
3. Open `security_report.html` in any browser to inspect the visual incident reports.

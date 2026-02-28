# 📈 Automated Intraday Market Data Pipeline (ETL)

## 📌 Overview
This project is an automated, end-to-end Data Engineering pipeline built in Python. It is designed to autonomously extract live stock market data, transform the data with precise timestamps, and load it into a local CSV database for real-time session analysis. 

This project demonstrates core **ETL (Extract, Transform, Load)** principles and serves as a foundational architecture for algorithmic trading bots and future GenAI data integrations.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.14
* **Libraries:** `yfinance`, `csv`, `datetime`, `time`
* **Architecture:** ETL Data Pipeline
* **Target Data:** Indian Stock Market (NSE/BSE) via Yahoo Finance API

## 🚀 Core Features
1. **Autonomous Data Extraction:** Utilizes a `while` loop and API integration to fetch live market prices at programmed intervals without manual intervention.
2. **Data Transformation:** Standardizes raw API data and merges it with local system timestamps for accurate time-series tracking.
3. **Enterprise Database Integration:** Upgraded from local CSV storage to a robust **PostgreSQL** relational database for secure, scalable time-series data storage.
4. **Secure Credential Management:** Implemented `python-dotenv` to securely manage database passwords and API keys outside of the source code.

## ⚙️ How to Run the Pipeline
**1. Install Dependencies**
Ensure Python is installed, then install the required Yahoo Finance library:
`pip install yfinance`

**2. Start the Bot**
Run the data extraction script to begin building your database:
`python intraday_bot.py`
*(The bot will fetch and log the target stock price every 60 seconds. Press `Ctrl+C` in the terminal to stop).*

**3. Analyze the Data**
Once you have collected data, run the analysis script to generate a session summary:
`python analyze_data.py`

## 🔮 Future Scope
* Integrate **PostgreSQL** to replace the local CSV database for enterprise-grade data storage.
* Implement **Retrieval-Augmented Generation (RAG)** using local LLMs to provide automated, AI-driven summaries of the market session.
* Build a full-stack **React.js / Node.js** dashboard to visualize the real-time data flow.

---
*Author: Yashvardhan* | *Focus: Data Engineering & AI Infrastructure*
# 📈 AI-Powered Intraday Data Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?logo=postgresql)
![React](https://img.shields.io/badge/React-Vite-61DAFB?logo=react)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Render](https://img.shields.io/badge/Render-Deployed-000000?logo=render)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-000000?logo=vercel)

## 🚀 Overview
An end-to-end, fault-tolerant ETL (Extract, Transform, Load) pipeline and real-time analytical dashboard designed to track intraday financial market data. 

This full-stack SaaS application autonomously streams live stock prices into a managed cloud database, serves the data via a production-ready REST API, and utilizes an AI-driven microservice to generate executive market summaries with built-in algorithmic fallbacks.

**🔗 Live Demo:** [Insert your Vercel Link Here]
**🔗 Production API:** [Insert your Render Link Here]/api/data

---

## 🏗️ System Architecture



1. **Extraction Node:** A Python worker (`intraday_bot.py`) scraping live stock metrics and streaming them to the cloud.
2. **Cloud Vault (Database):** A managed PostgreSQL instance hosted on AWS via Supabase, utilizing IPv4 connection pooling.
3. **AI Microservice:** A Docker-containerized analytics engine utilizing the Google GenAI SDK (Gemini) to evaluate market trends.
4. **Backend API:** A Flask RESTful API served by Gunicorn with CORS enabled, deployed globally on Render.
5. **Frontend Dashboard:** A responsive React.js interface visualizing time-series data using Recharts, deployed on Vercel.

---

## ✨ Key Engineering Features
* **Fault-Tolerant AI Engine:** Designed with high availability in mind. If the external LLM API drops or rate-limits, the system seamlessly boots a local algorithmic fallback to calculate standard deviation and statistical price momentum without crashing.
* **Infrastructure as Code (IaC):** Analytical microservice is fully containerized using Docker (`Dockerfile`), ensuring consistent, cross-platform execution environments.
* **Enterprise Security:** Strict credential management utilizing `.env` files and environment variables; no hardcoded API keys or database URIs.
* **CI/CD Integration:** Automated deployment pipelines linked directly to GitHub. Pushing to the `main` branch triggers zero-downtime builds on both Vercel and Render.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| **Data Engineering** | Python, `yfinance`, `psycopg2`, ETL pipelines |
| **Database** | PostgreSQL, Supabase, Connection Pooling (IPv4) |
| **Backend API** | Flask, Gunicorn, `flask-cors` |
| **Frontend** | React.js, Vite, Recharts, HTML/CSS |
| **AI / ML** | Google GenAI SDK (Gemini 1.5) |
| **DevOps & Cloud** | Docker, Render, Vercel, Git/GitHub |

---

## 💻 Local Setup & Installation

If you wish to run this pipeline on your local machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/kakashi-yash/](https://github.com/kakashi-yash/)AI.git
cd [AI]
# 📊 Market Data Visualizer (React + Vite)

## 📌 Overview
This is the frontend user interface for my automated Intraday Market Data Pipeline. Built with React and Vite, this dashboard connects to a custom Python/Flask backend to fetch and visualize live stock market data in real-time.

## 🛠️ Tech Stack
* **Framework:** React.js (Vite)
* **Data Visualization:** Recharts
* **Backend Integration:** REST API (Python/Flask)
* **State Management:** React Hooks (`useState`, `useEffect`)

## 🚀 Core Features
* **Real-Time Data Polling:** Automatically fetches new market ticks from the local Python API every 60 seconds using an optimized `setInterval` loop.
* **Dynamic Charting:** Utilizes `Recharts` to render a responsive, dark-mode financial line chart with interactive tooltips.
* **Memory Management:** Implements strict React cleanup functions to prevent browser memory leaks during continuous API polling.

## ⚙️ How to Run Locally
1. Ensure the Python Data Pipeline and Flask API are running on `localhost:5000`.
2. Install frontend dependencies: `npm install`
3. Start the development server: `npm run dev`
4. Open `http://localhost:5173` in your browser.

---
*Focus: Full-Stack Integration & Frontend Data Visualization*

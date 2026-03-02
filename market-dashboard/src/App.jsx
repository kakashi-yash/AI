import { useState, useEffect } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import './App.css'

// 1. THE SAFETY NET: Realistic mock intraday data for portfolio display
const mockPortfolioData = [
  { time: "09:15", ticker: "RELIANCE.NS", price: 2980.50 },
  { time: "10:00", ticker: "RELIANCE.NS", price: 2995.20 },
  { time: "11:00", ticker: "RELIANCE.NS", price: 2985.00 },
  { time: "12:00", ticker: "RELIANCE.NS", price: 3010.80 },
  { time: "13:00", ticker: "RELIANCE.NS", price: 3005.40 },
  { time: "14:00", ticker: "RELIANCE.NS", price: 3025.10 },
  { time: "15:15", ticker: "RELIANCE.NS", price: 3030.00 }
];

function App() {
  const [marketData, setMarketData] = useState([])

  useEffect(() => {
    const fetchMarketData = () => {
      console.log("Attempting to fetch live data from Python API...")
      fetch("https://market-data-api-bx7e.onrender.com/api/data")
        .then(response => {
          if (!response.ok) throw new Error("Backend offline");
          return response.json();
        })
        .then(data => {
          // If the Python bot hasn't fetched anything yet, use the mock data
          if (data.length === 0) {
            setMarketData(mockPortfolioData);
          } else {
            setMarketData(data);
          }
        })
        .catch(error => {
          // 2. THE CATCH: If the fetch fails (like when hosted on Vercel), load the safety net!
          console.log("Local API offline. Loading Mock Portfolio Data.");
          setMarketData(mockPortfolioData);
        })
    }

    fetchMarketData()
    const intervalId = setInterval(fetchMarketData, 60000)
    return () => clearInterval(intervalId)
  }, [])

  return (
    <div style={{ width: '80vw', height: '80vh', padding: '20px' }}>
      <h2 style={{ color: '#646cff' }}>📈 Live Market Data Pipeline</h2>
      
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={marketData}>
          <CartesianGrid strokeDasharray="3 3" opacity={0.2} />
          <XAxis dataKey="time" stroke="#ccc" />
          <YAxis domain={['auto', 'auto']} stroke="#ccc" />
          <Tooltip contentStyle={{ backgroundColor: '#1a1a1a', borderRadius: '8px', border: 'none' }} />
          <Line 
            type="monotone" 
            dataKey="price" 
            stroke="#00ff88" 
            strokeWidth={3} 
            dot={{ r: 4 }} 
            activeDot={{ r: 8 }} 
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}

export default App
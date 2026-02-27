import { useState, useEffect } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import './App.css'

function App() {
  // 1. Set up the digital bucket to hold our API data
  const [marketData, setMarketData] = useState([])

// 2. Fetch the data automatically every 60 seconds
  useEffect(() => {
    // We wrap the fetch in a function so we can call it repeatedly
    const fetchMarketData = () => {
      console.log("Fetching live data from Python API...")
      fetch('http://127.0.0.1:5000/api/data')
        .then(response => response.json())
        .then(data => setMarketData(data))
        .catch(error => console.error("Error fetching data:", error))
    }

    // Call it immediately when the page first loads
    fetchMarketData()

    // Set up the timer to call it again every 60,000 milliseconds (60 seconds)
    const intervalId = setInterval(fetchMarketData, 60000)

    // CRITICAL REACT STEP: Clean up the timer if the user leaves the page
    // This stops the browser from crashing due to memory leaks!
    return () => clearInterval(intervalId)
  }, [])

  // 3. Draw the User Interface
  return (
    <div style={{ width: '80vw', height: '80vh', padding: '20px' }}>
      <h2 style={{ color: '#646cff' }}>📈 Live Market Data Pipeline</h2>
      
      {/* 4. Draw the Chart */}
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={marketData}>
          <CartesianGrid strokeDasharray="3 3" opacity={0.2} />
          <XAxis dataKey="time" stroke="#ccc" />
          {/* domain={['auto', 'auto']} zooms the chart in on the price changes */}
          <YAxis domain={['auto', 'auto']} stroke="#ccc" />
          <Tooltip contentStyle={{ backgroundColor: '#1a1a1a', borderRadius: '8px' }} />
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

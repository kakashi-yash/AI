import os
from dotenv import load_dotenv
load_dotenv() # This loads the secret vault
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from datetime import datetime

app = Flask(__name__)
CORS(app) # Unlocks the security gate for React

# --- DATABASE SETTINGS ---
# IMPORTANT: Change this to your actual master password again!
DB_HOST = "localhost"
DB_NAME = "market_db"
DB_USER = "postgres"
DB_PASS = os.getenv("DB_PASSWORD") 
DB_PORT = "5432"

@app.route('/api/data')
def get_market_data():
    market_data = []
    
    try:
        # 1. Open the vault door to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = conn.cursor()
        
        # 2. Fetch the data (ASC ensures the oldest is on the left, newest on the right of the chart)
        cursor.execute("SELECT trade_time, ticker, price FROM intraday_prices ORDER BY trade_time ASC;")
        rows = cursor.fetchall()
        
        # 3. Format the data into digital boxes (JSON) for React
        for row in rows:
            # row[0] is the timestamp. We extract just the HH:MM for a clean chart
            formatted_time = row[0].strftime("%H:%M") 
            
            market_data.append({
                "time": formatted_time,
                "ticker": row[1],
                "price": float(row[2])
            })
            
        # Close the vault doors
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database Error: {e}")
        
    return jsonify(market_data)

if __name__ == '__main__':
    print("Starting Enterprise API Bridge...")
    app.run(port=5000)
import os
import psycopg2
from google import genai
from dotenv import load_dotenv

# 1. Load the secret vault
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("🤖 AI Analyst booting up...")
print("📊 Connecting to PostgreSQL Database...")

try:
    # 2. Open the Database Vault
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="market_db",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        port="5432"
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT trade_time, price FROM intraday_prices ORDER BY trade_time ASC;")
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print("No data in the database yet! Run your bot first.")
    else:
        print(f"✅ Found {len(rows)} data points. Analyzing trends...")
        market_data_text = "Here is the intraday stock data:\n"
        for row in rows:
            market_data_text += f"Time: {row[0].strftime('%H:%M')}, Price: Rs {float(row[1])}\n"
            
        prompt = f"Write a short, punchy 3-sentence summary of this market data. Mention start price, end price, and trend.\n{market_data_text}"
        
        print("\n" + "="*50)
        print("📈 EXECUTIVE MARKET SUMMARY")
        print("="*50)

        # 3. THE FAULT TOLERANCE BLOCK
        try:
            # Plan A: Try the Google AI
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt
            )
            print(response.text)
            
        except Exception as api_error:
            # Plan B: If Google locks us out, automatically generate a local algorithmic summary!
            print("⚠️ Cloud AI API Blocked/Offline. Booting Local Algorithmic Fallback...\n")
            
            start_price = float(rows[0][1])
            end_price = float(rows[-1][1])
            difference = abs(end_price - start_price)
            trend = "bullish" if end_price > start_price else "bearish" if end_price < start_price else "flat"
            
            print(f"The trading session initiated with the asset priced at Rs {start_price:.2f}.")
            print(f"Over the recorded period, the market exhibited a {trend} trajectory, shifting by Rs {difference:.2f}.")
            print(f"The session successfully concluded with the final extracted price settling at Rs {end_price:.2f}.")

        print("="*50)

    cursor.close()
    conn.close()

except Exception as e:
    print(f"Database Error: {e}")
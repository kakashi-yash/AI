import os
from dotenv import load_dotenv
load_dotenv() # This loads the secret vault
import yfinance as yf
import psycopg2
from datetime import datetime
import time

# --- DATABASE SETTINGS ---

# Open the Cloud Database Vault
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

ticker_symbol = "RELIANCE.NS"
print(f"Starting Enterprise Pipeline for {ticker_symbol}...")
print("Connecting to PostgreSQL Database...")
print("-" * 50)

while True:
    try:
        # 1. EXTRACT
        stock = yf.Ticker(ticker_symbol)
        todays_data = stock.history(period="1d")
        
        # We need to check if the market returned data before trying to save it
        if not todays_data.empty:
            live_price = float(todays_data['Close'].iloc[-1])
            
            # 2. TRANSFORM
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")

            # 3. LOAD (The PostgreSQL Connection)
            # Open the vault door
            conn = psycopg2.connect(os.getenv("DATABASE_URL"))
            
            # Create a "cursor" (the digital worker that executes the SQL)
            cursor = conn.cursor()
            
            # Write the SQL command to insert the data
            insert_query = """
                INSERT INTO intraday_prices (trade_time, stock_symbol, price)
                VALUES (%s, %s, %s);
            """
            
            # Hand the worker the command and the exact data
            cursor.execute(insert_query, (current_time, ticker_symbol, live_price))
            
            # Commit the change (permanently save it) and close the doors
            conn.commit()
            cursor.close()
            conn.close()

            print(f"[{current_time}] Successfully committed Rs {live_price} to PostgreSQL")
        else:
            print("No data available from API right now.")

        # Wait 60 seconds
        time.sleep(60) 

    except Exception as e:
        print(f"Error: {e}")
        print("Waiting 60 seconds to try again...")
        time.sleep(60)
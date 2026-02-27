import yfinance as yf
import csv
from datetime import datetime
import time # The new tool that lets us pause the code

ticker_symbol = "RELIANCE.NS"
print(f"Starting automated market data pipeline for {ticker_symbol}...")
print("IMPORTANT: Click inside the terminal and press Ctrl+C to stop the bot!")
print("-" * 50)

# The Infinite Loop (The green light is always on)
while True:
    try:
        # 1. EXTRACT
        stock = yf.Ticker(ticker_symbol)
        todays_data = stock.history(period="1d")
        live_price = round(todays_data['Close'].iloc[-1], 2)

        # 2. TRANSFORM
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # 3. LOAD
        with open("market_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([current_time, ticker_symbol, live_price])

        print(f"[{current_time}] Successfully logged Rs {live_price}")

        # 4. THE PIT STOP: Wait for 60 seconds before checking again
        time.sleep(60) 

    except Exception as e:
        # If your Wi-Fi drops, this stops the program from crashing
        print(f"Connection error. Waiting 60 seconds to try again...")
        time.sleep(60) 
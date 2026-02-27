import yfinance as yf

# 1. Choose the stock ticker (Reliance on the National Stock Exchange)
ticker_symbol = "SBIN.NS"

print(f"Fetching live market data for {ticker_symbol}...")

# 2. Ask Yahoo Finance for the stock data
stock = yf.Ticker(ticker_symbol)

# 3. Get today's market data
todays_data = stock.history(period="1d")

# 4. Extract the most recent closing price
live_price = todays_data['Close'].iloc[-1]

# 5. Print the result!
# We use round() to keep it to 2 decimal places so it looks like real money
print(f"The current price is: Rs {round(live_price, 2)}")
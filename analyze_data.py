import csv

print("Reading market data database...")
prices = [] # This is an empty list (our digital bucket)

# 1. Open the file in "Read" mode ('r')
with open("market_data.csv", mode="r") as file:
    reader = csv.reader(file)
    
    # 2. Go through the spreadsheet row by row
    for row in reader:
        # row[0] is the Time, row[1] is the Ticker, row[2] is the Price
        # We grab the price and convert it from text into a decimal number
        current_price = float(row[2]) 
        
        # Toss the price into our bucket
        prices.append(current_price) 

# 3. Make sure the bucket isn't empty, then calculate!
if len(prices) > 0:
    highest = max(prices)
    lowest = min(prices)
    total_records = len(prices)
    
    print("-" * 30)
    print(f"Total trades recorded: {total_records}")
    print(f"Session High: Rs {highest}")
    print(f"Session Low: Rs {lowest}")
    print("-" * 30)
else:
    print("No data found! Let your bot run for a bit first.")
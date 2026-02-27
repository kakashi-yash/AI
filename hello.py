import csv

# 1. Gather the trade data
buy_price = float(input("Enter the buying price: "))
sell_price = float(input("Enter the selling price: "))
quantity = int(input("Enter the number of shares: "))

profit = (sell_price - buy_price) * quantity

# 2. Determine the outcome
if profit > 0:
    status = "Profit"
elif profit < 0:
    status = "Loss"
else:
    status = "Breakeven"

# 3. Save the data to a CSV file
print("Saving trade to database...")

with open("my_trades.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([buy_price, sell_price, quantity, profit, status])

print("Trade saved successfully!")
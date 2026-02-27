from flask import Flask, jsonify
from flask_cors import CORS
import csv

# 1. Start the API engine
app = Flask(__name__)
CORS(app) # This unlocks the security gate so React can get the data

# 2. Create the data route
@app.route('/api/data')
def get_market_data():
    market_data = []
    
    # Read the database
    try:
        with open('market_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Package each row into a neat digital box (JSON format)
                market_data.append({
                    "time": row[0].split(" ")[1], # Just grab the hour/minute
                    "ticker": row[1],
                    "price": float(row[2])
                })
    except Exception as e:
        print("Waiting for data...")
        
    return jsonify(market_data)

# 3. Run the server on Port 5000
if __name__ == '__main__':
    print("Starting Python API Bridge...")
    app.run(port=5000)
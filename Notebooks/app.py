from flask import Flask, jsonify
import pandas as pd
import numpy as np
from ruptures import Pelt

app = Flask(__name__)

# Load the cleaned data once to avoid repeated reads
data = pd.read_csv('cleaned_brent_oil_prices.csv')

@app.route('/api/change_points', methods=['GET'])
def get_change_points():
    prices = data['price'].values

    # Identify change points using PELT method
    model = "l2"
    algo = Pelt(model=model).fit(prices)
    change_points = algo.predict(pen=5)

    # Calculate 
    if len(change_points) > 1:
        change_point = change_points[1]
        average_before = np.mean(prices[:change_point])
        average_after = np.mean(prices[change_point:])
    else:
        change_point = None
        average_before = None
        average_after = None
    
    return jsonify({
        'change_point': change_point,
        'average_before': average_before,
        'average_after': average_after
    })

@app.route('/api/historical_data', methods=['GET'])
def get_historical_data():
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
   
    events = [
        {"date": "2020-01-01", "event": "Event A", "description": "Description of Event A"},
        {"date": "2020-02-01", "event": "Event B", "description": "Description of Event B"},
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
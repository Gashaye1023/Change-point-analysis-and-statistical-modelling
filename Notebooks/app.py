from flask import Flask, jsonify
import pandas as pd
import numpy as np
from ruptures import Pelt
from ruptures.costs import CostL2

app = Flask(__name__)

@app.route('/api/change_points', methods=['GET'])
def get_change_points():
    # Load the cleaned data
    data = pd.read_csv('cleaned_brent_oil_prices.csv')
    
    # Assume the dataset has a column 'price' for Brent oil prices and 'date' for dates
    prices = data['price'].values

    # Step 1: Identify change points using PELT method from ruptures library
    model = "l2"  # Cost model
    algo = Pelt(model=model).fit(prices)
    change_points = algo.predict(pen=5)  # Adjust penalty as needed

    # Step 2: Calculate averages
    if len(change_points) > 1:
        change_point = change_points[1]  # The first change point
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

if __name__ == '__main__':
    app.run(debug=True)
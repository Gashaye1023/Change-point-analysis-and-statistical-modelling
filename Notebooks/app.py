from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/change_points', methods=['GET'])
def get_change_points():
    # Load the cleaned data
    data = pd.read_csv('cleaned_brent_oil_prices.csv')
    
    # Assume the analysis has already been run and results are available
    change_point = 1500  # Placeholder for actual change point
    average_before = 0.01  # Placeholder for average before change
    average_after = 0.02  # Placeholder for average after change
    
    return jsonify({
        'change_point': change_point,
        'average_before': average_before,
        'average_after': average_after
    })

if __name__ == '__main__':
    app.run(debug=True)
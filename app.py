from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# API route for sample data
@app.route('/api/soil-data')
def soil_data():
    data_path = os.path.join('data', 'sample_data.json')
    with open(data_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
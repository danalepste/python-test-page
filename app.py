from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    # Simulating travel destination popularity over months
    destinations = ["Paris", "New York", "Tokyo", "Cape Town", "Sydney"]
    months = pd.date_range("2023-01-01", "2023-12-01", freq="MS").strftime("%B").tolist()
    
    data = {
        "months": months,
        "popularity": {
            destination: [random.randint(50, 100) for _ in months] for destination in destinations
        }
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
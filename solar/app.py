
from flask import Flask, request, jsonify

import numpy as np

import pandas as pd

import pickle

from sklearn.ensemble import RandomForestRegressor

from flask_cors import CORS



app = Flask(__name__)

CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})



# Load the trained model

with open('solar_model.pkl', 'rb') as model_file:

    regressor = pickle.load(model_file)



@app.route('/predict', methods=['POST'])

def predict():

    # Get the input data from the request

    input_data = request.get_json()



    # Convert input data to array

    input_array = np.array(input_data['input'])



    # Make prediction

    prediction = regressor.predict([input_array])[0]

    break_even = input_array[4] / prediction



    # Prepare response

    response = {

        "Annual Savings": int(prediction),

        "Break Even Point (years)": break_even

    }



    # Manually adding CORS headers for diagnostic purposes

    resp = jsonify(response)

    resp.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")

    return resp



if __name__ == '__main__':

    app.run(debug=True)


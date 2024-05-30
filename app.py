from flask import Flask, request, jsonify
import joblib
import pandas as pd
import json
import os
app = Flask(__name__)

# Load the trained model
model = joblib.load('./model/tree_model.pkl')

# Load configuration
current_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_path, 'config', 'config.json')

with open(config_path, 'r') as f:
    config = json.load(f)
dict_status = config['dict_status']


@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from request
    data = request.get_json()

    # Load input data into DataFrame
    input_df = pd.DataFrame(data)

    # Encode 'status' column
    input_df['status'] = input_df['status'].map(dict_status)

    # Predict using the model
    predictions = model.predict(input_df.drop('id', axis=1))  # Assuming 'id' is the first column

    # Prepare output DataFrame
    output_df = pd.DataFrame({
        'id': input_df['id'],
        'abw_at_harvest': predictions[:, 0],
        'adg': predictions[:, 1],
        'biomass': predictions[:, 2],
        'survival_rate': predictions[:, 3],
        'revenue': predictions[:, 4]
    })

    # Convert output DataFrame to JSON
    output_json = output_df.to_json(orient='records')

    return output_json


if __name__ == '__main__':
    app.run(debug=True)
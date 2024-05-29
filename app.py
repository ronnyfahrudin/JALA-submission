from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('./model/gbr_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = pd.DataFrame(data, index=[0])

    prediction = model.predict(features)
    output = {
        'abw_samples': prediction[0][0],
        'adg': prediction[0][1],
        'biomassa': prediction[0][2],
        'survival_rate': prediction[0][3],
        'revenue_idr': prediction[0][4]
    }
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)

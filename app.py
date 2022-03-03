import joblib
import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from model.train import train_model

app = Flask(__name__)
api = Api(app)

if not os.path.isfile('credit-card-fraud-model.model'):
    train_model()

loaded_model = joblib.load('credit-card-fraud-model.model')

class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        transaction_info = posted_data['transaction_detail']

        prediction = loaded_model.predict([transaction_info])[0]

        if prediction == 0:
            predicted_class = 'Normal Transaction'
        else:
            predicted_class = 'Fraud Transaction'

        return jsonify({
            'Prediction': predicted_class
        })

api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True)

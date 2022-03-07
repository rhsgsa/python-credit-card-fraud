import joblib
import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from model.train import train_model
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
api = Api(app)
metrics = PrometheusMetrics(app, group_by='endpoint')


if not os.path.isfile('credit-card-fraud-model.model'):
    train_model()

loaded_model = joblib.load('credit-card-fraud-model.model')

class predict(Resource):
    @staticmethod
    @metrics.counter('predict', 'Number of prediction',
         labels={'result': lambda: request.predicted_class})
    def post():
        posted_data = request.get_json()
        transaction_info = posted_data['transaction_detail']

        prediction = loaded_model.predict([transaction_info])[0]
        if prediction == 0:
            request.predicted_class = 'normal'
        else:
            request.predicted_class = 'fraud'

        return jsonify({
            'Prediction': request.predicted_class
        })

api.add_resource(predict, '/predict')


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

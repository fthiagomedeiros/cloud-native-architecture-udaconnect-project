import os

from flask import Flask, jsonify, g, request, Response
from kafka import KafkaProducer

from api.services import publish_location

app = Flask(__name__)


@app.before_request
def before_request():
    # Set up a Kafka producer
    KAFKA_URL = os.getenv("KAFKA_URL")
    producer = KafkaProducer(bootstrap_servers=KAFKA_URL)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer


@app.route('/health')
def health():
    return jsonify({'response': 'PublisherLocationService is up!'})


@app.route('/api/location', methods=['POST'])
def computers():
    if request.method == 'POST':
        request_body = request.json
        publish_location(request_body)
        return Response(status=202)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()

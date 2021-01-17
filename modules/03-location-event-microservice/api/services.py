import json
import os

from flask import g


def publish_location(location_payload):
    """
     This is a method of publishing a location to kafka.
     """

    TOPIC_NAME = os.getenv("KAFKA_TOPIC")

    # TODO: send the data using kafka_producer using .send()
    kafka_data = json.dumps(location_payload).encode()
    kafka_producer = g.kafka_producer
    kafka_producer.send(TOPIC_NAME, kafka_data)

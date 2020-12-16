import json
import os
import logging

from kafka import KafkaConsumer

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

print('KAFKA URL ' + KAFKA_URL)
print('started listening topic ' + KAFKA_TOPIC)

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_URL)


def save_in_db(_location):
    print('processing print location ', _location)
    logging.info('processing log location ', _location)


for location in consumer:
    message = location.value.decode('utf-8')
    # print('{}'.format(message))
    location_message = json.loads(message)
    save_in_db(location_message)

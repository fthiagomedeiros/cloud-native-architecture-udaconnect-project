import json
import os
from concurrent import futures
from kafka import KafkaProducer

import grpc

import coordinates_event_pb2
import coordinates_event_pb2_grpc

kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]
producer = KafkaProducer(bootstrap_servers=kafka_url)


class CoordinatesEventServicer(coordinates_event_pb2_grpc.ItemServiceServicer):

    def Create(self, request, context):

        request_value = {
            'userId': int(request.userId),
            'latitude': int(request.latitude),
            'longitude': int(request.longitude)
        }
        user_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(kafka_topic, user_encode_data)
        return coordinates_event_pb2.EventCoordinatesMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
coordinates_event_pb2_grpc.add_ItemServiceServicer_to_server(CoordinatesEventServicer(), server)

print('server starting... on port 5005')
server.add_insecure_port('[::]:5005')
server.start()
server.wait_for_termination()
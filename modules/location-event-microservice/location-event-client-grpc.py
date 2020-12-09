import grpc

import coordinates_event_pb2
import coordinates_event_pb2_grpc

"""
Simulates user mobiles sending coordinates to gRPC
"""

print("Coordinates sent...")

channel = grpc.insecure_channel("localhost:5005")
stub = coordinates_event_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
user_coordinates = coordinates_event_pb2.EventCoordinatesMessage(
    userId=1920,
    latitude=1000,
    longitude=1001
)

response = stub.Create(user_coordinates)

print(user_coordinates)
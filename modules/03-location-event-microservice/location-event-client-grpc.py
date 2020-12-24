import grpc

import coordinates_event_pb2
import coordinates_event_pb2_grpc

"""
Simulates user mobiles sending coordinates to gRPC
"""

print("Coordinates sent...")

channel = grpc.insecure_channel("127.0.0.1:30003")
stub = coordinates_event_pb2_grpc.ItemServiceStub(channel)

for i in range(1):
    # Update this with desired payload
    user_coordinates = coordinates_event_pb2.EventCoordinatesMessage(
        userId=200,
        latitude=-100,
        longitude=30
    )

    response = stub.Create(user_coordinates)

    print(user_coordinates)

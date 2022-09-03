# zeromq server to stream keypoints
import cv2
import zmq
import json
import base64
import numpy as np


context = zmq.Context()
stream_socket = context.socket(zmq.PUB)
stream_socket.connect("tcp://localhost:6666")

print("Starting server at tcp://localhost:6666, make sure you\'re listening to it.")
camera = cv2.VideoCapture(0)  # init the camera
frame_count = 0

while True:
    try:
        success, frame = camera.read()
        if success:
            frame_count += 1
            encoded, buffer = cv2.imencode(".jpg", frame)
            stream_socket.send_string(base64.b64encode(buffer).decode("UTF-8"))

    except KeyboardInterrupt:
        stream_socket.send_json(json.dumps({"message": "quit"}))
        camera.release()
        cv2.destroyAllWindows()
        break

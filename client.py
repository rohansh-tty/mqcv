# dummy zeromq client
import zmq
import numpy as np
import base64
import cv2

ctx = zmq.Context()
rcv_sock = ctx.socket(zmq.SUB)
rcv_sock.bind("tcp://*:6666")
rcv_sock.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    try:
        frame = rcv_sock.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("image", source)
        cv2.waitKey(0)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        print("closing zeromq client...")
        break

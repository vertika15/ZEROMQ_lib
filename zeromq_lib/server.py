import zmq
import time

class ZMQPublisher:
    def __init__(self, host="127.0.0.1", port=6001):
        self.host = host
        self.port = port

        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)          # PUB socket
        self.socket.bind(f"tcp://{self.host}:{self.port}")

        print(f"[PUBLISHER] Running at tcp://{self.host}:{self.port}")

    def publish(self, message):
        print(f"[PUBLISHER] Sending: {message}")
        self.socket.send_string(message)
        time.sleep(0.1)  # prevents message drop

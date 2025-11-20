import zmq

class ZMQClient:
    def __init__(self, host="127.0.0.1", port=6000):
        self.host = host
        self.port = port

        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{self.host}:{self.port}")

        print(f"Client connected to tcp://{self.host}:{self.port}")

    def send(self, message):
        print(f"[CLIENT] Sending: {message}")
        self.socket.send_string(message)

        reply = self.socket.recv_string()
        print(f"[CLIENT] Received: {reply}")

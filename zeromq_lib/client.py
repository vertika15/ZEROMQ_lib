import zmq

class ZMQSubscriber:
    def __init__(self, host="127.0.0.1", port=6001, topic=""):
        self.host = host
        self.port = port

        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)          # SUB socket
        self.socket.connect(f"tcp://{self.host}:{self.port}")
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topic)  # subscribe to a topic filter

        print(f"[SUBSCRIBER] Connected to tcp://{self.host}:{self.port}  Topic: '{topic}'")

    def listen(self):
        while True:
            message = self.socket.recv_string()
            print(f"[SUBSCRIBER] Received: {message}")

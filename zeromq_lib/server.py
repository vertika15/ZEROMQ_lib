import zmq

class ZMQServer:
    def __init__(self, host="127.0.0.1", port=6000):
        self.host = host
        self.port = port

        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind(f"tcp://{self.host}:{self.port}")

        print(f"Server started at tcp://{self.host}:{self.port}")

    def start(self):
        while True:
            message = self.socket.recv_string()
            print(f"[SERVER] Received: {message}")

            reply = f"Echo: {message}"
            self.socket.send_string(reply)

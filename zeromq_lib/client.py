import zmq
import time

class ZMQSubscriber:
    def __init__(self, host="127.0.0.1", port=6001, topic=""):
        self.host = host
        self.port = port
        self.topic = topic
        self.running = True

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self._connect_socket()

    #checking the connection-
    def _connect_socket(self):
        try:
            self.socket.connect(f"tcp://{self.host}:{self.port}")
            self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)
            print(f"[SUBSCRIBER] Connected to tcp://{self.host}:{self.port} Topic='{self.topic}'")
        except Exception as e:
            print("[SUBSCRIBER] Connect error:", e)
            print("[SUBSCRIBER] Retrying in 2 seconds...")
            time.sleep(2)
            self._connect_socket()    # retry connect

    # alive()-
    def is_alive(self):
        return self.running

    #recieving heartbeat
    def listen(self):
        while self.running:
            #preventing from subscriber freezing (can be a deadlock)
            try:
                message = self.socket.recv_string(flags=zmq.NOBLOCK)
                if message != "HEARTBEAT":
                    print(f"[SUBSCRIBER] Received: {message}")
            except zmq.Again:
                # No message yet,avoid blocking
                time.sleep(0.1)
            except Exception as e:
                print("[SUBSCRIBER] Error:", e)
                print("[SUBSCRIBER] Reconnecting...")
                self._connect_socket()

    #stop()
    def stop(self):
        print("[SUBSCRIBER] Stopping...")
        self.running = False
        time.sleep(0.2)
        self.socket.close()
        self.context.term()
        print("[SUBSCRIBER] Stopped.")

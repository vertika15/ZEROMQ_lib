import zmq
import time
import threading

class ZMQPublisher:
    def __init__(self, host="127.0.0.1", port=6001, heartbeat_interval=3):
        self.host = host
        self.port = port
        self.heartbeat_interval = heartbeat_interval
        self.running = True

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)

        self._bind_socket()
        self._start_heartbeat_thread()

   #socket binding
    def _bind_socket(self):
        try:
            self.socket.bind(f"tcp://{self.host}:{self.port}")
            print(f"[PUBLISHER] Running at tcp://{self.host}:{self.port}")
            #retrying for binding or connecting
        except Exception as e:
            print("[PUBLISHER] Bind failed:", e)
            print("[PUBLISHER] Retrying in 2 seconds...")
            time.sleep(2)
            self._bind_socket()        # retry

    #alive() checking
    def is_alive(self):
        return self.running

    #check for publisher status as it its stalled or dead or running fine
    def _start_heartbeat_thread(self):
        def heartbeat():
            while self.running:
                try:
                    self.socket.send_string("HEARTBEAT")
                except Exception as e:
                    print("[PUBLISHER] Heartbeat failed:", e)
                time.sleep(self.heartbeat_interval)

        t = threading.Thread(target=heartbeat, daemon=True)
        t.start()

    #publish msgs
    def publish(self, message):
        if not self.running:
            print("[PUBLISHER] Cannot publish, stopped.")
            return

        try:
            print(f"[PUBLISHER] Sending: {message}")
            self.socket.send_string(message)
            time.sleep(0.1)
        except Exception as e:
            print("[PUBLISHER] Publish error:", e)
            print("[PUBLISHER] Attempting to reconnect...")
            self._bind_socket()

    #stop()
    def stop(self):
        print("[PUBLISHER] Stopping...")
        self.running = False
        time.sleep(0.2)
        self.socket.close()
        self.context.term()
        print("[PUBLISHER] Stopped.")

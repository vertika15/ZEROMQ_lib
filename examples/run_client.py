from zeromq_lib import ZMQClient

if __name__ == "__main__":
    client = ZMQClient()
    client.send("Hello server")

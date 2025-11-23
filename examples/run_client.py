from zeromq_lib import ZMQSubscriber

if __name__ == "__main__":
    subscriber = ZMQSubscriber(topic="")
    subscriber.listen()

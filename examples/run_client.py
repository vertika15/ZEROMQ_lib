from zeromq_lib import ZMQSubscriber

if __name__ == "__main__":
    subscriber = ZMQSubscriber(topic="")

    try:
        subscriber.listen()
    except KeyboardInterrupt:
        subscriber.stop()

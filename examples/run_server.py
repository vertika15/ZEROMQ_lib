from zeromq_lib import ZMQPublisher
import time

if __name__ == "__main__":
    publisher = ZMQPublisher()

    try:
        while True:
            publisher.publish("Hello subscribers!")
            time.sleep(1)
    except KeyboardInterrupt:
        publisher.stop()

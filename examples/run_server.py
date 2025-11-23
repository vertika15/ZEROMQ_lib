from zeromq_lib import ZMQPublisher
import time

if __name__ == "__main__":
    publisher = ZMQPublisher()

    while True:
        publisher.publish("Hello subscribers!")
        time.sleep(1)

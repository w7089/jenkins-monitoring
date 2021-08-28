import time
import random

from prometheus_client import start_http_server


def get_metrics():
    pass


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        get_metrics()
        time.sleep(random.randrange(1,10))
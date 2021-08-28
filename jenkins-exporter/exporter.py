import time
import random

from prometheus_client import start_http_server, Gauge
from api4jenkins import Jenkins

jenkins_client = Jenkins('http://jenkins:8080/', auth=('admin', 'admin'))

JENKINS_JOB_COUNT = Gauge('jenkins_jobs_count', "Number of Jenkins jobs")

def get_metrics():
    JENKINS_JOB_COUNT.set(len(list(jenkins_client.iter_jobs())))


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        get_metrics()
        time.sleep(random.randrange(1,10))
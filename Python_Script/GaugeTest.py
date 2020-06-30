from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent and requests made.

g = Gauge('test', 'testdescription')

# Decorate function with metric.
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)
    g.set(t)
    print (t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())


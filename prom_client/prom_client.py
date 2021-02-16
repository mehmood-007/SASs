from prometheus_client import start_http_server, Summary
import prometheus_client as prom
import random
import time
import psutil


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
gauge = prom.Gauge('prometheus_active_client_cpu', 'Custom gauge')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        gauge.set( psutil.cpu_percent() )
        process_request(random.random())

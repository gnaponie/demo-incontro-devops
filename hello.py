from flask import Flask, Response
from prometheus_client import generate_latest, Counter, CollectorRegistry, CONTENT_TYPE_LATEST
app = Flask(__name__)

registry = CollectorRegistry()
c = Counter('num_requests_total', 'Number of requests for the / endpoint', registry=registry)

@app.route('/')
def hello_world():
    # incrementing the counter
    c.inc()
    return 'hello, world!'

@app.route('/metrics', methods=['GET'])
def metrics():
    # CONTENT_TYPE_LATEST is only for pretty printing
    return Response(generate_latest(registry), content_type=CONTENT_TYPE_LATEST)

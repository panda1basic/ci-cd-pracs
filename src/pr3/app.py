from flask import Flask, Response
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REQUEST_COUNT = Counter('flask_app_requests_total', 'Total HTTP requests')

@app.before_request
def count_requests():
    REQUEST_COUNT.inc()

@app.route('/')
def home():
    logger.info('Home page requested')
    return 'Hello, Monitoring!'

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

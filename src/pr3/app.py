from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    'flask_app_requests_total',
    'Общее число HTTP-запросов к Flask-приложению',
    ['method', 'endpoint', 'http_status']
)

@app.before_request
def before_request():


    pass

@app.after_request
def after_request(response):
    REQUESTS.labels(
        method  = flask.request.method,
        endpoint= flask.request.path,
        http_status=response.status_code
    ).inc()
    return response

@app.route('/')
def home():
    app.logger.info('Received request on home page')
    return 'Hello, Monitoring!'

@app.route('/metrics')
def metrics():
    """
    Экспозиция всех метрик Prometheus на /metrics
    """
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

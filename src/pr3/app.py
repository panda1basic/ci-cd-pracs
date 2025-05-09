from flask import Flask, Response, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    'flask_app_requests_total',
    'Общее число HTTP-запросов к Flask-приложению',
    ['method', 'endpoint', 'http_status']
)

@app.after_request
def after_request(response):
    REQUESTS.labels(
        method=request.method,
        endpoint=request.path,
        http_status=response.status_code
    ).inc()
    return response

@app.route('/')
def home():
    return 'Hello, Monitoring!'

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

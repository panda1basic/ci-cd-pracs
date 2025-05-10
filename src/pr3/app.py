from flask import Flask, Response, request, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

REQ = Counter(
    "flask_app_requests_total",
    "HTTP-запросы к Flask-приложению",
    ["method", "endpoint", "http_status"],
)

@app.after_request
def after(resp):
    REQ.labels(request.method, request.path, resp.status_code).inc()
    return resp

@app.route("/")
def home():
    return "Hello, Monitoring!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
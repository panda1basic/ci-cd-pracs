from flask import Flask, request, jsonify
import requests, os

AUTH_URL = os.environ.get('AUTH_URL', 'http://auth_service:5001')

app = Flask(__name__)
orders = []

@app.route('/create_order', methods=['POST'])
def create_order():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message':'Unauthorized'}), 403

    auth_response = requests.get(f'{AUTH_URL}/health')
    if auth_response.status_code != 200:
        return jsonify({'message':'Auth service unavailable'}), 503

    data = request.json or {}
    order_id = len(orders) + 1
    orders.append({'order_id': order_id, 'item': data.get('item')})
    return jsonify({'message':'Order created','order_id':order_id}), 201

@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

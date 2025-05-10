from flask import Flask, request, jsonify

app = Flask(__name__)
users = {'user1': 'password123', 'user2': 'securepass'}

@app.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    if users.get(data.get('username')) == data.get('password'):
        return jsonify({'message':'Login successful','token':'fake-jwt-token'})
    return jsonify({'message':'Invalid credentials'}), 401

@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

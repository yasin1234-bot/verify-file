from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/verify', methods=['POST'])
def verify_license():
    data = request.get_json() or {}
    client_key = data.get("key")
    
    # আপনার পাসওয়ার্ড
    server_password = os.environ.get("ZIP_PASSWORD", "YASIN x TCP BOT OB55")
    
    if client_key == server_password:
        return jsonify({"status": "success", "message": "Access granted!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid password!"}), 401

@app.route('/', methods=['GET'])
def home():
    return "API Server is running successfully!", 200

if __name__ == '__main__':
    app.run(debug=True)

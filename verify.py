from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# একসাথে সর্বোচ্চ কত সাইজের ডেটা রিকোয়েস্ট আসবে তার লিমিট (যেমন: ২০ মেগাবাইট)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024 

@app.route('/api/verify', methods=['POST'])
def verify_license():
    try:
        # রিকোয়েস্ট থেকে জেসন ডাটা রিড করা
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({"status": "error", "message": "Invalid JSON or empty request!"}), 400
            
        client_key = data.get("key")
        server_password = os.environ.get("ZIP_PASSWORD", "YASIN x TCP BOT OB55")
        
        if client_key == server_password:
            return jsonify({"status": "success", "message": "Access granted!"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid password!"}), 401
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "API Server is active and running!", 200

if __name__ == '__main__':
    # একসাথে মাল্টিপল রিকোয়েস্ট হ্যান্ডেল করার জন্য threaded=True এবং পোর্চ সেটআপ
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

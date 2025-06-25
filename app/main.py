from flask import Flask, jsonify
import os
app = Flask(__name__)
App_Version = os.environ.get("App_Version", "0.1.0")
@app.route('/version', methods=['GET'])
def get_vresion():
    return jsonify(version=App_Version)
@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify(status="healthy", message="API is running")
@app.route('/metrics', methods=['GET'])
def get_metrics():
    return "Not implemented yet, but will serve Prometheus metrics here.", 200, {'Content-Type': 'text/plain'}
@app.route('/')
def home():
    return "Welcome to HiveBox API. Check /version, /healthz, or /metrics for more info."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




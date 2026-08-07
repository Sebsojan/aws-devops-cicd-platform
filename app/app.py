from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "AWS DevOps CI/CD Platform",
        "status": "Running",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

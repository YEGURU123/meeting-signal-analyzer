from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyse', methods=['POST'])
def analyse():
    return jsonify({
        "signals": [
            {
                "type": "objection",
                "quote": "That seems steep. We pay under $200 currently.",
                "tip": "Acknowledge budget concern"
            }
        ]
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is working"})

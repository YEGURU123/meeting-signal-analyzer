from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyse', methods=['POST'])
def analyse():
    data = request.get_json()
    transcript = data.get('transcript', '')
    
    signals = [{
        "type": "objection",
        "quote": "That seems steep. We pay under $200 currently.",
        "tip": "Acknowledge budget concerns then reframe ROI"
    }]
    
    return jsonify({"signals": signals})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

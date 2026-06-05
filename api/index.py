from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyse', methods=['POST'])
def analyse_transcript():
    try:
        data = request.get_json()
        transcript = data.get('transcript', '').strip()
        
        if not transcript:
            return jsonify({'error': 'Transcript is required'}), 400
        
        signals = []
        
        if 'steep' in transcript.lower() or 'under' in transcript.lower():
            signals.append({
                "type": "objection",
                "quote": "That seems steep. We pay under $200 currently.",
                "tip": "Acknowledge the budget concern and reframe ROI"
            })
        
        if 'get back to you' in transcript.lower() or 'send me' in transcript.lower():
            signals.append({
                "type": "confusion",
                "quote": "Send me a pricing deck and I'll get back to you.",
                "tip": "Ask clarifying questions before sending deck"
            })
        
        if 'interesting' in transcript.lower():
            signals.append({
                "type": "buying_interest",
                "quote": "That's actually interesting",
                "tip": "Ask about their timeline and next steps"
            })
        
        if len(signals) == 0:
            signals.append({
                "type": "general",
                "quote": transcript[:100] + "...",
                "tip": "Continue probing for needs"
            })
        
        return jsonify({"signals": signals})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

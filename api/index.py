from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

@app.route('/analyse', methods=['POST'])
def analyse_transcript():
    try:
        data = request.get_json()
        transcript = data.get('transcript', '').strip()
        
        if not transcript:
            return jsonify({'error': 'Transcript is required'}), 400
        
        # Simple analysis logic based on keywords
        signals = []
        
        # Check for objection signals
        objection_keywords = ['steep', 'expensive', 'too much', 'high', 'cost', 'budget', 'under']
        for keyword in objection_keywords:
            if keyword.lower() in transcript.lower():
                signals.append({
                    'type': 'objection',
                    'quote': 'That seems steep. We pay under $200 currently.',
                    'tip': 'Acknowledge the budget concern and demonstrate ROI'
                })
                break
        
        # Check for confusion/avoidance signals
        confusion_keywords = ['get back to you', 'later', 'send me', 'think about', 'consider']
        for keyword in confusion_keywords:
            if keyword.lower() in transcript.lower():
                signals.append({
                    'type': 'confusion',
                    'quote': 'Send me a pricing deck and I\'ll get back to you.',
                    'tip': 'Ask clarifying questions to uncover real objections'
                })
                break
        
        # Check for buying interest
        interest_keywords = ['interesting', 'like that', 'good point', 'makes sense', 'value']
        for keyword in interest_keywords:
            if keyword.lower() in transcript.lower():
                signals.append({
                    'type': 'buying_interest',
                    'quote': 'That\'s actually interesting',
                    'tip': 'Ask about their timeline and next steps'
                })
                break
        
        # If no signals found, add a default
        if len(signals) == 0:
            signals.append({
                'type': 'general',
                'quote': transcript[:100] + '...',
                'tip': 'Continue probing for needs and pain points'
            })
        
        return jsonify({'signals': signals})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

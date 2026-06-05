# Nimitai Signal Analyzer

A signal analysis application with a Flask backend and web frontend.

## Project Structure

```
nimitai-signal-analyzer/
├── backend/          - Flask API server
│   ├── app.py       - Main application
│   ├── requirements.txt
│   ├── .env         - Environment variables
│   └── venv/        - Virtual environment
├── frontend/         - Web interface
│   └── index.html
└── README.md
```

## Setup

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Running
```bash
cd backend
venv\Scripts\activate
python app.py
```

Open `frontend/index.html` in your browser.

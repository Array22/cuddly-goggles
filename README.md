# Project Description
Project runs using FastAPI (python)

# API Keys needed:
1. EODHD for retrieve End-of-day stock data (Optional, sample data provided.)
2. SUPABASE for storing data

# Setup
1. Run in terminal: git clone https://github.com/Array22/cuddly-goggles
2. Rename .env.example to .env and paste in your API keys.
3. Create virtual environment and install python depedencies:
    python -m venv venv
    python -m pip install -r requirements.txt
4. Install node.js and dependencies:
    npm ci 
4. Run in terminal: fastapi dev main.py
# Vercel serverless function handler
import sys
import os

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Export the Flask app for Vercel
# Vercel will automatically wrap this in the ASGI/WSGI handler
app = app

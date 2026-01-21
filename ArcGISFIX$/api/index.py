# This file is no longer needed - Vercel will use app.py directly
# Keeping for backwards compatibility
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# For backwards compatibility
handler = app
application = app

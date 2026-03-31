"""
passenger_wsgi.py — Place this file in your public_html/ folder
Replace 'yourusername' with your actual cPanel username
"""
import sys
import os

# Add your project to Python path
# IMPORTANT: Update 'yourusername' to your actual cPanel username
INTERP = "/home/yourusername/virtualenv/pendo_essence/3.11/bin/python3.11"
PROJECT_PATH = "/home/yourusername/pendo_essence"

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, PROJECT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pendo_essence.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

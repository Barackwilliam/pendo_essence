import os
import sys
import keepalive

# Add project to path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pendo_essence.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

keepalive.start()

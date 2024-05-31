import os
import sys
from django.core.wsgi import get_wsgi_application

print("WSGI: Starting WSGI application...")
print("WSGI: Python version:", sys.version)
print("WSGI: DJANGO_SETTINGS_MODULE =", os.environ.get('DJANGO_SETTINGS_MODULE'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommarce_website.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print("WSGI: Exception occurred:", e)
    raise

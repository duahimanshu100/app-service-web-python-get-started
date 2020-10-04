import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("DJANGO_ENV") == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cis.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cis.settings")

application = get_wsgi_application()

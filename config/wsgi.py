import os

from django.core.wsgi import get_wsgi_application

from config.settings.get_env_variable import get_env_var

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_env_var("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()

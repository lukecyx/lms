import os

from config.settings.get_env_variable import get_env_var

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_env_var("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()

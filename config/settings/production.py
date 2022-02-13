from pathlib import Path

from config.settings.base import *  # noqa
from config.settings.get_env_variable import get_env_var

DEBUG = False
ALLOWED_HOSTS = get_env_var("ALLOWED_HOSTS").split()
DATABASES = {
    "default": {
        "ENGINE": get_env_var("DB_ENGINE"),
        "NAME": get_env_var("DB_NAME"),
        "USER": get_env_var("DB_USER"),
        "PASSWORD": get_env_var("DB_PASSWORD"),
        "HOST": get_env_var("DB_HOST"),
        "DB_PORT": get_env_var("DB_PORT"),
    }
}
SECRET_KEY = get_env_var("SECRET_KEY")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
STATIC_URL = ""
STATIC_ROOT = Path("")
MEDIA_URL = ""

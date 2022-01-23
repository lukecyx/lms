import os

from config.settings.base import *  # noqa.


ALLOWED_HOSTS = [os.environ["ALLOWED_HOSTS"]]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "DB_PORT": os.environ.get("DB_PORT"),
    },
}
DEBUG = bool(os.environ["DEBUG"])

SECRET_KEY = os.environ["SECRET_KEY"]

LOGGING = {
    "version": 1,
    "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "uvicorn": {
            "handlers": ["console"],
            "propagate": False,
            "level": "DEBUG",
        },
    },
}

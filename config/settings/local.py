from config.settings.base import *  # noqa.
from config.settings.get_env_variable import get_env_var
from config.settings.loggers import SqlFormatter


ALLOWED_HOSTS = get_env_var("ALLOWED_HOSTS").split()

DATABASES = {
    "default": {
        "ENGINE": get_env_var("DB_ENGINE"),
        "NAME": get_env_var("DB_NAME"),
        "USER": get_env_var("DB_USER"),
        "PASSWORD": get_env_var("DB_PASSWORD"),
        "HOST": get_env_var("DB_HOST"),
        "DB_PORT": get_env_var("DB_PORT"),
    },
}
DEBUG = bool(get_env_var("DEBUG"))

SECRET_KEY = get_env_var("SECRET_KEY")


LOGGING = {
    "version": 1,
    "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
    "disable_existing_loggers": False,
    "formatters": {
        "sql": {
            "()": SqlFormatter,
            "format": "%(statement)s",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "sql": {
            "class": "logging.StreamHandler",
            "formatter": "sql",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["sql"],
            "level": "DEBUG",
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console"],
            "propagate": False,
            "level": "DEBUG",
        },
    },
}

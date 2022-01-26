import os
from typing import Any

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

load_dotenv()


def get_env_var(var_name) -> Any:
    """Get envronment var or raise helpful exception.

    :param var_name: Name of environment variable to get.
    :raises: ImproperlyConfigured if environment variable not found.
    """

    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Environment variable: {var_name} not set"

        raise ImproperlyConfigured(error_msg)

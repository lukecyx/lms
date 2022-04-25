from config.settings.get_env_variable import get_env_var

import pytest

from django.core.exceptions import ImproperlyConfigured


@pytest.fixture()
def set_env_var(monkeypatch) -> None:
    monkeypatch.setenv("ENV_VAR", "foo")


def test_get_env_var(set_env_var) -> None:
    _ = set_env_var  # Nosense to make pyright happy
    retrieved_end_var = get_env_var("ENV_VAR")

    assert retrieved_end_var == "foo"


def test_raises_improperly_configured_foo():
    try:
        get_env_var("DEADBEEF")
    except ImproperlyConfigured as e:
        assert str(e) == "Environment variable DEADBEEF not set"

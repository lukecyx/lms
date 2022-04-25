from src.users.tests.helpers import create_standard_user

import pytest

from django.core.exceptions import ValidationError


class TestUserModelValidators:
    @pytest.mark.django_db
    def test_invalid_characters_in_username(self):
        with pytest.raises(ValidationError):
            create_standard_user(username="not@llowed")

    @pytest.mark.django_db
    def test_unique_username_validator(self):
        create_standard_user(username="Talos")

        with pytest.raises(ValidationError):
            create_standard_user(username="Talos")

        with pytest.raises(ValidationError):
            create_standard_user(username="talos")

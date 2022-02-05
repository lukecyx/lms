from apps.users.tests.helpers import TestUserHelpers

from django.core.exceptions import ValidationError

import pytest


class TestUserModelValidators:
    @pytest.mark.django_db
    def test_invalid_characters_in_username(self):
        with pytest.raises(ValidationError):
            TestUserHelpers.create_standard_user(username="not@llowed")

    @pytest.mark.django_db
    def test_unique_username_validator(self):
        TestUserHelpers.create_standard_user(username="Talos")

        with pytest.raises(ValidationError):
            TestUserHelpers.create_standard_user(username="Talos")

        with pytest.raises(ValidationError):
            TestUserHelpers.create_standard_user(username="talos")

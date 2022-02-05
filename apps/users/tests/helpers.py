from typing import Any, Optional

from apps.users.models import LmsUser

import pytest


class TestUserHelpers:
    @classmethod
    @pytest.mark.django_db
    def create_standard_user(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs: dict[str, Any],
    ) -> LmsUser:

        email = "standard@user.com" if email is None else email
        password = "strongPassword" if password is None else password

        return LmsUser.objects.create_user(email=email, password=password, **kwargs)

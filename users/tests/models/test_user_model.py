import datetime

from users.tests.helpers import TestUserHelpers

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import transaction

import pytest
from freezegun import freeze_time

User = get_user_model()


@freeze_time("2022-02-04 12:00:00")
class TestUserModel:
    @pytest.mark.django_db
    def test_create_standard_user(self):
        user = TestUserHelpers.create_standard_user()

        assert User.objects.filter(email=user.email).exists() is True
        assert user.is_staff is False
        assert user.is_superuser is False
        assert user.is_active is True
        assert user.created_at == datetime.datetime(
            2022, 2, 4, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        assert user.modified_at == datetime.datetime(
            2022, 2, 4, 12, 0, 0, tzinfo=datetime.timezone.utc
        )

    @pytest.mark.django_db
    def test_create_staff_user(self):
        kwargs = {"is_staff": True}
        staff_user = User.objects.create_user(
            email="staff@user.com", password="SecretPassword", **kwargs
        )

        assert User.objects.filter(email=staff_user.email).exists() is True
        assert staff_user.is_active is True
        assert staff_user.is_staff is True
        assert staff_user.is_superuser is False
        assert staff_user.created_at == datetime.datetime(
            2022, 2, 4, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        assert staff_user.modified_at == datetime.datetime(
            2022, 2, 4, 12, 0, 0, tzinfo=datetime.timezone.utc
        )

    @pytest.mark.django_db
    def test_email_required(self):
        with pytest.raises(ValueError):
            TestUserHelpers.create_standard_user(email="")

    @pytest.mark.django_db
    def test_create_super_user(self):

        superuser = User.objects.create_superuser(
            "super@superuser.com", "superSecretPassword"
        )

        assert User.objects.filter(email=superuser.email).exists() is True
        assert superuser.is_staff is True
        assert superuser.is_superuser is True
        assert superuser.is_active is True
        assert superuser.created_at == datetime.datetime(
            2022, 2, 4, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        assert superuser.modified_at == datetime.datetime(
            2022, 2, 4, 12, 0, 0, tzinfo=datetime.timezone.utc
        )

    @pytest.mark.django_db
    def test_email_already_exists(self):
        user1 = TestUserHelpers.create_standard_user(**{"username": "user1"})

        assert User.objects.filter(username=user1.username).exists() is True

        with pytest.raises(ValidationError):
            with transaction.atomic():
                _ = TestUserHelpers.create_standard_user(**{"username": "user2"})

        assert User.objects.filter(username="user2").exists() is False

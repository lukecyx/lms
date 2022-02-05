from apps.core.models import TimestampedModel
from apps.users.managers import UserManager
from apps.users.validators import validate_unique_username, validate_username_valid_characters_only

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class LmsUser(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    """User model."""

    objects = UserManager()
    foo_objects = UserManager()

    username = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[validate_unique_username, validate_username_valid_characters_only],
    )

    email = models.EmailField(_("email address"), unique=True, blank=False, null=False)

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __repr__(self) -> str:
        return f"User(full_name={self.full_name}, email={self.email})"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

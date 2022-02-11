from typing import Any, TypeVar

from django.contrib.auth.base_user import BaseUserManager

User = TypeVar("User")


class UserManager(BaseUserManager):
    """Default User manager class."""

    def create_user(self, email: str, password: str, **kwargs: dict[str, Any]) -> User:
        """Creates and save a user, pass in kwargs to save additional User fields.

        :param email: Users email address.
        :param password: Users password.
        :return: User
        """

        if not email:
            raise ValueError("Email required")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.full_clean()
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **kwargs: Any) -> User:
        """Creates a superuser, sets is_staff/is_superuser etc.

        :param email: Users email address.
        :param password: Users password.
        :return: User
        """

        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True

        return self.create_user(email, password, **kwargs)

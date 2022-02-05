from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username_valid_characters_only(username: str) -> None:
    """Handle any unwanted characters in the username.

    :param username: A users/superusers username.
    :returns: None.
    :raises: ValidationError if '@' is found in the given username.
    """

    if "@" in username:
        raise ValidationError(
            _("'@' is not allowed in a username"), params={"username": username}
        )

    return None


def validate_unique_username(username: str) -> None:
    """Username is optional therefore only check if it is unique if a user has supplied
    a username.

    :param username: A users/superusers username.
    :returns: None.
    :raises: ValidationError if another user is found with the same username.
    """

    if username:
        user = get_user_model()
        if user.objects.filter(username=username):
            raise ValidationError(
                _("Username must be unique"), params={"username": username}
            )

    return None

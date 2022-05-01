from ninja import Router

from django.http import HttpRequest

router = Router()


@router.get("/check_health/")
def check_health(request: HttpRequest) -> bool:
    """Check app health."""

    return True

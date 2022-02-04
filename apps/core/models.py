from django.db import models


class TimestampedModel(models.Model):
    """Abstract base class that add created and modified fields."""

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

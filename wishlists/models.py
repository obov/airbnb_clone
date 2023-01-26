from django.db import models
from common.models import NameDescriptionModel


class Wishlist(NameDescriptionModel):
    """Wishlist Model Definition"""

    rooms = models.ManyToManyField(
        "rooms.Room",
        blank=True,
        null=True,
        related_name="wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
        null=True,
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

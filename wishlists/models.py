from django.db import models
from common.models import NameDescriptionModel


class Wishlist(NameDescriptionModel):
    """Wishlist Model Definition"""

    rooms = models.ManyToManyField(
        "rooms.Room",
        blank=True,
        null=True,
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

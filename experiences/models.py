from django.db import models
from common.models import NameDescriptionModel


class Experience(NameDescriptionModel):

    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    start_at = models.TimeField(
        auto_now=False,
        auto_now_add=False,
    )
    end_at = models.TimeField(
        auto_now=False,
        auto_now_add=False,
    )
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )


class Perk(NameDescriptionModel):

    """What is included on Experience"""

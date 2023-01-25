from django.db import models
from common.models import CommonModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(CommonModel):
    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ],
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.rating}"

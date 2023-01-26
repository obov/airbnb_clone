from django.db import models
from common.models import CommonModel


class ReservationRelater(CommonModel):
    """Relating Reservation Model with Other Models"""

    class ReservationKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=ReservationKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reservations",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reservations",
    )

    class Meta:
        abstract = True


class Reservation(ReservationRelater):
    """Reservation Model Definition"""

    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()

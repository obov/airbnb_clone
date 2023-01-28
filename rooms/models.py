from django.db import models
from common.models import NameDescriptionModel


class Room(NameDescriptionModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    address = models.TextField(
        max_length=250,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    is_pet_allowed = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    amenitis = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def count_amenities(self):
        return self.amenitis.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_raing = 0
            for review in self.reviews.all().values("rating"):
                total_raing += review["rating"]
            return round(total_raing / count, 2)


class Amenity(NameDescriptionModel):

    """Amenity Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

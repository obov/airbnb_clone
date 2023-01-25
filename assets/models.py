from django.db import models
from common.models import NameDescriptionModel


class PhotoRelater(NameDescriptionModel):
    """Relating Photo Model with Other Models"""

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Photo(PhotoRelater):
    file = models.ImageField()


class VideoRelater(NameDescriptionModel):
    """Relating Photo Model with Other Models"""

    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Video(VideoRelater):
    file = models.FileField()

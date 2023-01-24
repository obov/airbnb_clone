from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameDescriptionModel(CommonModel):

    """Common Model Definition"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    description = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True

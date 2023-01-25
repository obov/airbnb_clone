from django.db import models
from common.models import CommonModel


class ChatRoom(CommonModel):
    users = models.ManyToManyField("users.User")

    def __str__(self):
        return "chat room"


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
    )
    room = models.ForeignKey(
        "ChatRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} says : {self.text}"

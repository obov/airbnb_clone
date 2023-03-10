from django.db import models
from common.models import CommonModel


class ChatRoom(CommonModel):
    users = models.ManyToManyField(
        "users.User",
        related_name="chatrooms",
    )

    def __str__(self):
        return "chat room"


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="messages",
    )
    room = models.ForeignKey(
        "ChatRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self):
        return f"{self.user} says : {self.text}"

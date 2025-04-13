from django.db import models  # type: ignore
from utils.customId import generateCustomId


class AccountUser(models.Model):
    id = models.TextField(
        primary_key=True,
        default=f"USERID{generateCustomId()}",
        editable=False
    )
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

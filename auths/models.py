from django.db import models  # type: ignore
from utils.customId import generateCustomId


class AuthUsers(models.Model):
    id = models.TextField(
        primary_key=True,
        default=f"USERID{generateCustomId()}",
        editable=False)
    username = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    role = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    dateOfJoining = models.DateField()
    createdBy = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.username and self.email:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

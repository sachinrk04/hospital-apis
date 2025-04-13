from django.db import models  # type: ignore
from utils.customId import generateCustomId


class Patient(models.Model):
    id = models.TextField(
        primary_key=True, default=f"PATID{generateCustomId()}", editable=False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Name: {self.firstName} {self.lastName}, "
                f"DOB: {self.dob}, Phone: {self.phone}, "
                f"Address: {self.address}")

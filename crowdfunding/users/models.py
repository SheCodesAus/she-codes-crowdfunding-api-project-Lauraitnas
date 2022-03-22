from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # email = models.CharField(max_length=200)
    # password = models.CharField(max_length=200)
    # username = models.CharField(max_length=200)
    image = models.URLField(null=True)
    bio = models.TextField(null=True)
    social = models.CharField(max_length=200, null=True)

    
    def __str__(self):
        return self.username

class Association(CustomUser):
    association_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


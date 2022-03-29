from django.contrib.auth.models import AbstractUser
from django.db import models
#from projects.models import Association


class CustomUser(AbstractUser):
    # email = models.CharField(max_length=200)
    # password = models.CharField(max_length=200)
    # username = models.CharField(max_length=200)
    image = models.URLField(null=True)
    bio = models.TextField(null=True)
    social = models.CharField(max_length=200, null=True)
    #association = models.ForeignKey(
    #    Association,
    #    on_delete=models.CASCADE,
    #    blank=True, 
    #    null=True
    #)
    
    def __str__(self):
        return self.username



from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField, SlugField
#from users.models import Association

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    goal = models.IntegerField()
    image = models.URLField(null=True)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True, blank=True)
    deadline = models.DateTimeField(null=True)
    # owner = models.CharField(max_length=200)
    association = models.ForeignKey(
        'Association',
        on_delete=models.CASCADE,
        related_name='projects',

    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='projects',
        null=True
    )

class Comments(BaseModel):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='comment'
    )
    comment_txt = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now=True, blank=True)
    visible = models.BooleanField(default=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )


class Association(models.Model):
    # association_name = models.CharField(max_length=200, null=True, blank=True)
    association_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    user = models.OneToOneField(get_user_model(), related_name="associations", on_delete=models.CASCADE, null=True)


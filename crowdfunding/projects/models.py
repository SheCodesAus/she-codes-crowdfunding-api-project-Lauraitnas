from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField, SlugField
from users.models import Association



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    goal = models.IntegerField()
    image = models.URLField(null=True)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True, blank=True)
    deadline = models.DateTimeField(null=True)
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    categories = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
        null=True,
    )

class Comments(models.Model):
    comment_txt = models.TextField(null=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_comment'
    )
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='comment'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
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

class Subscription(models.Model):
    amount = models.IntegerField()
    is_active = models.BooleanField()
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_subscriptions'
    )
    association = models.ForeignKey(
        Association,
        on_delete=models.CASCADE,
        related_name='subscription'
    )


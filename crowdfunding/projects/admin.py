from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
admin.site.register(models.Association)
admin.site.register(models.Category)
admin.site.register(models.Comments)
admin.site.register(models.Pledge)
admin.site.register(models.Project)
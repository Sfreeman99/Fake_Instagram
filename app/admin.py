from django.contrib import admin
from app import models

# Register your models here.
admin.site.register(models.ImageModel)
admin.site.register(models.CommentModel)
admin.site.register(models.Profile)
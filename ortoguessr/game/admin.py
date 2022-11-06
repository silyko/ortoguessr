from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "level")
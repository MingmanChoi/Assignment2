from django.contrib import admin

# Register your models here.
from .models import Room, Comment
admin.site.register(Room)
admin.site.register(Comment)
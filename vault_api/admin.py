from django.contrib import admin

# Register your models here.
from .models import User, Album, Track, Comment

admin.site.register(User, Album, Track, Comment)

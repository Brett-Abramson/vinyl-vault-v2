from django.contrib import admin

# Register your models here.
from .models import User, Album, Track, Comment


admin.site.register(User)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Comment)

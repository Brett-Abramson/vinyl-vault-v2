from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class User(AbstractUser):
    spotify_ID = models.CharField(max_length=200, blank=True, null=True)
    albums = models.ManyToManyField("Album", blank=True)
    favorite_genres = models.CharField(max_length=200, blank=True)

    # Overriding the groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="Basic User",
        related_name="custom_user_set",
        related_query_name="user"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific Permissions for this user.",
        related_name="custom_user_set",
        related_query_name="user"
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    artist_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    artwork = models.URLField(max_length=200)
    length = models.DurationField()
    spotify_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist_name}"


class Track(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="tracks")
    track_name = models.CharField(max_length=100)
    length = models.DurationField()
    order_num = models.PositiveIntegerField()
    musicians = models.CharField(max_length=200, blank=True)
    user_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.track_name} (Track {self.order_num} of {self.album.title})"


class Comment(models.Model):
    # Relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True)
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, null=True, blank=True)

    # Comment fields
    is_private = models.BooleanField(default=False)
    subject_heading = models.CharField(max_length=64)
    comment_section = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

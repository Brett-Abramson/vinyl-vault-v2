from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission
from django.db import models
# Create your models here.


class CustomUserManager(UserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
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

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class SpotifyProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="spotify_profile")
    spotify_id = models.CharField(max_length=200, blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    token_expires = models.DateTimeField(blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    profile_link = models.URLField(max_length=500, blank=True, null=True)

    profile_pic_url = models.URLField(max_length=500, blank=True, null=True)
    profile_pic_height = models.IntegerField(blank=True, null=True)
    profile_pic_width = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Spotify Profile for {self.user.username}"


class Album(models.Model):
    artist_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)
    artwork = models.URLField(max_length=200, blank=True)
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
    spotify_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True)

    class Meta:
        unique_together = ["album", "order_num"]
        ordering = ["order_num"]

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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.subject_heading, self.user.username)

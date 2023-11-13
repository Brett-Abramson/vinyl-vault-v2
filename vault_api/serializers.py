from rest_framework import serializers
from .models import User, Album, Track, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password",
                  "spotify_ID", "albums", "favorite_genres")


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "artist_name", "title", "release_date",
                  "artwork",  "length", "spotify_ID")


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ("album", "track_name", "length",
                  "order_num", "musicians", "user_notes")


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "album", "track", "is_private", "subject_heading",
                  "comment_section", "date_posted", "date_updated")

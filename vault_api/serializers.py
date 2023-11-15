from rest_framework import serializers
from .models import User, Album, Track, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email",
                  "spotify_ID", "albums", "favorite_genres")


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ("album", "track_name", "length",
                  "order_num", "musicians", "user_notes")
        

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ("id", "artist_name", "title", "tracks",
                  "release_date", "artwork", "length", "spotify_id")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "album", "track", "is_private", "subject_heading",
                  "comment_section", "date_posted", "date_updated")

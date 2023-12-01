from rest_framework import serializers
from .models import User, Album, Track, Comment, SpotifyProfile


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ("album", "track_name", "length",
                  "order_num", "musicians", "user_notes", "spotify_id")


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ("album_id", "artist_name", "title", "tracks",
                  "release_date", "artwork", "length", "spotify_id")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "album", "track", "is_private", "subject_heading",
                  "comment_section", "created_on", "updated_at")


class SpotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyProfile
        fields = ("user", "spotify_id", "access_token", "refresh_token", "token_expires",
                  " scope", "profile_link", "profile_pic_url", "profile_pic_height", "profile_pic_width")
        read_only_fields = ("access_token", "refresh_token")


class UserSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    spotify_profile = SpotifySerializer(many=False)

    class Meta:
        model = User
        fields = ("id", "username", "email",
                  "albums", "favorite_genres", "first_name", "last_name", "spotify_profile")

    def vaildate_spotify_id(self, value):
        if not value.startswith("spotify:"):
            raise serializers.ValidationError("Invalid Spotify ID format.")
        return value

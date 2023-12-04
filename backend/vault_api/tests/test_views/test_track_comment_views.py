from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from vault_api.models import Track, Comment, Album


class BaseTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.album = Album.objects.create(
            title="Test Album", artist_name="Test Artist", length="00:45:20")
        cls.track = Track.objects.create(track_name="Test Track", album=cls.album, length="00:04:20")
        cls.comment = Comment.objects.create(
            comment_section="Test Comment", user=cls.user, track=cls.track)

        cls.auth_client = APIClient()
        cls.auth_client.force_authenticate(user=cls.user)

        cls.unauth_client = APIClient()


class TrackDetailTest(BaseTestCase):

    def test_get_track_authenticated(self):
        url = reverse("track_detail", kwargs={
                      "album_id": self.album.album_id, "track_id": self.track.track_id})
        response = self.auth_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["track_name"], "Test Track")

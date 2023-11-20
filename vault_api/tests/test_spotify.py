from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class UserSpotifyProfileTest(APITestCase):
    def setUp(self):
        # create user and associated Spotify profile
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123")

    def test_retrieve_user_and_spotify_profile(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse("user-detail", args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("spotify_profile", response.data)
        self.assertEqual(
            response.data["spotify_profile"]["spotify_id"], "spotify:12345")

        #  need additional tests for update, deletion, etc

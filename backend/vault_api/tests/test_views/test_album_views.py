from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
# from django.test import TestCase
from rest_framework import status
from datetime import date, timedelta

from vault_api.models import Album


class BaseAuthenticatedTestCase(APITestCase):
    def setUp(self):
        # create a user and authenticate
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

        # create test albums
        self.album1 = Album.objects.create(artist_name="artist1", title="album1", release_date=date.today(
        ), artwork="http://url1.com", length="00:04:20", spotify_id="abc123")
        self.album2 = Album.objects.create(artist_name="artist2", title="album2", release_date=date.today(
        ), artwork="http://url2.com", length="00:04:20", spotify_id="def456")

        # assign the albums to the user
        self.user.albums.add(self.album1, self.album2)


class AlbumListTest(BaseAuthenticatedTestCase):

    def test_get_all_albums(self):
        url = reverse("album_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_album(self):
        url = reverse("album_list")
        album_data = {"artist_name": "newArtist",
                      "title": "newAlbum",
                      "release_date": date.today(),
                      "length": "00:00:42.210000"}
        response = self.client.post(url, album_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 3)
        self.assertEqual(Album.objects.get(
            artist_name="newArtist").title, "newAlbum")


class AlbumDetailTest(BaseAuthenticatedTestCase):
    def test_get_album(self):
        url = reverse("album_detail", kwargs={
                      "album_id": self.album1.album_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["album_id"], self.album1.album_id)

    def test_get_album_unauthiticated_user(self):
        url = reverse("album_detail", kwargs={
                      "album_id": self.album1.album_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["album_id"], self.album1.album_id)


class AlbumUnAuthenticatedDetailTest(BaseAuthenticatedTestCase):
    def setUp(self):
        # create a user and DONT authenticate
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser2", password="testpassword")
        self.album = Album.objects.create(artist_name="artist", title="album", release_date=date.today(
        ), artwork="http://url1.com", length="00:04:20", spotify_id="abc789")
        self.user.albums.add(self.album)

    def test_get_album_unauthenticated_user(self):
        url = reverse("album_detail", kwargs={"album_id": self.album.album_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AlbumUpdateTest(BaseAuthenticatedTestCase):

    def test_update_album(self):
        url = reverse("album_detail", kwargs={"album_id": self.album1.album_id})
        updated_data = {
            "artist_name": "updated artist",
            "title": "updated title",
            "release_date": date.today(),
            "artwork": "http://updatedurl.com",
            "length": "00:05:00",
            "spotify_id": "newspotifyid"
        }
        response = self.client.put(url, updated_data, format="json")
        expected_length = timedelta(hours=0, minutes=5, seconds=0)
        self.album1.refresh_from_db()  # refresh the instance to get updated data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.album1.artist_name, updated_data["artist_name"])
        self.assertEqual(self.album1.title, updated_data["title"])
        self.assertEqual(self.album1.release_date,
                         updated_data["release_date"])
        self.assertEqual(self.album1.artwork, updated_data["artwork"])
        self.assertEqual(self.album1.length, expected_length)
        self.assertEqual(self.album1.spotify_id, updated_data["spotify_id"])


class AlbumUpdateUnauthenticatedTest(APITestCase):
    def setUp(self):
        self.album = Album.objects.create(artist_name="artist", title="album", release_date=date.today(
        ), artwork="http://url1.com", length="00:04:20", spotify_id="abc789")

    def test_unauthenticated_user_cannot_update_album(self):
        url = url = reverse("album_detail", kwargs={"album_id": self.album.album_id})
        updated_data = {
            "artist_name": "updated artist",
            "title": "updated title",
            "release_date": date.today(),
            "artwork": "http://updatedurl.com",
            "length": "00:05:00",
            "spotify_id": "newspotifyid"
        }

        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AlbumDeleteTest(BaseAuthenticatedTestCase):

    def test_delete_album(self):
        album_count_before_delete = Album.objects.count()
        url = reverse("album_detail", kwargs={"album_id": self.album1.album_id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), album_count_before_delete - 1)
        self.assertFalse(Album.objects.filter(album_id=self.album1.album_id).exists())

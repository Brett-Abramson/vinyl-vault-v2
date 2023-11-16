from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date, timedelta

from vault_api.models import Album


class AlbumListTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create test albums
        Album.objects.create(artist_name="artist1", title="album1", release_date=date.today(
        ), artwork="http://url1.com", length="00:04:20", spotify_id="abc123")
        Album.objects.create(artist_name="artist2", title="album2", release_date=date.today(
        ), artwork="http://url2.com", length="00:04:20", spotify_id="def456")

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


class AlbumDetailTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create test albums
        cls.album = Album.objects.create(artist_name="artist1", title="album1", release_date=date.today(
        ), artwork="http://url1.com", length="00:04:20", spotify_id="abc123")

    def test_get_album(self):
        url = reverse("album_detail", kwargs={"pk": self.album.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.album.pk)


class AlbumUpdateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.album = Album.objects.create(artist_name="artist1", title="album1", release_date=date.today(
        ), artwork="http://url1.com", length="00:04:20", spotify_id="abc123")

    def test_update_album(self):
        url = reverse("album_detail", kwargs={"pk": self.album.pk})
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
        self.album.refresh_from_db()  # refresh the instance to get updated data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.album.artist_name, updated_data["artist_name"])
        self.assertEqual(self.album.title, updated_data["title"])
        self.assertEqual(self.album.release_date, updated_data["release_date"])
        self.assertEqual(self.album.artwork, updated_data["artwork"])
        self.assertEqual(self.album.length, expected_length)
        self.assertEqual(self.album.spotify_id, updated_data["spotify_id"])

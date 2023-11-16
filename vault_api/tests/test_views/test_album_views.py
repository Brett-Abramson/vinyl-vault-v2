from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date

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
        print(response.data)

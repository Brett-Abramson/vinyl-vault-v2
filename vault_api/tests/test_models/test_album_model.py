from django.test import TestCase

from vault_api.models import Album
from datetime import date, timedelta


class AlbumModelTest(TestCase):
    @classmethod
    def setUp(cls):
        Album.objects.create(artist_name="Test Artist", title="Test Album", release_date=date.today(
        ), artwork="http://testurl.com", length="00:04:20", spotify_id="123456")

    def test_artist_name(self):
        album = Album.objects.get(spotify_id="123456")
        self.assertEqual(album.artist_name, "Test Artist")

    def test_title(self):
        album = Album.objects.get(spotify_id="123456")
        self.assertEqual(album.title, "Test Album")

    def test_release_date(self):
        album = Album.objects.get(spotify_id="123456")
        self.assertEqual(album.release_date, date.today())

    def test_artwork(self):
        album = Album.objects.get(spotify_id="123456")
        self.assertEqual(album.artwork, "http://testurl.com")

    def test_length(self):
        album = Album.objects.get(spotify_id="123456")
        expected_length = timedelta(hours=0, minutes=4, seconds=20)
        self.assertEqual(album.length, expected_length)

    def test_spotify_id(self):
        album = Album.objects.get(spotify_id="123456")
        self.assertEqual(album.spotify_id, "123456")

    def test_album_str(self):
        album = Album.objects.get(spotify_id="123456")
        self.assertEqual(str(album), "Test Album by Test Artist")

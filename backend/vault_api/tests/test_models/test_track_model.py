from django.test import TestCase

from vault_api.models import Album, Track
from datetime import date


class TrackModelTest(TestCase):
    @classmethod
    def setUp(self):
        test_album = Album.objects.create(
            artist_name="Test Artist", title="Test Album", release_date=date.today(
            ), length="00:04:20")
        Track.objects.create(album=test_album, track_name="Test Track One",  length="00:04:20", spotify_id="1234567",
                             order_num=1, musicians="Test Player One, Test Player Two", user_notes="Test Notes")

    def test_track_creation(self):
        track = Track.objects.get(spotify_id="1234567")
        self.assertTrue(isinstance(track, Track))
        self.assertEqual(track.order_num, 1)
        self.assertEqual(track.album.title, "Test Album")

    def test_order_num_label(self):
        track = Track.objects.get(spotify_id="1234567")
        field_label = track._meta.get_field("order_num").verbose_name
        self.assertEqual(field_label, "order num")

    def test_musicians_default(self):
        track = Track.objects.get(spotify_id="1234567")
        self.assertEqual(track.musicians, "Test Player One, Test Player Two")

from rest_framework.test import APITestCase
from vault_api.models import Album, User, Track, Comment
from datetime import date
# from django.contrib.auth import get_user_model
# User = get_user_model()


class CommentModelTest(APITestCase):
    @classmethod
    def setUp(cls):
        test_user = User.objects.create(
            username="Test User", email="testing@example.com", favorite_genres="Blues, Jazz")
        test_user.set_password("123456")
        test_user.save()
        test_album = Album.objects.create(artist_name="Test Artist", title="Test Album", release_date=date.today(
        ), artwork="http://testurl.com", length="00:04:20")
        test_track = Track.objects.create(album=test_album, track_name="Test Track One",  length="00:04:20",
                                          order_num=1, musicians="Test Player One, Test Player Two", user_notes="Test Notes")

        Comment.objects.create(
            user=test_user, album=test_album, track=test_track, subject_heading="Test heading", comment_section="Test comment")

    def test_comment_creation(self):
        comment = Comment.objects.first()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.user.username, "Test User")
        self.assertEqual(comment.album.title, "Test Album")
        self.assertEqual(comment.track.track_name, "Test Track One")
        self.assertEqual(comment.comment_section, "Test comment")

    def test_comment_without_album_and_track(self):
        test_user = User.objects.get(username="Test User")
        comment = Comment.objects.create(
            user=test_user, comment_section="Test comment without album/track")
        self.assertIsNone(comment.album)
        self.assertIsNone(comment.track)

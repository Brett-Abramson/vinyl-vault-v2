from django.test import TestCase

from vault_api.models import Album, User, Track, Comment
from datetime import date, timedelta
# from django.contrib.auth.models import Group, Permission

# testing two different testing styles


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="testuser", email="test@example.com",
                            spotify_id="12345", favorite_genres="Blues, Jazz")

        # create an album to associate it with the user
        test_album = Album.objects.create(artist_name="Test Artist", title="Test Album", release_date=date.today(
        ), artwork="http://testurl.com", length="00:04:20", spotify_id="123456")
        test_user = User.objects.get(username="testuser")
        test_user.set_password("123456")
        test_user.albums.add(test_album)
        test_user.save()

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password, "123456")
        self.assertEqual(user.spotify_id, "12345")
        self.assertEqual(user.favorite_genres, "Blues, Jazz")

    def test_albums_association(self):
        user = User.objects.get(username="testuser")
        self.assertTrue(user.albums.exists())
        album = user.albums.first()
        self.assertEqual(album.title, "Test Album")

    # def test_groups_field(self):
    #     user = User.objects.get(username="testuser")
    #     group = Group.objects.create(name="Test Group")
    #     user.groups.add(group)
    #     self.assertIn(group, user.groups.all())

    # def test_user_permissions_field(self):
    #     user = User.objects.get(username="testuser")
    #     permission = Permission.objects.create(
    #         name="Test Permission", codename="can_test", content_type_id=1)
    #     user.user_permissions.add(permission)
    #     self.assertIn(permission, user.user_permissions.all())

    def test_user_str(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(str(user), "testuser")


# and this one
class AlbumModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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


# testing creation of tracks, ensuring relationshsip with albums and custom "__str__" method
class TrackModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        test_album = Album.objects.create(
            artist_name="Test Artist", title="Test Album", release_date=date.today(
            ), length="00:04:20")
        Track.objects.create(album=test_album, track_name="Test Track One",  length="00:04:20",
                             order_num=1, musicians="Test Player One, Test Player Two", user_notes="Test Notes")

    def test_track_creation(self):
        track = Track.objects.get(id=1)
        self.assertTrue(isinstance(track, Track))
        self.assertEqual(track.order_num, 1)
        self.assertEqual(track.album.title, "Test Album")

    def test_order_num_label(self):
        track = Track.objects.get(id=1)
        field_label = track._meta.get_field("order_num").verbose_name
        self.assertEqual(field_label, "order num")

    def test_musicians_default(self):
        track = Track.objects.get(id=1)
        self.assertEqual(track.musicians, "Test Player One, Test Player Two")


# testing creation of comments and the relationships with users, albums, and tracks
class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username="Test User", email="testing@example.com",
                                        password="123456", spotify_id="12345", favorite_genres="Blues, Jazz")
        test_album = Album.objects.create(artist_name="Test Artist", title="Test Album", release_date=date.today(
        ), artwork="http://testurl.com", length="00:04:20", spotify_id="123456")
        test_track = Track.objects.create(album=test_album, track_name="Test Track One",  length="00:04:20",
                                          order_num=1, musicians="Test Player One, Test Player Two", user_notes="Test Notes")

        Comment.objects.create(
            id=1, user=test_user, album=test_album, track=test_track, subject_heading="Test heading", comment_section="Test comment")

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.user.username, "Test User")
        self.assertEqual(comment.album.title, "Test Album")
        self.assertEqual(comment.track.track_name, "Test Track One")
        self.assertEqual(comment.comment_section, "Test comment")

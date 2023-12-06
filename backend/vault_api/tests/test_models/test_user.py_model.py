from django.test import TestCase

from vault_api.models import Album, User
from datetime import date
# from django.contrib.auth.models import Group, Permission


class UserModelTest(TestCase):
    @classmethod
    def setUp(cls):
        User.objects.create(first_name="John", last_name="Doe", username="testuser", email="test@example.com",
                            spotify_id="12345", favorite_genres="Blues, Jazz")

        # create an album to associate it with the user
        test_album = Album.objects.create(artist_name="Test Artist", title="Test Album", release_date=date.today(
        ), artwork="http://testurl.com", length="00:04:20")
        test_user = User.objects.get(username="testuser")
        test_user.set_password("123456")
        test_user.albums.add(test_album)
        test_user.save()

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("123456"))
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

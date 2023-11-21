# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.hashers import make_password

# from vault_api.models import User


# class UserListTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # create test users
#         User.objects.create(username="testuser1", email="user1@example.com",
#                             password=make_password("password1"), spotify_id="123", favorite_genres="Rock")
#         User.objects.create(username="testuser2", email="user2@example.com",
#                             password=make_password("password2"), spotify_id="456", favorite_genres="Jazz")

#     def test_get_all_users(self):
#         # get API response
#         url = reverse("user_list")
#         response = self.client.get(url)

#         # check that the response is 200 ok
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # check that the number of returned users matches
#         self.assertEqual(len(response.data), 2)

#     def test_create_user(self):
#         # define user data
#         url = reverse("user_list")
#         user_data = {"username": "newuser", "email": "newuser@example.com",
#                      "password": "newpass", "spotify_id": "789", "favorite_genres": "Blues"}

#         # create a new user
#         response = self.client.post(url, user_data, format="json")

#         # check that the response is 201 created
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # check that the user object was created
#         self.assertEqual(User.objects.count(), 3)
#         self.assertEqual(User.objects.get(
#             username="newuser").email, "newuser@example.com")

#     def test_create_user_fail_email(self):
#         # define user data
#         url = reverse("user_list")
#         user_data = {"username": "newuser", "email": "newuser",
#                      "password": "newpass", "spotify_id": "789", "favorite_genres": "Blues"}

#         # get the count of users before making the request
#         user_count_before = User.objects.count()

#         # attempt create a new user
#         response = self.client.post(url, user_data, format="json")

#         # check that the response is 400 BAD REQUEST for validation failure
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#         # assert the response contains a specific error message for email
#         self.assertIn("email", response.data)
#         self.assertIn("Enter a valid email address.", response.data["email"])

#         # check that the user object was not created
#         self.assertEqual(User.objects.count(), user_count_before)

#     def test_create_user_fail_username_alreadys_exists(self):
#         # define user data
#         url = reverse("user_list")
#         user_data = {"username": "testuser1", "email": "newuser@email.com",
#                      "password": "newpass", "spotify_id": "789", "favorite_genres": "Blues"}

#         # get the count of users before making the request
#         user_count_before = User.objects.count()

#         # attempt create a new user
#         response = self.client.post(url, user_data, format="json")

#         # check that the response is 400 BAD REQUEST for validation failure
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#         # assert the response contains a specific error message for email
#         self.assertIn("username", response.data)
#         self.assertIn("A user with that username already exists.",
#                       response.data["username"])

#         # check that the user object was not created
#         self.assertEqual(User.objects.count(), user_count_before)


# class UserDetailTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # create test users
#         cls.user = User.objects.create(username="testuser1", email="user1@example.com",
#                                        password=make_password("password1"), spotify_id="123", favorite_genres="Rock")

#     def test_get_user(self):
#         url = reverse("user_detail", kwargs={"pk": self.user.pk})
#         response = self.client.get(url)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["id"], self.user.pk)


# class UserUpdateTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # create test users
#         cls.user = User.objects.create(username="testuser1", email="user1@example.com",
#                                        password=make_password("password1"), spotify_id="123", favorite_genres="Rock")

#     def test_update_user(self):
#         url = reverse("user_detail", kwargs={"pk": self.user.pk})
#         updated_data = {
#             "username": "testUser",
#             "email": "testing@test.com",
#             "password": "password2",
#             "spotify_id": "abcdef",
#             "favorite_genres": "Ska"
#         }
#         response = self.client.put(url, updated_data, format="json")
#         self.user.refresh_from_db()

#         # print(response.data) django's default user model handling the password, this will be updated with Auth anyhow
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(self.user.username, updated_data["username"])
#         self.assertEqual(self.user.email, updated_data["email"])
#         # self.assertTrue(self.user.check_password("password2"))
#         self.assertEqual(self.user.spotify_id, updated_data["spotify_id"])
#         self.assertEqual(self.user.favorite_genres,
#                          updated_data["favorite_genres"])


# class UserDeleteTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # create test users
#         cls.user = User.objects.create(username="testuser1", email="user1@example.com",
#                                        password=make_password("password1"), spotify_id="123", favorite_genres="Rock")

#     def test_delete_user(self):
#         user_count_before_delete = User.objects.count()
#         url = reverse("user_detail", kwargs={"pk": self.user.pk})
#         response = self.client.delete(url)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(User.objects.count(), user_count_before_delete - 1)
#         self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

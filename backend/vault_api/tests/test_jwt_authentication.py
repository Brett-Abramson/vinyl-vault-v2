from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from django.core import mail
from rest_framework import status
import re

User = get_user_model()


class JWTAuthenticationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create a client instance
        cls.client_instance = cls.client_class()

        # register user
        url = reverse("user-list")
        response = cls.client_instance.post(
            url, {"first_name": "John", "last_name": "Doe", "username": "newtestuser", "email": "test@example.com", "password": "testpassword123", "re_password": "testpassword123"}, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert len(mail.outbox) == 1

        # activate user
        activation_email = mail.outbox[0]
        activation_url = re.search(
            r"http://localhost:3000/activation/\S+", activation_email.body).group()
        _, uid, token = activation_url.split("/")[-3:]

        response = cls.client_instance.post(reverse("user-activation"), {
            "uid": uid,
            "token": token
        })

        assert response.status_code == status.HTTP_204_NO_CONTENT

        # log in user and store tokens from cookies
        login_url = reverse("jwt_create")
        login_response = cls.client_instance.post(
            login_url, {"username": "newtestuser", "password": "testpassword123"}, format="json")

        assert login_response.status_code == status.HTTP_200_OK

        cls.access_cookie = login_response.cookies.get("access").value
        cls.refresh_cookie = login_response.cookies.get("refresh").value

        cls.client_instance.cookies["access"] = cls.access_cookie
        cls.client_instance.cookies["refresh"] = cls.refresh_cookie

        # store user for further testing
        cls.user = User.objects.get(email="test@example.com")

    def test_jwt_verify(self):

        url = reverse("jwt_verify")
        response = self.client_instance.post(
            url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jwt_verify_bad_token(self):
        url = reverse("jwt_verify")
        self.client.cookies["access"] = "bad token"
        response = self.client.post(
            url)

        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"],
                         "Token is invalid or expired")

    def test_jwt_refresh(self):
        url = reverse("jwt_refresh")
        response = self.client_instance.post(
            url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertTrue("access" in response.data)
        # print(response.data)

    def test_jwt_refresh_bad_token(self):
        url = reverse("jwt_refresh")
        self.client.cookies["refresh"] = "bad token"
        response = self.client.post(
            url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"],
                         "Token is invalid or expired")

    def test_get_user(self):
        url = reverse("user-me")
        response = self.client_instance.get(
            url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["email"], "test@example.com")

    def test_password_reset(self):
        url = reverse("user-reset-password")
        response = self.client_instance.post(
            url, {"email": "test@example.com"})

        self.assertEqual(len(mail.outbox), 1)

        # extract uid and token from email
        email_body = mail.outbox[0].body
        password_reset_url = re.search(
            r"http://localhost:3000/password-reset/(\S+)/(\S+)", email_body)
        if password_reset_url:
            uid, token = password_reset_url.groups()
        else:
            self.fail("Password reset URL not found in the email body")

        # confirm password reset
        new_password = "newtestpassword123"
        url = reverse("user-reset-password-confirm")
        response = self.client_instance.post(url, {
            "uid": uid, "token": token, "new_password": new_password, "re_new_password": new_password
        })

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # check if user can login with new password
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(new_password))

    def test_user_deletion(self):
        url = reverse("user-me")
        response = self.client_instance.delete(
            url, {"current_password": "testpassword123"})

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="newtestuser")

    def test_update_user(self):
        url = reverse("user-me")
        updated_data = {
            "email": "newTestEmail@example.com",
            # "first_name": "John",
        }
        response = self.client_instance.patch(
            url, updated_data)

        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["email"], "newTestEmail@example.com")
        # self.assertEqual(
        #     self.user.first_name, "John")

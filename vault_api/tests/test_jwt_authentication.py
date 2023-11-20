from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from django.core import mail
from rest_framework import status
import re
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class JWTAuthenticationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create a client instance
        cls.client_instance = cls.client_class()

        # register user
        url = reverse("user-list")
        response = cls.client_instance.post(
            url, {"username": "newtestuser", "email": "test@example.com", "password": "testpassword123", "re_password": "testpassword123"}, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert len(mail.outbox) == 1

        # activate user
        activation_email = mail.outbox[0]
        activation_url = re.search(
            r"http://testserver/activation/\S+", activation_email.body).group()
        _, uid, token = activation_url.split("/")[-3:]

        response = cls.client_instance.post(reverse("user-activation"), {
            "uid": uid,
            "token": token
        })

        assert response.status_code == status.HTTP_204_NO_CONTENT

        # store user for further testing
        cls.user = User.objects.get(email="test@example.com")

        # log in and store token
        login_url = reverse("jwt-create")
        login_response = cls.client_instance.post(
            login_url, {"username": "newtestuser", "password": "testpassword123"}, format="json")

        assert login_response.status_code == status.HTTP_200_OK
        cls.access_token = login_response.data["access"]
        cls.refresh_token = login_response.data["refresh"]

    def test_jwt_verify(self):
        url = reverse("jwt-verify")
        response = self.client.post(
            url, {"token": self.access_token}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jwt_verify_bad_token(self):
        url = reverse("jwt-verify")
        response = self.client.post(
            url,  {"token": self.access_token + "1"}, format="json")

        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"],
                         "Token is invalid or expired")

    def test_jwt_refresh(self):
        url = reverse("jwt-refresh")
        response = self.client.post(
            url, {"refresh": self.refresh_token}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)

    def test_jwt_refresh_bad_token(self):
        url = reverse("jwt-refresh")
        response = self.client.post(
            url, {"refresh": self.refresh_token + "1"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"],
                         "Token is invalid or expired")

    def test_get_user(self):
        url = reverse("user-me")
        response = self.client.get(
            url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["email"], "test@example.com")

    def test_update_user(self):
        url = reverse("user-me")
        updated_data = {
            # "username": "updatedUser",
            "email": "updatedemail@example.com",
            "first_name": "John"
        }

        response = self.client.put(
            url, updated_data, format="json", HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(response.data)

        user = User.objects.get(username="newtestuser")
        self.assertEqual(user.email, "updatedemail@example.com")
        self.assertEqual(user.first_name, "John")

    # def test_access_protected_endpoint_with_token(self):
    #     # obtain JWT token
    #     url = reverse("token_obtain_pair")
    #     response = self.client.post(
    #         url, {"username": "testuser", "password": "testpassword123"}, format="json")
    #     access_token = response.data["access"]

    #     # access the protected endpoint
    #     self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    #     url = reverse("protected")
    #     response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTrue("message" in response.data)
    #     self.assertEqual(
    #         response.data["message"], "This is a protected endpoint accessible only to authenticated users")

    # def test_token_refresh(self):
    #     # obtain refresh token
    #     refresh = RefreshToken.for_user(self.user)

    #     url = reverse("token_refresh")
    #     response = self.client.post(
    #         url, {"refresh": str(refresh)}, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTrue("access" in response.data)

    # def test_token_verify(self):
    #     # obtain token
    #     access = RefreshToken.for_user(self.user).access_token

    #     url = reverse("token_verify")
    #     response = self.client.post(url, {"token": str(access)}, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # # testing with invalid credentials to ensure it doesn't issue a token
    # def test_token_obtain_with_invalid_credentials(self):
    #     url = reverse("token_obtain_pair")
    #     response = self.client.post(
    #         url, {"username": "wrong", "password": "wrong"}, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # # attempting to access a protected API endpoint without a token to ensure it denies access
    # # def test_access_protected_endpoint_without_token(self):
    # #   url = reverse("your_protected_view")
    # #   response = self.client.post(url, {"refresh": "invalidtoken"}, format="json")
    # #   self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # # testing token verify enndpoint with an invalid token
    # def test_token_verify_invalid(self):
    #     url = reverse("token_verify")
    #     response = self.client.post(
    #         url, {"token": "invalidtoken"}, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

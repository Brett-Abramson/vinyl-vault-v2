from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthenticationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword123")

    def test_token_obtain_pair(self):
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url, {"username": "testuser", "password": "testpassword123"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)
        self.assertTrue("refresh" in response.data)

        access_token = response.data["access"]

        # use this token to access protectedendpoint
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    def test_access_protected_endpoint_with_token(self):
        # obtain JWT token
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url, {"username": "testuser", "password": "testpassword123"}, format="json")
        access_token = response.data["access"]

        # access the protected endpoint
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        url = reverse("protected")
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {access_token}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("message" in response.data)
        self.assertEqual(
            response.data["message"], "This is a protected endpoint accessible only to authenticated users")

    def test_token_refresh(self):
        # obtain refresh token
        refresh = RefreshToken.for_user(self.user)

        url = reverse("token_refresh")
        response = self.client.post(
            url, {"refresh": str(refresh)}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)

    def test_token_verify(self):
        # obtain token
        access = RefreshToken.for_user(self.user).access_token

        url = reverse("token_verify")
        response = self.client.post(url, {"token": str(access)}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # testing with invalid credentials to ensure it doesn't issue a token
    def test_token_obtain_with_invalid_credentials(self):
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url, {"username": "wrong", "password": "wrong"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # attempting to access a protected API endpoint without a token to ensure it denies access
    # def test_access_protected_endpoint_without_token(self):
    #   url = reverse("your_protected_view")
    #   response = self.client.post(url, {"refresh": "invalidtoken"}, format="json")
    #   self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # testing token verify enndpoint with an invalid token
    def test_token_verify_invalid(self):
        url = reverse("token_verify")
        response = self.client.post(
            url, {"token": "invalidtoken"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

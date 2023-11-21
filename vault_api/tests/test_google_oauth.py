# from unittest.mock import patch
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status


# class GoogleOAuth2Test(APITestCase):
#   @patch()
#   def test_google_oauth2_authentication(self, mock_google_oauth2):
#     # mock the Google OAuth2 responses
#     mock_google_oauth2.return_value = {
#       "access_token": "fake_access_token",
#       "refresh_token": "fake_refresh_token",
#       "user_infoe": {
#         "email":"test@example.com",
#         "first_name": "Test",
#         "last_name": "User"
#       }
#     }
    
#     # simulate the OAuth2 process
#     response = self.client.post(reverse("provider-auth", kwargs={"provider":"google"}))

#     # assert the user is created and tokens are set in cookies
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     self.assertIn("access", response.cookies)
#     self.assertIn("refresh", response.cookies)
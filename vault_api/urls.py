from django.urls import path
from . import views
from .views import (
  CustomTokenObtainPairView,
  CustomTokenRefreshView,
  CustomTokenVerifyView,
  LogoutView
)
from django.conf.urls import include

urlpatterns = [
    path("jwt/create/", CustomTokenObtainPairView.as_view()),
    path("jwt/refresh/", CustomTokenRefreshView.as_view()),
    path("jwt/verify/", CustomTokenVerifyView.as_view()),
    path("logout/", LogoutView.as_view()),
]

from django.urls import path, re_path
from . import views
from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)
from django.conf.urls import include

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(), name='provider-auth'
    ),
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", CustomTokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", CustomTokenVerifyView.as_view(), name="jwt-verify"),
    path("logout/", LogoutView.as_view()),
    path("api/albums", views.AlbumList.as_view(), name="album_list"),
    path("api/albums/<int:pk>", views.AlbumDetail.as_view(), name="album_detail"),
]

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
    # OAuth2 - (works for Google and Facebook)
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(), name='provider_auth'
    ),
    # JWT Auth
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt_create"), 
    path("jwt/refresh/", CustomTokenRefreshView.as_view(), name="jwt_refresh"), 
    path("jwt/verify/", CustomTokenVerifyView.as_view(), name="jwt_verify"),
    path("logout/", LogoutView.as_view()),
    # Album
    path("albums/", views.AlbumList.as_view(), name="album_list"),
    path("albums/<int:album_id>/", views.AlbumDetail.as_view(), name="album_detail"),
    # Tracks
    path("albums/<int:album_id>/tracks/<int:track_id>", views.TrackDetail.as_view(),name="track_detail"),
    # Comments
    path("albums/<int:album_id>/comments/",
         views.CommentListCreateView.as_view(), name="album_comments"),
    path("albums/<int:album_id>/tracks/<int:track_id>/comments/",
         views.CommentListCreateView.as_view(), name="track_comments"),
    path("comments/<int:comment_id>/",
         views.CommentRetrieveUpdateDestroyAPIView.as_view(), name="comment_detail"),
]

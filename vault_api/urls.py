from django.urls import path
from . import views
from .views import ProtectedView
from django.conf.urls import include

urlpatterns = [
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    # path("api/users", views.UserList.as_view(), name="user_list"),
    # path("api/users/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    # path("api/albums", views.AlbumList.as_view(), name="album_list"),
    # path("api/albums/<int:pk>", views.AlbumDetail.as_view(), name="album_detail"),
    # path("protected/", ProtectedView.as_view(), name="protected")
]

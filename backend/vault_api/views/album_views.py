from django.shortcuts import render
from rest_framework import generics, permissions


from ..serializers import AlbumSerializer
from ..models import Album


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("album_id")
    serializer_class = AlbumSerializer
    lookup_field = "album_id"
    permission_classes = [permissions.AllowAny]


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by("album_id")
    serializer_class = AlbumSerializer
    lookup_field = "album_id"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

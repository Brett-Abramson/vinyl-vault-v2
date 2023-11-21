from django.shortcuts import render
from rest_framework import generics

from ..serializers import AlbumSerializer
from ..models import Album


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer

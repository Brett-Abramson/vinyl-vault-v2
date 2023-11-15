from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, AlbumSerializer, TrackSerializer, CommentSerializer
from .models import User, Album, Track, Comment
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by("id")
    serializer_class = AlbumSerializer



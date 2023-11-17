from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.headers)
        content = {
            "message": "This is a protected endpoint accessible only to authenticated users"}
        return Response(content)

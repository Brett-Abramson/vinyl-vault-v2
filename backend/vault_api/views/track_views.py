from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..serializers import TrackSerializer
from ..models import Track


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Track.objects.all().order_by("track_id")
  serializer_class = TrackSerializer
  permission_classes = [IsAuthenticated]
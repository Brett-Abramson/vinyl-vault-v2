from django.shortcuts import render
from rest_framework import generics, permissions


from ..serializers import TrackSerializer
from ..models import Track


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all().order_by("track_id")
    serializer_class = TrackSerializer
    lookup_field = "track_id"
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import generics, permissions
from ..models import Comment
from ..serializers import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "comment_id"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "comment_id"
    permission_classes = [permissions.IsAuthenticated]

    # queryset so a user can only control their own comment
    # def get_queryset(self):
    #   user = self.request.user
    #   return user.comments.all()

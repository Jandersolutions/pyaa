from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from .models import Comment, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    """API view to list all posts or create a new one."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Set the author of the post to the current user."""
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a single post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = "slug"


class CommentListCreateAPIView(ListCreateAPIView):
    """API view to list and create comments for a post."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Return a list of all approved comments for a post."""
        post = get_object_or_404(Post, slug=self.kwargs["slug"])
        return Comment.objects.filter(post=post, is_approved=True)

    def perform_create(self, serializer):
        """Set the author and post of the comment."""
        post = get_object_or_404(Post, slug=self.kwargs["slug"])
        serializer.save(author=self.request.user, post=post)


class CommentApproveAPIView(UpdateAPIView):
    """API view to approve a comment."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        """Approve the comment."""
        instance = self.get_object()
        instance.is_approved = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentDeleteAPIView(DestroyAPIView):
    """API view to delete a comment."""

    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]

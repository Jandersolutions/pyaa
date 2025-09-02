from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer


class PostListAPIView(ListAPIView):
    """API view to list all posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostRetrieveAPIView(RetrieveAPIView):
    """API view to retrieve a single post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

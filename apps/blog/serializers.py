from rest_framework import serializers

from .models import Category, Comment, Post, Product, Tag


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "content", "created_at")
        read_only_fields = ("author",)


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    author = serializers.StringRelatedField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "content",
            "author",
            "category",
            "tags",
            "products",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("author",)

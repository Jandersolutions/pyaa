from rest_framework import serializers

from .models import Category, Post, Product, Tag


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

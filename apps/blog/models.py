from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from meta.models import ModelMeta

from apps.shop.models import Product


class Category(models.Model):
    """A model for blog post categories."""

    name = models.CharField(
        _("name"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    """A model for blog post tags."""

    name = models.CharField(
        _("name"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(ModelMeta, models.Model):
    """A model for blog posts."""

    title = models.CharField(
        _("title"),
        max_length=255,
    )
    slug = models.SlugField(
        _("slug"),
        max_length=255,
        unique=True,
    )
    content = models.TextField(
        _("content"),
    )
    description = models.TextField(
        _("description"),
        blank=True,
        null=True,
        help_text=_("A short description for SEO."),
    )
    author = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("author"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name=_("category"),
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
        verbose_name=_("tags"),
        blank=True,
    )
    products = models.ManyToManyField(
        Product,
        related_name="posts",
        verbose_name=_("products"),
        blank=True,
    )
    is_published = models.BooleanField(
        _("is published"),
        default=False,
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ["-created_at"]

    _metadata = {
        "title": "title",
        "description": "description",
        "keywords": "get_tags",
        "url": "get_absolute_url",
        "image": "get_image_url",
        "schemaorg_type": "Article",
        "schemaorg_properties": {
            "name": "title",
            "description": "description",
            "author": "get_author_name",
            "date_published": "created_at",
            "date_modified": "updated_at",
        },
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("web:blog_detail", kwargs={"slug": self.slug})

    def get_tags(self):
        return [tag.name for tag in self.tags.all()]

    def get_image_url(self):
        # Placeholder for post image
        return ""

    def get_author_name(self):
        return self.author.get_full_name()


class Comment(models.Model):
    """A model for blog post comments."""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("post"),
    )
    author = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("author"),
    )
    content = models.TextField(
        _("content"),
    )
    is_approved = models.BooleanField(
        _("is approved"),
        default=False,
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

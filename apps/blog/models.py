from django.db import models
from django.utils.translation import gettext_lazy as _


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


class Post(models.Model):
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

    def __str__(self):
        return self.title

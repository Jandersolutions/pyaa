from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.blog.models import Category, Post


class BlogAPITest(APITestCase):
    """Test suite for the blog API."""

    def setUp(self):
        """Set up the test case."""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password",
        )
        self.category = Category.objects.create(name="Tech", slug="tech")
        self.post1 = Post.objects.create(
            title="Post 1",
            slug="post-1",
            content="Content 1",
            author=self.user,
            category=self.category,
        )
        self.post2 = Post.objects.create(
            title="Post 2",
            slug="post-2",
            content="Content 2",
            author=self.user,
            category=self.category,
        )

    def test_list_posts(self):
        """Test that the API can list posts."""
        url = reverse("blog:post-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["results"][0]["title"], self.post2.title)
        self.assertEqual(response.data["results"][1]["title"], self.post1.title)

    def test_retrieve_post(self):
        """Test that the API can retrieve a single post."""
        url = reverse("blog:post-detail", kwargs={"slug": self.post1.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.post1.title)
        self.assertEqual(response.data["slug"], self.post1.slug)

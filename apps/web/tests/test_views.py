from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.blog.models import Post


class BlogViewTest(TestCase):
    """Test suite for the blog views."""

    def setUp(self):
        """Set up the test case."""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password",
        )
        self.post = Post.objects.create(
            title="My First Blog Post",
            slug="my-first-blog-post",
            content="<p>This is the content.</p>",
            description="A short description.",
            author=self.user,
        )

    def test_blog_detail_view(self):
        """Test the blog detail view."""
        url = reverse("web:blog_detail", kwargs={"slug": self.post.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)
        self.assertContains(
            response, f'<meta name="description" content="{self.post.description}">'
        )
        self.assertContains(
            response, f'<meta property="og:title" content="{self.post.title}">'
        )

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.blog.models import Category, Comment, Post, Tag
from apps.shop.models import Product


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
        self.tag = Tag.objects.create(name="Python", slug="python")
        self.product = Product.objects.create(
            name="Test Product", price=10.00, currency="USD"
        )
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
        self.post1.products.add(self.product)
        url = reverse("blog:post-detail", kwargs={"slug": self.post1.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.post1.title)
        self.assertEqual(response.data["slug"], self.post1.slug)
        self.assertIn(self.product.id, response.data["products"])

    def test_create_post(self):
        """Test that the API can create a post."""
        self.client.force_authenticate(user=self.user)
        url = reverse("blog:post-list")
        self.tag2 = Tag.objects.create(name="Testing", slug="testing")
        data = {
            "title": "New Post",
            "slug": "new-post",
            "content": "Some content.",
            "category": self.category.id,
            "tags": [self.tag.id, self.tag2.id],
            "products": [self.product.id],
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 3)
        self.assertEqual(response.data["title"], "New Post")
        self.assertIn(self.product.id, response.data["products"])

    def test_update_post(self):
        """Test that the API can update a post."""
        self.client.force_authenticate(user=self.user)
        url = reverse("blog:post-detail", kwargs={"slug": self.post1.slug})
        data = {"title": "Updated Title", "content": "Updated content."}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.title, "Updated Title")

    def test_unauthorized_user_cannot_update_post(self):
        """Test that an unauthorized user cannot update a post."""
        other_user = get_user_model().objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="password",
        )
        self.client.force_authenticate(user=other_user)
        url = reverse("blog:post-detail", kwargs={"slug": self.post1.slug})
        data = {"title": "Updated Title"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post(self):
        """Test that the API can delete a post."""
        self.client.force_authenticate(user=self.user)
        url = reverse("blog:post-detail", kwargs={"slug": self.post1.slug})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)

    def test_unauthorized_user_cannot_delete_post(self):
        """Test that an unauthorized user cannot delete a post."""
        other_user = get_user_model().objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="password",
        )
        self.client.force_authenticate(user=other_user)
        url = reverse("blog:post-detail", kwargs={"slug": self.post1.slug})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentAPITest(APITestCase):
    """Test suite for the comment API."""

    def setUp(self):
        """Set up the test case."""
        self.user = get_user_model().objects.create_user(
            username="commenter",
            email="commenter@example.com",
            password="password",
        )
        self.post_author = get_user_model().objects.create_user(
            username="postauthor",
            email="author@example.com",
            password="password",
        )
        self.post = Post.objects.create(
            title="Post for Comments",
            slug="post-for-comments",
            author=self.post_author,
        )

    def test_create_comment(self):
        """Test that the API can create a comment."""
        self.client.force_authenticate(user=self.user)
        url = reverse("blog:comment-list-create", kwargs={"slug": self.post.slug})
        data = {"content": "This is a new comment."}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.post.comments.count(), 1)
        comment = self.post.comments.first()
        self.assertEqual(comment.author, self.user)
        self.assertFalse(comment.is_approved)

    def test_list_comments(self):
        """Test that the API can list approved comments for a post."""
        Comment.objects.create(
            post=self.post, author=self.user, content="Approved comment.", is_approved=True
        )
        Comment.objects.create(
            post=self.post, author=self.user, content="Unapproved comment."
        )
        url = reverse("blog:comment-list-create", kwargs={"slug": self.post.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["content"], "Approved comment.")

    def test_admin_can_approve_comment(self):
        """Test that an admin can approve a comment."""
        admin_user = get_user_model().objects.create_superuser(
            username="adminuser", email="admin@example.com", password="password"
        )
        comment = Comment.objects.create(
            post=self.post, author=self.user, content="Awaiting approval."
        )
        self.client.force_authenticate(user=admin_user)
        url = reverse("blog_admin:comment-approve", kwargs={"pk": comment.pk})
        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()
        self.assertTrue(comment.is_approved)

    def test_non_admin_cannot_approve_comment(self):
        """Test that a non-admin user cannot approve a comment."""
        comment = Comment.objects.create(
            post=self.post, author=self.user, content="Awaiting approval."
        )
        self.client.force_authenticate(user=self.user)
        url = reverse("blog_admin:comment-approve", kwargs={"pk": comment.pk})
        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_comment(self):
        """Test that an admin can delete a comment."""
        admin_user = get_user_model().objects.create_superuser(
            username="adminuser", email="admin@example.com", password="password"
        )
        comment = Comment.objects.create(
            post=self.post, author=self.user, content="A comment to delete."
        )
        self.client.force_authenticate(user=admin_user)
        url = reverse("blog_admin:comment-delete", kwargs={"pk": comment.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)

    def test_non_admin_cannot_delete_comment(self):
        """Test that a non-admin user cannot delete a comment."""
        comment = Comment.objects.create(
            post=self.post, author=self.user, content="A comment to delete."
        )
        self.client.force_authenticate(user=self.user)
        url = reverse("blog_admin:comment-delete", kwargs={"pk": comment.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.blog.models import Category, Comment, Post, Tag
from apps.shop.models import Product


class CategoryModelTest(TestCase):
    """Test suite for the Category model."""

    def test_can_create_category(self):
        """Test that a Category can be created with a name and slug."""
        category = Category.objects.create(name="Tech", slug="tech")
        self.assertEqual(category.name, "Tech")
        self.assertEqual(category.slug, "tech")
        self.assertEqual(str(category), "Tech")


class TagModelTest(TestCase):
    """Test suite for the Tag model."""

    def test_can_create_tag(self):
        """Test that a Tag can be created with a name and slug."""
        tag = Tag.objects.create(name="Django", slug="django")
        self.assertEqual(tag.name, "Django")
        self.assertEqual(tag.slug, "django")
        self.assertEqual(str(tag), "Django")


class PostModelTest(TestCase):
    """Test suite for the Post model."""

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
            name="Test Product",
            price=10.00,
            currency="USD",
        )

    def test_can_create_post(self):
        """Test that a Post can be created."""
        post = Post.objects.create(
            title="My First Post",
            slug="my-first-post",
            content="This is the content of my first post.",
            author=self.user,
            category=self.category,
        )
        post.tags.add(self.tag)

        self.assertEqual(post.title, "My First Post")
        self.assertEqual(post.slug, "my-first-post")
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.category, self.category)
        self.assertIn(self.tag, post.tags.all())
        self.assertEqual(str(post), "My First Post")

    def test_post_can_have_products(self):
        """Test that a Post can be associated with products."""
        post = Post.objects.create(
            title="Post with Product",
            slug="post-with-product",
            author=self.user,
        )
        post.products.add(self.product)
        self.assertIn(self.product, post.products.all())


class CommentModelTest(TestCase):
    """Test suite for the Comment model."""

    def setUp(self):
        """Set up the test case."""
        self.user = get_user_model().objects.create_user(
            username="commenter",
            email="commenter@example.com",
            password="password",
        )
        self.post = Post.objects.create(
            title="Post for Comments",
            slug="post-for-comments",
            author=self.user,
        )

    def test_can_create_comment(self):
        """Test that a Comment can be created."""
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="This is a test comment.",
        )
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, "This is a test comment.")
        self.assertFalse(comment.is_approved)
        self.assertIsNotNone(comment.created_at)

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category
import jdatetime

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        # ایجاد یک کاربر برای تست
        self.user = User.objects.create_user(username='testuser', password='12345')
        # ایجاد یک دسته‌بندی برای تست
        self.category = Category.objects.create(name='Test Category')
        # ایجاد یک پست برای تست
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user,
            published_date="2023-07-25"
        )
        self.post.category.add(self.category)

    def test_post_creation(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.content, "This is a test post.")
        self.assertEqual(post.author.username, "testuser")
        self.assertEqual(post.category.first().name, "Test Category")

    def test_shamsi_publish_date(self):
        post = Post.objects.get(title="Test Post")
        shamsi_date = post.shamsi_publish_date()
        self.assertEqual(shamsi_date.year, 1402)  # سال شمسی معادل 2023

    def test_persian_published_date(self):
        post = Post.objects.get(title="Test Post")
        persian_month = post.persian_published_date()
        self.assertEqual(persian_month, "تیر")  # ماه شمسی معادل جولای

    def test_post_str_method(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(str(post), f'{post.id} - Test Post')

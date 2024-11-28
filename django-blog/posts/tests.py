from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post

# Create your tests here.


class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        testUser1 = User.objects.create_user(
            username="testuser",
            password="testuser",
        )

        testUser1.save()

        test_post = Post.objects.create(
            author=testUser1,
            title="Blog title",
            body="Body content",
        )

        test_post.save()

    def test_block_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "testuser")
        self.assertEqual(title, "Blog title")
        self.assertEqual(body, "Body content")

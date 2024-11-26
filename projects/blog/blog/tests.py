from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .views import Post

# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username= 'testuser',
            email= "test@gmail.com",
            password= "test@test",
        )

        self.post = Post.objects.create(
            title = "A test title",
            body = "A test body",
            author = self.user,
        )

    def test_string_represenation(self):
        post = Post(title='A test title')
        self.assertEqual(str(post), post.title)
        
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/post/1")

    def tes_post_content(self):
        self.assertEqual(f"{self.post.title}", "A test title")
        self.assertEqual(f"{self.post.body}", "A test body")
        self.assertEqual(f"{self.post.author}", "testuser")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A test body")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1")
        no_response = self.client.get("/post/1000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A test title")
        self.assertTemplateUsed(response, "post_detail.html")
    

    def test_post_create_view(self):
        response = self.client.post(reverse("post_new"), {
            'title': "New title",
            'body': "New text",
            'author': self.user.id,
        },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")

        self.assertEqual(Post.objects.last().body, "New text")


    def test_post_update_view(self):
        response = self.client.post(reverse("post_edit", args='1'), {
            "title": "Updated title",
            "body": "Updated body"
        })
        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args="1"))
        self.assertEqual(response.status_code, 302)






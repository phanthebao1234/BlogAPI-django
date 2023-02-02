from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testusername",
            email = "testemail@gmail.com",
            password = "password"
        )
        
        cls.post = Post.objects.create(
          title = "This is title",
          body = "Hello world!",
          author = cls.user  
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testusername")
        self.assertEqual(self.post.title, "This is title")
        self.assertEqual(self.post.body, "Hello world!")
        self.assertEqual(str(self.post), "This is title")
from django.test import TestCase, client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.
# client work as web browser
# get_user_model is reference to our active user
class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email    = 'test123@gmail.com',
            password =  'secret',
        )

        self.post = Post.objects.create(
            title = 'A good title',
            author = self.user,
            body  = 'This is my content',
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'This is my content')
        self.assertEqual(f'{self.post.author}', 'testuser')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home-page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is my content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'Blog_detail.html')
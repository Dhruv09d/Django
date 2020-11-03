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

    def test_string_representation(self): #test 1
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self): #test 2
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'This is my content')
        self.assertEqual(f'{self.post.author}', 'testuser')
    
    def test_post_list_view(self): #test 3
        response = self.client.get(reverse('home-page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is my content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self): #test 4
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'Blog_detail.html')

    def test_post_create_view(self): #test 5
        response = self.client.post(reverse('post-new'), {
                                'title': 'New title',
                                'body': 'New text',
                                'author': self.user,
                            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self): #test 6
        response = self.client.post(reverse('post-update', args='1'), {
                                            'title': 'Updated title',
                                            'body': 'Updated text',
                                            })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self): #test 7
        response = self.client.get(
        reverse('post-delete', args='1'))
        self.assertEqual(response.status_code, 200)


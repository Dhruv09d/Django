from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='It is just simple test')
    
    def test_text_content(self):   # test 1
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'It is just simple test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='second test')
    
    def test_view_url_exist_at_proper_location(self): # test 2
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url_by_name(self):                        # test 3
        resp = self.client.get(reverse('home-view'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):          # test 4
        resp = self.client.get(reverse('home-view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

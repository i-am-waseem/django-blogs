from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Blog


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@email.com',
            password = 'secret'
            )
        
        self.blog = Blog.objects.create(
            title = 'Test title',
            body = 'Nice test body',
            author = self.user
        )
    def test_string_representation(self):
        blog = Blog(title='A sample title')
        self.assertEqual(str(blog), blog.title)

    def test_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/blog/1/')


    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'Test title')
        self.assertEqual(f'{self.blog.body}', 'Nice test body')
        self.assertEqual(f'{self.blog.author}','test' )

    def test_blog_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice test body')
        self.assertTemplateUsed(response, 'home.html')

    def test_blog_detail_view(self):
        response = self.client.get('/blog/1', follow=True)
        no_response = self.client.get('/blog/1313', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Nice test body')
        self.assertTemplateUsed(response, 'blog_detail.html')

    def test_blog_create_view(self):
        response = self.client.post(reverse('new_blog'),{
            'title' : 'New title',
            'body' : 'New Body',
            'author' : self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response,'New Body')

    def test_blog_update_view(self):
        response = self.client.post(reverse('update_blog', args='1'), {
            "title": "Updated Title",
            'body' : 'Updated Body'
        })
        self.assertEqual(response.status_code, 302)

    def test_blog_delete_view(self):
        response = self.client.get(reverse('blog_delete', args='1'))
        self.assertEqual(response.status_code, 200)
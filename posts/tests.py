from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostTests(TestCase):
    
    @classmethod
    def setUp(self):
        user1 = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='1234test4321'
        )
        post1 = Post.objects.create(
            author=user1,
            title='test title',
            body='test post body',
        )

        post1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.author}', 'testuser')
        self.assertEqual(f'{post.title}', 'test title')
        self.assertEqual(f'{post.body}', 'test post body')
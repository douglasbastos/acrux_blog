#coding: utf-8
from django.test import TestCase

from django.contrib.auth.models import User
from ...views import Post, Tag, Base

class BaseTest(TestCase, Base):

    @classmethod
    def setUpClass(cls):
        cls.author1 = User.objects.create(username='Author 1')
        cls.author2 = User.objects.create(username='Author 2')
        cls.tag = Tag.objects.create(name='Esportes')
        cls.post = Post.objects.create(title='Um titulo teste', subtitled='Um subtitulo', slug='um-titulo-teste', content='Lorem Ipsum', tag_id=cls.tag.pk, author_id=cls.author1.pk)

    @classmethod
    def tearDownClass(cls):
        cls.post.delete()
        cls.tag.delete()
        cls.author2.delete()
        cls.author1.delete()

    def test_authors_with_post(self):
        self.assertEqual(self.authors_with_post.count(), 1)

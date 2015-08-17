#coding: utf-8
from django.test import TestCase, Client

from django.contrib.auth.models import User
from ...models.models import Post, Tag

class PostTest(TestCase):

    def setUp(self):
        self.tag1 = Tag.objects.create(name='Esportes')
        self.tag2 = Tag.objects.create(name='Cinema')
        self.author1 = User.objects.create(username='author')
        self.post1 = Post.objects.create(title='Um titulo teste', subtitled='Um subtitulo', slug='um-titulo-teste', content='Lorem Ipsum', tag_id=self.tag1.pk, author_id=self.author1.pk)
        self.c = Client()

    def tearDown(self):
        self.post1.delete()
        self.author1.delete()
        self.tag2.delete()
        self.tag1.delete()

    def test_post_por_slug(self):
        response = self.c.get('/um-titulo-teste/')
        self.assertEqual(response.status_code, 200)

    def test_post_sem_barra(self):
        response = self.c.get('/um-titulo-teste')
        self.assertEqual(response.status_code, 301)

    def test_slug_nao_existe(self):
        response = self.c.get('/um-titulo/')
        self.assertEqual(response.status_code, 404)

    def test_get_tags(self):
        response = self.c.get('/um-titulo-teste/')
        tags = response.context['tags'].values()
        self.assertEqual(tags[0]['name'], u'Esportes')

    def test_count_tags(self):
        response = self.c.get('/um-titulo-teste/')
        tags = response.context['tags'].values()        
        self.assertEqual(tags.count(), 2)

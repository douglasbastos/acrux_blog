#coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView

from simple_blog.models.qs_redis import Post, Tag, Author

class Base(TemplateView):

    @property
    def tags(self):
        return Tag.all()

    def authors(self):
        return Author.all()

    @property
    def authors_with_post(self):
        '''Retorna uma lista com todos os usuários que realizaram pelo menos um post no blog'''
        authors_with_post = []
        authors = Author.all()
        for username in authors:
            last_name = Author.last_name(username) if Author.last_name(username) else ''
            first_name = Author.first_name(username) if Author.first_name(username) else ''
            authors_with_post.append({'last_name': last_name, 'first_name': first_name, 'username': username})
        return authors_with_post

class ListPosts(Base):
    template_name = 'simple_blog/home.html'

    def aaa(self, request, *args, **kwargs):
        context['tags'] = self.tags
        return render(request, template, context)

    def get_queryset(self):
        return Post.objects.order_by('-date_publication')

    def get_context_data(self, **kwargs):
        context = super(ListPosts, self).get_context_data(**kwargs)
        context['tags'] = self.tags
        context['authors'] = self.authors_with_post
        return context


class DetailPost(Base):
    template_name = 'simple_blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        self.slug = kwargs['slug']
        context['tags'] = self.tags
        context['authors'] = self.authors_with_post
        context['post'] = self.get_context_post()
        return context


    def get_context_post(self):
        post = {}
        post['slug'] = self.slug
        post['title'] = Post.title(self.slug)
        post['subtitled'] = Post.subtitled(self.slug)
        post['content'] = Post.content(self.slug)
        post['date_publication'] = Post.date_publication(self.slug)
        post['date_edition'] = Post.date_edition(self.slug)
        post['tag'] = Post.tag(self.slug)
        post['author'] = Post.author(self.slug)
        return post

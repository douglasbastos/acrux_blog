# coding: utf-8

from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Post, Tag


class Base:

    @property
    def tags(self):
        return Tag.objects.all()

    @property
    def authors_with_post(self):
        posts = Post.objects.select_related('author').all()
        authors_unique_id = set([post.author.pk for post in posts])
        authors_id = []
        for i in xrange(len(authors_unique_id)):
            authors_id.append(authors_unique_id.pop())
        return User.objects.filter(pk__in=authors_id)


class ListPosts(ListView, Base):
    model = Post
    template_name = 'acrux_blog/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-date_publication')

    def get_context_data(self, **kwargs):
        context = super(ListPosts, self).get_context_data(**kwargs)
        context['tags'] = self.tags
        context['authors'] = self.authors_with_post
        return context


class ListPostsAuthor(ListPosts):

    def get_queryset(self, **kwargs):
        author = User.objects.get(username=self.kwargs['author'])
        return Post.objects.filter(author_id=author.id).order_by('-date_publication')


class ListPostsTag(ListPosts):

    def get_queryset(self):
        tag = Tag.objects.get(slug=self.kwargs['tag'])
        return Post.objects.filter(tag_id=tag.id).order_by('-date_publication')


class DetailPost(DetailView, Base):
    model = Post
    template_name = 'acrux_blog/post.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context['tags'] = self.tags
        context['tags_related'] = Post.objects.filter(tag_id=context['post'].tag_id)\
            .exclude(slug=self.kwargs['slug'])[::-1][:5]
        context['authors'] = self.authors_with_post
        return context

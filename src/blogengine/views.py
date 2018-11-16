from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
# for code markdown
#from django.utils.encoding import force_str
#from django.utils.safestring import mark_safe
#import markdown2

from django.contrib.syndication.views import Feed

from blogengine.models import Post, Category, Tag
from blogengine.forms import PostCreateForm

from django.utils import timezone
# Create your views here.

class PostCreateView(View):
    form_class = PostCreateForm
    template_name = 'post_create.html'
    success_url = '/success/'
    initial = {
        'pub_date': timezone.now(),
        }
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            instance=form.save(commit=False)
            instance.save()
            # return HttpResponseRedirect( self.success_url )
            return HttpResponse ("Success")
        return render(request, self.template_name, {'form': form})    #

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class DetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostsFeed(Feed):
    title = "ionescu77.com RSS feed - posts"
    link = "blog/feeds/posts/"
    description = "ionescu77.com RSS feed - blog posts"
    def items(self):
        return Post.objects.order_by('-pub_date')
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.text

class CategoryListView(ListView):
    template_name = 'category_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()                     # returns "No posts found"
    def get_context_data(self, **kwargs):       # see Github #41
        slug = self.kwargs['slug']
        context = super(CategoryListView, self).get_context_data(**kwargs) # get the default context data
        context['category_name'] = slug
        return context

class TagListView(ListView):
    template_name = 'tag_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()
    def get_context_data(self, **kwargs):       # see Github #41
        slug = self.kwargs['slug']
        context = super(TagListView, self).get_context_data(**kwargs) # get the default context data
        context['tag_name'] = slug
        return context

from django.conf.urls import include, url
from blogengine.models import Post, Category, Tag
from blogengine.views import PostCreateView, PostListView, DetailView, CategoryListView, TagListView, PostsFeed

from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    # Blog Create Post Form
    url(r'^create/$',
        login_required(PostCreateView.as_view()),
        name = 'create_post'    # added login_required but need settings.LOGIN_URL for user friendlines
     ),

    # Index Blog - Posts List
    url(r'^(?P<page>\d+)?/?$',
     PostListView.as_view(
        paginate_by=7
        ), name = 'post_list'),       # Generic ListView

    # Individual posts - Post Detail
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
     DetailView.as_view()),

    # Categories - Posts List by Category
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/(?P<page>\d+)?/?$',
     CategoryListView.as_view(
        paginate_by=5,
        model=Category,
        ), name = 'category_list'),

    # Tags - Posts List by Tag
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/(?P<page>\d+)?/?$',
     TagListView.as_view(
        paginate_by=5,
        model=Tag,
        ), name = 'tag_list'),

    # Posts RSS feed
    url(r'^feeds/posts/$', PostsFeed()),

]

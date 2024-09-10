from django.urls import path, include, re_path

from blogengine.models import Post, Category, Tag
from blogengine.views import (
    PostCreateView,
    PostListView,
    DetailView,
    CategoryListView,
    TagListView,
    PostsFeed,
)

from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # Blog Create Post Form
    path(
        "create/",
        login_required(PostCreateView.as_view()),
        name="create_post",  # added login_required but need settings.LOGIN_URL for user friendlines
    ),
    # Index Blog - Posts List
    re_path(
        r"^(?P<page>\d+)?/?$", PostListView.as_view(paginate_by=7), name="post_list"
    ),  # Generic ListView
    # Individual posts - Post Detail
    re_path(
        r"^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$",
        DetailView.as_view(),
    ),
    # Categories - Posts List by Category
    path(
        r"category/<slug:slug>/",
        CategoryListView.as_view(
            paginate_by=5,
            model=Category,
        ),
        name="category_list",
    ),
    # Categories - Posts List by Category by page
    path(
        r"category/<slug:slug>/<int:page>/",
        CategoryListView.as_view(
            paginate_by=5,
            model=Category,
        ),
        name="category_list",
    ),
    # Tags - Posts List by Tag
    path(
        "tag/<slug:slug>/",
        TagListView.as_view(
            paginate_by=5,
            model=Tag,
        ),
        name="tag_list",
    ),
    # Tags - Posts List by Tag by page
    path(
        "tag/<slug:slug>/<int:page>/",
        TagListView.as_view(
            paginate_by=5,
            model=Tag,
        ),
        name="tag_list",
    ),
    # Posts RSS feed
    path("feeds/posts/", PostsFeed()),
]

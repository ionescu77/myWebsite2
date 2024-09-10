from django.urls import path, include

from django.views.generic import TemplateView

# from landing.views import PostListView, DetailView

urlpatterns = [
    # Index Landing
    path("", TemplateView.as_view(template_name="landing.html"), name="landing"),
]

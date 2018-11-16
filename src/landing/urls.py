from django.conf.urls import include, url

from django.views.generic import TemplateView

#from landing.views import PostListView, DetailView

urlpatterns = [
    # Index Landing
    url(r'', TemplateView.as_view(template_name='landing.html'), name='landing'),
]

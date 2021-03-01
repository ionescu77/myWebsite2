from django.urls import path, include, re_path

from django.contrib import admin
from django.views.generic.base import RedirectView

from django.contrib.flatpages import views

from django.contrib.sitemaps.views import sitemap
from blogengine.sitemap import PostSitemap, FlatpageSitemap

from accounts.views import (login_view, register_view, logout_view)

# from axes.decorators import axes_dispatch

sitemaps = {
    'posts': PostSitemap,
    'pages': FlatpageSitemap
}

admin.autodiscover()

urlpatterns = [
    path('administrare/', admin.site.urls),

    # Blogengine URLs
    path('blog/', include('blogengine.urls')),

    # Landing page URLs
    path('', include('landing.urls')),

    # Accounts page URLs
    #url(r'^$', include('accounts.urls', namespace='accounts')),
    # Accounts login page URLs
    #    url(r'^mylogin/$', axes_dispatch(login_view), name="mylogin"),
    # path(r'^mylogin/$', axes_dispatch(login_view), name="mylogin"),
    path('mylogin/', login_view, name="mylogin"),

    # Accounts logout page URLs
    path('mylogout/', logout_view, name="mylogout"),


    # Create sitemaps.xml
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # FlatPage URLs
    # path(r'^$', include('django.contrib.flatpages.urls')), # this or catchall does not really work
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),


]

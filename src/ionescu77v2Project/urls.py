from django.conf.urls import include, url
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
    url(r'^administrare/', include('admin.site.urls')),

    # Blogengine URLs
    url(r'^blog/', include('blogengine.urls')),

    # Landing page URLs
    url(r'^$', include('landing.urls', namespace='landing')),

    # Accounts page URLs
    #url(r'^$', include('accounts.urls', namespace='accounts')),
    # Accounts login page URLs
#    url(r'^mylogin/$', axes_dispatch(login_view), name="mylogin"),
    url(r'^mylogin/$', login_view, name="mylogin"),

    # Accounts logout page URLs
    url(r'^mylogout/$', logout_view, name="mylogout"),


    # Create sitemaps.xml
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # FlatPage URLs
    # url(r'^$', include('django.contrib.flatpages.urls')), # this or catchall does not really work
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),


]

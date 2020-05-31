import os
from .base import *

SECRET_KEY=os.environ['SECRET_KEY_RAZ']

DEBUG = True
# TEMPLATE_DEBUG = True # Deprecated see below TEMPLATES:
DISQUS = False

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += (
    'landing',
    'blogengine',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.syndication',
    'django.contrib.sitemaps',
    'crispy_forms',
    'axes',
)

SITE_ID = 1

#TEST_DATABASE_CHARSET=UTF8
#CHARSET=UTF8 # supported for PG and MySQL only

# ///////
# ------- django-axes: CACHES enabled, 20181119
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'axes_cache': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# ------- #

INSTALLED_APPS += ('django_jenkins',)
JENKINS_TASKS = ()

PROJECT_APPS = ['blogengine']

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# ///////
# ------- django-axes: Settings for this:
AXES_CACHE = 'axes_cache'
AXES_VERBOSE = True
AXES_LOCKOUT_TEMPLATE = 'lockout.html'
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# ------- #

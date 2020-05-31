import os
from .base import *

if 'TRAVIS' in os.environ:
    SECRET_KEY=os.environ['SECRET_KEY_RAZ']

    INSTALLED_APPS += ('django_jenkins',)

    JENKINS_TASKS = (
        'django_jenkins.tasks.run_pylint',
        'django_jenkins.tasks.with_coverage',
        )

    PROJECT_APPS = ['blogengine']
else:
    SECRET_KEY=os.environ['SECRET_KEY_IONESCU77']


# Setup Database
from .database_production import DATABASES
DATABASES = DATABASES

DEBUG = False
# TEMPLATE_DEBUG = True # Deprecated see below TEMPLATES:
DISQUS = True

ALLOWED_HOSTS = ['ionescu77.com','www.ionescu77.com','staging.ionescu77.com']

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

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AXES_VERBOSE = False

AXES_LOCKOUT_TEMPLATE = 'lockout.html'

# ///////
# ------- django-axes: CACHES enabled, 20181119
# ------- django-axes: CACHES enabled, 20200531
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'axes_cache': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# ------- #

# ///////
# ------- django-axes: Settings for this:
AXES_CACHE = 'axes_cache'
AXES_VERBOSE = False
AXES_LOCKOUT_TEMPLATE = 'lockout.html'
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# ------- #

import os
from .base import *

SECRET_KEY=os.environ['SECRET_KEY_RAZ']

DEBUG = True
TEMPLATE_DEBUG = True
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

INSTALLED_APPS += ('django_jenkins',)

JENKINS_TASKS = ()

PROJECT_APPS = ['blogengine']

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AXES_VERBOSE = False

AXES_LOCKOUT_TEMPLATE = 'lockout.html'

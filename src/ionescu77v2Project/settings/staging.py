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
    SECRET_KEY=os.environ['SECRET_KEY_IONESCU77_DEV']


# Setup Database
from .database_staging import DATABASES
DATABASES = DATABASES

DEBUG = False
TEMPLATE_DEBUG = False
DISQUS = False

ALLOWED_HOSTS = ['ionescu77.staging.avproiect.com']

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

STATIC_ROOT = '/home/ionescu77/webapps/apollo7/ionescu77/static/'
MEDIA_ROOT = '/home/ionescu77/webapps/apollo7/ionescu77/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AXES_VERBOSE = False

AXES_LOCKOUT_TEMPLATE = 'lockout.html'

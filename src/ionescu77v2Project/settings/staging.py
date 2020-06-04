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
# TEMPLATE_DEBUG = True # Deprecated see below TEMPLATES:
DISQUS = False

ALLOWED_HOSTS = ['ionescu77.staging.avproiect.com']

SITE_ID = 1

#TEST_DATABASE_CHARSET=UTF8
#CHARSET=UTF8 # supported for PG and MySQL only

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# ///////
# ------- django-axes: Settings for this:
AXES_VERBOSE = True
# ------- #

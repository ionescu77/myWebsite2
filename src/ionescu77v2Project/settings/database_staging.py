"""A basic database set-up for Travis CI.
The set-up uses the 'TRAVIS' (== True) environment variable on Travis
to detect the session, and changes the default database accordingly.
Be mindful of where you place this code, as you may accidentally
assign the default database to another configuration later in your code.
"""

import os

# (...)

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travisci',
            'USER': 'postgres',
#            'PASSWORD': '',
            'HOST':     'localhost',
#            'PORT':     '',
        }
    }

else:
# Database on staging:
# Data is passed from ENV Variables or from activate
    DB_NAME_IONESCU77=os.environ['DB_NAME_IONESCU77_DEV']
    DB_USER_IONESCU77=os.environ['DB_USER_IONESCU77_DEV']
    DB_PASS_IONESCU77=os.environ['DB_PASS_IONESCU77_DEV']
    DB_PORT_IONESCU77=os.environ['DB_PORT_IONESCU77_DEV']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME_IONESCU77,
            'USER': DB_USER_IONESCU77,
            'PASSWORD': DB_PASS_IONESCU77,
            'HOST': '127.0.0.1',
            'PORT': DB_PORT_IONESCU77,
        }
    }

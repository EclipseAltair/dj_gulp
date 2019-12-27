# -*- coding: utf-8 -*-
from .settings import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'set_fullstack',
        'USER': 'postgres',
        'PASSWORD': 'Guido!956',
        'HOST': 'localhost',
        'PORT': '',
    }
}
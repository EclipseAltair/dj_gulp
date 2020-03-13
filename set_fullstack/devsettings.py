# -*- coding: utf-8 -*-
from .settings import *


DEBUG = True

ALLOWED_HOSTS = []

MIDDLEWARE.append('livereload.middleware.LiveReloadScript',)

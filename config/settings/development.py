from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_website',
        'USER': 'django_website',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SECRET_KEY = 'g^%t%(h1ghce5r*7vw4(8sb3!40t&mpwyky+&586dr!9%&bjnr'

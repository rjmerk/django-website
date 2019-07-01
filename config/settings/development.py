from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "django-website",
        'USER': "rj",
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': "localhost",
        'PORT': 5432
    }
}

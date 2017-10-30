from .base import *

DEBUG = FALSE

SECRET_KEY = get_secret("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': get_secret("DATABASE_HOST"),
        'PORT': get_secret("DATABASE_PORT"),
    }
}


ALLOWED_HOSTS = ["robbert-jan.net", "www.robbert-jan.net"]

from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "website",
        'USER': "website",
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': "127.0.0.1",
        'PORT': 5432
    }
}


ALLOWED_HOSTS = ["robbert-jan.net", "www.robbert-jan.net"]

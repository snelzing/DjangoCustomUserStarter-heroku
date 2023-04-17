from config.settings.common import *

import os


DEBUG = False


ALLOWED_HOSTS = ['flynnt-knapp-djangostarter-elzinga.herokuapp.com']


MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware']


# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = BASE_DIR / 'staticfiles'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Create a specific `SECRET_KEY` for production and use it in production only.
SECRET_KEY = os.environ.get('SECRET_KEY')

# To create a new `SECRET_KEY`:
"""
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""

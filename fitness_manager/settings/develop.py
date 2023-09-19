from .base import *  # noqa: F401

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1@r*u2*&9^dfhjja52fep8qu8o$q8#q^+y@ta6@m-k$xzl@l$%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}

"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['muminoff.com']
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com') 
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '') 
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com') 
EMAIL_PORT = environ.get('EMAIL_PORT', 587) 
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME 
EMAIL_USE_TLS = True 
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ohmywallet',
        'USER': 'ohmywallet',
        'PASSWORD': 'ohmywallet',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'slave': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ohmywallet',
        'USER': 'ohmywallet',
        'PASSWORD': 'ohmywallet',
        'HOST': 'pg-node2.muminoff.com',
        'PORT': '5432',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION

INSTALLED_APPS += (
    'core',
)

########## SSL CONFIGURATION
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
########## END SSL CONFIGURATION 

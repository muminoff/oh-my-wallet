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
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'watchmywallet',
        'USER': 'watchmywallet',
        'PASSWORD': 'watchmywallet',
        'HOST': 'localhost',
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
    'pipeline',
    'core',
)

########## SSL CONFIGURATION
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
########## END SSL CONFIGURATION

########## DJANGO-PIPELINE
PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'css/bootstrap.css',
        ),
        'output_filename': 'css/bootstrap.compressed.min.css',
    },
    'watchmywallet': {
        'source_filenames': (
            'css/watchmywallet.css',
        ),
        'output_filename': 'css/watchmywallet.compressed.min.css',
    },
}
PIPELINE_JS = {
    'jquery': {
        'source_filenames': (
            'js/jquery.js',
        ),
        'output_filename': 'js/jquery.compressed.min.js',
    },
    'bootstrap': {
        'source_filenames': (
            'js/bootstrap.js',
        ),
        'output_filename': 'js/bootstrap.compressed.min.js',
    },
    'watchmywallet': {
        'source_filenames': (
            'js/watchmywallet.js',
        ),
        'output_filename': 'js/watchmywallet.compressed.min.js',
    },
}
MIDDLEWARE_CLASSES += (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
STATICFILES_FINDERS += (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_ENABLED = True
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'
########## END PIPELINE CONFIGURATION

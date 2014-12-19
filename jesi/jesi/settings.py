import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG=False
SITE_ROOT = '/home/alon10/jessicasteiber.com/'
SITE_URL = 'http://www.jesisteiber.com/'
SITE_NAME = 'JesiSteiber.com'
ADMINS = (('Alan Beam', 'alan@alanbeam.net'))
MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.jesisteiber.com','.jessicasteiber.com']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'about',
    'accounts',
    'blog',
    'photos',
    'links',
    'verses',
    'contact',
    'badges'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jesi.urls'
WSGI_APPLICATION = 'jesi.wsgi.application'
USE_TZ = True

MEDIA_ROOT = SITE_ROOT + 'public/media/'
MEDIA_URL = SITE_URL + 'media/'
ADMIN_MEDIA_PREFIX = SITE_URL + 'media/admin/'
STATIC_ROOT = SITE_ROOT + 'jesi/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    SITE_ROOT + 'public/static/',
)

TEMPLATE_DIRS = (SITE_ROOT + 'jesi/templates')

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

try:
        from local_settings import *
except ImportError:
        pass


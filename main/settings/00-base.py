import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '8d&j_3zjc^4!)+3_s0!waya72jhx8j=3iryhexz=uq)9t)vbcs'

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'modifi3d.urls'

WSGI_APPLICATION = 'modifi3d.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True = True = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '.static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')

FAVICON = '/static/favicon.ico'

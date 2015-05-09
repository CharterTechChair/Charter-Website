"""
Django settings for charterclub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(mihe#rzn6$nxj0=ht()h==#315l7ojk@b5s#b_d)p6*6geyi6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "templates2").replace(
    "\\","/"),)

ALLOWED_HOSTS = [
    '.princetoncharterclub.org',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'charterclub',
    'crispy_forms',
    'events',
    'menus',
    'feedback',
    'cal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # required for CAS
    'django_cas.middleware.CASMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

# needed for CAS
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas.backends.CASBackend',
)

ROOT_URLCONF = 'charterclub.urls'

WSGI_APPLICATION = 'charterclub.wsgi.application'

# CAS settings
CAS_SERVER_URL = 'https://fed.princeton.edu/cas/'
CAS_LOGOUT_COMPLETELY = False
CAS_REDIRECT_URL = 'templates2/hello.html'

# email backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'roryf@princeton.edu'
EMAIL_HOST_PASSWORD = 'bjxslmlxjynwyfef'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
ON_HEROKU = os.environ.get('ON_HEROKU')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
if ON_HEROKU:
    # recommend heroku settings for databases at <https://devcenter.heroku.com/articles/getting-started-with-django>
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']
    # Static asset configuration
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)



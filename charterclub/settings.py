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
 

# if this is true, get_username(request) will return testuser. use for
# testing when CAS is not available
CAS_DISABLED = False

TEMPLATE_DEBUG = True

# TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "templates").replace(
#     "\\","/"),)

# Needed for Django Flatpages
SITE_ID = 1

# For managing templates
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "..", "templates").replace('\\', '/'),)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]


ALLOWED_HOSTS = [
    '.princetoncharterclub.org',
    'localhost'
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.formtools',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'jquery',
    'dajaxice',
    'dajax',
    'charterclub',
    'crispy_forms',
    'events',
    'recruitment',
    'menus',
    'feedback',
    'kitchen',
    'django_bootstrap_calendar',
    'storages', # For AWS
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # required for CAS
    'django_cas.middleware.CASMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
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
CAS_REDIRECT_URL = 'templates/hello.html'

# email backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'roryf@princeton.edu'
EMAIL_HOST_PASSWORD = 'bjxslmlxjynwyfef'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# FOR IMAGES
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, '..', 'media/')
MEDIA_URL = '/media/'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
ON_HEROKU = os.environ.get('ON_HEROKU')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # WAS 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Or path to database file if using sqlite3.
        'NAME': 'ddkidtgk9fbdge',
        # The following settings are not used with sqlite3:
        'USER': 'eywigllpkckjyf',
        'PASSWORD': 'bZcWz2ZdXU3vye3tqsCyIRk1Tm',
        'HOST': 'ec2-54-204-20-164.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
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

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Static files on AWS S3 with Heroku:
# (1) http://stackoverflow.com/questions/20480984/serve-static-files-on-heroku-using-aws-s3-for-django
#    (1a) http://blog.doismellburning.co.uk/django-and-static-files/
#     (1b) http://blog.doismellburning.co.uk/using-amazon-s3-to-host-your-django-static-files/

# STATIC_URL = '/static/'

if ON_HEROKU:
    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
else:
    AWS_STORAGE_BUCKET_NAME = 'charter-website' # because i'm too lazy to use virtual environments

STATIC_URL='http://your_s3_bucket.s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = 'staticfiles'

STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       'dajaxice.finders.DajaxiceFinder')
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# From: https://devcenter.heroku.com/articles/django-assets
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Django settings for hasdocs project.
import os

if os.environ.get('DEVELOPMENT'):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
else:
    DEBUG = False
    TEMPLATE_DEBUG = False

ADMINS = (
    ('Chee-Hyung Yoon', 'yoon@virect.com'),
)

MANAGERS = (
    ('Chee-Hyung Yoon', 'yoon@virect.com'),
    ('Naezin Hyeon', 'hyeon@virect.com'),
    ('Taenyon Kim', 'taenyon.kim@virect.com'),
    ('Hye Ryeon Lee', 'lee@virect.com'),
)

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Seoul'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2$+dp%u926(lr*e24#$1_daj9f@%jb=zpf*uvihx$wc2yqbc^)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': os.environ['MEMCACHE_SERVERS'],
        'TIMEOUT': 500,
        'BINARY': True,
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'hasdocs.core.middleware.SubdomainMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'hasdocs.accounts.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'hasdocs.urls'
SUBDOMAIN_URLCONF = 'hasdocs.core.subdomain_urls'
CNAME_URLCONF = 'hasdocs.core.cname_urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hasdocs.wsgi.application'

TEMPLATE_DIRS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'hasdocs', 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    # Third-party apps
    'gunicorn',
    'kombu.transport.django',
    'djcelery',
    'storages',
    'south',
    'crispy_forms',
    'debug_toolbar',
    # Hasdocs apps
    'hasdocs.accounts',
    'hasdocs.core',
    'hasdocs.projects',
    'hasdocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s \
            %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'hasdocs': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

# Added to enable request context processor
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
)

# Added to use bcrypt for storing passwords
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# Email settings
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[HasDocs] '

# Enables session cookies in subdomains
if DEBUG:
    SESSION_COOKIE_DOMAIN = '.test.com'
elif os.environ.get('STAGING'):
    SESSION_COOKIE_DOMAIN = '.docsome.com'
else:
    SESSION_COOKIE_DOMAIN = '.hasdocs.com'

# User profile
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/%s/" % o.username,
}

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'hasdocs.accounts.backends.GithubBackend',
)

# Debug toolbar
INTERNAL_IPS = ('127.0.0.1',)

# Django storages
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Amazon S3
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']
AWS_DOCS_BUCKET_NAME = os.environ['AWS_DOCS_BUCKET_NAME']
AWS_IS_ZIPPED = True
GZIP_CONTENT_TYPE = (
    'text/html',
    'text/css',
    'text/plain',
    'application/javascript',
    'application/x-javascript',
)

# GitHub
GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_API_URL = 'https://api.github.com'

# Heroku
HEROKU_API_URL = 'https://api.heroku.com'
HEROKU_API_KEY = os.environ['HEROKU_API_KEY']

# Celery
BROKER_URL = 'django://'
if os.environ.get('CELERY_ALWAYS_EAGER', None) == '1':
    CELERY_ALWAYS_EAGER = True

import djcelery
djcelery.setup_loader()

# Google Storages
GS_ACCESS_KEY_ID = os.environ['GS_ACCESS_KEY_ID']
GS_SECRET_ACCESS_KEY = os.environ['GS_SECRET_ACCESS_KEY']
GS_BUCKET_NAME = os.environ['GS_BUCKET_NAME']

# Stripe
STRIPE_API_KEY = os.environ['STRIPE_API_KEY']

# Pusher
PUSHER_APP_ID = os.environ['PUSHER_APP_ID']
PUSHER_API_KEY = os.environ['PUSHER_API_KEY']
PUSHER_API_SECRET = os.environ['PUSHER_API_SECRET']

# Virtualenv
VENV_NAME = 'venv'
VENV_FILENAME = '.venv.tar.gz'

# Gravatar
GRAVATAR_API_URL = 'https://secure.gravatar.com/avatar'

"""
Django settings for EnviroD project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(r+klk7n0w4o)k76%@l^^0!fm+)t7*rrl+e6jk+iq+s-j17k-l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['envirod.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'crispy_forms',
    'events',
    'cart',
    'payment',
    'location',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EnviroD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EnviroD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {'default': dj_database_url.parse('postgres://iuijewwtzawklf:965d0f6614cf438718a3b8b341e4149eaab4d9c60c17f4c6691ec8c5fd294efa@ec2-174-129-254-235.compute-1.amazonaws.com:5432/dedlliih324b2k')}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_LOCATION="static"
STATICFILES_STORAGE='custom_storages.StaticStorage'

DEFAULT_FILE_STORAGE='custom_storages.MediaStorage'
MEDIAFILES_LOCATION="media"


AUTH_USER_MODEL = 'accounts.MyUser'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",

)

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

LOGIN_URL = "/accounts/login"


CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY=os.environ['MAILGUN_PRIVATE_KEY']
MAILGUN_SERVER_NAME = 'sandbox4f13f8deef0546cea57d7b36f2ef9946.mailgun.org'

DEFAULT_FROM_EMAIL = "admin@sandbox4f13f8deef0546cea57d7b36f2ef9946.mailgun.org"
FROM_EMAIL = "admin@sandbox4f13f8deef0546cea57d7b36f2ef9946.mailgun.org"

STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

MAPBOX_ACCESS_TOKEN = os.getenv('MAPBOX_ACCESS_TOKEN')

AWS_S3_OBJECT_PARAMETERS={
    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl':'max-age=946800'
}

AWS_STORAGE_BUCKET_NAME="nd-django-project"
AWS_S3_REGION_NAME="ap-southeast-1"
AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY=os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_S3_CUSTOM_DOMAIN="{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)

STATICFILES_STORAGE="storages.backends.s3boto3.S3Boto3Storage"
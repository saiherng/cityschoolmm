from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# -- Recommended CodeRed Cloud settings ---------------------------------------

import os

ALLOWED_HOSTS = os.environ['ALLOWED_H0STS'].split()

SECRET_KEY = os.environ['SECRET_KEY']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Built-in email sending service provided by CodeRed Cloud.
# Change this to a different backend or SMTP server to use your own.
EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'HOST': os.environ["DB_HOST"],
         'NAME': os.environ["DB_NAME"],
         'USER': os.environ["DB_USER"],
         'PASSWORD': os.environ["DB_PASSWORD"],
     }
}


# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.mysql',
#          'HOST': os.environ["DB_HOST"],
#          'NAME': os.environ["DB_NAME"],
#          'USER': os.environ["DB_USER"],
#          'PASSWORD': os.environ["DB_PASSWORD"],
#          'OPTIONS': {
#              'ssl': {},
#              'charset': 'utf8mb4',
#              'collation': 'utf8mb4_0900_ai_ci',
#          },
#      }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

MAILGUN_API_KEY = os.environ["MAILGUN_API_KEY"]
MAILGUN_SENDER_DOMAIN = os.environ["MAILGUN_SENDER_DOMAIN"]

ANYMAIL = {
    "MAILGUN_API_KEY": MAILGUN_API_KEY,
    "MAILGUN_SENDER_DOMAIN": MAILGUN_SENDER_DOMAIN,  
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend" 

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587

EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

WAGTAIL_PASSWORD_RESET_ENABLED = True

RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
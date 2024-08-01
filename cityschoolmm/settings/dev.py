from .base import *

import os
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_SENDER_DOMAIN = os.getenv("MAILGUN_SENDER_DOMAIN")

ANYMAIL = {
    "MAILGUN_API_KEY": MAILGUN_API_KEY,
    "MAILGUN_SENDER_DOMAIN": MAILGUN_SENDER_DOMAIN,  
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend" 

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

WAGTAIL_PASSWORD_RESET_ENABLED = True


try:
    from .local import *
except ImportError:
    pass

from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# Flag to determine whether the FOIA request form gets shown.
SHOW_WEBFORM = False

ALLOWED_HOSTS = ['foia.18f.us']

# If testing out production settings in development:
# ALLOWED_HOSTS = ['foia.18f.us', 'localhost']

# In production we will have HTTPS setup. 
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True

AWS_STORAGE_BUCKET_NAME = 'openfoia-static'
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

try:
    from .local_settings import *
except ImportError:
    pass

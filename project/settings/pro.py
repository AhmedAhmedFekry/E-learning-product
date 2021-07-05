from .base import *

DEBUG = False
ADMINS = (
 ('Antonio M', 'email@mydomain.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'elearning',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
   }
}
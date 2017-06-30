from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SuperSecret'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        ]

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media"),

MEDIA_URL = '/media/'

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dbLocal.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static/"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"



QUILL_CONFIGS = {
    'default': {
        'theme': 'snow',
        'modules': {
            'toolbar': [
                [{'header': [1, 2, False]}],
                ['bold', 'italic', 'underline'],
                ['link', 'image', 'video'],
            ],
        }
    }
}


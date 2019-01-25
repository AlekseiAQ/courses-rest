from .settings_default import *

SECRET_KEY = "123"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "courses",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "static", "files", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static", "files", "static")

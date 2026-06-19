from .base import *


DATABASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASE_BASE_DIR / "db.sqlite3",
    }
}

# CORS_ALLOW_ALL_ORIGINS = True
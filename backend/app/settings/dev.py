from __future__ import absolute_import, unicode_literals

from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

FORCE_SERVE_STATIC = True

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True

SECRET_KEY = env("DJANGO_SECRET_KEY")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = ("127.0.0.1",)

try:
    from .local import *  # noqa
except ImportError:
    pass

CACHES["default"] = {
    "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
}

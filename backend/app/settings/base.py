from __future__ import absolute_import, unicode_literals

import datetime
import os
import sys

import environ

from .sections.auth import *
from .sections.databases import *
from .sections.installed_apps import *
from .sections.locale import *
from .sections.middleware import *
from .sections.staticfiles import *
from .sections.templates import *

env = environ.Env()

ROOT_URLCONF = "app.urls"

CORS_URLS_REGEX = r"^/(auth|graphql)/.*$"

WSGI_APPLICATION = "app.wsgi.application"

SITE_ID = 1

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "unix:/tmp/memcached.sock",
    }
}

GRAPHENE = {
    "SCHEMA": "api.schema.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

SLACK_API_TOKEN = env("SLACK_API_TOKEN", default=None)
SLACK_CHANNEL_FOR_TASK_UPDATES = "#task-updates"

FAID_QUIZ_URL = "www.quiz.com/faid"

ACTION_CONF = "app.actions"

STATE_MACHINE_CONF = "app.state_machines"

ONBOARDING_QUESTIONS_TEMPLATE_URL = env(
    "ONBOARDING_QUESTIONS_TEMPLATE_URL",
    default="https://docs.google.com/document/d/1nZbM9o2QOi1y6oIir55Ceo2q-D7fmU8Y0Nx5_rTNwAc/edit?ts=5eba3b24#",
)

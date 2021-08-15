DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "django_extensions",
    "graphene_django",
    "graphql_auth",
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
]

LOCAL_APPS = [
    "api.apps.ApiConfig",
    "app.apps.AppConfig",
    "project_requests.apps.ProjectRequestsConfig",
    "tasks.apps.TasksConfig",
    "users.apps.UsersConfig",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

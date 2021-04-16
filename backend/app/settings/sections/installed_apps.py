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
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
    "graphql_auth",
    "todo",
    "dal",  # needed for todo
    "dal_select2",  # needed for todo
]

LOCAL_APPS = [
    "app.apps.MainAppConfig",
    "users.apps.UsersConfig",
    "project_requests.apps.ProjectRequestsConfig",
    "tasks.apps.TasksConfig",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

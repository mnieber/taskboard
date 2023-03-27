import datetime

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

DJANGO_RTK = {
    "BACKEND": "django_rtk_green.backends.Backend",
    "VALIDATOR": "django_rtk.validators.Validator",
    "EMAIL_TEMPLATES": {
        "RegisterAccount": "users/activation_email.html",
        "RequestPasswordReset": "users/password_reset_email.html",
    },
    "EMAIL_SUBJECTS": {
        "RegisterAccount": "Activate your ProjectTogether account",
        "RequestPasswordReset": "Reset your ProjectTogether password",
    },
    "EMAIL_CONTEXT": {
        "domain": "www.projecttogether.org",
    },
    "EMAIL_FROM": "noreply@projecttogether.org",
}

TERMS_VERSION = "15-08-2021"

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=7),
    "JWT_ALLOW_ANY_CLASSES": [
        "django_rtk_green.mutations.RegisterAccount",
        "django_rtk_green.mutations.ActivateAccount",
        "django_rtk_green.mutations.RequestPasswordReset",
        "django_rtk_green.mutations.ResetPassword",
        "django_rtk_green.mutations.ObtainJSONWebToken",
        "django_rtk_green.queries.MeQuery",
        "graphql_jwt.mutations.Verify",
        "graphql_jwt.mutations.Refresh",
        "graphql_jwt.mutations.Revoke",
    ],
}

AUTH_USER_MODEL = "users.User"

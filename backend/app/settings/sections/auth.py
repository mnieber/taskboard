import datetime

AUTHENTICATION_BACKENDS = [
    "graphql_auth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

GRAPHQL_AUTH = {
    "REGISTER_MUTATION_FIELDS": {
        "email": "String",
    },
    "UPDATE_MUTATION_FIELDS": ["username"],
    "LOGIN_ALLOWED_FIELDS": ["email"],
    "EMAIL_TEMPLATE_ACTIVATION": "users.email.ActivationEmail",
    "EMAIL_TEMPLATE_ACTIVATION_RESEND": "users.email.ActivationEmail",
    "EMAIL_TEMPLATE_PASSWORD_RESET": "users.email.PasswordResetEmail",
}

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=7),
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
}

AUTH_USER_MODEL = "users.User"

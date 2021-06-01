import graphene
from django.db import transaction
from graphene_django.types import DjangoObjectType
from graphql_auth import mutations, schema
from graphql_auth.settings import graphql_auth_settings

from users import models

# Schema app


class ProfileType(DjangoObjectType):
    class Meta:
        model = models.Profile


class UpdateProfile(graphene.Mutation):
    class Arguments:
        pass

    ok = graphene.Boolean()

    def mutate(self, info):
        return UpdateProfile(ok=True)


class UserType(DjangoObjectType):
    class Meta:
        model = models.User
        exclude = graphql_auth_settings.USER_NODE_EXCLUDE_FIELDS

    groups = graphene.List(graphene.String)
    archived = graphene.Boolean()
    verified = graphene.Boolean()
    secondary_email = graphene.String()

    def resolve_archived(self, info):
        return self.status.archived

    def resolve_verified(self, info):
        return self.status.verified

    def resolve_secondary_email(self, info):
        return self.status.secondary_email

    def resolve_groups(self, info):
        return self.groups.all()


class MeQuery(schema.MeQuery):
    me = graphene.Field(UserType)


class ObtainJSONWebToken(mutations.ObtainJSONWebToken):
    user = graphene.Field(UserType)


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Mutations(AuthMutation, graphene.ObjectType):
    pass


class Query(MeQuery, graphene.ObjectType):
    user_profile = graphene.Field(ProfileType)
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.String())

    def resolve_users(self, info, **kwargs):
        return models.User.objects.all()

    def resolve_user(self, info, id):
        return models.User.objects.get(id=id)

    def resolve_user_profile(self, info):
        result = models.Profile.objects.filter(owner_id=info.context.user.id).first()
        return result

import graphene
from graphene.types.datetime import Date
from graphene_django.types import DjangoObjectType

from project_requests.models import ProjectRequest
from project_requests.utils import create_project_request


class ProjectRequestType(DjangoObjectType):
    class Meta:
        model = ProjectRequest
        exclude = ["task"]


class ProjectRequestsQuery:
    project_requests = graphene.List(ProjectRequestType)

    def resolve_project_requests(self, info, **kwargs):
        return ProjectRequest.objects.all()


class RejectProjectRequestFormType(graphene.InputObjectType):
    project_request_id = graphene.String()
    send_email = graphene.Boolean()
    email_to = graphene.String()
    email_body = graphene.String()


class RejectProjectRequest(graphene.Mutation):
    class Arguments:
        form = graphene.Argument(RejectProjectRequestFormType)

    success = graphene.Boolean()

    @staticmethod
    def mutate(parent, info, form):
        actions.reject_project_request(form)
        return dict(success=True)


class ApproveProjectRequestFormType(graphene.InputObjectType):
    project_request_id = graphene.String()


class ApproveProjectRequest(graphene.Mutation):
    class Arguments:
        form = graphene.Argument(ApproveProjectRequestFormType)

    success = graphene.Boolean()

    @staticmethod
    def mutate(parent, info, form):
        actions.approve_project_request(form)
        return dict(success=True)


class PostProjectRequest(graphene.Mutation):
    class Arguments:
        form = graphene.Argument(ProjectRequestType)

    success = graphene.Boolean()

    @staticmethod
    def mutate(parent, info, form):
	actions.create_project_request(form)
        return dict(success=True)


class Query(ProjectRequestsQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    post_reject_project_request_form = PostRejectProjectRequestForm.Field()
    post_approve_project_request_form = PostApproveProjectRequestForm.Field()
    post_project_request = PostProjectRequest.Field()

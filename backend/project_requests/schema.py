import graphene
from graphene.types.datetime import Date
from graphene_django.types import DjangoObjectType

from project_requests.models import ProjectRequest
from project_requests.utils import create_project_request
from tasks.utils import log_task_msg


class ProjectRequestType(DjangoObjectType):
    class Meta:
        model = ProjectRequest


# Mutation
class CreateProjectRequestInput(graphene.InputObjectType):
    location = graphene.String(required=True)
    description = graphene.String(required=False)
    changemaker_name = graphene.String(required=True)
    date_of_birth = Date(required=True)
    project_name = graphene.String(required=True)
    email = graphene.String(required=True)
    google_doc_url = graphene.String(required=False)
    description_url = graphene.String(required=False)


class CreateProjectRequest(graphene.Mutation):
    class Arguments:
        input = CreateProjectRequestInput()

    success = graphene.Boolean()
    project_request = graphene.Field(ProjectRequestType)

    def mutate(self, info, **kwargs):
        kwargs = kwargs["input"]
        project_request = create_project_request(**kwargs)
        project_request.task.transition("receive", {})
        log_task_msg(
            project_request.task,
            "New project request received: %s" % project_request.project_name,
        )

        return CreateProjectRequest(project_request=project_request, success=True)


class Mutation(graphene.ObjectType):
    create_project_request = CreateProjectRequest.Field()
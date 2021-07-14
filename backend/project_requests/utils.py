from django.template import loader

from project_requests.models import ProjectRequest
from tasks.models import Task


def create_project_request(**kwargs):
    task = Task.objects.create(
        state="ProjectRequest.created",
        title="Project request: %s" % kwargs["project_name"],
    )
    return ProjectRequest.objects.create(
        task=task,
        **kwargs
    )

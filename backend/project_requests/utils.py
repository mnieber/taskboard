from django.template import loader

from project_requests.models import ProjectRequest
from tasks.models import Task, TaskList


def create_project_request(**kwargs):
    project_requests_tasklist = TaskList.objects.get(slug="project-requests")
    template = loader.get_template("project_requests/task_note.txt")

    task = Task.objects.create(
        state="ProjectRequest.created",
        title="Project request: %s" % kwargs["project_name"],
        note=template.render(kwargs),
        task_list=project_requests_tasklist,
    )
    return ProjectRequest.objects.create(task=task, **kwargs)

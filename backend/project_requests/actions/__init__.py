from django.conf import settings
from django.urls import reverse

from project_requests.models import ProjectRequest


def reject(task):
    project_request = ProjectRequest.objects.get(task_id=task.id)

    return dict(
        title="Reject",
        template_filename="actions/ProjectRequest.reject.html",
        template_context=dict(project_request=project_request),
        url=reverse("project_request_reject", args=[project_request.id]),
    )


def request_onboarding_call(task):
    project_request = ProjectRequest.objects.get(task_id=task.id)

    return dict(
        title="Request onboarding call",
        template_filename="actions/ProjectRequest.request_onboarding_call.html",
        template_context=dict(
            project_request=project_request,
            onboarding_questions_template_url=settings.ONBOARDING_QUESTIONS_TEMPLATE_URL,
        ),
        url=reverse(
            "project_request_request_onboarding_call", args=[project_request.id]
        ),
    )


def request_quiz_results(task):
    project_request = ProjectRequest.objects.get(task_id=task.id)

    return dict(
        title="Request quiz results",
        template_filename="actions/ProjectRequest.request_quiz_results.html",
        template_context=dict(
            project_request=project_request,
            quiz_url=settings.FAID_QUIZ_URL,
        ),
        url=reverse("project_request_request_quiz_results", args=[project_request.id]),
    )


def reopen(task):
    project_request = ProjectRequest.objects.get(task_id=task.id)

    return dict(
        title="Reopen the request",
        template_filename="actions/ProjectRequest.reopen.html",
        template_context=dict(project_request=project_request),
        url=reverse("project_request_reopen", args=[project_request.id]),
    )


def approve(task):
    project_request = ProjectRequest.objects.get(task_id=task.id)

    return dict(
        title="Approve the request",
        template_filename="actions/ProjectRequest.approve.html",
        template_context=dict(project_request=project_request),
        url=reverse("project_request_approve", args=[project_request.id]),
    )

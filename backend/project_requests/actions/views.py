from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404

from project_requests.models import ProjectRequest
from tasks.views import ActionView

from .forms import (
    ApproveForm,
    RejectionFormWithEmail,
    RejectionFormWithoutEmail,
    RequestOnboardingCallForm,
    RequestQuizResultsForm,
)


class ProjectRequestActionView(ActionView):
    def post(self, request, project_request_id):
        self.project_request = get_object_or_404(ProjectRequest, id=project_request_id)
        return self.handle_post(self.project_request.task)


class ProjectRequestRejectView(PermissionRequiredMixin, ProjectRequestActionView):
    permission_required = "project_requests.can_reject_project_requests"

    def form_cls(self):
        return (
            RejectionFormWithEmail
            if self.request.POST.get("send_email", False)
            else RejectionFormWithoutEmail
        )

    def transition(self, data):
        self.task.transition(
            "reject",
            project_request=self.project_request,
            send_email=data.get("send_email", False),
            email_subject=data.get("email_subject"),
            email_body=data.get("email_body"),
        )
        return "Project request `%s`: rejected" % self.project_request


class ProjectRequestReopenView(ProjectRequestActionView):
    def transition(self, data):
        self.task.transition("reopen", project_request=self.project_request)
        return "Project request `%s`: reopened" % self.project_request


class ProjectRequestRequestOnboardingCallView(
    PermissionRequiredMixin, ProjectRequestActionView
):
    permission_required = (
        "project_requests.can_request_onboarding_calls_and_quiz_results"
    )

    def form_cls(self):
        return RequestOnboardingCallForm

    def transition(self, data):
        self.task.transition(
            "request_onboarding_call",
            project_request=self.project_request,
            email_subject=data.get("email_subject"),
            email_body=data.get("email_body"),
            google_doc_url=data.get("google_doc_url"),
            calendar_url=data.get("calendar_url"),
        )
        return "Project request `%s`: onboarding call requested" % self.project_request


class ProjectRequestRequestQuizResultsView(
    PermissionRequiredMixin, ProjectRequestActionView
):
    permission_required = (
        "project_requests.can_request_onboarding_calls_and_quiz_results"
    )

    def form_cls(self):
        return RequestQuizResultsForm

    def transition(self, data):
        self.task.transition(
            "request_quiz_results",
            project_request=self.project_request,
            email_subject=data.get("email_subject"),
            email_body=data.get("email_body"),
            quiz_url=data.get("quiz_url"),
        )
        return "Project request `%s`: quiz results requested" % self.project_request


class ProjectRequestApproveView(PermissionRequiredMixin, ProjectRequestActionView):
    permission_required = "project_requests.can_approve_project_requests"

    def form_cls(self):
        return ApproveForm

    def transition(self, data):
        self.task.transition(
            "approve",
            project_request=self.project_request,
            email_subject=data.get("email_subject"),
            email_body=data.get("email_body"),
        )
        return "Project request `%s`: approved" % self.project_request

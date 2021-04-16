from django.urls import path

from .views import (
    ProjectRequestApproveView,
    ProjectRequestRejectView,
    ProjectRequestReopenView,
    ProjectRequestRequestOnboardingCallView,
    ProjectRequestRequestQuizResultsView,
)

urlpatterns = [
    path(
        "<project_request_id>/reject",
        ProjectRequestRejectView.as_view(),
        name="project_request_reject",
    ),
    path(
        "<project_request_id>/reopen",
        ProjectRequestReopenView.as_view(),
        name="project_request_reopen",
    ),
    path(
        "<project_request_id>/request_onboarding_call",
        ProjectRequestRequestOnboardingCallView.as_view(),
        name="project_request_request_onboarding_call",
    ),
    path(
        "<project_request_id>/request_quiz_results",
        ProjectRequestRequestQuizResultsView.as_view(),
        name="project_request_request_quiz_results",
    ),
    path(
        "<project_request_id>/approve",
        ProjectRequestApproveView.as_view(),
        name="project_request_approve",
    ),
]

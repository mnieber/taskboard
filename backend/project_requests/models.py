from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.models import Entity
from app.utils import generate_unique_slug
from tasks.models import Task


class ProjectRequest(Entity):
    class Meta:
        permissions = (
            ("can_reject_project_requests", "Can reject project requests"),
            (
                "can_request_onboarding_calls_and_quiz_results",
                "Can request onboarding calls and quiz results",
            ),
            ("can_approve_project_requests", "Can approve project requests"),
        )

    changemaker_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    description = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    is_approved = models.BooleanField(_("approved"), default=False)
    # The task that is used for managing this request
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    google_doc_url = models.URLField(
        _("Contains additional onboarding information"),
        max_length=255,
        null=True,
        blank=True,
    )
    description_url = models.URLField(
        _("A video describing the project"),
        max_length=255,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(ProjectRequest, self.project_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name

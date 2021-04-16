import django.utils.timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import transaction

from app.utils.template_from_string import template_from_string

User = get_user_model()


class Model:
    def effect_maybe_send_rejection_email(
        self, project_request, send_email, email_subject=None, email_body=None, **kwargs
    ):
        if send_email:
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_REPLY_ADDRESS,
                [project_request.email],
            )

    def effect_close_project_request(self, project_request, **kwargs):
        project_request.task.completed = True
        project_request.task.completed_date = django.utils.timezone.now()
        project_request.task.save()

    def effect_approve_project_request(self, project_request, **kwargs):
        project_request.is_approved = True
        project_request.save()

    def effect_reopen_project_request(self, project_request, **kwargs):
        project_request.task.completed = False
        project_request.task.completed_date = None
        project_request.task.save()

    def effect_request_onboarding_call(
        self,
        project_request,
        google_doc_url,
        calendar_url,
        email_subject,
        email_body,
        **kwargs
    ):
        template = template_from_string(email_body)
        template_context = dict(
            project_request=project_request,
            google_doc_url=google_doc_url,
            calendar_url=calendar_url,
        )
        send_mail(
            email_subject,
            template.render(template_context),
            settings.EMAIL_REPLY_ADDRESS,
            [project_request.email],
        )

    def effect_request_quiz_results(
        self, project_request, quiz_url, email_subject, email_body, **kwargs
    ):
        template = template_from_string(email_body)
        template_context = dict(
            project_request=project_request,
            quiz_url=quiz_url,
        )
        send_mail(
            email_subject,
            template.render(template_context),
            settings.EMAIL_REPLY_ADDRESS,
            [project_request.email],
        )

    def effect_create_accounts(
        self, project_request, email_subject, email_body, **kwargs
    ):
        password = User.objects.make_random_password()

        with transaction.atomic():
            user = User.objects.create_user(
                email=project_request.email, password=password
            )

        template = template_from_string(email_body)
        template_context = dict(
            project_request=project_request,
            password_reset_url="www.frontlineaid.org/password-reset",
            project_profile_url="www.frontlineaid.org/profile",
        )

        send_mail(
            email_subject,
            template.render(template_context),
            settings.EMAIL_REPLY_ADDRESS,
            [project_request.email],
        )

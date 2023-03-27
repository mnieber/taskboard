from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from faker import Faker

from project_requests import models
from .utils import create_project_request


@admin.register(models.ProjectRequest)
class ProjectRequestAdmin(admin.ModelAdmin):
    change_list_template = "project_requests/admin/project_requests_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("create-fake/", self.create_fake),
        ]
        return my_urls + urls

    def create_fake(self, request):
        f = Faker()
        project_request = create_project_request(
            **dict(
                location=f.country(),
                description=f.text(),
                changemaker_name=f.name(),
                date_of_birth=f.date(),
                project_name=f.word(),
                email=f.email(),
                google_doc_url=f.url(),
                description_url=f.url(),
            )
        )
        project_request.task.transition("receive", {})
        return HttpResponseRedirect("../")

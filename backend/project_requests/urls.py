from django.urls import include, path

urlpatterns = [
    path(
        "actions/",
        include("project_requests.actions.urls"),
    ),
]

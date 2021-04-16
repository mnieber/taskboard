import uuid

import todo.abstract_models
from django.db import models
from django_extensions.db.models import TimeStampedModel

from .task_model import Task  # noqa


class Attachment(todo.abstract_models.AbstractAttachment):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


class Comment(todo.abstract_models.AbstractComment):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


class TaskList(todo.abstract_models.AbstractTaskList):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


class TaskLogMessage(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.TextField()

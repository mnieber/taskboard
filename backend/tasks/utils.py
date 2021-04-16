from django.conf import settings

from app.utils.post_to_slack import post_to_slack

from .models import TaskLogMessage


def log_task_msg(task, message):
    TaskLogMessage.objects.create(task=task, message=message)
    if settings.SLACK_API_TOKEN and settings.SLACK_CHANNEL_FOR_TASK_UPDATES:
        post_to_slack.delay(settings.SLACK_CHANNEL_FOR_TASK_UPDATES, message)

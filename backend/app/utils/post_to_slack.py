import logging

from django.conf import settings
from slack import WebClient
from slack.errors import SlackApiError


def post_to_slack(channel, msg):
    assert channel.startswith("#")

    try:
        client = WebClient(token=settings.SLACK_API_TOKEN)
        client.chat_postMessage(channel=channel, text=msg)
    except SlackApiError as e:
        logging.getLogger("root").error(
            f"Error while posting to slack: {e.response['error']}"
        )

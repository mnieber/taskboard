# Conceptually, an action is whatever you do to move a task to its next state.
# For example, when you've receive a project request, then one of the possible
# actions is to reject it.
#
# In the code, an action is a record that contains all the data related to
# advancing a Task to one of its possible next states:
# - an id. Within the context of a task, action ids are unique.
# - a title, e.g. "Reject Project Request"
# - a template that renders a form that captures all necessary data
#   that is needed to be able to perform the action, e.g. "rejection reason".
# - a url to which this form must be posted. There should be a Django view
#   that handles this url by calling task.transition()
#
# Note that a state machine will be used to transition the task. For each trigger
# in the state machine, there wil be a corresponding action. The control flow is:
#
# - When a task is created, it has an associated state machine and state
# - When the task is rendered in the task admin backend, task.actions is called
#   to get a list of actions
# - All actions are shown to the user (using action.title and action.template)
# - Posting the action form (to action.url) triggers a specific Django view.
# - The Django view retrieves the task and calls task.transition(trigger, data),
#   where `data` is whatever data is necessary to run the trigger (usually, this
#   data will be based on the posted form data)

import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.models import Entity

from .builders import build_state_machine, get_action


def _state_name(task):
    return task.state.split(".")[1]


def _state_machine_name(task):
    return task.state.split(".")[0]


class Task(Entity):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    state = models.CharField(
        _("Current state of the task"),
        default="",
        max_length=255,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=140)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="+"
    )

    def __str__(self):
        return self.title

    def actions(self):
        state_name = _state_name(self)
        state_machine_name = _state_machine_name(self)
        state_machine = build_state_machine(state_machine_name, state_name)

        if not self.state:
            return []
        return [
            get_action(state_machine_name, trigger, self)
            for trigger in state_machine.get_triggers(state_name)
        ]

    def transition(self, trigger: str, *args, **kwargs):
        state_machine = build_state_machine(
            _state_machine_name(self), _state_name(self)
        )
        if state_machine.dispatch(trigger, *args, **kwargs):
            self.state = "%s.%s" % (
                _state_machine_name(self),
                state_machine.model.state,
            )
            self.save()

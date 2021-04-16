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

import todo.abstract_models
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .builders import build_action, build_state_machine


def _state(task):
    return task.state.split(".")[1]


def _state_machine_name(task):
    return task.state.split(".")[0]


def _state_machine(task):
    return build_state_machine(_state_machine_name(task), _state(task))


def _triggers(task):
    return _state_machine(task).get_triggers(_state(task))


class Task(todo.abstract_models.AbstractTask):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    state = models.CharField(
        _("Current state of the task"),
        default="",
        max_length=255,
        null=True,
        blank=True,
    )

    def actions(self):
        if not self.state:
            return []
        return [
            build_action(_state_machine_name(self), trigger, self)
            for trigger in _triggers(self)
        ]

    def transition(self, trigger, *args, **kwargs):
        state_machine = _state_machine(self)
        if state_machine.dispatch(trigger, *args, **kwargs):
            self.state = "%s.%s" % (
                _state_machine_name(self),
                state_machine.model.state,
            )
            self.save()

import importlib

from django.conf import settings
from django.template import loader
from django.utils.text import slugify


def get_action(state_machine_name, trigger, task):
    def _add_action_id(action):
        action["id"] = slugify(action["title"])

    def _add_action_form(action, task):
        template = loader.get_template(action["template_filename"])
        action["form"] = template.render(
            {"task": task, "action": action, **action["template_context"]}
        )

    builders = importlib.import_module(settings.ACTION_CONF).action_builders
    action = builders[state_machine_name][trigger](task)
    _add_action_id(action)
    _add_action_form(action, task)
    return action


def build_state_machine(state_machine_name, state_name):
    builders = importlib.import_module(
        settings.STATE_MACHINE_CONF
    ).state_machine_builders
    return builders[state_machine_name](state_name)

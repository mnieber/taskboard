import django.utils.timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .utils import log_task_msg


class ActionView(LoginRequiredMixin, View):
    def handle_post(self, task):
        self.task = task
        data, errors = self.get_data()

        if errors:
            for field, field_errors in errors.items():
                messages.error(self.request, "%s: %s" % (field, field_errors[0]))
        else:
            log_msg = self.transition(data)
            if log_msg:
                now = django.utils.timezone.now()
                log_task_msg(
                    self.task,
                    "%s by %s on %s at %s."
                    % (
                        log_msg,
                        self.request.user.username,
                        now.strftime("%m/%d/%Y"),
                        now.strftime("%H:%M:%S"),
                    ),
                )

        return HttpResponseRedirect(reverse("todo:task_detail", args=(self.task.id,)))

    def get_data(self):
        form_cls = self.form_cls()
        if form_cls:
            form = form_cls(self.request.POST)
            is_valid = form.is_valid()
            return form.data if is_valid else None, form.errors
        return self.request.POST, {}

    def form_cls(self):
        None

    # Implemented by the child View.
    # Returns either None or a log message that will be added to the task history
    def transition(self, data):
        raise NotImplementedError()

from transitions import Machine

from .model import Model

states = [
    "created",
    "received",
    "rejected",
    "onboarding_call_requested",
    "quiz_results_requested",
    "approved",
]

transitions = [
    (("receive", "created", "received"), {}),
    (
        (
            "reject",
            ["received", "onboarding_call_requested", "quiz_results_requested"],
            "rejected",
        ),
        {},
    ),
    (("reopen", "rejected", "received"), {"before": "effect_reopen_project_request"},),
    (("request_onboarding_call", "received", "onboarding_call_requested"), {},),
    (
        ("request_quiz_results", "onboarding_call_requested", "quiz_results_requested"),
        {},
    ),
    (("approve", "quiz_results_requested", "approved"), {},),
]


def create_project_request_machine(initial_state):
    machine = Machine(
        model=Model(), states=states, initial=initial_state, auto_transitions=False
    )

    for (trigger, source, dest), kwargs in transitions:
        machine.add_transition(trigger, source, dest, **kwargs)

    machine.on_enter_rejected("effect_maybe_send_rejection_email")
    machine.on_enter_rejected("effect_close_project_request")
    machine.on_enter_onboarding_call_requested("effect_request_onboarding_call")
    machine.on_enter_quiz_results_requested("effect_request_quiz_results")
    machine.on_enter_approved("effect_create_accounts")
    machine.on_enter_approved("effect_approve_project_request")
    machine.on_enter_approved("effect_close_project_request")

    return machine

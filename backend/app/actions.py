import project_requests.actions as project_request_actions

action_builders = {
    "ProjectRequest": dict(
        reject=project_request_actions.reject,
        request_onboarding_call=project_request_actions.request_onboarding_call,
        request_quiz_results=project_request_actions.request_quiz_results,
        reopen=project_request_actions.reopen,
        approve=project_request_actions.approve,
    )
}

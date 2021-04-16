from project_requests.state_machine import create_project_request_machine

state_machine_builders = {
    "ProjectRequest": create_project_request_machine,
}

from .exceptions import (
    NotCallableActionRegisteredException,
    StateMustBeInitToRunException,
)


class Agent:
    def __init__(self):
        self.state_actions = {}
        self.state = ""

    def add_action(self, state, action):
        if callable(action):
            self.state_actions.update({state: action})
        else:
            raise NotCallableActionRegisteredException

    def set_state(self, state):
        self.state = state

    def run(self):
        if self.state == "":
            raise StateMustBeInitToRunException

        action_to_run = self.state_actions.get(self.state)
        action_to_run()

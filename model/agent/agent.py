from .exceptions import (
    NotCallableActionRegisteredException,
    StateMustBeInitToRunException,
    NotRegisteredStateCall,
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
        if state in self.state_actions:
            self.state = state

        raise NotRegisteredStateCall

    def run(self):
        if self.state == "":
            raise StateMustBeInitToRunException

        action_to_run = self.state_actions.get(self.state)
        action_to_run()

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
        if not callable(action):
            raise NotCallableActionRegisteredException

        self.state_actions.update({state: action})

    def set_state(self, state):
        if state not in self.state_actions.keys():
            raise NotRegisteredStateCall

        self.state = state

    def run(self):
        if self.state == "":
            raise StateMustBeInitToRunException

        action_to_run = self.state_actions.get(self.state)
        action_to_run()

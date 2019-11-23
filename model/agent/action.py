class Action:
    def __init__(self, success_state, failure_state):
        self.success_state = success_state
        self.failure_state = failure_state

    def __call__(self) -> str:
        pass


class DummyAction(Action):
    def __call__(self) -> str:
        return self.success_state

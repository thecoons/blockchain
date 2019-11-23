from .action import DummyAction

WAIT_STATE = "wait"

AGENT_CONFIGURATIION_BASE = {
    WAIT_STATE: DummyAction(success_state=WAIT_STATE, failure_state=WAIT_STATE),
}

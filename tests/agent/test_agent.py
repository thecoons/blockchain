from unittest import TestCase
from unittest.mock import Mock

from model import Agent
from model.agent.exceptions import (
    NotCallableActionRegisteredException,
    StateMustBeInitToRunException,
)


class AgentTestCase(TestCase):
    def setUp(self):
        self.agent = Agent()


class TestAgent(AgentTestCase):
    def test_agent_action(self):
        expected_action_executed = Mock()

        self.agent.add_action("ANY_STATE", expected_action_executed)
        self.agent.set_state("ANY_STATE")
        self.agent.run()

        expected_action_executed.assert_called_once()

    def test_agent_dont_accept_uncallable_action(self):
        action_to_refuse = "not_a_callable_object"

        with self.assertRaises(NotCallableActionRegisteredException):
            self.agent.add_action("ANY_STATE", action_to_refuse)

    def test_must_init_state_to_run(self):
        self.agent.add_action("ANY_STATE", Mock())
        with self.assertRaises(StateMustBeInitToRunException):
            self.agent.run()

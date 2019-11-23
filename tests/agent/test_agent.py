from unittest import TestCase
from unittest.mock import Mock

from model import Agent
from model.agent.exceptions import (
    NotCallableActionRegisteredException,
    StateMustBeInitToRunException,
    NotRegisteredStateCall,
)


class AgentTestCase(TestCase):
    def setUp(self):
        self.agent = Agent()


class TestAgent(AgentTestCase):
    def test_agent_action(self):
        expected_action_executed = Mock(return_value="NEXT_STATE")

        self.agent.add_action("ANY_STATE", expected_action_executed)
        self.agent.add_action("NEXT_STATE", Mock())
        self.agent.set_state("ANY_STATE")
        self.agent.run()

        expected_action_executed.assert_called_once()
        self.assertEqual(self.agent.state, "NEXT_STATE")

    def test_agent_dont_accept_uncallable_action(self):
        action_to_refuse = "not_a_callable_object"

        with self.assertRaises(NotCallableActionRegisteredException):
            self.agent.add_action("ANY_STATE", action_to_refuse)

    def test_must_init_state_to_run(self):
        self.agent.add_action("ANY_STATE", Mock())
        with self.assertRaises(StateMustBeInitToRunException):
            self.agent.run()

    def test_cant_set_an_not_existant_state(self):
        with self.assertRaises(NotRegisteredStateCall):
            self.agent.set_state("NOT_REGISTERED_STATE")

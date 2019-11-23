from unittest import TestCase
from unittest.mock import Mock

from model.agent.factory import AgentFactory


class TestAgentFactory(TestCase):
    def test_generate_agent_with_configuration(self):
        first_expected_action_called = Mock()
        second_expected_action_called = Mock()
        configurations = {
            "FIRST_ACTION": first_expected_action_called,
            "SECOND_ACTION": second_expected_action_called,
        }

        factory = AgentFactory()

        created_agent = factory.create(configuration=configurations)
        created_agent.set_state("SECOND_ACTION")
        created_agent.set_state("FIRST_ACTION")
        created_agent.run()

        first_expected_action_called.assert_called_once()


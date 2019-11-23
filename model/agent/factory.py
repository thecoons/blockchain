from .agent import Agent


from .configuratons import AGENT_CONFIGURATIION_BASE, WAIT_STATE


class AgentFactory:
    @staticmethod
    def create(init_state, configuration):
        agent = Agent()
        for state, action in configuration.items():
            agent.add_action(state, action)

        agent.set_state(init_state)

        return agent

    @classmethod
    def create_from_base_configuration(cls):
        agent = cls.create(
            init_state=WAIT_STATE, configuration=AGENT_CONFIGURATIION_BASE
        )

        return agent

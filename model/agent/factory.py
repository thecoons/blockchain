from .agent import Agent


from .configuratons import AGENT_CONFIGURATIION_BASE


class AgentFactory:
    @staticmethod
    def create(configuration):
        agent = Agent()
        for state, action in configuration.items():
            agent.add_action(state, action)

        return agent

    @classmethod
    def create_from_base_configuration(cls):
        agent = cls.create(configuration=AGENT_CONFIGURATIION_BASE)

        return agent

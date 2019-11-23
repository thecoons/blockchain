from datetime import timedelta

from timeloop import Timeloop

from model.agent.factory import AgentFactory

timeloop = Timeloop()
agent = AgentFactory.create_from_base_configuration()


@timeloop.job(interval=timedelta(seconds=2))
def clock():
    agent.run()
    print("> agent.state = {}".format(agent.state))


if __name__ == "__main__":
    timeloop.start(block=True)

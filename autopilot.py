import logging
import datetime

from datetime import timedelta

from timeloop import Timeloop

from model.agent.factory import AgentFactory

logging.basicConfig(
    filename="logs/{}.log".format(
        datetime.datetime.now().strftime("%b-%d-%I%M%p-%G")
    ),
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)

timeloop = Timeloop()
agent = AgentFactory.create_from_base_configuration()


@timeloop.job(interval=timedelta(seconds=2))
def clock():
    agent.run()
    logging.info("> agent.state = {}".format(agent.state))


if __name__ == "__main__":
    timeloop.start(block=True)

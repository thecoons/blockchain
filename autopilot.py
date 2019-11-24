import logging
import datetime

from datetime import timedelta

from timeloop import Timeloop

from model.agent.factory import AgentFactory

format_template = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"

logging.basicConfig(
    filename="logs/{}.log".format(
        datetime.datetime.now().strftime("%b-%d-%I%M%p-%G")
    ),
    level=logging.INFO,
    format=format_template,
)

formatter = logging.Formatter(format_template)
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)

logger = logging.getLogger("autopilot")
logger.addHandler(console)


timeloop = Timeloop()
agent = AgentFactory.create_from_base_configuration()


@timeloop.job(interval=timedelta(seconds=2))
def clock():
    agent.run()
    logger.info("agent.state = {}".format(agent.state))


if __name__ == "__main__":
    timeloop.start(block=True)

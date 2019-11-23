from datetime import timedelta

from timeloop import Timeloop

timeloop = Timeloop()


@timeloop.job(interval=timedelta(seconds=2))
def clock():
    print("This job will be lunch each 2sec.")


if __name__ == "__main__":
    timeloop.start(block=True)

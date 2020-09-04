from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from runner import Runner

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=0.5)
def job():
    print('Running [{0}]'.format(datetime.utcnow()))
    runner = Runner()
    runner.run()


scheduler.start()

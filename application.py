from website import create_application
from refresh_management import backfill_trade_data
from sqlalchemy import create_engine
from apscheduler.schedulers.background import BackgroundScheduler


application = create_application()

sched = BackgroundScheduler(daemon=True)#below job is scheduled to run at 6:30 on weekdays.
sched.add_job(backfill_trade_data,'cron',month='1-12',day_of_week='mon,tue,wed,thu,fri,sat,sun',hour='0-7,18-23',minute='30')
sched.start()

if __name__ == '__main__': #only if we run this file. not if we import it, are we going to execute this line
	application.run(debug=True,use_reloader=False)#every time we make a change, it's going to automatically rerun web-serv
	#use_reloader=False stops app from initializing twice
	#MAKE SURE IT IS SET TO FALSE WHEN TESTING CRON JOB. WILL INTERFERE & CAUSE PROBLEMS

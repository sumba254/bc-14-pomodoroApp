from threading import Timer
import time
import datetime

class Pomodoro(object):
	"""docstring for ClassName"""
	def __init__(self, cycletime = 25, short_break = 5, long_break = 15):
		super(Pomodoro, self).__init__()
		self.time = time
		self.short_break = short_break
		self.long_break = long_break
		self.run = True

	"""def config_time(cycletime):
		#gets the pomodoro cycle time and changes it
		cycletime = input("Enter time in minutes taken to finish one pomodoro cycle: >")"""

	def get_timer(self):
		mins = 0
		#Only run if user types "start"

		if self.run == True:
			# Loop until we reach 25 minutes running
			while mins != 1:
				print (">>>>>>>>>>"), mins
				#sleep for minute
				time.sleep(60)
				#Increment the minute total
				mins += 1
			# Brings up the dialog box here

	def stop_task(self):
		tasks_done = {}
		continue_cycle = input("continue task? ")
		if continue_cycle == "yes":
			Pomodoro.start_task(self)
		else:
			self.run = False
		start_task()
	
	def start_task(self):
		task_title = input()
		task_date = datetime.datetime.now() # takes date and time

		#run = True
		while True:
			Pomodoro.get_timer(self)
			if not stop_task(self):
				break



	def config_short_break():
		short_break = input("Enter the short break time in minutes: >")


	def config_long_break():
		long_break = input("Enter the long break time in minutes: >")


	def config_sound():
		pass

	def list_tasks():
		pass



p = Pomodoro()
p.start_task()
		
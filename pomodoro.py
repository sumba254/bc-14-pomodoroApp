from threading import Timer
import time
from datetime import datetime
import sys
import threading
import time
from os import system
import pyglet

tasktime = 120
breaktime = 30
longtime = 60
cycle = 0

def set_breaktime(): # set short break time method
	global breaktime
	print ("enter new short break time: ")
	breaktime = input()

	return breaktime

def set_tasktime(): # set task time method
	global tasktime
	print ("enter new task time: ")
	tasktime = input()

	return tasktime
	

def set_long_break_timer(): # set long break time method
	global longtime

	print ("enter new long break time: ")
	longtime = input()
	return longtime

def longbreak():  # long break timer method
	global longtime
	minutes = longtime
	print ("LONG BREAK")

	while minutes:
		mins, secs = divmod(minutes, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		minutes -=1
	print("promodoro task done")


def shortbreak(): # short break timer method
	global breaktime
	minutes = breaktime
	#print ("SHORT BREAK")

	while minutes:
		mins, secs = divmod(minutes, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		minutes -= 1
	timer()

def timer(): # task timer method
	global tasktime
	global cycle
	minutes = tasktime

	while minutes:
		mins, secs = divmod(minutes, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		minutes -=1
	
	cycle +=1 # cycle increment

	if cycle != 4:
		shortbreak()
	else:
		longbreak()
		print("task done")

def counter():
	pass

def start():
	running = True
	choice = input("Do you wish to configure your time: (Y/N) =>")
	if choice == "Y":
		set_tasktime()
		set_breaktime()
		set_long_break_timer()
		timer()
	else:
		timer() #calls timer method

def new_task(): #add task and start timer method
	# creates a new task, sets running to true and starts the timer method
	task_title = input("Enter task title: ")
	task_date = datetime.now();
	tasks = task_title, task_date
	print(task_title)
	start()

new_task()

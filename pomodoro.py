from threading import Timer
import time
from datetime import datetime
import sys
import threading
import time
from os import system
import pyglet

tasktime = 10
breaktime = 2
longtime = 5
cycle = 0


def longbreak():
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


def shortbreak():
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

def timer():
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
	timer() #calls timer method

def new_task():
	# creates a new task, sets running to true and starts the timer method
	cycle = 0
	task_title = input("Enter Task title: ")
	task_date = datetime.now();
	tasks = task_title, task_dat
	print(task_title)
	start()
		
new_task()
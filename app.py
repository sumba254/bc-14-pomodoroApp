"""
welcome to Pomodoro Timer.
pomodoro timer app is task managing app. it adds tasks once a task is start  each cycle by default is 25 minute wih 5 short breaks after 4 cycle a 15 minutes long break

Usage:
	app.py pomodoro start <task-title>
	app.py pomodoro config time <duration in minutes>
	app.py pomodoro config short_break | long_break | sound
	app.py pomodoro (-i | --interactive)
	app.py pomodoro (-h | --version)
	app.py pomodoro exit


Arguments:
	<task-title> unique task title
	<duration in minutes> duration of pomodoro cyle in minute


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""

import os
import sys
import cmd 
from docopt import docopt, DocoptExit
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit


def docopt_cmd(func):
	"""
	This decorator is used to simplify the try/except block and pass the result
	of the docopt parsing to the called action
	"""

	def fn(self, args):
		try:
			opt = docopt(fn.__doc__, args)
		except DocoptExit as error:
    		#The DocoptExit is thrown when the args do not match
			print ("The command entered is invalid")
			print (error)
			return
		except SystemExit:
    		# The SystemExit exception prints the usage for --help
			return
		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn


def app_header():
	
	'''
		This function creates the header that is displayed when app
		launches
	'''

	os.system(clear)
	print ("\n\n")

	cprint(figlet_format('Pomodoro Timer', font = 'roman'), green)
	cprint('--------------------------------------------------------------------------', 'magenta')
	cprint("A Pomodoro Timer App That tasks and counts cycles done on that task and outputs list of tasks", 'yellow')
	cprint('--------------------------------------------------------------------------', 'magenta')
	cprint("\n New to the APP? Type 'help' to see a list of commands\n", white)


def pomodoro_print(arg, color = 'green'):

	''' This is a simple print function that adds color to printe output'''

	cprint("\n" + arg + "\n", color)


class PomodoroCLI(cmd.Cmd):
	'''
		This class create the Pomodoro Timer APP Command line Interface for user interaction
	'''

	pomodoro_prompt = colored('Pomodoro > ', 'magenta', attrs=['bold'])
	prompt = pomodoro_prompt

	@docopt_cmd
	def do_start_task(self, args):
		"""
			this commands start a tasks with a unique name on pomodoro.

			The <task_title> argument specifics which task is being created and being started
		
		Usage: start <task_title>

		"""
		tasks_args = []

		for task in args['task_title']:
			tasks_args.append(task.capitalize())

		pomodoro_print(pomodoro.task_title(tasks_args))






opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
	app_header()
	pomodoro = pomodoro()
	PomodoroCLI.cmdloop()

















#!/usr/bin/env python
# -*-coding: utf-8 -*-


"""
Welcome to Chonjo App.
Chonjo is a simple Commandline Pomodoro App
Usage:
    app.py pomodoro_start <task-title>...
    app.py pomodoro_config_time <duration-in-minutes>
    app.py pomodoro_config_short_break <duration-in-minutes>
    app.py pomodoro_config_long_break <duration-in-minutes>
    app.py pomodoro_config_sound <off/on>
    app.py pomodoro_stop
    app.py pomodoro_list
    app.py (-i | --interactive)
    app.py (-h | --help)
    app.py (-v | --version)
    app.py quit
    quit
Arguments
    <task-title>            Name of the task at hand
    <duration-in-minutes>   Duration of in minutes
    <off/on>                The states of the sound
Options:
    -i --interactive        Interactive Mode
    -h --help               Show this screen and exit
    -v --version
"""

import os
import sys
import cmd
import signal
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit

from chonjo import ChonjoApp


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """
    def fn(self, args):
        try:
            opt = docopt(fn.__doc__, args)
        except DocoptExit as error:
            # The DocoptExit is thrown when the args do not match
            print('The command entered is invalid!')
            print(error)
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
        This function creates the header that is displayed when the app
        launches
    '''
    os.system("clear")
    print("\n")
    cprint(figlet_format('CHONJO', font='roman'), 'green')
    cprint('--------------------------------------------------------------------------', 'magenta')
    cprint("\t\tChonjo is a simple Commandline Pomodoro App.", 'yellow')
    cprint('--------------------------------------------------------------------------', 'magenta')
    cprint("\n\tNew to the app? Type 'help' to see a full list of commands\n", 'white')


def custom_print(arg, color='green'):
    ''' This is a simple print function that adds color to printed output. '''
    cprint("\n" + arg + "\n", color)


class ChonjoCLI(cmd.Cmd):
    '''
        This class creates Chonjo Command Line Interface for user interaction
    '''
    app_prompt = colored('Chonjo > ', 'green', attrs=['bold'])
    prompt = app_prompt

    @docopt_cmd
    def do_pomodoro_start(self, args):
        """
        Usage: pomodoro_start <task-title>...
        """
        # print "\n"
        chonjo.start(" ".join(args['<task-title>']))

    @docopt_cmd
    def do_pomodoro_config_time(self, args):
        """
        Usage: pomodoro_config_time <duration-in-minutes>
        """
        custom_print(chonjo.config_app(task_time=args['<duration-in-minutes>']))

    @docopt_cmd
    def do_pomodoro_config_short_break(self, args):
        """
        Usage: pomodoro_config_short_break <duration-in-minutes>
        """
        custom_print(chonjo.config_app(short_break=args['<duration-in-minutes>']))

    @docopt_cmd
    def do_pomodoro_config_long_break(self, args):
        """
        Usage: pomodoro_config_long_break <duration-in-minutes>
        """
        custom_print(chonjo.config_app(long_break=args['<duration-in-minutes>']))

    @docopt_cmd
    def do_pomodoro_config_sound(self, args):
        """
        Usage: pomodoro_config_sound <off/on>
        """
        custom_print(chonjo.config_app(sound=args['<off/on>']))

    @docopt_cmd
    def do_pomodoro_stop(self, args):
        """
        Usage: pomodoro_stop
        """
        chonjo.stop_app()

    @docopt_cmd
    def do_pomodoro_list(self, args):
        """
        Usage: pomodoro_list
        """
        chonjo.list_tasks()

    def do_quit(self, args):
        """ Quits the interactive mode """
        print("Saving current state to DB...")
        chonjo.stop_app()
        chonjo.save_state()
        print("Quiting App...")
        exit()


opt = docopt(__doc__, sys.argv[1:])


def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    chonjo.stop_app()
    print '\nChonjo > '
    # sys.exit(0)

if opt['--interactive']:
    app_header()
    chonjo = ChonjoApp()
    chonjo.load_state()
    signal.signal(signal.SIGINT, signal_handler)
    ChonjoCLI().cmdloop()

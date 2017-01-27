# Chonjo Pomodoro Time App

Chonjo, meaning alert in sheng' is a Pomodoro app which is a time management app. The app uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks of 5 minutes and a long break of 15 minutes


## Installation

Clone this repo:
```
$ git clone https://github.com/sumba254/bc-14-pomodoroApp.git
```

Navigate to the `bc-14-pomodoroApp` directory:
```
$ cd bc-14-pomodoroApp
```

Create a vitual environment and activate it.

Install the required packages:
```
$ pip install -r requirements.txt
```

## Usage

Run ```python app.py -i``` to launch the app in interactive mode

Basic usage and commands are shown below. You can also access this by typing `help` while in interactive mode of the app.

```
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
```


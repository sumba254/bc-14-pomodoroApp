# Pomodoro time app
Build a Pomodoro method timer with standard time periods. Each Pomodoro is a 25-minute cycle followed by a 5-minute break. After the fourth Pomodoro, the user takes a 15-minute break.

## Installation

`$ pip install -r requiremnts.txt`

## Usage
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


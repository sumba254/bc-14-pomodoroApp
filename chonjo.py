# -*-coding: utf-8 -*-
import sys
import time
import threading
import sqlite3 as lite
import subprocess
from datetime import datetime
from texttable import Texttable
from clock_font import translate, clear


class ChonjoApp(object):
    app_data = {}
    threads = []

    def __init__(self, task_time=15, short_break=4, long_break=10, sound=True):
        self.task_time = task_time
        self.short_break = short_break
        self.long_break = long_break
        self.sound = sound
        self.cycle = 0
        self.stop = False
        self.date_today = time.strftime("%d/%m/%Y")
        self.day_today = datetime.now().strftime('%A')
        self.day = self.day_today + ", " + self.date_today
        self.app_data[self.day] = {}

    def start(self, title):
        self.title = title
        self.start_time = datetime.now()
        # now let's save the small data we have to app_data
        self.app_data[self.day][self.title] = []
        self.app_data[self.day][self.title].append(time.strftime("%H:%M:%S"))
        # call the flow control thread here
        self.stop = False
        self.t = threading.Thread(target=self.flow_control)
        self.threads.append(self.t)
        self.t.start()

    def app_timer(self, minutes):
        while minutes:
            if self.stop is True:
                break
            mins, secs = divmod(minutes, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            # print(timeformat, end='\r')
            # print
            clear()
            print "\n\n\n\t\t\t\tPomodoro Task: " + self.title + "\n\n"
            translate(timeformat)
            print("\n\n\n")
            time.sleep(1)
            minutes -= 1

    def flow_control(self):
        """thread flow_control function"""
        # print("\n\n")
        while not self.stop:
            self.app_timer(self.task_time)
            # time.sleep(1)
            if self.cycle == 3:
                self.tone("long")
                self.app_timer(self.long_break)
                self.cycle = 0
            else:
                self.tone("short")
                self.app_timer(self.short_break)
                self.cycle += 1  # cycle increment

    def tone(self, period):
        if self.sound:
            if period == "short":
                sound_file = "beep.wav"
            else:
                sound_file = "bell.wav"
            # bell = sys.stdout.write('\a')
            sys.stdout.write('\a')
            sys.stdout.flush()
            subprocess.call(["afplay", sound_file])
            # wave_obj = sa.WaveObject.from_wave_file(sound_file)
            # play_obj = wave_obj.play()
            # play_obj.wait_done()

    def config_app(self, **kwargs):
        try:
            for key in kwargs:
                if key == 'task_time':
                    self.task_time = int(kwargs[key])
                elif key == 'short_break':
                    self.short_break = int(kwargs[key])
                elif key == 'long_break':
                    self.long_break = int(kwargs[key])
                elif key == 'sound':
                    if kwargs[key] == 'True' or kwargs[key] == 'False' or kwargs[key] == 'true' or kwargs[key] == 'false':
                        self.sound = kwargs[key]
                    else:
                        return "Sound only accepts 'True' or 'False'"
        except:
            return 'Please provide a number for all configurations except  sound which is a Boolean'
        sound_status = "Off"
        if self.sound == 'True' or self.sound == 'true':
            sound_status = "On"
        msg = "Your Configurations are as follows:"
        msg += "\nPomodoro Task Time: " + str(self.task_time)
        msg += "\nPomodoro Short Break: " + str(self.short_break)
        msg += "\nPomodoro Long Break: " + str(self.long_break)
        msg += "\nPomodoro Sound Status: " + sound_status
        return msg

    def stop_app(self):
        self.stop = True
        try:
            self.app_data[self.day][self.title].append(time.strftime("%H:%M:%S"))
        except:
            pass
        print "The current task has been stopped successfully"

    def list_tasks(self):
        print("\n\n")
        t = Texttable()
        t.add_rows([['Day', 'Title', 'Start Time', 'Stop Time']])
        for each_day in self.app_data:
            for each_task in self.app_data[each_day]:
                t.add_row(
                    [each_day,
                     each_task,
                     self.app_data[each_day][each_task][0],
                     self.app_data[each_day][each_task][1]])
        print t.draw()
        print("\n\n")

    def save_state(self):
        # let's first stop our daemon
        con = lite.connect('app_state.db')
        with con:
            cur = con.cursor()
            cur.executescript('''
                    DROP TABLE IF EXISTS Tasks;
                    CREATE TABLE Tasks(Id INTEGER PRIMARY KEY,
                    Day TEXT NOT NULL, Title TEXT NOT NULL,
                    'Start Time' TEXT NOT NULL, 'Stop Time' TEXT NOT NULL);
                    ''')
            for each_day in self.app_data:
                for each_task in self.app_data[each_day]:
                    cur.execute('''INSERT INTO Tasks (Day, Title, \
                        'Start Time', 'Stop Time') VALUES(?, ?, ?, ?)''',
                                (each_day, each_task,
                                    self.app_data[each_day][each_task][0],
                                    self.app_data[each_day][each_task][1]))
            return "All tasks have been saved to the DB"

    def load_state(self):
        con = lite.connect('app_state.db')
        with con:
            cur = con.cursor()
            self.app_data = {}
            cur.execute("SELECT * from Tasks")
            all_rows = cur.fetchall()
            for row in all_rows:
                if str(row[1]) not in self.app_data:
                    self.app_data[str(row[1])] = {}
                self.app_data[str(row[1])][str(row[2])] = []
                self.app_data[str(row[1])][str(row[2])].append(str(row[3]))
                self.app_data[str(row[1])][str(row[2])].append(str(row[4]))
            print "A previous app state has been loaded"
            return "A previous app state has been loaded"

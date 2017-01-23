# bc-14-promodoroApp
Build a Pomodoro method timer with standard time periods. 
Each Pomodoro is a 25-minute cycle followed by a 5-minute break. 
After the fourth Pomodoro, the user takes a 15-minute break. As a user, 
I should be able to adjust my settings to determine how long each pomodoro takes, other than the default timings.

The app has the following commands:
    pomodoro start <task-title> - Starts a pomodoro timer and records the task-title and start-time/date. 
        Play a gentle bell-ring sound (e.g. this) to signify the end of every pomodoro cycle.
    pomodoro config time <duration-in-minutes> - Sets the duration for a pomodoro. By default, it’s 25 minutes.
    
    pomodoro config short_break <duration-in-minutes> - Sets the duration for the short break in between a pomodoro task. 
        By default, it’s 5 minutes.
    pomodoro config long_break <duration-in-minutes> - Sets the duration for the long break in between a pomodoro task.
    
    pomodoro config sound <off/on> - Turn off or on the sound notification.
    
    pomodoro stop - Marks the end end of the current running pomodoro task; and marks the task as complete.
    
    pomodoro list - List all the pomodoro tasks done on a particular day, and details on how many pomodoro cycles spent on each task.

All data should be persisted in an SQLite database.


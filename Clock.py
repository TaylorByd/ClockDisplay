from datetime import datetime

class Clock:
    def __init__(self):
        self.time = datetime.now()
        self.date = datetime.now()
        self.day = datetime.today()
    def get_time(self):
        current_time = self.time.strftime("%I:%M:%S %p")
            # formats the time to be HH:MM:SS am/pm
        if (current_time[0] == '0'):
            current_time = current_time[1:]
            # if the hour of time has a 0 at the start of the string, skip that character of the string.
        return current_time

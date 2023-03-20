from datetime import datetime

class Clock:
    def __init__(self):
        self.time = datetime.now()
        self.date = datetime.now()
        self.day = datetime.today()
    def get_time(self):
        self.time = datetime.now()
        current_time = self.time.strftime("%I:%M:%S %p")
            # formats the time to be HH:MM:SS am/pm
        if (current_time[0] == '0'):
            current_time = current_time[1:]
            # if the hour of time has a 0 at the start of the string, skip that character.
        return current_time
    def get_date(self):
        self.date = datetime.now()
        current_date = self.date.strftime("%m/%d/%Y")
            # formats the date to be MM/DD/YYYY
        if (current_date[0] == '0'):
            current_date = current_date[1:]
            # if the start of the date has a 0 at the start of the string, skip the character.
        return current_date
    def get_day(self):
        self.day = datetime.today()
        current_day = self.day.strftime("%A")
            # formats to string to show the day of the week
        return current_day

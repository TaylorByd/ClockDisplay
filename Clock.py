from datetime import datetime

class Clock:
    def __init__(self):
        self.time = datetime.now()
        self.date = datetime.now()
        self.day = datetime.today()
        

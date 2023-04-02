from Clock import Clock
from tkinter import Label, Tk

class ClockWindow(Clock):
    def __init__(self): 
        self.window = Tk()
        self.font_time = ('Arial', 150)
        self.time_label = Label(text= "", font= self.font_time)
        self.time_label.pack(padx=50, pady=50)
        self.update_clock()
        self.window.attributes('-fullscreen', True)

    def setup_time_font(self, font_type, font_size):
        self.font_time = (font_type, font_size)
        self.time_label.configure(font= self.font_time)
    
    def setup_day_font(self, fontsize, font_type):
        return
    
    def setup_date_font(self, fontsize, font_type):
        return
   
    def setup_font_color(self, font_color):
        return

    def setup_background_color(self, background_color):
        return

    def setup_background_img(self, url):
        return

    def create_background_img(self):
        return

    def update_clock(self):
        self.time_label.configure(text=Clock.get_time(self))
        self.window.after(100, self.update_clock)
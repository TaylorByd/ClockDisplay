from Clock import Clock
from tkinter import Tk, Canvas

class ClockWindow(Clock):
    def __init__(self): 
        self.window = Tk()
        self.my_canvas = Canvas(self.window, bg= "black", highlightthickness=0)
        self.font_time = ('Arial', 150)
        self.update_clock()
        self.window.attributes('-fullscreen', True)

    def setup_time_font(self, font_type, font_size):
        return
    
    def setup_day_font(self, fontsize, font_type):
        return
    
    def setup_date_font(self, fontsize, font_type):
        return
   
    def setup_color(self, font_color, background_color):
        return

    def setup_background_img(self, url):
        return

    def create_background_img(self):
        return

    def update_clock(self):
        self.window.after(100, self.update_clock)
from Clock import Clock
from tkinter import Label, Tk

class ClockWindow(Clock):
    def __init__(self): 
        window = Tk()
        self.time_label = Label(window, text= "")
        self.date_label = Label(window, text= "")
        self.date_label = Label(window, text= "")
        self.time_label.pack(padx=10, pady=10)
        window.attributes('-fullscreen', True)
        window.mainloop()

    def setup_time_font(self, fontsize, font_type):
        return
    
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

    def set_text(self):
        return
from Clock import Clock
from tkinter import Tk, Canvas

class ClockWindow(Clock):
    def __init__(self): 
        # defining the window, and the screen width and height.
        self.window = Tk()
        self.win_width = self.window.winfo_screenwidth()
        self.win_height = self.window.winfo_screenheight()
        # defining the canvas with its default background color
        self.my_canvas = Canvas(self.window, bg= "black", highlightthickness=0)
        self.my_canvas.pack(fill="both", expand=True)
        # creating the text on the canvas
        self.font_time = ('Arial', 150)
        self.time_label = self.my_canvas.create_text(self.win_width / 2, self.win_height / 2, 
                                                     text= "", fill= "white", font= self.font_time)
        # updating the clock text in intervals of 100 ms
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
        self.my_canvas.itemconfig(self.time_label, text=Clock.get_time(self))
        self.window.after(100, self.update_clock)
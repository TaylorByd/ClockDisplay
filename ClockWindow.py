from Clock import Clock
from tkinter import Tk, Canvas
from PIL import Image
from PIL import ImageTk

class ClockWindow(Clock):
    def __init__(self): 
        self.background_setup = False
        # defining the window, and the screen width and height.
        self.window = Tk()
        self.win_width = self.window.winfo_screenwidth()
        self.win_height = self.window.winfo_screenheight()
        # defining the canvas with its default background color
        self.my_canvas = Canvas(self.window, bg= "black", highlightthickness=0)
        self.bg_img = 0
        self.my_canvas.pack(fill="both", expand=True)
        # used for deleting a background image it is already set
        self.image_bg_id = self.my_canvas.create_image(0, 0)
        # creating the text on the canvas
        self.font_time = ('Arial', 150)
        self.time_label = self.my_canvas.create_text(self.win_width / 2, self.win_height / 2, 
                                                     text= "", fill= "white", font= self.font_time)
        # updating the clock text in intervals of 100 ms
        self.update_clock()
        self.window.attributes('-fullscreen', True)

    def setup_time_font(self, font_type, font_size):
        self.font_time = (font_type, font_size)
        self.my_canvas.itemconfig(self.time_label, font= self.font_time)
    
    def setup_day_font(self, fontsize, font_type):
        return
    
    def setup_date_font(self, fontsize, font_type):
        return
   
    def setup_color(self, font_color, background_color):
        if (self.background_setup == True):
            self.my_canvas.delete(self.image_bg_id)
        self.my_canvas.itemconfig(self.time_label, fill= font_color)
        self.my_canvas.configure(bg= background_color)
        self.background_setup = False

    def setup_background_img(self, url):
        img_read = Image.open(url)
        img_resized = img_read.resize((self.win_width, self.win_height), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(img_resized)
        self.image_bg_id = self.my_canvas.create_image(0, 0, image= self.bg_img, anchor= "nw")
        self.time_label = self.my_canvas.create_text(self.win_width / 2, self.win_height / 2, 
                                                    text= "", fill= "white", font= self.font_time)
        self.background_setup = True

    def update_clock(self):
        self.my_canvas.itemconfig(self.time_label, text=Clock.get_time(self))
        self.window.after(100, self.update_clock)
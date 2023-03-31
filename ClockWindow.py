from Clock import Clock
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt

class ClockWindow(QWidget, Clock):
    def __init__(self): 
        super().__init__()
    # These are the variables that will be used in the background image method
        self.background_img_set = False
        self.background_img = QLabel()
    # default font options
        self.font_time = QFont('Arial', 150)
        self.font_day = QFont('Arial', 75)
        self.font_date = QFont('Arial', 75)
        self.font_color = 'cyan'
    # setting up all the lables with the default font options
        self.time_label = QLabel()
        self.time_label.setFont(self.font_time)
        self.time_label.setStyleSheet(f"color: {self.font_color};")
        self.date_label = QLabel()
        self.date_label.setFont(self.font_date)
        self.date_label.setStyleSheet(f"color: {self.font_color};")
        self.day_label = QLabel()
        self.day_label.setFont(self.font_day)
        self.day_label.setStyleSheet(f"color: {self.font_color};")
	# creating a horizontal layout with a day label and date label
        hbox = QHBoxLayout()
        hbox.addWidget(self.day_label)
        hbox.addWidget(self.date_label)
        hbox.setAlignment(Qt.AlignCenter)
	# combining the horizontal layout of the date label and day label with the vertical layout of the time label
    # This is effectively nesting two layouts together
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.time_label)
        self.vbox.addLayout(hbox)
        self.vbox.setAlignment(Qt.AlignCenter)
        self.setLayout(self.vbox)
	# This is a timer that will execute the function every 100 milliseconds
        timer = QTimer(self)
        if (self.background_img_set == True):
            timer.timeout.connect(self.setup_background_img)
            timer.start(100)
        else:
            timer.timeout.connect(self.set_text)
            timer.start(100)
    
    def setup_time_font(self, fontsize, font_type):
        self.font_time = QFont(f'{font_type}', fontsize)
        self.time_label.setFont(self.font_time)
    
    def setup_day_font(self, fontsize, font_type):
        self.font_day = QFont(f'{font_type}', fontsize)
        self.day_label.setFont(self.font_day)
    
    def setup_date_font(self, fontsize, font_type):
        self.font_date = QFont(f'{font_type}', fontsize)
        self.date_label.setFont(self.font_date)
   
    def setup_font_color(self, font_color):
        self.font_color = font_color
        self.day_label.setStyleSheet(f"color: {font_color};")
        self.time_label.setStyleSheet(f"color: {font_color};")
        self.date_label.setStyleSheet(f"color: {font_color};")

    def setup_background_color(self, background_color):
        self.setStyleSheet(f"background-color: {background_color};")

    def setup_background_img(self, url):
        self.background_img_set = True

    def set_text(self):
        self.day_label.setText(Clock.get_day(self) + " ")
        self.date_label.setText(Clock.get_date(self))
        self.time_label.setText(Clock.get_time(self))
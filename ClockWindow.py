from Clock import Clock
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt

class ClockWindow(QWidget, Clock):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel()
        self.date_label = QLabel()
        self.day_label = QLabel()
        # creating a horizontal layout with a day label and date label
        hbox = QHBoxLayout()
        hbox.addWidget(self.day_label)
        hbox.addWidget(self.date_label)
        hbox.setAlignment(Qt.AlignCenter)
        # combining the horizontal layout of the date label and day label with the vertical layout of the time label
        # This is effectively nesting two layouts together
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)
        vbox.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)
        # This is timer that will execute the function every 100 milliseconds
        timer = QTimer(self)
        timer.timeout.connect(self.set_text)
        timer.start(100)
    
    def setup_time_font(self, fontsize, font_type):
        font = QFont(f'{font_type}', fontsize)
        self.time_label.setFont(font)
    
    def setup_day_font(self, fontsize, font_type):
        font = QFont(f'{font_type}', fontsize)
        self.day_label.setFont(font)
    
    def setup_date_font(self, fontsize, font_type):
        font = QFont(f'{font_type}', fontsize)
        self.date_label.setFont(font)
   
    def setup_font_color(self, font_color):
        self.day_label.setStyleSheet(f"color: {font_color};")
        self.time_label.setStyleSheet(f"color: {font_color};")
        self.date_label.setStyleSheet(f"color: {font_color};")

    def setup_background_color(self, background_color):
        self.setStyleSheet(f"background-color: {background_color};")

    def set_text(self):
        self.day_label.setText(Clock.get_day(self) + " ")
        self.date_label.setText(Clock.get_date(self))
        self.time_label.setText(Clock.get_time(self))
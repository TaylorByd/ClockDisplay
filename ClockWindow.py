from Clock import Clock
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont

class ClockWindow(QWidget, Clock):
    def __init__(self):
        super.__init__()
        self.time_label = QLabel()
        self.date_label = QLabel()
        self.day_label = QLabel()
    def setup_font(self, fontsize, font_type):
        font = QFont(f'{font_type}', fontsize)
        self.time_label.setFont(font)
        self.date_label.setFont(font)
        self.day_label.setFont(font)
    def setup_color(self,background_color, font_color):
        self.setStyleSheet(f"background-color: {background_color};")
        self.day_label.setStyleSheet(f"color: {font_color};")
        self.time_label.setStyleSheet(f"color: {font_color};")
        self.date_label.setStyleSheet(f"color: {font_color};")
    def set_text(self):
        self.day_label.setText(Clock.get_date())
        self.date_label.setText(Clock.get_date())
        self.time_label.setText(Clock.get_time())
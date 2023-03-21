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


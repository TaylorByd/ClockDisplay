from ClockWindow import ClockWindow
from PyQt5.QtWidgets import QApplication
import sys

App = QApplication(sys.argv)
 
clock_window = ClockWindow()
clock_window.setup_time_font(150, 'Arial')
clock_window.setup_day_font(75, 'Arial')
clock_window.setup_date_font(75, 'Arial')
clock_window.setup_font_color('white')
clock_window.setup_background_color('black')

clock_window.showMaximized()

App.exit(App.exec_())
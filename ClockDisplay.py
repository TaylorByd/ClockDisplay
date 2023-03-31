from ClockWindow import ClockWindow
from PyQt5.QtWidgets import QApplication
import sys

App = QApplication(sys.argv)
clock_window = ClockWindow()
clock_window.setup_background_img('test2.png')

clock_window.showMaximized()

App.exit(App.exec_())
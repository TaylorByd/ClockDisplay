from ClockWindow import ClockWindow

clock_window = ClockWindow()
clock_window.setup_time_font('times new roman', 150)
clock_window.setup_background_img("test.png")
clock_window.window.mainloop()
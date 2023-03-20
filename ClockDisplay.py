import Clock
import time
clock = Clock.Clock()

while True:
    time.sleep(0.1)
    print(clock.get_time())
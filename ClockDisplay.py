from Clock import Clock
import time
clock = Clock()
while True:
    time.sleep(0.1)
    print(clock.get_time())
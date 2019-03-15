#! python3
#stopwatch.py - a simple stopwatch program

import time
#display instructions

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch Press CTRL-C to quit.')
input() #press enter to begin
print('Started.')
startTime = time.time() #grabs the first 'lap's' startime
lastTime = startTime
lapNum = 1

#TODO Start tracking laptimes
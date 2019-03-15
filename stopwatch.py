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


try: 
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # resets the last laptime

except KeyboardInterrupt:
	#Handle the ctrl-c exception to keep its error message from displaying.
	print('\nDone!') 
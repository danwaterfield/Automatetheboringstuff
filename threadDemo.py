import threading, time
print('Start of program.')

def takeANap(): #defines function for use in a new thread
	time.sleep(5)
	print('Wake up!')

threadObj = threading.Thread(target=takeANap) #calls function in new thread.
threadObj.start()

print('End of program!')
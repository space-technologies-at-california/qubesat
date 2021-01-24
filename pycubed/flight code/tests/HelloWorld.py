import time
import board

# print a string only once
print('Hello World!')

# ------- MAIN LOOP -------
while True:
	# print a string followed by the time in seconds since boot
	print('Time on: ',time.monotonic())
	time.sleep(0.1) # sleep 1 second
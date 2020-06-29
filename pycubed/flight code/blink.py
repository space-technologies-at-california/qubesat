import time
import board
import neopixel

# Initialize an instance of the neopixel class called "RGB"
RGB = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5, auto_write=True)

# ------- MAIN LOOP -------
delay = 2 # make bigger to slow down
i = 0 # a counter to increment each loop
while True:
  print(i)
  RGB[0] = (0,255,0) # pure green in Red,Green,Blue format
  time.sleep(delay)
  RGB[0] = (0,0,0) # turn the NeoPixel off
  time.sleep(delay)
  i += 1
import neopixel
import board
pixel = neopixel.NeoPixel(board.IO12, 1, brightness=0.2)
pixel[0] = (255,0,255)  # equivalent

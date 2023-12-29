import board
import displayio
import busio
from adafruit_displayio_sh1106 import SH1106
import adafruit_imageload

# Release any resources currently in use for the displays
displayio.release_displays()

i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# Define the width and height of the display
WIDTH = 128
HEIGHT = 64
display = SH1106(display_bus, width=WIDTH, height=HEIGHT)

maingroup = displayio.Group() # everything goes in maingroup
display.root_group = maingroup # set the root group to display
bitmap, palette = adafruit_imageload.load("goofnug.bmp")
image = displayio.TileGrid(bitmap, pixel_shader=palette)
maingroup.append(image) # shows the image

while True:
    pass

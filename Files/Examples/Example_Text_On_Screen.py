import board
import displayio
import terminalio
from adafruit_display_text import label
import busio
from adafruit_displayio_sh1106 import SH1106

# Release any resources currently in use for the displays
displayio.release_displays()

i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# Define the width and height of the display
WIDTH = 128
HEIGHT = 64
display = SH1106(display_bus, width=WIDTH, height=HEIGHT)

# Create a display group
group = displayio.Group()

# Create a text label
text = "Hallo World"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)

# Center the text
text_area.x = WIDTH // 2 - text_area.bounding_box[2] // 2
text_area.y = HEIGHT // 2 - text_area.bounding_box[3] // 2

# Add the text label to the display group
group.append(text_area)

# Show the group on the display
display.root_group = group  # Updated line

while True:
    pass  # Loop forever

import touchio
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

touch_pin = touchio.TouchIn(board.IO12)

while True:
    if touch_pin.value:
        led.value = True
    else:
        led.value = False

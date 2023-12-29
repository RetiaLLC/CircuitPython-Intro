# Skicka 2023 - Turn on an LED for 1 second
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(1)

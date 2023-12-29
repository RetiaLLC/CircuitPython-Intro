import board # Allows us to use the board.LED pin
import digitalio # Allows us to use digital input/output pins

# Initialize the LED pin as an output
led = digitalio.DigitalInOut(board.LED) # Create a new DigitalInOut object for the board.LED pin
led.direction = digitalio.Direction.OUTPUT # Set the direction of the pin to OUTPUT

while True:
    print("Type ON to turn on LED, OFF to turn it off: ", end='')
    my_str = input().lower()  # type and press ENTER or RETURN
    if 'on' in my_str: # If we see the "on" command over serial
        led.value = True # Turn on the LED
    if 'off' in my_str: # If we see the "off" command over serial
        led.value = False # Turn off the LED
    if 'on' not in my_str and 'off' not in my_str: # If we see a value that matches neither
        print("IDK what this means: ", my_str) # Express confusion

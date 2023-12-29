# 2023 by Skickar for Retia LLC
# Import the necessary libraries
import time # Allows us to use the time.sleep() function
import board # Allows us to use the board.LED pin
import digitalio # Allows us to use digital input/output pins

# Initialize the LED pin as an output
led = digitalio.DigitalInOut(board.LED) # Create a new DigitalInOut object for the board.LED pin
led.direction = digitalio.Direction.OUTPUT # Set the direction of the pin to OUTPUT

# Enter an infinite loop that toggles the LED on and off once per second
while True:
    led.value = not led.value # Toggle the value of the LED pin (on/off)
    if led.value: # If the LED is on...
        print("LED is ON") # Print "LED is ON" to the terminal
    else: # Otherwise (if the LED is off)...
        print("LED is OFF") # Print "LED is OFF" to the terminal
    time.sleep(1) # Wait for 1 second before repeating the loop

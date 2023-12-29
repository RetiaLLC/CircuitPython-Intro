import board
import pwmio
import time

out1 = pwmio.PWMOut(board.LED, frequency=25000, duty_cycle=0) # Create a PWM output on the LED pin
out1.duty_cycle = 32768 # Set one example value

while True: # Fade in and out loop
    for i in range(100): # Fade in
        out1.duty_cycle = int(i * 65535 / 100) # Increase duty cycle
        time.sleep(0.01)  # Wait for 10ms

    for i in range(100, -1, -1): # Fade out
        out1.duty_cycle = int(i * 65535 / 100) # Decrease duty cycle
        time.sleep(0.01)  # Wait for 10ms

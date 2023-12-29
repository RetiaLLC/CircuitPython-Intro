import time, board, digitalio

# Define the buttons with their corresponding directions
buttons = {
    'up': digitalio.DigitalInOut(board.IO9),
    'down': digitalio.DigitalInOut(board.IO18),
    'left': digitalio.DigitalInOut(board.IO11),
    'right': digitalio.DigitalInOut(board.IO7)
}

# Initialize the buttons
for button in buttons.values():
    button.switch_to_input(pull=digitalio.Pull.UP)

# Main loop
while True:
    for direction, button in buttons.items():
        if not button.value:  # Button is pressed
            print(f"{direction} button pressed!")
    time.sleep(0.1)  # Debounce delay

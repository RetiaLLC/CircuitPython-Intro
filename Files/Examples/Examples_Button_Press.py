import time, board, digitalio

button = digitalio.DigitalInOut(board.IO18) #Down Button
button.switch_to_input(digitalio.Pull.UP)

while True:
    if button.value == False:
        print("button pressed!")
    time.sleep(0.1)

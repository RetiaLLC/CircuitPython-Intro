import time, board, digitalio

button = digitalio.DigitalInOut(board.IO18) #Down Button
# Down button - IO18
# Up button - IO9
# Left button - IO11
# Right button - IO7
button.switch_to_input(digitalio.Pull.UP)



while True:
    if button.value == False:
        print("button pressed!")
    time.sleep(0.1)

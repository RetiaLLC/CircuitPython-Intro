import touchio
import board
touch_pin = touchio.TouchIn(board.IO12)

while True:
    if touch_pin.value:
        print("touched!")

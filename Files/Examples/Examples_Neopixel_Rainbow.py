import supervisor, board, neopixel, rainbowio
num_leds = 1
speed = 10  # lower is faster, higher is slower
leds = neopixel.NeoPixel(board.IO12, num_leds, brightness=0.4)

while True:
  t = supervisor.ticks_ms() / speed
  leds[:] = [rainbowio.colorwheel( t + i*(255/len(leds)) ) for i in range(len(leds))]

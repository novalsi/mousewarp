#!/usr/bin/env python3

import time
import subprocess

SCALE = 2
TICK = 0.01
WARP_COOLDOWN = 0.3

last_time = 0
last_x = 0

def get_mouse():
    out = subprocess.check_output(['xdotool', 'getmouselocation', '--shell']).decode()
    vals = dict(line.split('=') for line in out.strip().splitlines())
    return int(vals['X']), int(vals['Y'])

def warp(x, y):
    subprocess.call(['xdotool', 'mousemove', str(x), str(y)])

while True:
    x, y = get_mouse()
    dx = x - last_x
    now = time.time()

    if now - last_time > WARP_COOLDOWN:

        # LEFT to CENTER
        if 1900 <= x <= 1930 and y <= 1079 and dx > 0:
            new_y = min(y * SCALE, 2159)
            warp(1930, int(new_y))
            print(f"→ LEFT → CENTER: 1930, {int(new_y)}")
            last_time = now

        # RIGHT to CENTER
        elif 5740 <= x <= 5770 and y <= 1079 and dx < 0:
            new_y = min(y * SCALE, 2159)
            warp(5740, int(new_y))
            print(f"→ RIGHT → CENTER: 5740, {int(new_y)}")
            last_time = now

        # CENTER to LEFT
        elif 1900 <= x <= 1930 and y <= 2159 and dx < 0:
            new_y = int(y / SCALE)
            warp(1910, new_y)
            print(f"→ CENTER → LEFT: 1910, {new_y}")
            last_time = now

        # CENTER to RIGHT
        elif 5740 <= x <= 5770 and y <= 2159 and dx > 0:
            new_y = int(y / SCALE)
            warp(5765, new_y)
            print(f"→ CENTER → RIGHT: 5765, {new_y}")
            last_time = now

    last_x = x
    time.sleep(TICK)


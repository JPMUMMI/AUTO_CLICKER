import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import sys

clicking = False
mouse = Controller()
click_event = threading.Event()

def clicker():
    while True:
        click_event.wait()
        mouse.click(Button.left, 1)
        time.sleep(0.01)

def toggle_event(key):
    global clicking
    if key == KeyCode.from_char('c'):
        clicking = not clicking
        if clicking:
            click_event.set()
        else:
            click_event.clear()
    elif key == KeyCode.from_char('q'):
        listener.stop()
        sys.exit()

click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

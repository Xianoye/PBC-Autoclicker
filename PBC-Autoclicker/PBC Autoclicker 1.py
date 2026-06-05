# VERSION 1.0
import time
import threading
import os
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

toggle_key = KeyCode(char="o")
exit_key = KeyCode(char="p")
clicking = False
mouse = Controller()
button = None

print("Welcome to PBC Autoclicker")
right_or_left = input("Right or Left mouse button? R/L: ")
if right_or_left.lower() in ["right", "r"]:
    button = Button.right
elif right_or_left.lower() in ["left", "l"]:
    button = Button.left
else:
    print("Invalid choice, defaulting to Left click.")
    button = Button.left

print(f"{button} is the chosen key.")
print()
print("Press 'O' to toggle.")
print("Press 'P' to quit.")


def clicker():
    while True:
        if clicking:
            mouse.click(button, 1)
        time.sleep(0.001)


def on_press_event(key):
    global clicking

    # Toggle functionality
    if key == toggle_key:
        clicking = not clicking
        print(f"Autoclicker toggled: {'ON' if clicking else 'OFF'}")

    # Exit functionality
    elif key == exit_key:
        print("\nExiting program...")
        os._exit(0)


# Start the clicker thread
click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

# Start the listener
with Listener(on_press=on_press_event) as listener:
    listener.join()

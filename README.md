# PRODIGY_CS_04
Simple Keylogger Tool
This Python script logs keystrokes using the pynput library and saves them to a file. The keylogger runs in the background, recording every key pressed until the ESC key is pressed, which stops the logging process.

How to Use
Install Dependencies: Ensure you have the pynput library installed. You can install it using pip:

pip install pynput
Run the script:

python keylogger.py
Keystrokes are logged:

All keystrokes will be saved to key_log.txt in the same directory as the script.
The script continues running until the ESC key is pressed.
Example
The script creates a file named key_log.txt and appends each keypress to this file.
Pressing the ESC key will stop the logging process and close the file.

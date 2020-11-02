
from pyfirmata import Arduino

import time                                         # Time

import pyautogui                        
            # Module for programmatically controlling the mouse and keyboard
arduino=Arduino('dev/cu.usbmodem411')

time.sleep(2)                                       # Wait for Arduino

  
while True:
    x, y = pyautogui.position();                    # Get the position of the mouse
    x = (x)*0.141;                                  # Get just x axis and map[0-1270 Scream Size to 0 - 180 turning angle]
    x = (int(x))                                    # Covertion to Integer Values
    x = str(x)                                      # Convert it into string
    x = str.encode(x)                               # Encoding strings
    arduino.write(x)                                # Send data by the port selected
    time.sleep(1.5)                                 # Delay(ms), If you have a servo with quick response decrease the time
    print(x)                                        # See the actual position
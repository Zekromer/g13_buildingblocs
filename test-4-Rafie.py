from microbit import *

while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    
    if readings_y > 20:
        display.show("F")
    elif reading_y < -20:
        display.show("B")
    else:
        display.show("~")
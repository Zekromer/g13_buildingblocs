from microbit import *

while true:
    presses = button_a.get_presses()
    if presses > 5: 
        display.show(Image.DIAMOND)
    else:
        display.show(Image.ANGRY)
    sleep(2000)
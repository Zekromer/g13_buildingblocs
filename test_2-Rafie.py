from microbit import *


test = Image("05050:"
             "50505:"
             "05050:"
             "50505:"
             "05050")
test2 = Image("50505:"
              "05050:"
              "50505:"
              "05050:"
              "50505")
tests =[test , test2]
while True:
    if button_b.is_pressed():
        display.show(tests , delay = 200)
    elif button_a.is_pressed():
        display.show(Image.SMILE)
    else:
        display.show(Image.SAD)
         
        
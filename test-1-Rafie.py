from microbit import *

# Write your code here :-)
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
    display.show(tests , delay = 200)      
        
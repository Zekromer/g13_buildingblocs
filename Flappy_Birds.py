from microbit import *

DELAY = 20
FPS_wall = 20
FPS_nwall = 100
Frames_per_score= 50
import random 
y = 50
speed=0
score=0
frame=0
def make_pipe():
    pipe = Image("00003:00003:00003:00003:00003")
    """00003
       00003
       00003
       00003
       00003
       """
    gap = random.randint(0,3)
    
    pipe.set_pixel(4, gap, 0)
    pipe.set_pixel(4, gap+1, 0)
    return pipe
    
pipe=make_pipe()

while True:
    
    display.show(pipe)
    
    if button_a.is_pressed():
        speed = -3
    speed += 1
    if speed > 2:
        speed = 2
        
        
    y += speed
    if y > 99:
        y = 99
    if y < 0:
        y = 0
            
   
    bird_y = int(y/20)
    display.set_pixel(1 , bird_y ,9)
    
    
    if pipe.get_pixel(1,bird_y) !=0:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("Score:" + str(score))
        break
        
    if frame % FPS_wall == 0:
        pipe = pipe.shift_left(1)
        
    if frame % FPS_nwall == 0:
        pipe = make_pipe()
        
    if frame % Frames_per_score == 0:
        score += 1
    sleep(DELAY)
    frame += 1
        
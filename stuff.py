from microbit import *
import music
tune1=["G4:2", "A4:1", "B4:1", " G4:2", "F4:1", "G4:2", "F4:1", "G4:2", "A4:1", "F4:2"]
tune2=["B3:1", "E4:1", "F4:1", "G4:2", "G4:2", "G4:1", "F4:1", "E4:1", "D4:1", "E4:2", "E4:2", "E4:1", "D4:1", "C4:1", "B3:1", "C4:2", "B3:2", "E4:1", "F4:1", "E4:1", "D4:2"]

x = 0
y = 0
while True:
    
    if button_a.is_pressed():
        x += 1
        if x > 1:
            display.show(Image.HAPPY)
            music.play(tune2)
        
        else:
            display.show(Image.SAD)
            music.play(music.NYAN)
            
    elif button_b.is_pressed():
        display.show("Thank you!" ,delay = 1000)
        
    
        
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
            
     
   
        
    
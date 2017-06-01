from microbit import *
boat1 = Image("10111:"
             "10100:"
             "11111:"
             "00101:"
             "11101")
boat2 = Image("20222:"
             "20200:"
             "22222:"
             "00202:"
             "22202")
boat3 = Image("30333:"
             "30300:"
             "33333:"
             "00303:"
             "33303")
boat4 = Image("40444:"
             "40400:"
             "44444:"
             "00404:"
             "44404")
boat5 = Image("50555:"
             "50500:"
             "55555:"
             "00505:"
             "55505")
boat6 = Image("60666:"
             "60600:"
             "66666:"
             "00606:"
             "66606")
boat7 = Image("70777:"
             "70700:"
             "77777:"
             "00707:"
             "77707")
boat8 = Image("80888:"
             "80800:"
             "88888:"
             "00808:"
             "88808")
boat9 = Image("90999:"
             "90900:"
             "99999:"
             "00909:"
             "99909")
boat0 = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00000")
all=[boat1,boat2,boat3,boat4,boat5,boat6,boat7,boat8,boat9]
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        display.show(all , delay=100)
    else:
        display.show(boat0)
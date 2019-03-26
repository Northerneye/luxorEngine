import time
import luxor
while(True):
    luxor.refreshbackground("-", luxor.colors.green, backgroundcolor = luxor.backcolor.blue)
    luxor.createborder(luxor.colors.red)
    luxor.sprite(9,6,"B",luxor.colors.white,1,True)
    luxor.sprite(14,5,"=",luxor.colors.white,2,False)
    luxor.sprite(3,5,"A",luxor.colors.magenta,0, True)
    if(luxor.onsprite(1)):
        luxor.style[9][6] = luxor.styles.underline
        luxor.speech = "B: please get off me"
    else:
        luxor.style[9][6] = luxor.styles.bright
    if(luxor.nearsprite(1)):
        luxor.speech = "B: hello, how are you?"
    luxor.controls()
    luxor.collisions()
    luxor.movement()
    luxor.graphics()
    if(luxor.key==27):
        break

from turtle import *
from random import *


colormode(255)
pensize(4)

color_red = randint(0,255)
color_green = randint(0,255)
color_blue = randint(0,255)

print((color_red, color_green, color_blue))

def carre():
    for i in range(4):
            forward(100)
            left(90)

def ligne():
    fillcolor(color_red, color_green, color_blue)
    begin_fill()
    for i in range(4):    
        carre()
        forward(100)
    end_fill()
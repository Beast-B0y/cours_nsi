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

def tetro_s():
    fillcolor(color_red, color_green, color_blue)
    begin_fill()
    carre()
    forward(100)
    carre()
    left(90)
    end_fill()
    forward(100)
    right(90)
    begin_fill()
    carre()
    forward(100)
    carre()
    end_fill()

tetro_s()
done


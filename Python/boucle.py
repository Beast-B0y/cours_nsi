from turtle import *
from random import randint
pensize(5)

def poly_n(n):
    a = 360/n
    for i in range(n):
        forward(100)
        left(a)

def poly_alea():
    n = randint(3,10)
    while n > 3 :
        poly_n(n)
        n = randint(3,10)
    color("red")
    poly_n(3)
    
poly_alea()
done
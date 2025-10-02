import turtle
import time
import random

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))



def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.penup()

def main():
    screen = turtle.Screen()
    screen.title("Étoiles")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(6)
    

    while True:  
        size = 40
        spacing = 30
        baseline = -150
        x = -900

        for i in range(random.randint(5,10)):
            taille = random.randint(0,25)
            t.pensize(taille)
            color = random_color()  
            y = baseline + (size / 2)
            draw_star(t, x, y, size, color)
            next_size = int(size * 1.5)
            x += (size / 2) + spacing + (next_size / 2)
            size = next_size
            
                
        time.sleep(1)  
        #t.clear()      

    screen.mainloop()

if __name__ == "__main__":
    main()
    


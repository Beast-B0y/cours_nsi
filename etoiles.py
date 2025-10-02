import turtle

colors = [
    "#FF6F61",  # corail
    "#FFD700",  # or
    "#6A5ACD",  # bleu violacé
    "#3CB371",  # vert menthe
    "#FF69B4"   # rose vif
]

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
    t.pensize(4)  

    size = 40
    spacing = 30
    baseline = -150
    x = -300

    for i in range(5):
        color = colors[i % len(colors)]
        y = baseline + (size / 2)
        draw_star(t, x, y, size, color)
        next_size = int(size * 1.5)
        x += (size / 2) + spacing + (next_size / 2)
        size = next_size

    screen.mainloop()

if __name__ == "__main__":
    main()

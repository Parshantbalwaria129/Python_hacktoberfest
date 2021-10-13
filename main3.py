import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(600,500)
screen.bgcolor('black')
turtle.colormode(255)
t.ht()
t.speed(50)
x = 0
r = 254
g = 0
b = 0


for angle in range(0, 360, 2):
    tup = (r, g, b)
    t.pencolor(tup)

    for i in range(1, 5):
        if r == 254 and g < 254 and b == 0:
            g += 2
        elif r > 0 and g == 254 and b == 0:
            r -= 2
        elif r == 0 and g == 254 and b < 254:
            b += 2
        elif r == 0 and g > 0 and b == 254:
            g -= 2
        elif r < 254 and g == 0 and b == 254:
            r += 2
        elif r == 254 and g == 0 and b > 0:
            b -= 2
    for i in range(2):
        # two arcs
        t.circle(100, 90)
        t.circle(100 // 3, 90)
    t.seth(angle)
turtle.done()

import turtle
import random


window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('blue')
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)


ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
ball.shapesize(1)
ball.up()
randx = random.randint(0, 290)
randy = random.randint(0, 290)

ball2 = turtle.Turtle()
ball2.hideturtle()
ball2.shape('circle')
ball2.shapesize(1)
ball2.up()
randx2 = random.randint(-290, 0)
randy2 = random.randint(-290, 0)

ball3 = turtle.Turtle()
ball3.hideturtle()
ball3.shape('circle')
ball3.shapesize(1)
ball3.up()
randx3 = random.randint(-100, 100)
randy3 = random.randint(-100, 100)

ball.goto(randx, randy)
ball.showturtle()
dx = 7
dy = 8
ball2.goto(randx2, randy2)
ball2.showturtle()
dx2 = 7
dy2 = 8

ball3.goto(randx3, randy3)
ball3.showturtle()
dx3 = 7
dy3 = 8

while True:
    x, y = ball.position()
    x2, y2 = ball2.position()
    x3, y3 = ball3.position()
    if x + dx >= 300 or x + dx <= -300:
        dx = - dx
    if x2 + dx2 >= 300 or x2 + dx2 <= -300:
        dx2 = -dx2
    if x3 + dx3 >= 300 or x3 + dx3 <= -300:
        dx3 = - dx3
    if y + dy >= 300 or y + dy <= -300:
        dy = - dy
    if y2 + dy2 >= 300 or y2 + dy2 <= -300:
        dy2 = - dy2
    if y3 + dy3 >= 300 or y3 + dy3 <= -300:
        dy3 = - dy3

    ball.goto(x + dx, y + dy)
    ball2.goto(x2 + dx2, y2 + dy2)
    ball3.goto(x3 + dx3, y3 + dy3)

window.mainloop()

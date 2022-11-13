import time
import turtle
from random import randint

screen = turtle.Screen()
screen.title('Labirint game')
screen.bgcolor('black')
screen.setup(600, 600)
screen.tracer(0)

#labirint maker
grid = []
x = -270
y = 270
i = False
while (y > -270):
    if i == True:
        i = False
    else:
        i = True
    while (x < 270):
        cube = turtle.Turtle()
        cube.color('white')
        cube.shape('square')
        cube.shapesize(1, 1, 1)
        cube.penup()
        cube.goto(x, y)
        grid.append(cube)
        if i:
            x += 20
        else:
            x += 40
    y -= 20
    if i:
        x = -250
    else:
        x = -270

helper = []
for item in grid:
    if (randint(1, 100) > 70):
        item.reset()
    else:
        helper.append(item)
grid = helper

#labirint maker

gamer = turtle.Turtle()
gamer.color('red')
gamer.shape('square')
gamer.shapesize(0.9, 0.9, 1)
gamer.penup()
gamer.goto(-290, 290)

def Move(gamer, grid, dir):
    run = True
    if dir == "Up" and gamer.position()[1] < 290:
        gamer.setheading(90)
        gamer.forward(20)
        for item in grid:
            if gamer.distance(item) < 10:
                run = False
                break
        if not run:
            gamer.setheading(270)
            gamer.forward(20)
    if dir == "Down" and gamer.position()[1] > -290:
        gamer.setheading(270)
        gamer.forward(20)
        for item in grid:
            if gamer.distance(item) < 10:
                run = False
                break
        if not run:
            gamer.setheading(90)
            gamer.forward(20)
    if dir == "Left" and gamer.position()[0] > -290:
        gamer.setheading(180)
        gamer.forward(20)
        for item in grid:
            if gamer.distance(item) < 10:
                run = False
                break
        if not run:
            gamer.setheading(0)
            gamer.forward(20)
    if dir == "Right" and gamer.position()[0] < 290:
        gamer.setheading(0)
        gamer.forward(20)
        for item in grid:
            if gamer.distance(item) < 10:
                run = False
                break
        if not run:
            gamer.setheading(180)
            gamer.forward(20)


screen.onkeypress(lambda: Move(gamer, grid, 'Up'), 'Up')
screen.onkeypress(lambda: Move(gamer, grid, 'Down'), 'Down')
screen.onkeypress(lambda: Move(gamer, grid, 'Left'), 'Left')
screen.onkeypress(lambda: Move(gamer, grid, 'Right'), 'Right')
screen.onkeypress(lambda: gamer.goto(-290, 290), 'a')
screen.listen()

while True:
    screen.update()
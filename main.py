import time
import turtle
from random import randint, choice

screen = turtle.Screen()
screen.title('Labirint game')
screen.bgcolor('black')
screen.setup(605, 605)
screen.tracer(0)

# labirint maker
grid = []

def Board(grid, gamer):
    for item in grid:
        if gamer.distance(item) < 10:
            return True
    return False

def Board_index(grid, gamer):
    for i in range(len(grid)):
        if gamer.distance(grid[i]) < 10:
            return i
    return False


def Make_grid():
    global grid
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

    build = turtle.Turtle()
    build.hideturtle()
    build.color('orange')
    build.penup()
    build.goto(-270, 250)
    fordelete = []
    while (build.position()[1] > -270):
        print(build.position()[1])
        while (build.position()[0] < 270):
            helper = []
            build.goto(build.position()[0], build.position()[1] + 20)
            if Board(grid, build):
                helper.append(Board_index(grid, build))
            build.goto(build.position()[0] + 20, build.position()[1] - 20)
            if Board(grid, build):
                helper.append(Board_index(grid, build))
            build.goto(build.position()[0] + 20, build.position()[1])
            if len(helper) > 1:
                fordelete.append(choice(helper))
        build.goto(-270, build.position()[1] - 40)
    build.reset()

    helper = []
    for i in range(len(grid)):
        if i in fordelete:
            grid[i].reset()
        else:
            helper.append(grid[i])
    grid = helper


# labirint maker

Make_grid()

gamer = turtle.Turtle()
gamer.color('red')
gamer.shape('square')
gamer.shapesize(0.9, 0.9, 1)
gamer.penup()
gamer.goto(-290, 290)


def Move(gamer, grid, dir):
    if dir == "Up" and gamer.position()[1] < 290:
        gamer.setheading(90)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(270)
            gamer.forward(20)
    if dir == "Down" and gamer.position()[1] > -290:
        gamer.setheading(270)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(90)
            gamer.forward(20)
    if dir == "Left" and gamer.position()[0] > -290:
        gamer.setheading(180)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(0)
            gamer.forward(20)
    if dir == "Right" and gamer.position()[0] < 290:
        gamer.setheading(0)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(180)
            gamer.forward(20)


RunWhile = True

def Stop():
    globals()['screen'].bgcolor('red')
    time.sleep(0.5)
    globals()['RunWhile'] = False


screen.onkeypress(lambda: Move(gamer, grid, 'Up'), 'Up')
screen.onkeypress(lambda: Move(gamer, grid, 'Down'), 'Down')
screen.onkeypress(lambda: Move(gamer, grid, 'Left'), 'Left')
screen.onkeypress(lambda: Move(gamer, grid, 'Right'), 'Right')
screen.onkeypress(lambda: gamer.goto(-290, 290), 'a')
screen.onkeypress(lambda: Stop(), 'b')

screen.listen()

def Clear():
    global grid
    for item in grid:
        item.reset()

def Update_win():
    global win
    win.reset()
    win = turtle.Turtle()
    win.color('orange')
    win.shape('square')
    win.penup()
    win.goto(0, 0)

win = turtle.Turtle()
Update_win()


while RunWhile:
    if gamer.distance(win) < 15:
        screen.bgcolor('red')
        time.sleep(0.5)
        Clear()
        grid = []
        Make_grid()
        gamer.goto(-290, 290)
        screen.bgcolor('black')
        Update_win()
    screen.update()

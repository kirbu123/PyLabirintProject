import time
import turtle
from random import randint, choice, randrange
import pygame

#music module
file = 'Dubsleep.mp3'
pygame.init()
pygame.mixer.init()
Music = pygame.mixer.Sound(file)
Music.play(-1)
#music module

screen = turtle.Screen()
screen.title('Labirint game')
screen.bgcolor('black')
screen.setup(620, 620)
screen.tracer(0)

# labirint maker
grid = []
field = []

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
    global grid, field
    x = -320
    y = 280
    i = False
    while (y > -300):
        if i == True:
            i = False
        else:
            i = True
        while (x < 280):
            if (x**2 + y**2 != 0):
                cube = turtle.Turtle()
                cube.color('white')
                cube.shape('square')
                cube.shapesize(0.7, 0.7, 1)
                cube.penup()
                cube.goto(x, y)
                grid.append(cube)
            if i:
                x += 20
            else:
                x += 40
        y -= 20
        if i:
            x = -300
        else:
            x = -320

    #algorithm of KRUSKAL (making labirint algorithm) start
    x = -280
    y = 260
    while (y > -300):
        while (x < 280):
            cube = turtle.Turtle()
            cube.hideturtle()
            cube.penup()
            cube.goto(x, y)
            field.append([cube])
            x += 40
        x = -280
        y -= 40


    def Find(a, b):
        global field
        mas = [-1, -1]
        for i in range(len(field)):
            if a in field[i]:
                mas[0] = i
            if b in field[i]:
                mas[1] = i
        return mas

    def Merge(left, right):
        global field
        for i in field[right]:
            field[left].append(i)
        field.pop(right)

    def Find_obj(obj):
        global field
        for i in range(len(field)):
            for j in range(len(field[i])):
                if obj.distance(field[i][j]) < 10:
                    return i
        return -1


    def FindBlocks(obj):
        global grid, field
        build = turtle.Turtle()
        build.hideturtle()
        build.penup()
        build.goto(obj.position()[0], obj.position()[1])
        for i in range(2):
            res = []
            build.setheading(i * 90)
            build.forward(20)
            x = Find_obj(build)
            if x == -1:
                build.forward(-20)
                continue
            res.append(x)
            build.forward(-40)
            x = Find_obj(build)
            if x == -1:
                build.forward(20)
                continue
            res.append(x)
            build.reset()
            return res
        build.reset()
        return []


    while (len(field) > 1):
        index = randint(0, len(grid) - 1)
        obj = grid[index]
        mas = FindBlocks(obj)
        flag = True
        if len(mas) <= 1 or mas[0] == mas[1]:
            continue
        cube = turtle.Turtle()
        cube.hideturtle()
        cube.penup()
        cube.goto(obj.position()[0], obj.position()[1])
        field[mas[0]].append(cube)
        Merge(mas[0], mas[1])
        grid.remove(obj)
        obj.reset()
    for i in field:
        for j in i:
            j.reset()
    field = []
    # algorithm of KRUSKAL (making labirint algorithm) end


# labirint maker

Make_grid()

def Update_gamer():
    global gamer
    gamer.reset()
    gamer = turtle.Turtle()
    gamer.color('blue')
    gamer.shape('turtle')
    gamer.shapesize(1, 1, 1)
    gamer.penup()
    gamer.goto(-280, 260)

gamer = turtle.Turtle()

Update_gamer()



def Move(gamer, grid, dir):
    if dir == "Up" and gamer.position()[1] < 280:
        gamer.setheading(90)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(270)
            gamer.forward(20)
    if dir == "Down" and gamer.position()[1] > -280:
        gamer.setheading(270)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(90)
            gamer.forward(20)
    if dir == "Left" and gamer.position()[0] > -300:
        gamer.setheading(180)
        gamer.forward(20)
        if Board(grid, gamer):
            gamer.setheading(0)
            gamer.forward(20)
    if dir == "Right" and gamer.position()[0] < 280:
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

screen.onkeypress(lambda: Move(gamer, grid, 'Up'), 'w')
screen.onkeypress(lambda: Move(gamer, grid, 'Down'), 's')
screen.onkeypress(lambda: Move(gamer, grid, 'Left'), 'a')
screen.onkeypress(lambda: Move(gamer, grid, 'Right'), 'd')

screen.onkeypress(lambda: gamer.goto(-300, 300), 'o')
screen.onkeypress(lambda: Stop(), 'q')

screen.listen()

def Clear():
    global grid
    for item in grid:
        item.reset()
    grid = []

def Update_win():
    global win
    win.reset()
    win = turtle.Turtle()
    win.color('orange')
    win.shape('turtle')
    win.shapesize(1, 1, 1)
    win.penup()
    win.goto(240, -260)

win = turtle.Turtle()
Update_win()

#star creating-deleting module---------------------------------
star_obj = []
mas_color = ['red', 'white', 'orange', 'blue', 'yellow']

StarClock = time.time()

StarBoard = 5 #time-board of switching stars

StarCount = 20 #count of all stars


def Make_star():
    global star_obj, StarCount, mas_color, StarClock, win
    for i in range(len(star_obj)):
        star_obj[i].reset()
    star_obj = []
    for i in range(StarCount):
        x = turtle.Turtle()
        x.shape('square')
        x.shapesize(0.3, 0.3, 1)
        x.setheading(45)
        x.penup()
        x.goto(randrange(-290, 290, 20), randrange(-290, 290, 20))
        star_obj.append(x)
    for i in range(len(star_obj)):
        star_obj[i].color(choice(mas_color))
    Update_win()
    StarClock = time.time()

Make_star()

#star creating-deleting module---------------------------------

while RunWhile:
    if time.time() - StarClock > StarBoard:
        Make_star()
    if gamer.distance(win) < 15:
        screen.bgcolor('red')
        time.sleep(0.5)
        Clear()
        grid = []
        Make_grid()
        Update_gamer()
        screen.bgcolor('black')
        Update_win()
    screen.update()
#THE END

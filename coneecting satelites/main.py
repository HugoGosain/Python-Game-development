from random import randint
import pgzrun
from time import time

WIDTH = 800
HEIGHT = 600

satcount = 0
gameover = False

satelites = []
satlines = []
satamount = 11
number = 1

for i in range(satamount):
    sat = Actor("satelite")
    sat.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
    satelites.append(sat)

def draw():
    global satelites
    global satlines
    global satcount
    global gameover
    screen.blit("space",(0,0))
    number = 1
    if satcount == 11:
        gameover = True
    if gameover:
        screen.fill("black")
        if satcount == 11:
            screen.draw.text("you did it!",center=(400,300))
        else:
            screen.draw.text("you failed!",center=(400,300))
    if gameover == False:
        for i in satelites:
            i.draw()
            screen.draw.text(str(number),center =(i.pos[0],i.pos[1]+20))
            number += 1
        for line in satlines:
            screen.draw.line(line[0],line[1], "#ffffff")

def update():
    global satcount
    global gameover
    # if satcount == 11:
    #     gameover ==  True


def on_mouse_down(pos):
    global satlines
    global satelites
    global satcount
    if satcount < satamount:
        if satelites[satcount].collidepoint(pos):
            if satcount:
                satlines.append((satelites[satcount-1].pos,satelites[satcount].pos))
            satcount += 1
        else:
            satcount = 0
            satlines = []

def time_up():
    global gameover
    gameover = True

clock.schedule(time_up, 20.0)

pgzrun.go()
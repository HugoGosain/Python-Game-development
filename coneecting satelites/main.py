from random import randint
import pgzrun
from time import time

WIDTH = 800
HEIGHT = 600

satcount = 0

start_time = 0
total_time = 0
end_time = 0

satelites = []
satlines = []
satamount = 11

for i in range(satamount):
    sat = Actor("satelite")
    sat.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
    satelites.append(sat)

start_time = time()

def draw():
    global satelites
    global satlines
    screen.blit("space",(0,0))
    number = 1
    for i in satelites:
        i.draw()
        screen.draw.text(str(number),center =(i.pos[0],i.pos[1]+20))
        number += 1
    for line in satlines:
        screen.draw.line(line[0],line[1], "#ffffff")
    if satcount<satamount:
        total_time = time() - start_time

def update():
    pass

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



pgzrun.go()
import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600
message = ""
score = 0

alien = Actor("alien")

def position():
    alien.x = randint(10,590)
    alien.y = randint(30,590)

def draw():
    screen.clear()
    alien.draw()
    screen.draw.text(message,center =(300,10), fontsize= 20)
    screen.draw.text(f"score = {score}",center =(30,10), fontsize= 20)


def on_mouse_down(pos):
    global message   
    global score  
    if alien.collidepoint(pos):
        position()
        message = "hit!"
        score += 1

    else:
        message = "miss!"

    
    
def update():
    pass
position()
pgzrun.go()
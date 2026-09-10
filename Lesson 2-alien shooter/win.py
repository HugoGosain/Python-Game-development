import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600
message = ""
score = 0
game_started = "Start"
button = Actor("startbutton")
alien = Actor("alien")

def position():
    alien.x = randint(10,590)
    alien.y = randint(30,590)

def draw():
    global game_started
    screen.clear()
    if game_started == "Start":
        screen.draw.text(
            "Alien Game",
            center=(300,180),
            fontsize=60
        )
        button.pos = (300,300)
        button.draw()
    elif game_started == "Game":
        alien.draw()
        screen.draw.text(message,center =(300,10), fontsize= 20)
        screen.draw.text(f"score = {score}",center =(30,10), fontsize= 20)
    else:
        wintext = "!YOU WIN!"
        screen.draw.text(wintext,center =(300,300), fontsize= 150)


def on_mouse_down(pos):
    global message   
    global score  
    global game_started
    if game_started == "Start":
        if button.collidepoint(pos):
            game_started = "Game"
            score = 0
            message = ""
            position()
    elif game_started == "Game":    
        if alien.collidepoint(pos):
            position()
            message = "hit!"
            score += 1
            if score == 30:
                game_started = "End"
        else:
            message = "miss!"
            score -= 5
    else:
        game_started = "End"



    


def update():
    pass
pgzrun.go()
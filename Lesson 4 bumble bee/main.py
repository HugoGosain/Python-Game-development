import pgzrun
import random
WIDTH = 600
HEIGHT = 500
TITLE = "bumble bee game"
score = 0
gameover = False

b = Actor("bee")
# b.pos=(50,50 )
b.x=(50)
b.y=(50)


flwr = Actor("flwr")
flwr.pos=(random.randint(50,550),random.randint(50,450) )


def draw():
    screen.blit("backg",(0,0))
    b.draw()
    flwr.draw()
    screen.draw.text(f"score: {score}",topleft=(300,0))
    if gameover:
        screen.fill("red")
        screen.draw.text(f"your final score is: {score}",topleft=(300,250))



def update():
    global score
    global gameover
    if gameover == False:
        if keyboard.a or keyboard.left:
            b.x = b.x-5
        if keyboard.w or keyboard.up:
            b.y = b.y-5
        if keyboard.s or keyboard.down:
            b.y = b.y+5
        if keyboard.d or keyboard.right:
            b.x = b.x+5
        if b.x > 600:
            b.x=600 
        if b.y > 500:
            b.y=500 
        if b.x < 0:
            b.x=0 
        if b.y < 0:
            b.y=0 
        if b.colliderect(flwr):
            score += 1
            flwr.pos=(random.randint(50,550),random.randint(50,450) )

def time_up():
    global gameover
    gameover = True

clock.schedule(time_up, 10.0)
pgzrun.go()
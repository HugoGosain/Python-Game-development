import pgzrun

WIDTH = 600
HEIGHT = 800

spaceship = Actor("ship")
spaceship.x=(WIDTH/2)
spaceship.y=(HEIGHT - 50)

bullets = []

buglist = []
bugcount = 25

for i in range(5):
    for j in range(5):
        bugs = Actor("bug")
        bugs.x=100+i*100
        bugs.y=100+j*50
        buglist.append(bugs)

def draw():
    screen.clear()
    spaceship.draw()
    for j in buglist:
        j.draw()
    for i in bullets:
        i.draw()





def update():
    if keyboard.a or keyboard.left:
        spaceship.x = spaceship.x-5
    if keyboard.d or keyboard.right:
        spaceship.x = spaceship.x+5
    if spaceship.x > 550:
        spaceship.x=550 
    if spaceship.x < 50:
        spaceship.x=50 

def on_key_down(key):
    global bullets
    if key == keys.SPACE:
        # draw bullet
        bullet = Actor("bullete")
        bullet.x=spaceship.x
        bullet.y=spaceship.y-100
        bullets.append(bullet)
pgzrun.go()
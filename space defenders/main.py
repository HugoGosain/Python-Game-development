import pgzrun

WIDTH = 600
HEIGHT = 800

gameover = False

spaceship = Actor("ship")
spaceship.x=(WIDTH/2)
spaceship.y=(HEIGHT - 50)

bullets = []

buglist = []
bugcount = 25

score = 0

for i in range(5):
    for j in range(5):
        bugs = Actor("bug")
        bugs.x=100+i*100
        bugs.y=100+j*50
        buglist.append(bugs)

def draw():
    global gameover,score
    screen.clear()
    if gameover == False:
        spaceship.draw()
        for j in buglist:
            j.draw()
        for i in bullets:
            i.draw()
    if gameover == "lost":
        screen.fill("black")
        screen.draw.text("You got eaten\npress r to replay",center = (WIDTH/2,HEIGHT/2))
    if len(buglist) == 0:
        gameover = True
        screen.draw.text("You win\npress r to replay",center = (WIDTH/2,HEIGHT/2))
    screen.draw.text(f"you killed {score} out of 25 aliens",topleft = (0,0))

def update():
    global gameover,score
    if keyboard.a or keyboard.left:
        spaceship.x = spaceship.x-5
    if keyboard.d or keyboard.right:
        spaceship.x = spaceship.x+5
    if spaceship.x > 550:
        spaceship.x=550 
    if spaceship.x < 50:
        spaceship.x=50 
    for r in bullets:
        r.y=r.y-10
    for b in buglist:
        b.y=b.y+2
        for r in bullets:
            if r.colliderect(b):
                score += 1
                buglist.remove(b)
                bullets.remove(r)

        if b.colliderect(spaceship):
            gameover = "lost"

def on_key_down(key):
    global bullets,buglist,gameover,score
    if key == keys.SPACE or key == keys.UP:
        # draw bullet
        bullet = Actor("bullete")
        bullet.x=spaceship.x
        bullet.y=spaceship.y-100
        bullets.append(bullet)
    if gameover == True or gameover == "lost":
        if key == keys.R:
            screen.fill("black")
            gameover = False
            bullets = []
            buglist = []
            score = 0
            for i in range(5):
                for j in range(5):
                    bugs = Actor("bug")
                    bugs.x=100+i*100
                    bugs.y=100+j*50
                    buglist.append(bugs)

pgzrun.go()
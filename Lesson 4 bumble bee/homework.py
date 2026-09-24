import pgzrun
import random
WIDTH = 600
HEIGHT = 500
TITLE = "apple  catching game"
score = 0
time = 0
gameover = False
n = random.randint(50,550)

app = Actor("apple")
app.x=(n)
app.y=(50)

basket = Actor("basket")
basket.x=(300)
basket.y=(450)

def draw():
    global time
    screen.blit("backg",(0,0))
    app.draw()
    basket.draw()
    screen.draw.text(f"score: {score}",topleft=(300,0))
    if gameover:
        screen.fill("red")
        screen.draw.text(f"your final time is: {time}",topleft=(300,250))

def end():
    global gameover
    gameover = True

def increase():
    global gameover
    global time
    if gameover == False:
        time += 1

def update():
    global score
    global gameover
    global n
    global time
    if gameover == False:
        global time
        if keyboard.a or keyboard.left:
            basket.x = basket.x-5
        if keyboard.d or keyboard.right:
            basket.x = basket.x+5
        if basket.x > 600:
            basket.x=600 
        if basket.y > 500:
            basket.y=500 
        if basket.x < 0:
            basket.x=0 
        if basket.y < 0:
            basket.y=0 
        app.y = app.y+5
        if basket.colliderect(app):
            n = random.randint(50,550)
            score += 1
            app.x=(n)
            app.y=(50)
        if app.y == 490:
            n = random.randint(50,550)
            app.x=(n)
            app.y=(50)
        if score >= 5:
            end()


clock.schedule_interval(increase, 1.0)

pgzrun.go()
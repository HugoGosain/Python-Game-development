import pgzrun

WIDTH = 800
HEIGHT = 600

wordbank = set()
currentword = ""
difference = wordbank.difference(currentword)
text = "Type a new word into word bank:"

def draw():
    screen.fill("#4499cc")
    screen.draw.rect(Rect(80, 165, 640, 55), "white")
    screen.draw.text(text, (105,185))

def update():
    global difference
    global currentword
    global wordbank
    global text
    if difference == "":
        text = "Word already in worbank. Try Again:"
    if difference == currentword:
        wordbank.add(currentword)

pgzrun.go()
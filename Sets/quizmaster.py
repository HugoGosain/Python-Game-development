import pgzrun

WIDTH = 870
HEIGHT = 630

times = 10

question = []
qfilename = "questions.txt"
qcount = 0
qindex = 0

score = 0

gameover = False

mbox = Rect(0, 0, 880, 80)
qbox = Rect(0, 0, 650, 150)
tbox = Rect(0, 0, 150, 150)
# abox = Rect(0, 0, 640, 370)
a1box = Rect(0, 0, 300, 150)
a2box = Rect(0, 0, 300, 150)
a3box = Rect(0, 0, 300, 150)
a4box = Rect(0, 0, 300, 150)
sbox = Rect(0, 0, 150, 330)

mbox.move_ip(0,0)
qbox.move_ip(20,100)
tbox.move_ip(700,100)
# abox.move_ip(10,270)
a1box.move_ip(20,270)
a2box.move_ip(370,270)
a3box.move_ip(20,450)
a4box.move_ip(370,450)
sbox.move_ip(700,270)

answerboxes = [a1box, a2box, a3box, a4box]

def draw():
    global times
    screen.draw.filled_rect(mbox,"blue")
    screen.draw.filled_rect(qbox,"green")
    screen.draw.filled_rect(tbox,"orange")
    # screen.draw.filled_rect(abox,"white")
    screen.draw.filled_rect(a1box,"red")   
    screen.draw.filled_rect(a1box,"red")  
    screen.draw.filled_rect(a2box,"red")  
    screen.draw.filled_rect(a3box,"red")  
    screen.draw.filled_rect(a4box,"red")  
    screen.draw.filled_rect(sbox,"yellow")  

    screen.draw.textbox("welcome to quiz master!!!!!!!!!", mbox, color = "black")
    screen.draw.textbox(str(times), tbox, color = "black")
    screen.draw.textbox("skip", sbox, color = "black", angle = -90)
    screen.draw.textbox(qu[0],qbox,color = "white")
    for i, box in enumerate(answerboxes, start=1):
        if i<len(qu):
            screen.draw.textbox(qu[i],box,color = "white")


def update():
    movebox()

def timeupdate():
    global times
    if times:
        times -= 1

def movebox():
    mbox.x = mbox.x-2
    if mbox.right<0:
        mbox.left=WIDTH

def readquestion():
    global qcount,question
    file = open(qfilename,"r")
    for q in file:
        question.append(q)
        qcount += 1
    file.close()

def readnextquestion():
    global qindex
    qindex += 1
    return question.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answerboxes:
        if box.collidepoint(pos):
            if index is int(qu[5]):
                correctanswer()
            else:
                gamend()
        index+=1
    if sbox.collidepoint(pos):
        skipquestion()

def correctanswer():
    global score,qu,times
    score+=1
    if question:
        qu = readnextquestion()
        times = 10
    else:
        gamend()

def skipquestion():
    global qu
    if question:
        qu = readnextquestion()
    else:
        gamend()

def gamend():
    global question,times,gameover
    message = f"Game Over!!!!! You got {score} questions correct!!!!!"
    question = [message, "-","-","-","-",5] 
    gameover = True
    times = 0

readquestion()

qu = readnextquestion()

clock.schedule_interval(timeupdate,1)
pgzrun.go()
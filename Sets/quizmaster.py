import pgzrun

WIDTH = 870
HEIGHT = 630

time = 10

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
    global time
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
    screen.draw.textbox(str(time), tbox, color = "black")
    screen.draw.textbox("skip", sbox, color = "black", angle = -90)

def update():
    movebox()

def movebox():
    mbox.x = mbox.x-2

pgzrun.go()
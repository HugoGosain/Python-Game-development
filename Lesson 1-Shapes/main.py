import pgzrun
from random import randint
from pygame import Rect

WIDTH = 900
HEIGHT = 900

def draw():
    screen.fill("black")
    r = 255
    g = 0
    b = randint(120,255)
    rectw = WIDTH-600
    recth = HEIGHT

    for i in range(25):
        rectangle = Rect((0,0),(rectw,recth))
        rectangle.center = 450,450
        screen.draw.rect(rectangle,(r,g,b))
        rectw += 20
        recth -= 20
        r -= 10
        g += 10

def update():
    pass

pgzrun.go()

# ShapeﾠPGZero codeﾠParameters
# 🟢 Filled circleﾠscreen.draw.filled_circle()ﾠ(center, radius, color)
# ⚪ Circle outlineﾠscreen.draw.circle()ﾠ(center, radius, color)
# 📏 Lineﾠscreen.draw.line()ﾠ(start, end, color)
# 🔺 Filled triangleﾠscreen.draw.polygon()ﾠ(points, color)
# 🔺 Triangle outlineﾠscreen.draw.polyline()ﾠ(points, color)
# ▭ Rectangleﾠscreen.draw.rect()ﾠ(rect, color)
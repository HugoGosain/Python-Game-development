# import pgzrun
# from random import randint
# from pygame import Rect

# WIDTH = 900
# HEIGHT = 900

# def draw():
#     screen.draw.filled_circle((450,450),300,"#ffff00")
#     screen.draw.filled_circle((330,350),70,"#000000")
#     screen.draw.filled_circle((570,350),70,"#000000")
#     screen.draw.filled_circle((450,600),100,"#000000")
#     screen.draw.polygon([(350,600),(550,600),(550,700),(350,700)],"#ffff00")



# pgzrun.go()

# import pgzrun
# import pygame
# from random import randint
# # from pygame import Rect, draw

# WIDTH = 900
# HEIGHT = 900

# def draw():
#     screen.draw.filled_circle((450,450), 300, "#ffff00")
#     screen.draw.filled_circle((330,350), 70, "#000000")
#     screen.draw.filled_circle((570,350), 70, "#000000")
#     screen.draw.filled_circle((450,600), 100, "#000000")

#     pygame.draw.polygon(
#         screen.surface,
#         [(350,600), (550,600), (550,700)],(255,255,0)
#     )

# pgzrun.go()

import pgzrun

WIDTH = 900
HEIGHT = 900


def draw():
    # Face
    screen.draw.filled_circle((450, 450), 300, "#ffff00")

    # Eyes
    screen.draw.filled_circle((330, 350), 70, "#000000")
    screen.draw.filled_circle((570, 350), 70, "#000000")

    # Mouth
    screen.draw.filled_circle((450, 600), 100, "#000000")

    # Yellow triangle over the mouth
    screen.draw.line((350, 600), (550, 600), "#ffff00")
    screen.draw.line((550, 600), (550, 700), "#ffff00")
    screen.draw.line((550, 700), (350, 600), "#ffff00")


pgzrun.go()
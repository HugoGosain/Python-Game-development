# Import the Pygame Zero Library
import pgzrun
from random import randint

TITLE = "Good Shot"
WIDTH = 500
HEIGHT = 500

# Variables
message = ""
score = 0
time_left = 30
game_over = False

# Alien actor
alien = Actor('alien')


def draw():
    screen.clear()
    screen.fill(color=(128, 0, 0))

    if not game_over:
        alien.draw()

    # Score
    screen.draw.text(
        "Score: " + str(score),
        center=(250, 30),
        fontsize=30
    )

    # Timer
    screen.draw.text(
        "Time: " + str(time_left),
        center=(400, 30),
        fontsize=25
    )

    # Message
    screen.draw.text(
        message,
        center=(250, 450),
        fontsize=30
    )


def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)


def update_timer():
    global time_left, game_over, message

    if time_left > 0:
        time_left -= 1
    else:
        game_over = True
        message = "Game Over!"


def on_mouse_down(pos):
    global message, score

    # Don't allow clicking after the game ends
    if game_over:
        return

    if alien.collidepoint(pos):
        score += 1
        message = "Good Shot!"
        place_alien()
    else:
        message = "You missed!"


# Place alien at the beginning
place_alien()

# Run timer every 1 second
clock.schedule_interval(update_timer, 1.0)

# Start the game
pgzrun.go()
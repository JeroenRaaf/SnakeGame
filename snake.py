# make nice start screen
# apple spawn
# apple eat and respawn
# growth when apple eaten
# game over when hit wall
# game over when hit self
# make x appear top left when game over to quit game
# be done

import random
import sys
import pygame

pygame.init()
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake by JeroenRaaf")


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, Coordinates, length, scolor):
        self.Coordinates = Coordinates
        self.length = length
        self.scolor = scolor
        self.width = 20
        self.height = 20

    def draw(self):
        pygame.draw.rect(win, self.scolor, (self.Coordinates.x, self.Coordinates.y, self.width, self.height))


def gameloop(playerSnake):
    # game_started = False
    # game_over = False
    game_close = False
    distance = 20
    xmove = 0
    ymove = 0

    clock = pygame.time.Clock()

    while not game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True

        # Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ymove == 0:
                    ymove = -distance
                    xmove = 0
                elif event.key == pygame.K_s and ymove == 0:
                    ymove = distance
                    xmove = 0
                elif event.key == pygame.K_a and xmove == 0:
                    xmove = -distance
                    ymove = 0
                elif event.key == pygame.K_d and xmove == 0:
                    xmove = distance
                    ymove = 0
        playerSnake.Coordinates.y += ymove
        playerSnake.Coordinates.x += xmove
        # Movement

        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), (0, 0, 780, 580))
        playerSnake.draw()
        pygame.display.update()
        clock.tick(15)


starty = random.randint(2, 27) * 20
startx = random.randint(2, 37) * 20
StartingPosition = Coordinate(startx, starty)
print(startx, starty)
color = (0, 0, 255)
Player = Snake(StartingPosition, 1, color)
gameloop(Player)

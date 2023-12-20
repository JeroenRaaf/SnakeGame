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


class Apple:
    def __init__(self, Coordinates):
        self.Coordinates = Coordinates
        self.radius = 20

    def drawApple(self):
        pygame.draw.circle(win, (255, 0, 0), (self.Coordinates.x, self.Coordinates.y), self.radius)


def display_start_message():
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    win.blit(text, text_rect)
    pygame.display.update()


def random_coordinate():
    y = random.randint(2, 27) * 20
    x = random.randint(2, 37) * 20
    return Coordinate(x, y)


def gameloop(playerSnake, apple):
    game_started = False
    # game_over = False
    game_close = False
    distance = 20
    xmove = 0
    ymove = 0

    clock = pygame.time.Clock()
    display_start_message()
    pygame.display.update()

    while not game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_started:
                if event.type == pygame.KEYDOWN:
                    game_started = True
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True

                # Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ymove == 0 or event.key == pygame.K_UP and ymove == 0:
                        ymove = -distance
                        xmove = 0
                    elif event.key == pygame.K_s and ymove == 0 or event.key == pygame.K_DOWN and ymove == 0:
                        ymove = distance
                        xmove = 0
                    elif event.key == pygame.K_a and xmove == 0 or event.key == pygame.K_LEFT and xmove == 0:
                        xmove = -distance
                        ymove = 0
                    elif event.key == pygame.K_d and xmove == 0 or event.key == pygame.K_RIGHT and xmove == 0:
                        xmove = distance
                        ymove = 0
                # Movement

        if not game_close:
            if game_started:
                playerSnake.Coordinates.y += ymove
                playerSnake.Coordinates.x += xmove

                win.fill((255, 255, 255))
                pygame.draw.rect(win, (0, 0, 0), (0, 0, 780, 580))
                playerSnake.draw()

                pygame.display.update()
                clock.tick(15)
            else:
                win.fill((0, 0, 0))
                display_start_message()
                pygame.display.update()

        # Apple

        # Apple

        # Game Over

        # Game Over


starty = random.randint(2, 27) * 20
startx = random.randint(2, 37) * 20
color = (0, 0, 255)
Player = Snake(random_coordinate(), 1, color)
Apple = Apple(random_coordinate())
gameloop(Player, Apple)

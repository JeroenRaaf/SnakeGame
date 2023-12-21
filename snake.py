# growth when apple eaten
# game over when hit wall
# game over when hit self
# make x appear top left when game over to quit game
# be done
# make apples round some day

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
    def __init__(self, Coordinates):
        self.Coordinates = Coordinates
        self.width = 20
        self.height = 20
        self.length = 1
        self.segments = [Coordinate(Coordinates.x, Coordinates.y)]

    def draw(self):
        pygame.draw.rect(win, (0, 0, 255), (self.Coordinates.x, self.Coordinates.y, self.width, self.height))

    def draw_segments(self):
        for segment in self.segments:
            pygame.draw.rect(win, (0, 0, 255), (segment.x, segment.y, self.width, self.height))

    def update_segments(self):
        if self.length > 1:
            for i in range(self.length - 1, 0, -1):
                if i < len(self.segments):
                    self.segments[i] = Coordinate(self.segments[i - 1].x, self.segments[i - 1].y)
                else:
                    self.segments.append(Coordinate(self.segments[i - 1].x, self.segments[i - 1].y))
        self.segments[0] = Coordinate(self.Coordinates.x, self.Coordinates.y)


class Segment:
    def __init__(self, Coordinates):
        self.Coordinates = Coordinates
        self.width = 20
        self.height = 20

    def drawSegment(self):
        pygame.draw.rect(win, (0, 0, 255), (self.Coordinates.x, self.Coordinates.y, self.width, self.height))


class Apple:
    def __init__(self, Coordinates):
        self.Coordinates = Coordinates
        self.width = 20
        self.height = 20

    def drawApple(self):
        pygame.draw.rect(win, (255, 0, 0), (self.Coordinates.x, self.Coordinates.y, self.width, self.height))


def respawn_apple():
    apple.Coordinates = random_coordinate()
    apple.drawApple()


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


apple = Apple(random_coordinate())


def gameloop(playerSnake, segments):
    game_started = False
    # game_over = False
    game_close = False
    apple_exists = False

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
                        playerSnake.facing = "up"
                    elif event.key == pygame.K_s and ymove == 0 or event.key == pygame.K_DOWN and ymove == 0:
                        ymove = distance
                        xmove = 0
                        playerSnake.facing = "do"
                    elif event.key == pygame.K_a and xmove == 0 or event.key == pygame.K_LEFT and xmove == 0:
                        xmove = -distance
                        ymove = 0
                        playerSnake.facing = "le"
                    elif event.key == pygame.K_d and xmove == 0 or event.key == pygame.K_RIGHT and xmove == 0:
                        xmove = distance
                        ymove = 0
                        playerSnake.facing = "ri"
                # Movement

        if not game_close:
            if game_started:
                playerSnake.Coordinates.y += ymove
                playerSnake.Coordinates.x += xmove

                win.fill((255, 255, 255))
                pygame.draw.rect(win, (0, 0, 0), (0, 0, 780, 580))

                apple.drawApple()
                playerSnake.draw()

                if not apple_exists:
                    respawn_apple()
                    apple_exists = True

                if apple.Coordinates.x == playerSnake.Coordinates.x and apple.Coordinates.y == playerSnake.Coordinates.y:
                    segments.append(Segment(Coordinate(-1, -1)))
                    playerSnake.length += 1
                    apple_exists = False

                # Update snake segments after checking for collisions
                playerSnake.update_segments()
                playerSnake.draw_segments()

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
Player = Snake(random_coordinate())
Segments = []
gameloop(Player, Segments)

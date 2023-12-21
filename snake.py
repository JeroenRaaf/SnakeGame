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

    def delete_segments(self):
        self.segments = [Coordinate(self.Coordinates.x, self.Coordinates.y)]


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


font = pygame.font.Font(None, 38)
sub_font = pygame.font.Font(None, 25)


def display_text_message(main_text, color, sub_text=None):
    main_text_surface = font.render(main_text, True, color)
    main_text_rect = main_text_surface.get_rect(center=(width // 2, height // 2))
    win.blit(main_text_surface, main_text_rect)

    if sub_text:
        sub_text_surface = sub_font.render(sub_text, True, color)
        sub_text_rect = sub_text_surface.get_rect(center=(width // 2, height // 2 + 20))
        win.blit(sub_text_surface, sub_text_rect)

    pygame.display.update()


def display_start_message():
    display_text_message("Press any key to start!", (255, 255, 255), "or press 'Q' to exit.")


def display_gameover_message():
    display_text_message("Game over! Press any key to continue.", (255, 0, 0), "or press 'Q' to exit.")


def display_quit_message():
    display_text_message("Are you sure? Press any key to continue.", (255, 0, 255), "or press 'Q' again to exit.")


def random_coordinate():
    y = random.randint(2, 27) * 20
    x = random.randint(2, 37) * 20
    return Coordinate(x, y)


apple = Apple(random_coordinate())


def gameloop(playerSnake):
    game_started = False
    game_over = False
    game_close = False
    game_paused = False
    apple_exists = False

    distance = 20
    xmove = 0
    ymove = 0
    pausedxmove = 0
    pausedymove = 0

    clock = pygame.time.Clock()

    while not game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_started:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                    elif event.type == pygame.KEYDOWN:
                        game_over = False
                        game_started = True
                        playerSnake.Coordinates = random_coordinate()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        if game_paused:
                            game_close = True

                        game_paused = True
                    else:
                        xmove = pausedxmove
                        ymove = pausedymove
                        game_paused = False

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
            if not game_over:
                if game_paused:
                    pausedxmove = xmove
                    pausedymove = ymove
                    xmove = 0
                    ymove = 0
                    win.fill((0, 0, 0))
                    display_quit_message()
                    pygame.display.update()
                elif game_started:
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
                        playerSnake.length += 1
                        apple_exists = False
                    # Collision Check
                    if playerSnake.Coordinates.x >= 780 or playerSnake.Coordinates.x <= 0:
                        game_over = True
                    elif playerSnake.Coordinates.y >= 580 or playerSnake.Coordinates.y <= 0:
                        game_over = True

                    for segment in playerSnake.segments:
                        if segment is not playerSnake.segments[0]:
                            if playerSnake.Coordinates.x == segment.x and playerSnake.Coordinates.y == segment.y:
                                game_over = True
                    # Collision Check

                    playerSnake.update_segments()
                    playerSnake.draw_segments()

                    pygame.display.update()
                    clock.tick(15)
                else:
                    win.fill((0, 0, 0))
                    display_start_message()
                    pygame.display.update()
            else:
                if playerSnake.length > 1:
                    playerSnake.delete_segments()
                    playerSnake.length = 1
                game_started = False
                xmove = 0
                ymove = 0
                win.fill((0, 0, 0))
                display_gameover_message()
                pygame.display.update()
        # Apple

        # Apple

        # Game Over

        # Game Over


starty = random.randint(2, 27) * 20
startx = random.randint(2, 37) * 20
Player = Snake(Coordinate(0, 0))
gameloop(Player)

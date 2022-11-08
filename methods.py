import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 700, 500

SCORE_FONT = pygame.font.SysFont("consolas", 50)
WINNING_SCORE = 10

def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)

    # Code goes here

    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    # Code goes here
    pass


def handle_paddle_movement(keys, left_paddle, right_paddle):
    pass
    # Code goes here

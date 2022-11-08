import pygame
from game_objects import Paddle, Ball
from methods import draw, handle_paddle_movement, handle_collision

pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10


def main():
    run = True

    # Code goes here

    pygame.quit()

if __name__ == "__main__":
    main()
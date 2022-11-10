import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 700, 500

class Paddle:
    warna = WHITE
    kecepatan = 8

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(
            win, self.warna, (self.x, self.y, self.width, self.height)) 

    def move(self, up=True):
        if up:
            self.y -= self.kecepatan 
        else:
            self.y += self.kecepatan

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    MAX_kecepatan = 5
    warna = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_kecepatan
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.warna, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
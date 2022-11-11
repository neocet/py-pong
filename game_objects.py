import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 700, 500

class Paddle:
    warna = WHITE
    VEL = 8

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
    warna = WHITE

    def __init__(self, x, y, radius, x_vel):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = x_vel
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


class Button:
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def is_clicked(self, pos):
        x, y = pos
        return self.x <= x <= self.x + self.image.get_width() and self.y <= y <= self.y + self.image.get_height()

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.image.get_width():
            if pos[1] > self.y and pos[1] < self.y + self.image.get_height():
                return True
        return False
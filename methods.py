import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 700, 500

SCORE_FONT = pygame.font.SysFont("consolas", 50)
SKOR_MENANG = 10

def draw(win, paddles, bola, skor_kiri, skor_kanan):
    win.fill(BLACK)

    text_skor_kiri = SCORE_FONT.render(f"{skor_kiri}", 1, WHITE)
    text_skor_kanan = SCORE_FONT.render(f"{skor_kanan}", 1, WHITE)
    win.blit(text_skor_kiri, (WIDTH//4 - text_skor_kiri.get_width()//2, 20))
    win.blit(text_skor_kanan, (WIDTH * (3/4) - text_skor_kanan.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    bola.draw(win)
    pygame.display.update()


def handle_collision(bola, paddle_kiri, paddle_kanan):
    if bola.y + bola.radius >= HEIGHT:
        bola.y_vel *= -1
    elif bola.y - bola.radius <= 0:
        bola.y_vel *= -1

    if bola.x_vel < 0:
        if bola.y >= paddle_kiri.y and bola.y <= paddle_kiri.y + paddle_kiri.height:
            if bola.x - bola.radius <= paddle_kiri.x + paddle_kiri.width:
                bola.x_vel *= -1

                middle_y = paddle_kiri.y + paddle_kiri.height / 2
                difference_in_y = middle_y - bola.y
                reduction_factor = (paddle_kiri.height / 2) / bola.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                bola.y_vel = -1 * y_vel

    else:
        if bola.y >= paddle_kanan.y and bola.y <= paddle_kanan.y + paddle_kanan.height:
            if bola.x + bola.radius >= paddle_kanan.x:
                bola.x_vel *= -1

                middle_y = paddle_kanan.y + paddle_kanan.height / 2
                difference_in_y = middle_y - bola.y
                reduction_factor = (paddle_kanan.height / 2) / bola.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                bola.y_vel = -1 * y_vel


def handle_paddle_movement(keys, paddle_kiri, paddle_kanan):
    if keys[pygame.K_w] and paddle_kiri.y - paddle_kiri.VEL >= 0:
        paddle_kiri.move(up=True)
    if keys[pygame.K_s] and paddle_kiri.y + paddle_kiri.VEL + paddle_kiri.height <= HEIGHT:
        paddle_kiri.move(up=False)

    if keys[pygame.K_UP] and paddle_kanan.y - paddle_kanan.VEL >= 0:
        paddle_kanan.move(up=True)
    if keys[pygame.K_DOWN] and paddle_kanan.y + paddle_kanan.VEL + paddle_kanan.height <= HEIGHT:
        paddle_kanan.move(up=False)

        #KEVINNNNN
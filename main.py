import pygame
from game_objects import Paddle, Ball, Button
from methods import draw, handle_paddle_movement, handle_collision

pygame.init()

# Constants
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("consolas", 50)
WINNING_SCORE = 7


def main():
    run = True
    clock = pygame.time.Clock()

    # Variabel menu
    menu = True
    difficulty = False
    end = False
    bgm = True
    DIFF = "Normal"
    
    # App version
    app_ver = "Pong, v0.2b"
    app_ver_text = pygame.font.SysFont("consolas", 20).render(app_ver, 1, WHITE)

    # Background audio
    pygame.mixer.music.load("assets/background.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # Inisialisasi objek dan skor
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 5)

    left_score = 0
    right_score = 0

    # Button pada menu utama
    start_img = pygame.image.load("assets/start.png")
    diff_img = pygame.image.load("assets/diff.png")
    quit_img = pygame.image.load("assets/quit.png")
    unmute_img = pygame.image.load("assets/unmuted.png")
    mute_img = pygame.image.load("assets/muted.png")

    start_btn = Button(WIDTH//2 - 110, HEIGHT//4 - 75, start_img, 1)
    diff_btn = Button(WIDTH//2 - 110, 2 * HEIGHT//4 - 50, diff_img, 1)
    quit_btn = Button(WIDTH//2 - 110, 3 * HEIGHT//4 - 25, quit_img, 1)
    unmute_btn = Button(WIDTH - 75, 395, unmute_img, 1)
    mute_btn = Button(WIDTH - 75, 395, mute_img, 1)

    # Button pada menu difficulty
    back_img = pygame.image.load("assets/back.png")
    normal_img = pygame.image.load("assets/normal.png")
    insane_img = pygame.image.load("assets/insane.png")
    godly_img = pygame.image.load("assets/godly.png")

    back_btn = Button(100, 64, back_img, 1)
    normal_btn = Button(WIDTH//2 - (110 * 0.8), 150, normal_img, 0.8)
    insane_btn = Button(WIDTH//2 - (110 * 0.8), 260, insane_img, 0.8)
    godly_btn = Button(WIDTH//2 - (110 * 0.8), 370, godly_img, 0.8)

    # Game loop
    while run:
        clock.tick(FPS)

        if menu:            # Menu utama    
            WIN.fill(BLACK)
            # Menampilkan tombol pada menu utama
            start_btn.draw(WIN)
            diff_btn.draw(WIN)
            quit_btn.draw(WIN)

            if bgm:
                pygame.mixer.music.unpause()
                pygame.draw.rect(WIN, BLACK, (WIDTH - 75, 395, 60, 60))
                unmute_btn.draw(WIN)
            else:
                pygame.mixer.music.pause()
                pygame.draw.rect(WIN, BLACK, (WIDTH - 75, 395, 60, 60))
                mute_btn.draw(WIN)

            # Teks tambahan
            diff_text = pygame.font.SysFont("comicsans", 36).render(DIFF, 1, WHITE)
            WIN.blit(diff_text, (WIDTH - 10 - diff_text.get_width(), HEIGHT - 10 - diff_text.get_height()))
            WIN.blit(app_ver_text, (10, HEIGHT - 10 - app_ver_text.get_height()))

            pygame.display.update()

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                state = pygame.mouse.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN and state[0]:
                    pos = pygame.mouse.get_pos()
                    if start_btn.is_over(pos):      # Menekan tombol start
                        menu = False

                    if diff_btn.is_over(pos):       # Menekan tombol difficulty
                        menu = False
                        difficulty = True

                    elif quit_btn.is_over(pos):     # Menekan tombol quit
                        run = False
                        
                    elif unmute_btn.is_over(pos):   # Menekan tombol unmute
                        bgm = False
                        unmute_btn.y = 1000
                        unmute_btn.draw(WIN)
                        mute_btn = Button(WIDTH - 75, 395, mute_img, 1)
                        mute_btn.draw(WIN)
                        pygame.display.update()

                    elif mute_btn.is_over(pos):     # Menekan tombol mute
                        bgm = True
                        mute_btn.y = 1000
                        mute_btn.draw(WIN)
                        unmute_btn = Button(WIDTH - 75, 395, unmute_img, 1)
                        unmute_btn.draw(WIN)
                        pygame.display.update()
                    

        elif difficulty:    # Menampilkan menu difficulty
            # Menampilkan tombol pada menu difficulty
            WIN.fill(BLACK)
            
            # Menampilkan tombol pada menu difficulty
            back_btn.draw(WIN)
            normal_btn.draw(WIN)
            insane_btn.draw(WIN)
            godly_btn.draw(WIN)

            if bgm:
                pygame.mixer.music.unpause()
                pygame.draw.rect(WIN, BLACK, (WIDTH - 75, 395, 60, 60))
                unmute_btn.draw(WIN)
            else:
                pygame.mixer.music.pause()
                pygame.draw.rect(WIN, BLACK, (WIDTH - 75, 395, 60, 60))
                mute_btn.draw(WIN)

            # Teks tambahan
            select_text = pygame.font.SysFont("consolas", 40).render("Select Difficulty", 1, WHITE)
            WIN.blit(select_text, (WIDTH//2 - select_text.get_width()//2, 65))
            WIN.blit(app_ver_text, (10, HEIGHT - 10 - app_ver_text.get_height()))
            WIN.blit(diff_text, (WIDTH - 10 - diff_text.get_width(), HEIGHT - 10 - diff_text.get_height()))

            pygame.display.update()

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                state = pygame.mouse.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN and state[0]:
                    pos = pygame.mouse.get_pos()
                    if normal_btn.is_over(pos):    # Menekan tombol normal
                        DIFF = "Normal"
                        difficulty = False
                        menu = True

                        left_paddle.kecepatan = 8
                        right_paddle.kecepatan = 8
                        ball.x_vel = 5

                    elif insane_btn.is_over(pos):   # Menekan tombol insane
                        DIFF = "Insane"
                        difficulty = False
                        menu = True

                        left_paddle.kecepatan = 12
                        right_paddle.kecepatan = 12
                        ball.x_vel = 10

                    elif godly_btn.is_over(pos):    # Menekan tombol godly
                        DIFF = "Godly"
                        difficulty = False
                        menu = True

                        left_paddle.kecepatan = 16
                        right_paddle.kecepatan = 16
                        ball.x_vel = 14
                    
                    elif back_btn.is_over(pos):     # Menekan tombol back
                        difficulty = False
                        menu = True

                    elif unmute_btn.is_over(pos):   # Menekan tombol unmute
                        bgm = False
                        unmute_btn.y = 1000
                        unmute_btn.draw(WIN)
                        mute_btn = Button(WIDTH - 75, 395, mute_img, 1)
                        mute_btn.draw(WIN)
                        pygame.display.update()

                    elif mute_btn.is_over(pos):     # Menekan tombol mute
                        bgm = True
                        mute_btn.y = 1000
                        mute_btn.draw(WIN)
                        unmute_btn = Button(WIDTH - 75, 395, unmute_img, 1)
                        unmute_btn.draw(WIN)
                        pygame.display.update()

        elif end:           # Menampilkan menu akhir (endgame)
            # Menampilkan menu akhir
            WIN.fill(BLACK)
            win_label = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(win_label, (WIDTH//2 - win_label.get_width()//2, HEIGHT//2 - win_label.get_height()//2 - 85))
            WIN.blit(app_ver_text, (10, HEIGHT - 10 - app_ver_text.get_height()))

            score = f"[ {left_score} - {right_score} ]"
            score_label = pygame.font.SysFont("consolas", 45).render(score, 1, WHITE)
            WIN.blit(score_label, (WIDTH//2 - score_label.get_width()//2, HEIGHT//2 - score_label.get_height()//2 - 5))

            # Menampilkan tombol pada menu akhir
            quit_btn_2 = Button(WIDTH//4 - 35 * 0.8, HEIGHT//2 + 70, quit_img, 0.8)
            quit_btn_2.draw(WIN)

            menu_img = pygame.image.load("assets/menu.png")
            menu_btn = Button(3 * WIDTH//4 - 185 * 0.8, HEIGHT//2 + 70, menu_img, 0.8)
            menu_btn.draw(WIN)

            pygame.display.update()
            
            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                state = pygame.mouse.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN and state[0]:
                    pos = pygame.mouse.get_pos()
                    if quit_btn_2.is_over(pos):    # Menekan tombol quit
                        run = False
                    elif menu_btn.is_over(pos):    # Menekan tombol menu
                        end = False
                        menu = True

                        # Reset posisi objek dan skor
                        ball.reset()
                        left_paddle.reset()
                        right_paddle.reset()

                        left_score = 0
                        right_score = 0

                        WIN.fill(BLACK)

        else:               # Masuk ke permainan
            # Menampilkan objek
            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # Mengatur gerakan paddle
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        # Mengatur gerakan bola
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        # Mengatur skor
        if ball.x < 0:
            # Update skor
            right_score += 1
            pygame.draw.rect(WIN, BLACK, (3 * WIDTH//4 - 50, 10, 100, 50))
            text_skor_kanan = SCORE_FONT.render(f"{right_score}", 1, WHITE)
            WIN.blit(text_skor_kanan, (3 * WIDTH//4 - text_skor_kanan.get_width()//2, 20))

            # Reset posisi objek
            left_paddle.reset()
            right_paddle.reset()
            ball.reset()

            # Banner penyekor
            scorer = "Right player scored!"
            scoring_text = pygame.font.SysFont("consolas", 40).render(scorer, 1, WHITE)

            pygame.draw.rect(WIN, WHITE, (WIDTH//2 - scoring_text.get_width()//2 - 30, HEIGHT//2 - scoring_text.get_height()//2 - 30, scoring_text.get_width() + 60, scoring_text.get_height() + 60))
            pygame.draw.rect(WIN, BLACK, (WIDTH//2 - scoring_text.get_width()//2 - 24, HEIGHT//2 - scoring_text.get_height()//2 - 24, scoring_text.get_width() + 48, scoring_text.get_height() + 48))

            WIN.blit(scoring_text, (WIDTH//2 - scoring_text.get_width()//2, HEIGHT//2 - scoring_text.get_height()//2))

            pygame.display.update()
            pygame.time.delay(2500)

        elif ball.x > WIDTH:
            # Update skor
            left_score += 1
            pygame.draw.rect(WIN, BLACK, (WIDTH//4 - 50, 10, 100, 50))
            text_skor_kiri = SCORE_FONT.render(f"{left_score}", 1, WHITE)
            WIN.blit(text_skor_kiri, (WIDTH//4 - text_skor_kiri.get_width()//2, 20))

            # Reset posisi objek
            left_paddle.reset()
            right_paddle.reset()
            ball.reset()

            # Banner penyekor
            scorer = "Left player scored!"
            scoring_text = pygame.font.SysFont("consolas", 40).render(scorer, 1, WHITE)

            pygame.draw.rect(WIN, WHITE, (WIDTH//2 - scoring_text.get_width()//2 - 30, HEIGHT//2 - scoring_text.get_height()//2 - 30, scoring_text.get_width() + 60, scoring_text.get_height() + 60))
            pygame.draw.rect(WIN, BLACK, (WIDTH//2 - scoring_text.get_width()//2 - 24, HEIGHT//2 - scoring_text.get_height()//2 - 24, scoring_text.get_width() + 48, scoring_text.get_height() + 48))

            WIN.blit(scoring_text, (WIDTH//2 - scoring_text.get_width()//2, HEIGHT//2 - scoring_text.get_height()//2))

            pygame.display.update()
            pygame.time.delay(2500)

        # Mengatur pemenang
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            end = True

    pygame.quit()

if __name__ == "__main__":
    main()
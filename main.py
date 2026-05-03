from pygame import *


win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
back = (200, 255, 255)

font.init()
font.init()
font1 = font.Font(None, 70)  
font2 = font.Font(None, 36)

score1 = 0
score2 = 0
win_score = 1

clock = time.Clock()
FPS = 60

WIN1 = font1.render('PLAYER1 WIN', True, (180, 0, 0))
WIN2 = font2.render('PLAYER2 WIN', True, (180, 0, 0))


class Racket:
    def __init__(self, color, x, y, w, h, speed):
        self.rect = Rect(x, y, w, h)
        self.color = color
        self.speed = speed

    def draw(self):
        draw.rect(window, self.color, self.rect)

    def move(self, up_key, down_key):
        keys = key.get_pressed()
        if keys[up_key] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.y < win_h - self.rect.h:
            self.rect.y += self.speed

class Ball:
    def __init__(self, color, x, y, size, speed_x, speed_y):
        self.rect = Rect(x, y, size, size)
        self.color = color
 
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        draw.rect(window, self.color, self.rect)

    def move(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


ball = Ball((255, 0, 0), 290, 240, 20, 4, 4)
rocket1 = Racket((0, 0, 255), 30, 200, 20, 100, 5)
rocket2 = Racket((0, 0, 255), 550, 200, 20, 100, 5)

game = True
game_over = False  # флаг завершения игры

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not game_over:
        rocket1.move(K_w, K_s)
        rocket2.move(K_UP, K_DOWN)
        ball.move()

        # Отскок от верхней и нижней границы
        if ball.rect.y <= 0 or ball.rect.y >= win_h - ball.rect.h:
            ball.speed_y *= -1

        # Отскок от ракеток
        if ball.rect.colliderect(rocket1.rect) or ball.rect.colliderect(rocket2.rect):
            ball.speed_x *= -1

        # ПРОПУСК МЯЧА И ПРОВЕРКА ПОБЕДЫ
        if ball.rect.x <= 0:  # мяч ушёл за левый край — очко для игрока 2
            score2 += 1
            # Проверяем, выиграл ли игрок 2
            if score2 >= win_score:
                game_over = True

            # Сброс позиции мяча в центр
            ball.rect.x = 290
            ball.rect.y = 240
            # Сброс направления (пусть летит к игроку 2)
            ball.speed_x = abs(ball.speed_x)

        if ball.rect.x >= win_w - ball.rect.w:  # мяч ушёл за правый край — очко для игрока 1
            score1 += 1
            # Проверяем, выиграл ли игрок 1
            if score1 >= win_score:
                game_over = True

            # Сброс позиции мяча в центр
            ball.rect.x = 290
            ball.rect.y = 240
            # Сброс направления (пусть летит к игроку 1)
            ball.speed_x = -abs(ball.speed_x)

    # Отрисовка
    window.fill(back)

    rocket1.draw()
    rocket2.draw()
    ball.draw()

    # Отображение счёта
    score_text = font2.render(f"{score1} : {score2}", True, (0, 0, 0))
    window.blit(score_text, (win_w // 2 - score_text.get_width() // 2, 10))

    # Если игра завершена — показываем победителя
    if game_over:
        if score1 >= win_score:
            window.blit(WIN1, (win_w // 2 - WIN1.get_width() // 2, win_h // 2 - WIN1.get_height() // 2))
        else:
            window.blit(WIN2, (win_w // 2 - WIN2.get_width() // 2, win_h // 2 - WIN2.get_height() // 2))


    display.update()
    clock.tick(FPS)


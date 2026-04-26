from pygame import *

# Настройки окна
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
back = (200, 255, 255)

clock = time.Clock()
FPS = 60

# --- Классы ---
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
        # Сохраняем скорость как атрибуты объекта
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        draw.rect(window, self.color, self.rect)

    def move(self):
        # Используем сохраненные атрибуты для движения
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

# --- Создание объектов (ВАЖНО!) ---
# Здесь мы передаем скорость мяча (4 пикселя по X и 4 по Y)
ball = Ball((255, 0, 0), 290, 240, 20, 4, 4)
rocket1 = Racket((0, 0, 255), 30, 200, 20, 100, 5)
rocket2 = Racket((0, 0, 255), 550, 200, 20, 100, 5)

# --- Игровой цикл ---
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Управление ракетками
    rocket1.move(K_w, K_s)
    rocket2.move(K_UP, K_DOWN)

    # Движение мяча
    ball.move()

    # Отскок от верхнего и нижнего края (чтобы мяч не улетал за экран)
    if ball.rect.y <= 0 or ball.rect.y >= win_h - ball.rect.h:
        ball.speed_y *= -1

    # Отскок от ракеток (меняем направление по горизонтали)
    if ball.rect.colliderect(rocket1.rect) or ball.rect.colliderect(rocket2.rect):
        ball.speed_x *= -1

    # Отрисовка
    window.fill(back)
    rocket1.draw()
    rocket2.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)
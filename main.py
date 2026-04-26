from pygame import *


win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
back = (200, 255, 255)

font.init()
font = font.Font(None, 70)

clock = time.Clock()
FPS = 60

WIN1 = font.render('PLAYER1 WIN', True, (180, 0, 0))
WIN2 = font.render('PLAYER2 WIN', True, (180, 0, 0))


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
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    rocket1.move(K_w, K_s)
    rocket2.move(K_UP, K_DOWN)

    ball.move()



    if ball.rect.y <= 0 or ball.rect.y >= win_h - ball.rect.h:
        ball.speed_y *= -1


    if ball.rect.colliderect(rocket1.rect) or ball.rect.colliderect(rocket2.rect):
        ball.speed_x *= -1


    window.fill(back)
    rocket1.draw()
    rocket2.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)
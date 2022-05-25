from pygame import *
from time import time as timer

mixer.init()
clock = time.Clock()
FPS = 60
font.init()

speed_x = 3
speed_y = 3

font1 = font.Font(None, 35)
lose = font1.render('Player 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('Player 2 LOSE!', True, (180, 0, 0))

screen = display.set_mode((700, 500))
display.set_caption("ping-pong")

background = transform.scale(image.load("0Eq3Pjm7E-Y.jpg"),(700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_p = key.get_pressed()
        if keys_p[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_s] and self.rect.y < 615:
            self.rect.y += self.speed
    def update_l(self):
        keys_t = key.get_pressed()
        if keys_t[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_t[K_DOWN] and self.rect.y < 615:
            self.rect.y += self.speed

ball = GameSprite('png-transparent-yellow-ball-illustration-table-tennis-ball-ping-pong-ball-sport-orange-ball.png',250,250,5,50,50)
player = Player('ddd.png', 10, 230, 20, 100, 7)
player1 = Player('ddd.png', 670, 230, 20, 100, 7)

finish = False
game = True
while game:
    screen.blit(background,(0, 0))
    for e in event.get():
        
        if e.type == QUIT:
            game = False
    if finish != True:
        player.update_l()
        player.reset()
        ball.reset()
        player1.update_r()
        player1.reset()
        ball.rect.x += speed_x
        ball.rect.y +=speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 670 or ball.rect.y < 0:
            speed_x *= -1
        if sprite.collide_rect(player, ball) or sprite.collide_rect(player1, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            screen.blit(lose, (200, 200))
        if ball.rect.x > 670:
            finish = True
            screen.blit(lose2, (200, 200))
        display.update()
        clock.tick(FPS)

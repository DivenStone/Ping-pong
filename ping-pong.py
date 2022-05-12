from pygame import *
from time import time as timer

mixer.init()
clock = time.Clock()
FPS = 60
font.init()

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

player = Player('ddd.png', 10, 230, 20, 100, 7)
player1 = Player('ddd.png', 670, 230, 20, 100, 7)

game = True
while game:
    screen.blit(background,(0, 0))
    for e in event.get():
        
        if e.type == QUIT:
            game = False
    player.update_r()
    player.reset()
    player1.update_l()
    player1.reset()
    display.update()
    clock.tick(FPS)
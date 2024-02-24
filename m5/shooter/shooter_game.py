#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

mixer.init()
mixer.music.load("m5/shooter/space.ogg")
mixer.music.set_volume(0)
mixer.music.play(-1)

height = 500
width = 700

window = display.set_mode([width, height])

background = scale(load("m5/shooter/galaxy.jpg"), [width, height])
game = True
finish = False
fps = 60
clock = time.Clock()

class GameSprite(Sprite):
    def __init__(self, image, x, y, width, height, speed):
        super().__init__()
        self.image = scale(load(image), [width, height])
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,[self.rect.x, self.rect.y])
        
class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
            
        if pressed[K_LEFT]:
            self.rect.x -= self.speed
                   
        if pressed[K_RIGHT]:
            self.rect.x += self.speed       

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    window.blit(background, [0, 0])
    display.update()
    clock.tick(fps)
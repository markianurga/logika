#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

mixer.init()
mixer.music.load("m5/shooter/space.ogg")
mixer.music.set_volume(0.05)
mixer.music.play(-1)

font.init()
f1 = font.Font(None, 36) 

f2 = font.Font(None, 80) 

ckore = 0
lose = 0

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
            
    def faer(self):
        bullet = Bullet("m5/shooter/bullet.png", self.rect.centerx, self.rect.top, 15, 20, 6)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lose
        if self.rect.y > 500:
            lose += 1
            self.rect.y = 0
            self.rect.x = randint(0, 620)
            
class Bullet (GameSprite):
    def update(self):
        self.rect.y -= self.speed
      
            
rocet = Player("m5/shooter/rocket.png", 300, 400, 80, 100, 12 )



enemy0 = Enemy("m5/shooter/ufo.png", randint(0, 620), 0, 80, 50, randint(1, 5) )
enemy1 = Enemy("m5/shooter/ufo.png", randint(0, 620), 0, 80, 50, randint(1, 5) )
enemy2 = Enemy("m5/shooter/ufo.png", randint(0, 620), 0, 80, 50, randint(1, 5) )
enemy3 = Enemy("m5/shooter/ufo.png", randint(0, 620), 0, 80, 50, randint(1, 5) )
enemy4 = Enemy("m5/shooter/ufo.png", randint(0, 620), 0, 80, 50, randint(1, 5) )
enemy5 = Enemy("m5/shooter/ufo.png", randint(0, 620), 0, 80, 50, randint(1, 5) )

enemys = sprite.Group(enemy0, enemy1, enemy2, enemy3)

bullets = sprite.Group()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocet.faer()
            
    if not finish:   
        window.blit(background, [0, 0])
        txt_lose = f1.render("пропушкно " +str(lose), 1, [255,255,255])
        window.blit(txt_lose, [0, 30])
        txt_ckor = f1.render("рахунок " +str(ckore), 1, [255,255,255])
        window.blit(txt_ckor, [0, 10])
        if lose == 3:
            finish = True
        rocet.reset()
        rocet.update()
        enemys.draw(window)
        enemys.update()
        bullets.draw(window)
        bullets.update()
    display.update()
    clock.tick(fps)
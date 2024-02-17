#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect, Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = scale(load(image), [82, 80])
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        WINDOW.blit(self.image,[self.rect.x, self.rect.y])

class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_UP]:
            self.rect.y -= self.speed
            
        if pressed[K_DOWN]:
            self.rect.y += self.speed
            
        if pressed[K_LEFT]:
            self.rect.x -= self.speed
            
        if pressed[K_RIGHT]:
            self.rect.x += self.speed
        
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        
        if self.direction == 'right':
            self.rect.x += self.speed
            
        if self.rect.x <= 500:
            self.direction = 'right'
       
        if self.rect.x >= 650:
            self.direction = 'left'
       
class Enemy2(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        
        if self.direction == 'right':
            self.rect.x += self.speed
            
        if self.rect.x <= 230:
            self.direction = 'right'
       
        if self.rect.x >= 430:
            self.direction = 'left'
       
class Wall(Sprite):
    def __init__ (self, x, y, width, height, color):
        self.width = width  
        self.height = height 
        self.image =  Surface([width, height])
        self.image.fill(color)   
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        WINDOW.blit(self.image,[self.rect.x, self.rect.y])

wall1 = Wall(100, 0, 10, 400, [81, 205, 45])
wall2 = Wall(230, 100, 10, 400, [81, 205, 45])
wall3 = Wall(340, 190, 50, 10, [81, 205, 45])
wall4 = Wall(510, 10, 10, 405, [81, 205, 45])
wall5 = Wall(360, 0, 15, 395, [81, 205, 45])
wall6 = Wall(360, 0, 15, 395, [81, 205, 45])
player = Player('hero.png', 10, 10, 6)
player2 = GameSprite('treasure.png', 670, 10, 2)
player3 = Enemy('cyborg.png', 660, 311, 4)
player4 = Enemy2('cyborg.png', 240, 311, 2)

WINDOW = display.set_mode([750, 500])

background = scale(load('background.jpg'), [750, 500])

game = True
finish = False

clock = time.Clock()
fps = 60

font.init()

f1 = font.Font(None, 80) 

win = f1.render('ти переміх', True, [81, 205, 45])
lose = f1.render('ти прохрав', True, [215, 0, 0])


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        WINDOW.blit(background, [0, 0])
        player.reset()
        wall1.reset() 
        wall2.reset() 
        wall3.reset() 
        wall4.reset() 
        player2.reset()
        player3.reset()
        player4.reset()
    
        player.update()
        player3.update()
        player4.update()
        
        if collide_rect(player, player2):
            finish = True
            WINDOW.blit(win, [250, 210])
            
        if collide_rect(player, player3):
            finish = True
            WINDOW.blit(lose, [250, 210])
            
        if collide_rect(player, player4):
            finish = True
            WINDOW.blit(lose, [250, 210])
        
        if collide_rect(player, wall1) or collide_rect(player, wall2) or collide_rect(player, wall3) or collide_rect(player, wall4):
            finish = True
            WINDOW.blit(lose, [250, 210])
        
    display.update()
    clock.tick(fps)  
    
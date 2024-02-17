from pygame import *

#створи вікно гри
window = display.set_mode([750, 550])

#задай фон сцени

#background = image.load('background.png')
#background = transform.scale(background, [750, 550])

background = transform.scale(image.load('background.png'), [750, 550])
#створи 2 спрайти та розмісти їх на сцені
sprite1 = transform.scale(image.load('sprite1.png'), [82, 80])
x1 = 50
y1 = 450

sprite2 = transform.scale(image.load('sprite2.png'), [82, 80])
x2 = 650
y2 = 450


#оброби подію «клік за кнопкою "Закрити вікно"»

geme = True

clock = time.Clock()
FPS = 60

while geme:
    for e in event.get():
        if e.type == QUIT:
            geme = False
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    keys = key.get_pressed()
    if keys[K_UP]:
        y1-=10
        
    if keys[K_DOWN]:
        y1+=10

    if keys[K_LEFT]:
        x1-=10
        
    if keys[K_RIGHT]:
        x1+=10

    if keys[K_w]:
        y2-=10
        
    if keys[K_s]:
        y2+=10

    if keys[K_a]:
        x2-=10
        
    if keys[K_d]:
        x2+=10

#K_a # вліво
#K_w # вверх
#K_s # вниз
#K_d # вправо

    
    
    
    
    display.update()
    clock.tick(FPS)
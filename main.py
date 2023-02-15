import pygame
from sys import exit
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((760,575))
pygame.display.set_caption('Vidya Gaem')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)
sky_surface = pygame.image.load("gfx/sky/mtsky.png").convert()
bird1 = pygame.image.load("gfx/sprite/bird1.png")
bird2 = pygame.image.load("gfx/sprite/bird2.png")
bird3 = pygame.image.load("gfx/sprite/bird3.png")
text_surface = test_font.render('WuTang Clan',True,'Green')
bird_sprite = [bird1,bird2,bird3]
animate = 0
bird_x = -200
bird_y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if animate == 2:
        animate = 0
    else:
        animate += 1
    screen.blit(sky_surface,(-300,-300))
    screen.blit(text_surface,(20,20))
    screen.blit(bird_sprite[animate],(bird_x,bird_y))
    bird_x += 10
    if bird_x == 800:
        bird_x = -400
    pygame.display.update()
    clock.tick(10)
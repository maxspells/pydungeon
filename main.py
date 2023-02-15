import pygame
from sys import exit
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((760,575))
pygame.display.set_caption('Vidya Gaem')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

sky_surface = pygame.image.load("gfx/sky.png")
text_surface = test_font.render('WuTang Clan',True,'Green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(20,20))

    pygame.display.update()
    clock.tick(60)
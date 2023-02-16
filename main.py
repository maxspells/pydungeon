import pygame
import random
from sys import exit
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Vidya Gaem')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)
sky_surface = pygame.image.load("gfx/field.jpg").convert()
pikachu = pygame.image.load("gfx/pikachu.png")
pika_rect = pikachu.get_rect(midbottom = (400,400))
pokeball = pygame.image.load("gfx/pokeball.png")
pos = [400,400]
ball_rect = pokeball.get_rect(midbottom = (pos))
counter = 0
text_surface = test_font.render(str(counter),True,'Black')
pikachu_x = 200
pikachu_y = 440

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            ball_rect.midbottom = pos
            print(pos)
    screen.blit(sky_surface,(-300,-500))
    screen.blit(text_surface,(20,20))
    screen.blit(pikachu,pika_rect)
    screen.blit(pokeball,ball_rect)
    if pika_rect.colliderect(ball_rect):
        pikachu_x = random.randint(100,700)
        pikachu_y = random.randint(350,520)
        pika_rect.midbottom = pikachu_x,pikachu_y
        counter += 1
        text_surface = test_font.render(str(counter),True,'Black')
    pygame.display.update()
    clock.tick(10)
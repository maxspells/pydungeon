import pygame
import random
import os
from sys import exit
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Pikachu')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)
music = pygame.mixer.music.load(os.path.join('sound/Route1.mp3'))
sky_surface = pygame.image.load("gfx/field.jpg").convert()
pikachu2 = pygame.image.load("gfx/pikachu2.png")
pikachu = pygame.image.load("gfx/pikachu.png")
pika_rect = pikachu.get_rect(midbottom = (400,400))
pokeball = pygame.image.load("gfx/pokeball.png")
pos = [400,400]
ball_rect = pokeball.get_rect(midbottom = (pos))
counter = 0
text_surface = test_font.render(str(counter),True,'Black')
pikachu_x = 200
pikachu_y = 440
caught = []
pocket_x = -35
pocket_y = -60
catch = False
pygame.mixer.music.play(-1)
while True:
    screen.blit(sky_surface,(-300,-500))
    if catch == True:
        pocket_x = -35
        for each in caught:
            screen.blit(each,(pocket_x,pocket_y))
            pocket_x += 33
    screen.blit(text_surface,(400,250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            ball_rect.midbottom = pos
      
    
    screen.blit(pikachu,pika_rect)
    screen.blit(pokeball,ball_rect)
    if pika_rect.colliderect(ball_rect):
        pikachu_x = random.randint(100,700)
        pikachu_y = random.randint(350,520)
        pika_rect.midbottom = pikachu_x,pikachu_y
        counter += 1
        text_surface = test_font.render(str(counter),True,'Black')
        caught.append(pikachu2)
        catch = True
    pygame.display.update()
    clock.tick(60)
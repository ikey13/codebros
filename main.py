import pygame
import sys
import random

pygame.init

screen = pygame.display.set_mode((575,1024))

background = pygame.image.load("/Users/isaac/Desktop/vscode/background.png").convert()
bird = pygame.image.load("/Users/isaac/Desktop/vscode/untitled folder/bluebird-midflap.png").convert()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0,0))
    screen.blit(bird , (0,0))
    pygame.display.update()

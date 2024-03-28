#import modules
import pygame
from sys import exit 
import random
#initialize modules
pygame.init()

#color variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
gray = (128, 128, 128)
light_gray = (200, 200, 200)
dark_gray = (100, 100, 100)

#define variables
width, height = 800, 600
running = True
clock = pygame.time.Clock()
w, h = 30, 30
man_speed = 3
score = 0
#create coin
coin_x, coin_y = random.randint(0, width), random.randint(0, height)
coin_image = pygame.image.load('desktop/assets/coin.png')
coin_image = pygame.transform.scale(coin_image, (w, h))
coin_rect = coin_image.get_rect(coin_x, coin_y)
def reset_coin():
    coin_x = random.randint(0, width - w)
    coin_y = random.randint(0, height - h)
#create background image
background = pygame.image.load('desktop/assets/background.jpeg')
background = pygame.transform.scale(background, (width, height))
#create player
man_x, man_y = width/2, height/2
man = pygame.Rect(man_x, man_y, 50, 50)
man.x = man_x
man.y = man_y
#create window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumper")

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     #movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        man_x -= man_speed
    if keys[pygame.K_d]:
        man_x += man_speed
    if keys[pygame.K_w]:
        man_y -= man_speed
    if keys[pygame.K_s]:
        man_y += man_speed
    man.x = man_x
    man.y = man_y
    if man.colliderect(coin_rect):
        score += 1
        reset_coin()
    
    #draw elements  
    screen.blit(background, (0, 0))
    screen.blit(coin_image, (coin_x, coin_y))
    pygame.draw.rect(screen, blue, man)
    #updates everything and defines frame rate

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    screen.fill((dark_gray))
if not running:
    exit()
import pygame
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
playerx = 0
playery = 0

player_height = 50
player_width = 50
player = pygame.Rect(screen_width/2,screen_height/2,player_height,player_width)

running = True

while running:
    screen.fill("black")
    pygame.draw.rect(screen,'red', player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1/2,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        pygame.display.update()
import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/pixeltype.ttf',50) #font type,font size

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surfacr = test_font.render('My game',False,'Black')
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
snail_x_pos = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0)) # blit means block of image transfer
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surfacr,(300,50))
    snail_x_pos -= 4
    if snail_x_pos< -100 : snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,250))
    screen.blit(player_surf,(player_rect))
    
            
    pygame.display.update()
    clock.tick(60)

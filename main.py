import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

sky_surface= pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game',False,'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
vx=-2
snail_x0=100

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,sky_surface.get_height()))
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  
  #screen.blit(test_surface,(200,100))
  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,sky_surface.get_height()))
  screen.blit(text_surface,(300,50))
  if snail_x0>0-snail_surface.get_width():
    snail_x0=snail_x0+vx
  else:
    snail_x0=screen.get_width()+snail_surface.get_width()
  screen.blit(snail_surface,(snail_x0,250))

  screen.blit(player_surface,player_rect)

  pygame.display.update()
  clock.tick(60)
  #


import pygame
from ship import *
pygame.init()
screen_info=pygame.display.Info()
print(screen_info)
size=(width,height)=(screen_info.current_w,screen_info.current_h)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
color= (30,0,30)
Numlevels = 4
Level = 1
AsteroidCount = 3
Player = Ship()
def main():
  while Level <= Numlevels:
    clock.tick(60)\
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT
          Player.speed[0] = 10
    Player.update()
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()
if __name__=='__main__':
  main()
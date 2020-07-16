import pygame , random
from ship import *
from asteroid import *
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
Player = Ship((20,200))
Attack = Asteroid(random.randint((50,500)),(random.randint(50,500))
#Asteroids = pygame.sprite.Group()
def main():
  while Level <= Numlevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 10
        if event.key == pygame.K_UP:
          Player.speed[1] = -10
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          Player.speed[0] = -10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 0
        if event.key == pygame.K_UP:
          Player.speed[1] = 0
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 0
        if event.key == pygame.K_LEFT:
          Player.speed[0] = 0
    Player.update()
    Attack.update()
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    screen.blit(Attack.image, Attack.rect)
    pygame.display.flip()
if __name__=='__main__':
  main()
import pygame , random , pandas as pd
from ship import *
from asteroid import *
pygame.init()
screen_info=pygame.display.Info()
print(screen_info)
size=(width,height)=(screen_info.current_w,screen_info.current_h)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
color= (30,0,30)
Numlevels = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
AsteroidCount = 0

Player = Ship((LevelData['PlayerX'],LevelData['PlayerY']))
#Attack = Asteroid((400,300))
Asteroids = pygame.sprite.Group()
gf =pd.read_csv('game_info.csv')
def init():
  global AsteroidCount
  Player.reset((20,200))
  Asteroids.empty()
  AsteroidCount = LevelData['AsteroidCount']
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid((400,300))) 

def main():
  global Level
  init()
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
    #Attack.update()
    screen.fill(color)
    Asteroids.update()
    gets_hit = pygame.sprite.spritecollide(Player, Asteroids, False)
    Asteroids.draw(screen)
    screen.blit(Player.image, Player.rect)
    #screen.blit(Attack.image, Attack.rect)
    pygame.display.flip()
    if Player.checkReset(width):
      init()
    if Level == NumLevels:
      break
    else:
      Level += 1
      init()
    elif gets_hit:
      Player.reset((LevelData['PlayerX'],LevelData['PlayerY']))
if __name__=='__main__':
  main()
 
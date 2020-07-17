import pygame , random

class Asteroid(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    self.image = pygame.image.load('asteroid.png')
    self.image = pygame.transform.smoothscale(self.image, (80,80))
    self.rect = self.image.get_rect()
    self.image = pygame.transform.rotate(self.image,(270))
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,3)
    rotation = random.randint(0,360)
    self.speed.rotate_ip(rotation)
    self.image = pygame.transform.rotate(self.image, int(180 - rotation))
  def update(self):
    screen_info = pygame.display.Info()
    self.rect.move_ip(self.speed)
    if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
      self.speed[1] *= -1
      self.image = pygame.transform.flip(self.image,True, False)
      self.rect.move_ip(self.speed[0], 0)
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:
      self.speed[0] *= -1
      self.image = pygame.transform.flip(self.image,False, True)
      self.rect.move_ip(0,self.speed[1])
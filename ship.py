import pygame

class Ship(pygame.sprite.Sprite):
  def __init()__(self):
    super().__init__()
    self.image = pygame.image.load('ship.png')
    self.image = pygame.transform.smoothscale((self.image,(80,80))
    self.rect = self.image.get_rect()
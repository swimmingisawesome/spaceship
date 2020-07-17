import pygame
import random

class Ship(pygame.sprite.Sprite): 
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load('ship.png')
    self.image = pygame.transform.smoothscale(self.image, (40, 40))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.image = pygame.transform.rotate(self.image, int(-90))

    self.speed = pygame.math.Vector2(0, 0)

  def update(self):
    self.rect.move_ip(self.speed)

  def checkReset(self, endPos):
    return self.rect.center[0] > endPos
    

  def reset(self, pos):
    self.rect.center = pos
    
    

  



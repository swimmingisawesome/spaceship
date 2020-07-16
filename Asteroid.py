import pygame 
import random

class Asteroid(pygame.sprite.Sprite): 
  def __init__ (self, pos):
    super().__init__()
    self.image = pygame.image.load('asteroid.png')
    self.image = pygame.transform.smoothscale(self.image, (40, 40))
    self.rect = self.image.get_rect()

    rotation = random.randint(1, 360)
    self.image = pygame.transform.rotate(self.image, int(rotation))
    self.rect.center = pos

    self.speed = pygame.math.Vector2(random.randint(-10, 10), random.randint(-10, 10))
     
    
  def update(self):
    self.rect.move_ip(self.speed)
    if self.rect.top < 0 or self.rect.bottom > 600:
      self.speed[1] *= -1
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect.move_ip(0, self.speed[1])    

    if self.rect.right < 0 or self.rect.left > 800:
      self.speed[0] *= -1
      self.image = pygame.transform.flip(self.image, True, False)
      self.rect.move_ip(self.speed[0], 0)  

  

import pygame
import random
from Ship import *
from Asteroid import *
pygame.init()

screen_info = pygame.display.Info()
print(screen_info)

w = pygame.display.set_mode((800, 600))
c = pygame.time.Clock()
color = (30, 0, 30)

NumLevels = 4
Level = 1
AsteroidCount = 3
Player = Ship((20, 200))
Asteroids = pygame.sprite.Group()
#Asteroids = Asteroid((random.randint(50, 500), random.randint(50, 700)

  #, (random.randint(10, 100), random.randint(10, 100))
def init():
  """
  global AsteroidCount
  Player.reset((20, 200))
  Asteroid.empty()
  AsteroidCount += 3
  """
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid((400, 300))
    
    
    #(random.randint(50, 500), random.randint(50, 700)))

def main():
  init()
  while Level <= NumLevels:
    c.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key== pygame.K_RIGHT:
          Player.speed[0] = 10
        if event.key== pygame.K_DOWN:
          Player.speed[1] = 10
        if event.key== pygame.K_UP:
          Player.speed[1] = -10
        if event.key== pygame.K_LEFT:
          Player.speed[0] = -10
      if event.type == pygame.KEYUP:
        if event.key== pygame.K_RIGHT:
          Player.speed[0] = 0
        if event.key== pygame.K_DOWN:
          Player.speed[1] = 0
        if event.key== pygame.K_UP:
          Player.speed[1] = 0
        if event.key== pygame.K_LEFT:
          Player.speed[0] = 0
    Player.update()
    Asteroids.update()
    w.fill(color)
    Asteroids.draw(w)
    w.blit(Player.image, Player.rect)
    w.blit(Asteroids.image, Asteroids.rect)
    pygame.display.flip()

    if Player.checkReset(width):
      init()

if __name__=='__main__':
  main() 





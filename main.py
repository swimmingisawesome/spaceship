import pygame
import random
import pandas as pd
from Ship import *
from Asteroid import *
pygame.init()

screen_info = pygame.display.Info()
print(screen_info)

w = pygame.display.set_mode((800, 600))
c = pygame.time.Clock()
color = (30, 0, 30)

df = pd.read_csv('game_info.csv')

# df stors the whole dataframe
#df['PlayerX'] -> gives you acess to the colunm PlayerX
#df.iloc[row_name/row_number] -> gives you acess to the row

NumLevels = df['LevelNum'].max() 
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
AsteroidCount = LevelData['AsteroidCount']
Player = Ship((LevelData['PlayerX'], LevelData['PlayerY']))
Asteroids = pygame.sprite.Group()
#Asteroids = Asteroid((random.randint(50, 500), random.randint(50, 700)

  #, (random.randint(10, 100), random.randint(10, 100))
def init():
  global AsteroidCount
  LevelData = df.iloc[Level]
  Player.reset((LevelData['PlayerX'], LevelData['PlayerY']))
  Asteroids.empty()
  AsteroidCount = LevelData['AsteroidCount']
 
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid((400, 300)))
def win():
  font = pygame.font.SysFont(None, 70)   
  text = font.render("You Escaped!", True, (255, 0, 0))
  text_rect = text.get_rect()
  text_rect.center = (400, 300)
  while True:
    w.fill(color)
    w.blit(text, text_rect)
    pygame.display.flip()


    #(random.randint(50, 500), random.randint(50, 700)))

def main():
  global Level
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
    gets_hit = pygame.sprite.spritecollide(Player, Asteroids, False)
    w.fill(color)
    Asteroids.draw(w)
    w.blit(Player.image, Player.rect)
    #w.blit(Asteroids.image, Asteroids.rect)
    pygame.display.flip()

    if Player.checkReset(800):
      if Level == NumLevels:
        break
      else:
        Level += 1
        init()

    elif gets_hit:
      Player.reset((LevelData['PlayerX'], LevelData['PlayerY']))

win()
if __name__=='__main__':
  main() 





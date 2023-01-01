import pygame
import sys

#spaceship class
class Base(pygame.sprite.Sprite):
    def __init__(self,width,height,position_x,position_y,direction,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center= [position_x,position_y]
    #def move(direction):

#da Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self,width,height,position_x,position_y,direction,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center= [position_x,position_y]


#basic game window
pygame.init()
clock =pygame.time.Clock()
screen = pygame.display.set_mode((1440,810))  
done = False  
borders=30


#the actual spaceships
ship_1 = Base(50,100,150,405,'R',(255,150,255))
ship_2 = Base(50,100,1290,405,'L',(150,255,100))

ship_group = pygame.sprite.Group()
ship_group.add(ship_1)
ship_group.add(ship_2)


    
while not done:
    pygame.display.flip()  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            done = True
            break
    pygame.display.flip()
    ship_group.draw(screen)
    clock.tick(60)

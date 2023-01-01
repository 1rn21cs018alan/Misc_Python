import pygame  
    
pygame.init()  
screen = pygame.display.set_mode((900,500))  
done = False
x=30
y=30
recwidth=70
recheight=60
timeval=0;
swtstate=0;
while not done:
    pygame.display.flip()  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            done = True
            break
        if (event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP):
            key_name = pygame.key.name(event.key)  
            key_name = key_name.upper()  
            if event.type == pygame.KEYDOWN:  
                #print(u'"{}" key pressed'.format(key_name))
                if(key_name=="UP")and(y>30):
                    y=y-1
                if(key_name=="DOWN")and(y<410):
                    y=y+1
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(x,y,recwidth,recheight))  

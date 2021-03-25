import pygame
import math


pygame.init()

pygame.display.set_caption('Fourier')
backwin = pygame.display.set_mode((1000,1250))
win = pygame.display.set_mode((1000,1250))



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball(object): 
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
       
time  = 0

run = True

epi = float (input("ingrese el valor de b: "))
if isinstance(epi, float) == True:
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        radio = 40
        posx = 250
        posy = 175
        jumper = Ball(posx,posy,radio)
        
        x = int (radio*2 *math.cos(time))
        y = int (radio* 2 * math.sin(time))
        
        keys = pygame.key.get_pressed()
        
        jumper2 = Ball(int(x*3/2 +posx),int(y*3/2 +posy) ,int(radio))
        
        rect = [0,0,450,350]
        rect2 = [1250/2,0, 1250, 500]
        
        newx = int (x*3/2 +posx)
        newy = int (y* 3/2 +posy )
        dosx = int (radio*epi *math.cos(3*time)) + 3*radio *math.cos(time) +posx
        dosy = int (radio*epi *math.sin(3*time)) +3*radio *math.sin(time) +posy
        
        time -= 0.003
        
        pygame.draw.lines(win, WHITE, False, [(posx, posy),( x+ posx, y +posy)] )
        pygame.draw.circle(win, WHITE, (jumper.x,jumper.y), int(2*radio),2)
        pygame.draw.circle(win, WHITE, (jumper2.x,jumper2.y), int(radio),2)
        
        
        pygame.draw.lines(win, RED, False, [(newx, newy),(dosx, dosy)])
        #pygame.draw.lines(backwin, WHITE, False, [(dosx, dosy), (int(-time*25)+posx+100, int(dosy))])
        
        pygame.display.update()  
        
        backwin.fill(BLACK, rect)
        
        if time > -15:
            pygame.draw.circle(backwin, WHITE, (int(-time*25)+posx+230, int(dosy)  ), 1,0)
            pygame.draw.circle(backwin, WHITE, (int(dosx)+400, int(dosy)+280), 1,0)
            pygame.draw.circle(backwin, WHITE, (int(dosx), int(-time*25)+posx+100), 1,0)
        
        
        
    pygame.quit()
    
print("Gracias por usar mi programita :3")


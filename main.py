import pygame
import random
pygame.init()

#Pygame initialization
pygame.init()
(width, height) = (1280,720)
bg_color = (0,0,0)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Algorithm visualizer")
screen.fill(bg_color)

#The bars
class Bar:
    def __init__(self,value,x):
        self.val = value
        self.pos = x
        self.color = (255,255,255)

    def draw(self):
        pygame.draw.line(screen, self.color, (self.pos,700), (self.pos,700-self.val), 10)

    def move(self,dest):
        self.pos = dest
        self.draw()
    
#To switch bars
def bar_switch(b1,b2):
    p1 = b1.pos
    p2 = b2.pos
    b1.move(p2)
    b2.move(p1)

# Tableau contenant les barres

def rand():
    tab = []
    screen.fill(bg_color)
    position = 40
    for i in range(100):
        b = Bar(random.randint(1,500),position)
        tab.append(b)
        position += 12
    for i in range(len(tab)):
        tab[i].draw()
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(25, 25, 25, 25))

rand()

running = True
while running:
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rand()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 25 <= mouse[0] <= 50 and 25 <= mouse[1] <= 50:
                rand()
                
import algorithms
import pygame
import random
pygame.init()

(width, height) = (1280,720)
bg_color = (0,0,0)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Algorithm visualizer")
screen.fill(bg_color)

class bar:
    def __init__(self,value,x):
        self.val = value
        self.pos = x

    def draw(self):
        pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.pos,700), (self.pos,700-self.val), 10)

    def move(self,dest):
        self.pos = dest
        self.draw()
    
def bar_switch(b1,b2):
    p1 = b1.pos
    p2 = b2.pos
    b1.move(p2)
    b2.move(p1)

tab = []
position = 40
for i in range(100):
    b = bar(random.randint(1,500),position)
    tab.append(b)
    tab[i].draw()
    position += 12

def rand():
    tab = []
    position = 40
    for i in range(100):
        b = bar(random.randint(1,500),position)
        tab.append(b)
        tab[i].draw()
        position += 12

def bubble(t):
    for i in range(len(t)):
        for n in range(len(t)-1-i):
            if t[n].val > t[n+1].val:
                bar_switch(t[n],t[n+1])
    return t

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                screen.fill(bg_color)
                bubble(tab)
            elif event.key == pygame.K_x:
                screen.fill(bg_color)
                rand()
import pygame
import random

pygame.init()

(width, height) = (1280,720)
bg_color = (255,255,255)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Algorithm visualizer")
screen.fill(bg_color)

class bar:
    def __init__(self,value,x):
        self.val = value
        self.pos = x

    def draw(self):
        pygame.draw.line(screen, (0,0,0), (self.pos,600), (self.pos,self.val), 10)

    #def move(self):



bars = []
pos = 40
for i in range(100):
    bars.append(bar(random.randint(0,600), pos))
    bars[i].draw()
    pos += 12


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
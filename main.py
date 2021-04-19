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
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.pos,400,10,self.val))

    #def move(self):

values = []
pos = 40
for i in range(100):
    values.append(random.randint(10,500))
    b = bar(values[i], pos)
    b.draw()
    pos += 12

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
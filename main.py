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
        pygame.draw.line(screen, (255,255,255), (self.pos,700), (self.pos,700-self.val), 10)

tab = []
position = 40
for i in range(100):
    b = bar(random.randint(1,500),position)
    tab.append(b)
    tab[i].draw()
    position += 12
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Bruh haram")
### test pour le code graphique ###
import pygame
import algorithms
from random import randint
pygame.init()

screen = pygame.display.set_mode((720,1080))
pygame.display.set_caption('Algorithm Visualiser')
color = {'white': (255, 255, 255), 'red': (255, 0, 0), 'blue': (0, 255, 0), 'green': (0, 0, 255), 'black': (0, 0, 0)}

class Stick:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos,700), (self.pos, 700-self.val), 10)

    def move(self, new_pos):
        self.pos = new_pos
        self.draw()

barres = []
base_pos = 50
for i in range(50):
    pos = base_pos+(10*i)
    barre = Stick(10*randint(0,50), pos)

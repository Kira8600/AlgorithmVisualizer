#Importatin des bibliothèques
import pygame
import random

#Initialisation de PyGame
pygame.init()

#Classe barre
class Bar:
    def __init__(self,value,x,surface):
        self.pos = x
        self.val = value
        self.surface = surface
        self.color = (255,255,255)

    def draw(self):
        #Dessine une barre
        pygame.draw.line(self.surface, self.color, (self.pos,700), (self.pos,700-self.val), 10)

class Window:
    def __init__(self, width, height, bg_color, caption):
        self.tableau = []
        self.bg = bg_color
        self.width = width
        self.height = height
        self.caption = caption
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        self.surface.fill(self.bg)
        
    def random_bars(self):
        """
        Commence à 40 pixels et dessine le nombre de barres pour remplir l'écran automatiquement selon sa largeur.
        """
        position = 40
        for i in range((self.width -80) // 12):
            self.tableau.append(Bar(random.randint(0,500),position,self.surface))
            position += 12
    
    def refresh(self):
        """
        Remplis l'écran de noir et redessine les barres.
        """
        self.surface.fill(self.bg)
        for Bar in self.tableau:
            Bar.draw()
        pygame.display.flip()

window = Window(1280, 720, (0,0,0), "AlgoViz")
window.random_bars()
window.refresh()

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
                window.random_bars()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 25 <= mouse[0] <= 50 and 25 <= mouse[1] <= 50:
                print('Button 1 pressed')
                
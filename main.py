#Importation des bibliothèques
from time import sleep
import pygame
from random import randint

#Initialisation de PyGame
pygame.init()

#Classe barre
class Bar:
    def __init__(self,value,x,surface):
        self.pos = x
        self.val = value
        self.surface = surface
        self.color = (255,0,0)

    def draw(self):
        #Dessine une barre
        pygame.draw.line(self.surface, self.color, (self.pos,700), (self.pos,700-self.val), 10)

class Window:
    def __init__(self, width, height, caption):
        self.barres = []
        self.width = width
        self.height = height

        #Rectangle contenant le menu
        self.menu = pygame.Rect(0, 0, self.width, self.height // 6)

        #Boutons du menu :
        
        #Nom de la fenêtre
        self.caption = caption

        #Création et configuration de la surface
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        self.surface.fill((0,42,0))
        
    def random_bars(self):
        #Commence à 40 pixels et dessine le nombre de barres pour remplir l'écran automatiquement selon sa largeur.
        self.barres = []
        position = 40
        for i in range((self.width -80) // 12):
            self.barres.append(Bar(randint(0,500),position,self.surface))
            position += 12
    
    def refresh(self):
        """
        Remplis l'écran de noir et redessine les barres.
        """
        self.surface.fill((0,0,0))
        pygame.draw.rect(self.surface, (230,230,230), self.menu)
        for Bar in self.barres:
            Bar.draw()
        pygame.display.flip()

window = Window(1280, 720, "AlgoViz")
window.random_bars()
window.refresh()

def tri_selection(tab):
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    for n in range (len(tab)):
        for v in range (n+1, len(tab)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        window.random_bars()
                        window.refresh()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 25 <= mouse[0] <= 50 and 25 <= mouse[1] <= 50:
                        print('Button 1 pressed')
            if tab[n].val > tab[v].val:
                tab[n].val, tab[v].val = tab[v].val, tab[n].val
                tab[n].color = (0,255,0)
                window.refresh()
    return tab

"""
def tri_insertion(tab):
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    for i in range(1, len(tab)):
        valeur = tab[i].val
        pos = i
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    window.random_bars()
                    window.refresh()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 25 <= mouse[0] <= 50 and 25 <= mouse[1] <= 50:
                        print('Button 1 pressed')
        while pos > 0 and tab[pos-1].val > valeur:
            tab[pos].val = tab[pos-1].val
            pos = pos - 1
            tab[pos].color = (0,255,0)
            window.refresh()
        tab[pos].val = valeur
        
    return tab
"""
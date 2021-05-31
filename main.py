#Importation des bibliothèques
from time import sleep
import pygame
from random import randint, random

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
        for Bar in self.barres:
            Bar.draw()
        pygame.display.flip()
        sleep(0.01)

window = Window(1280, 720, "AlgoViz")
window.random_bars()
window.refresh()
mouse = pygame.mouse.get_pos()
pygame.display.flip()


def boucle():
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

def tri_selection(tab):
    for n in range (len(tab)):
        for v in range (n+1, len(tab)):
            boucle()
            if tab[n].val > tab[v].val:
                tab[n].color = (255,200,0)
                tab[v].color = (255,200,0)
                tab[n].val, tab[v].val = tab[v].val, tab[n].val
                window.refresh()
                tab[v].color = (255,0,0)
        tab[n].color = (0,255,0)
        window.refresh()
    sleep(2)
    return tab

def tri_insertion(tab):
    tab[0].color = (0,255,0)
    for i in range(1, len(tab)):
        valeur = tab[i].val
        pos = i
        boucle()
        while pos > 0 and tab[pos-1].val > valeur:
            tab[pos].val, tab[pos-1].val = tab[pos-1].val, tab[pos].val
            tab[pos].color = (0,255,0)
            tab[pos-1].color = (255,0,0)
            pos = pos - 1
            window.refresh()
        tab[pos].color = (0,255,0)
        window.refresh()
        tab[pos].val = valeur      
    sleep(2)
    return tab

def tri_bulle(Tab):
    for i in range(len(Tab)):
        for n in range(len(Tab)-1-i):
            boucle()
            if Tab[n].val > Tab[n+1].val:
                Tab[n].val, Tab[n+1].val = Tab[n+1].val, Tab[n].val
                window.refresh()
        Tab[len(Tab)-i-1].color = (0,255,0)
        window.refresh()
    return Tab

def verification(tab):
    for i in range(len(tab)-1):
        if tab[i].val > tab[i+1].val:
            return False
    return True

def tri_bogo(tab):
    while not verification(tab):
        boucle()
        vals = [bar.val for bar in tab]
        for bar in tab:
            i = randint(0, len(vals)-1)
            bar.val = vals[i]
            vals.pop(i)
            bar.color = (randint(0,255), randint(0,255), randint(0,255))
        window.refresh()
    for bar in tab:
        bar.color = (0,255,0)
    window.refresh()
    sleep(3)
    return tab


def tri_rapide(Tab):
    boucle()
    if Tab == []:
        return Tab
    window.refresh()
    pivot = Tab[0]
    pivot.color = (255,200,0)
    L1 = [i for i in Tab[1:] if i.val <= pivot.val]
    L2 = [i for i in Tab[1:] if i.val > pivot.val]
    pivot.color = (0,255,0)
    window.refresh()
    return [tri_rapide(L1)] + [pivot] + [tri_rapide(L2)], window.refresh()

window.barres = tri_rapide(window.barres)
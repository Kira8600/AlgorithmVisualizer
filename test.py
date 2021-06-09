### test ####Importation des bibliothèques
from time import sleep
import pygame
from random import randint, random
import tkinter as tk

#Initialisation de PyGame
pygame.init()
noir = (0,0,0)
blanc = (255, 255, 255)
vert = (125, 255, 181)
rouge = (255, 0, 0)

#Classe barre
class Bar:
    def __init__(self,value,x,surface):
        self.pos = x
        self.val = value
        self.surface = surface
        self.color = blanc

    def draw(self):
        #Dessine une barre
        pygame.draw.line(self.surface, self.color, (self.pos,700), (self.pos,700-self.val), 5)

class Window:
    def __init__(self, width, height, caption):
        self.barres = []
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("arial.ttf", 24)

        #Rectangle contenant le menu
        self.menu = pygame.Rect(0, 0, self.width, self.height // 6)

        #Nom de la fenêtre
        self.caption = caption

        #Création et configuration de la surface
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        self.surface.fill((0,42,0))
        
    def generer(self):
        #Commence à 40 pixels et dessine le nombre de barres pour remplir l'écran automatiquement selon sa largeur.
        self.barres = []
        position = 40
        for i in range((self.width -80) // 7):
            self.barres.append(Bar(randint(1,500),position,self.surface))
            position += 7
    
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
window.generer()
window.refresh()
mouse = pygame.mouse.get_pos()
pygame.display.flip()

def boucle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def tri_selection(tab):
    for n in range (len(tab)):
        for v in range (n+1, len(tab)):
            boucle()
            if tab[n].val > tab[v].val:
                tab[n].color = (255,200,0)
                tab[v].color = (255,200,0)
                tab[n].val, tab[v].val = tab[v].val, tab[n].val

                tab[n].color = vert

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

def fusion(T1,T2):
    if T1 == []:
        return T2
    if T2 == []:
        return T1
    if T1[0].val < T2[0].val:
        return [T1[0]] + [fusion(T1[1:], T2)]
    else:
        return [T2[0]] + [fusion(T2[1:], T1)]

def tri_fusion(Tab):
    if Tab == []:
        return Tab
    else:
        milieu = len(Tab)//2
        return fusion(tri_fusion(Tab[:milieu]), tri_fusion(Tab[milieu:]))

#Initialisation de tKinter
root = tk.Tk()

titre = tk.Label(root, text = "Algorithm Visualizer", height = 3, width = 20,font = ('Arial Bold', 15))
sous_titre = tk.Label(root, text = "Programmé par :", font = ('Arial', 8))
noms = tk.Label(root, text = "ARCHAMBAULT Julien\n ATTLAN Jonas\n DESIDE Maxime\n GARRIGUES Jean-Gabriel", height = 5)

sous_titre.pack()
titre.pack()
noms.pack()

#Boutons
button1=tk.Button(root, text="Tri par insertion", command = lambda : tri_insertion(window.barres))
button1.pack()

button2=tk.Button(root, text="Tri par selection", command = lambda : tri_selection(window.barres))
button2.pack()

button3=tk.Button(root, text="Tri Bogo", command = lambda : tri_bogo(window.barres))
button3.pack()

button4=tk.Button(root, text="Tri à bulles", command = lambda : tri_bulle(window.barres))
button4.pack()

button5=tk.Button(root, text="Tri radix")
button5.pack()

button6=tk.Button(root, text="Tri rapide", command = lambda : tri_rapide(window.barres))
button6.pack()

button7=tk.Button(root, text="Tri rapide", command = lambda : tri_fusion(window.barres))
button7.pack()

root.mainloop()

running = True
while running:
    #mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
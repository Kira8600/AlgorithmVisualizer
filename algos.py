import pygame
import time
import main

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
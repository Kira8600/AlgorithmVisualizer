import pygame

pygame.init()

(width, height) = (1280,720)
bg_color = (255,255,255)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Algorithm visualizer")
screen.fill(bg_color)

rect = pygame.Rect(40,350,10,100)
rect2 = pygame.Rect(52,350,10,100)
pygame.draw.rect(screen, (0,0,0),rect)
pygame.draw.rect(screen, (0,0,0),rect2)


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
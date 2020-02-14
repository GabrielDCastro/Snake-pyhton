import pygame

pygame.init()

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)
preto = (0, 0, 0)
screen.fill(preto)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

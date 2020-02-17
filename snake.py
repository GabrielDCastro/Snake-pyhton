import random

import pygame

pygame.init()

resolution = (500, 500) #tamanho de 500 pixels por 500 pixels
screen = pygame.display.set_mode(resolution) #criamos a tela
preto = (0, 0, 0) # definimos uma cor preta. Modelo RGB que vai de 0 a 250
screen.fill(preto) # definimos a cor da tela

class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.corpo = [(100, 100), (90, 100)]

    def blit(self, screen):
        for posicao in self.corpo: #mostrando todos os blocos do corpo

            screen.blit(self.textura, posicao)

class Fruta: #criamos uma classe pra fruta
    cor = (255, 0 , 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho) #modo que o pygame define o objeto
        self.textura.fill(self.cor)
        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)  # colocamos a fruta na tela

frutinha = Fruta() #Instanciamos a fruta
cobrinha = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Botão de fechar o jogo
            exit()

    frutinha.blit(screen)
    cobrinha.blit(screen)

    pygame.display.update() #fazemos o update da tela a cada while

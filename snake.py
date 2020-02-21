import random
import time

import pygame

pygame.init()

resolution = (500, 500) #tamanho de 500 pixels por 500 pixels
screen = pygame.display.set_mode(resolution) #criamos a tela
preto = (20, 20, 20) # definimos uma cor preta. Modelo RGB que vai de 0 a 250
screen.fill(preto) # definimos a cor da tela
clock = pygame.time.Clock()#restringir o FPS, caso contrário cada máquina teria uma velocidade diferente

class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)
    velocidade = 10

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.corpo = [(100, 100), (90, 100)]
        self.direcao = 'direita' # a direção muda, por isso coloca ela no init e não nos atributos base

    def blit(self, screen):
        for posicao in self.corpo: #mostrando todos os blocos do corpo

            screen.blit(self.textura, posicao)

    def andar(self):
        cabeca = self.corpo[0]
        x =cabeca[0]
        y = cabeca[1]

        if self.direcao == "direita":
            self.corpo.insert(0, (x + self.velocidade , y))
        elif self.direcao == "esquerda":
            self.corpo.insert(0, (x - self.velocidade , y))
        elif self.direcao == "cima":
            self.corpo.insert(0, (x , y - self.velocidade))
        elif self.direcao == "baixo":
            self.corpo.insert(0, (x , y + self.velocidade))

        self.corpo.pop(-1)

    def cima(self):
        if self.direita != "baixo":
            self.direcao = "cima"
    def baixo(self):
        if self.direcao != "cima":
            self.direcao = "baixo"
    def esquerda(self):
        if self.direcao != "direita":
            self.direcao = "esquerda"
    def direita(self):
        if self.direcao != "esquerda":
            self.direcao = "direita"

    def colisao_frutinha(self, frutinha):
        return self.corpo[0] == frutinha.posicao

    def comer(self):
        self.corpo.append((0, 0))

    def colisao_parede(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        return x < 0 or y < 0 or x > 490 or y > 490

    def auto_colisao(self):
        return self.corpo[0] in self. corpo[1:] # se a cabeça (corpo[0]) encostar no resto (corpo1:) ele colide e perde

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
    clock.tick(20) #limitanto pra 20 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Botão de fechar o jogo
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cobrinha.cima()
                break
            if event.key == pygame.K_DOWN:
                cobrinha.baixo()
                break
            if event.key == pygame.K_LEFT:
                cobrinha.esquerda()
                break
            if event.key == pygame.K_RIGHT:
                cobrinha.direita()
                break



    if cobrinha.colisao_frutinha(frutinha):
        cobrinha.comer()
        frutinha = Fruta()

    if cobrinha.colisao_parede():
        cobrinha = Snake()

    if cobrinha.auto_colisao():
        cobrinha = Snake()
        
    cobrinha.andar()
    screen.fill(preto)
    frutinha.blit(screen)
    cobrinha.blit(screen)

    pygame.display.update() #fazemos o update da tela a cada while

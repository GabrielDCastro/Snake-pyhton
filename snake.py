import pygame

pygame.init()

resolution = (500, 500) #tamanho de 500 pixels por 500 pixels
screen = pygame.display.set_mode(resolution) #criamos a tela 
preto = (0, 0, 0) # definimos uma cor preta. Modelo RGB que vai de 0 a 250
screen.fill(preto) # definimos a cor da tela

class Fruta: #criamos uma classe pra fruta
    cor = (255, 0 , 0) 
    posicao = (100, 100)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho) #modo que o pygame define o objeto
        self.textura.fill(self.cor)

frutinha = Fruta() #Instanciamos a fruta

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Botão de fechar o jogo
            exit()

    screen.blit(frutinha.textura, frutinha.posicao) #colocamos a fruta na tela
    pygame.display.update() #fazemos o update da tela a cada while 

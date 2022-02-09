'''
Athor: Miqueias R.
Date: Mar 8, 2021
'''

import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()


#Configuração da tela
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('Maquina de separação')
fonte = pygame.font.SysFont('arial', 18, True, False)

#Contador
contador_x = 0
contador_y = 0

#Movimento
posicao_x = -50
posicao_y = 210
velocidade_x = 0
velocidade_y = 0
velocidade = 0.1

#Objeto
dimensao_objeto = 40
verificado_objeto = False
objeto_esteira = False

#Objetos cor
objeto_x = (50, 205, 50)
objeto_y = (30, 144, 255)
tipo_objeto = [objeto_x, objeto_y]
mensagem3 = 'SEPARADOR DESATIVADO'
texto3 = fonte.render(mensagem3, True, (255,0,0))

#Configuração da maquina 
esteira_ligada = False
while True:
    tela.fill((0,0,0))

    mensagem1 = f'Produtos X = {contador_x}'
    mensagem2 = f'Produtos Y = {contador_y}'
    texto1 = fonte.render(mensagem1, True, (250,250,250))
    texto2 = fonte.render(mensagem2, True, (250,250,250))
    

    if objeto_esteira == False:
        gerar_objeto = randint(0,1)
        objeto_esteira = True
    else:
        pygame.draw.rect(tela, tipo_objeto[gerar_objeto], (posicao_x, posicao_y, dimensao_objeto, dimensao_objeto))
        if posicao_y >= altura_tela + dimensao_objeto or posicao_y + dimensao_objeto <= 0:
            objeto_esteira = False
            if gerar_objeto == 0:
                contador_y += 1 
            else:
                contador_x += 1
            posicao_x = -50
            posicao_y = 210

            if esteira_ligada == False:
                velocidade_x = 0
            else:
                velocidade_x = velocidade
            velocidade_y = 0
        elif posicao_x >= (largura_tela/2 - dimensao_objeto) and verificado_objeto == False:
            if (gerar_objeto == 1):
                velocidade_x = 0
                velocidade_y = -velocidade - 0.02
            else:
                velocidade_x = 0
                velocidade_y = velocidade + 0.02
            verificado_objeto == True 

    posicao_x = posicao_x + velocidade_x
    posicao_y = posicao_y + velocidade_y
 
   
#Cenário
    #Esteira horizontal
    pygame.draw.line(tela, (250,250,250), (0,200),(320,200),2)
    pygame.draw.line(tela, (250,250,250), (0,260),(320,260),2)
    #Esteira vestical
    pygame.draw.line(tela, (255,255,0), (270,0),(270,480),2)
    pygame.draw.line(tela, (255,255,0), (330,0),(330,480),2)
    #Maquina
    pygame.draw.rect(tela, (128,128,128), (250,180,100,100))
    #Botão
    if esteira_ligada == False:
        pygame.draw.circle(tela, (255,0,0),(120,420),30) 
    else:
        pygame.draw.circle(tela, (0,255,0),(120,420),30)
    #Coletor
    pygame.draw.rect(tela, (105,105,105), (250,0,100,10))
    pygame.draw.rect(tela, (105,105,105), (250,470,100,10))
    pygame.draw.rect(tela, (105,105,105), (630,180,10,100))
    #Eventos no cenário
    if gerar_objeto == 0 and posicao_x >= (largura_tela/2 - dimensao_objeto):
        pygame.draw.rect(tela, (0,255,0), (250,180,100,100))
    elif gerar_objeto == 1 and posicao_x >= (largura_tela/2 - dimensao_objeto):
        pygame.draw.rect(tela, (0,0,255), (250,180,100,100))

    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
            #Funcionamento do butão
                pos = pygame.mouse.get_pos()
                if pos >= (90,390) and pos <= (150,470):
                    if esteira_ligada == False:
                        velocidade_x = velocidade                        
                        esteira_ligada = True
                        mensagem3 = 'SEPARADOR ATIVADO'
                        texto3 = fonte.render(mensagem3, True, (0,255,0)) 
                    else:
                        mensagem3 = 'SEPARADOR DESATIVADO'
                        texto3 = fonte.render(mensagem3, True,(255,0,0)) 
                        velocidade_x = 0 
                        esteira_ligada = False
                        
    tela.blit(texto1, (10,20))
    tela.blit(texto2, (10,40))
    tela.blit(texto3, (370,40))

    pygame.display.update()


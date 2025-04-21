import pygame
import time
import random

# Inicializa o pygame
pygame.init()

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobra')

# Clock
clock = pygame.time.Clock()
velocidade = 16

# Tamanho do bloco da cobra
tamanho_bloco = 10

# Fonte
fonte = pygame.font.SysFont("bahnschrift", 25)

def pontuacao(pontos):
    valor = fonte.render("Pontuação: " + str(pontos), True, white)
    tela.blit(valor, [0, 0])

def nossa_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, green, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo():
    game_over = False
    game_close = False

    x1 = largura / 2
    y1 = altura / 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not game_over:

        while game_close:
            tela.fill(black)
            mensagem("Você perdeu! Pressione C para continuar ou Q para sair", red)
            pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True

        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(blue)
        pygame.draw.rect(tela, red, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True

        nossa_cobra(tamanho_bloco, lista_cobra)
        pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()

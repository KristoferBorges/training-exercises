import pygame
import sys

pygame.init()

# Dimensões da janela
LARGURA = 800
ALTURA = 600

# Criando a janela do jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Cebola')

# Carregando a imagem do personagem
personagem = pygame.image.load('R.jpg')
# Coordenadas do personagem na tela
x = 0
y = 0

# Função para mover o personagem
def mover_personagem():
    global x, y
    # Verificando se alguma tecla foi pressionada
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # Mover para a esquerda
                x -= 10
            if event.key == pygame.K_RIGHT: # Mover para a direita
                x += 10
            if event.key == pygame.K_UP: # Mover para cima
                y -= 10
            if event.key == pygame.K_DOWN: # Mover para baixo
                y += 10

# Loop principal do jogo
while True:
    # Preenchendo a tela de branco
    tela.fill((255, 255, 255))

    # Movendo o personagem
    mover_personagem()

    # Desenhando o personagem na tela
    tela.blit(personagem, (x, y))

    # Atualizando a tela
    pygame.display.flip()

    # Verificando se o usuário deseja sair
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
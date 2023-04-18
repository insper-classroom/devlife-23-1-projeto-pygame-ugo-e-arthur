import pygame

pygame.init()

# Define as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define as cores
branco = (255, 255, 255)
laranja = (230, 115, 0)
laranja_escuro = (200, 100, 0)
laranja_claro = (255, 140, 0)

# Define Assets
titulo = pygame.font.Font('Chendolle.otf', 100)
imagem_texto_titulo = titulo.render('Show do Miranda', True, (0, 0, 0))
opcao1 = pygame.font.Font('Chendolle.otf', 4)
imagem_texto_opcao1 = titulo.render('Jogar', True, (0, 0, 0))
opcao2 = pygame.font.Font('Chendolle.otf', 40)
imagem_texto_opcao2 = titulo.render('Instruções', True, (0, 0, 0))
opcao3 = pygame.font.Font('Chendolle.otf', 40)
imagem_texto_opcao3 = titulo.render('Créditos', True, (0, 0, 0))


cara = pygame.image.load('Cara_Miranda.jpeg')
cara = pygame.transform.scale(cara, (150, 150))

# Define os retângulos de seleção
botao_largura = 400
botao_altura = 100
botao_x = (largura_tela - botao_largura) / 2
botao1_y = 200
botao2_y = botao1_y + botao_altura + 20
botao3_y = botao2_y + botao_altura + 20
botao1 = pygame.Rect(botao_x, botao1_y, botao_largura, botao_altura)
botao2 = pygame.Rect(botao_x, botao2_y, botao_largura, botao_altura)
botao3 = pygame.Rect(botao_x, botao3_y, botao_largura, botao_altura)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Preenche a tela com branco
    tela.fill(branco)

    # Desenha os retângulos de seleção com contorno laranja escuro
    pygame.draw.rect(tela, laranja, botao1)
    pygame.draw.rect(tela, laranja_escuro, botao1, 5)
    pygame.draw.rect(tela, laranja_claro, botao1.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, botao2)
    pygame.draw.rect(tela, laranja_escuro, botao2, 5)
    pygame.draw.rect(tela, laranja_claro, botao2.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, botao3)
    pygame.draw.rect(tela, laranja_escuro, botao3, 5)
    pygame.draw.rect(tela, laranja_claro, botao3.inflate(-10, -10))

    # Desenha Imagem
    tela.blit(cara, (650, 20))

    # Escreve Titulo
    tela.blit(imagem_texto_titulo, (60, 20))

    # Escreve Retangulos
    tela.blit(imagem_texto_opcao1, (300, 200))
    tela.blit(imagem_texto_opcao2, (210, 320))
    tela.blit(imagem_texto_opcao3, (250, 440))




    # Atualiza a tela
    pygame.display.update()


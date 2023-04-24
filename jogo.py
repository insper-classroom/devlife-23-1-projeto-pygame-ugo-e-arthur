import pygame, funcoes

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

# Define fontes
titulo = pygame.font.Font('Chendolle.otf', 100)
imagem_texto_titulo = titulo.render('Show do Miranda', True, (0, 0, 0))
opcao1 = pygame.font.Font('Chendolle.otf', 40)
imagem_texto_opcao1 = titulo.render('Jogar', True, (0, 0, 0))
opcao2 = pygame.font.Font('Chendolle.otf', 40)
imagem_texto_opcao2 = titulo.render('Instruções', True, (0, 0, 0))
opcao3 = pygame.font.Font('Chendolle.otf', 40)
imagem_texto_opcao3 = titulo.render('Créditos', True, (0, 0, 0))

# Define Imagens - Miranda
cara = pygame.image.load('Miranda_Fabio.png')
cara = pygame.transform.scale(cara, (150, 150))
olhos = pygame.image.load('Miranda_Fabio_2 (1).png')
olhos = pygame.transform.scale(olhos, (150, 150))
intervalos_animacao_miranda = 1000
imagem_atual = 1 # variavel para controlar qual imagem sera exibida na animacao

# Define os retângulos de seleção
botao_largura = 400
botao_altura = 100
botao_x = (largura_tela - botao_largura) / 2
jogar_y = 200
instrucoes_y = jogar_y + botao_altura + 20
creditos_y = instrucoes_y + botao_altura + 20
jogar = pygame.Rect(botao_x, jogar_y, botao_largura, botao_altura)
instrucoes = pygame.Rect(botao_x, instrucoes_y, botao_largura, botao_altura)
creditos = pygame.Rect(botao_x, creditos_y, botao_largura, botao_altura)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Verifica se o mouse foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # Posição do mouse ao clicar
            # Verifica se o mouse clicou em um dos botões
            if jogar.collidepoint(mouse_pos):
                print("Botão Jogar clicado")
            elif instrucoes.collidepoint(mouse_pos):
                print("Botão Instruções clicado")
                funcoes.tela_instrucoes(tela)
            elif creditos.collidepoint(mouse_pos):
                print("Botão Créditos clicado")
                funcoes.tela_creditos(tela)

    # Preenche a tela com branco
    tela.fill(branco)

    # Desenha os retângulos de seleção com contorno laranja escuro
    pygame.draw.rect(tela, laranja, jogar)
    pygame.draw.rect(tela, laranja_escuro, jogar, 5)
    pygame.draw.rect(tela, laranja_claro, jogar.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, instrucoes)
    pygame.draw.rect(tela, laranja_escuro, instrucoes, 5)
    pygame.draw.rect(tela, laranja_claro, instrucoes.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, creditos)
    pygame.draw.rect(tela, laranja_escuro, creditos, 5)
    pygame.draw.rect(tela, laranja_claro, creditos.inflate(-10, -10))

    # Desenha animacao do miranda
    if imagem_atual == 1:
        tela.blit(cara, (660, 8))
        imagem_atual = 2
    else:
        tela.blit(olhos, (660, 8))
        imagem_atual = 1

    # Escreve Titulo
    tela.blit(imagem_texto_titulo, (80, 20))

    # Escreve Retangulos
    tela.blit(imagem_texto_opcao1, (300, 200))
    tela.blit(imagem_texto_opcao2, (210, 320))
    tela.blit(imagem_texto_opcao3, (250, 440))

    # Atualiza a tela
    pygame.display.update()

    # Aguarda um tempo para atualizar a animação
    pygame.time.wait(intervalos_animacao_miranda)



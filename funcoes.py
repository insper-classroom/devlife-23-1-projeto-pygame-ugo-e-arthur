import pygame

def tela_instrucoes(tela):
    # Define cores, fontes e imagens
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 30)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))

    # Define o retângulo do botão de voltar
    voltar = pygame.Rect(20, 530, 150, 60)
    
    # Loop da tela de instruções
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    return  # Encerra a função e volta para a tela inicial
        
        # Desenha a tela de instruções
        tela.fill(branco)
        titulo = fonte_titulo.render('Instruções', True, preto)
        texto1 = fonte_texto.render('Bem-vindos ao Show do Miranda!!!', True, preto)
        texto2 = fonte_texto.render('Você deve responder corretamente as perguntas para ganhar o prêmio', True, preto)
        texto3 = fonte_texto.render('Cada pergunta possui 4 alternativas, apenas uma delas esta correta', True, preto)
        texto4 = fonte_texto.render('Use o mouse para selecionar a alternativa que você acha correta', True, preto)
        texto5 = fonte_texto.render('Clique no botão "Jogar" para começar o jogo', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto1, (230, 150))
        tela.blit(texto2, (25, 200))
        tela.blit(texto3, (30, 250))
        tela.blit(texto4, (50, 300))
        tela.blit(texto5, (160, 350))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()


def tela_creditos(tela):
    # Define cores, fontes e imagens
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 30)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))

    # Define o retângulo do botão de voltar
    voltar = pygame.Rect(20, 530, 150, 60)
    
    # Loop da tela de instruções
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    return  # Encerra a função e volta para a tela inicial
        
        # Desenha a tela de instruções
        tela.fill(branco)
        titulo = fonte_titulo.render('Creditos', True, preto)
        texto1 = fonte_texto.render('Arthur Meschede', True, preto)
        texto2 = fonte_texto.render('Ugo Mello De Alcantara', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto1, (230, 150))
        tela.blit(texto2, (230, 200))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()

 



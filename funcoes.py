import pygame

# desenha a tela de instrucoes
def tela_instrucoes(tela):
# -----------cores--------------------------------------
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
# -----------cores--------------------------------------
# -----------fonte--------------------------------------
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 30)
# -----------fonte--------------------------------------
# -----------imagem--------------------------------------
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
# -----------imagem--------------------------------------

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

# desenha a tela de creditos
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
            mouse_pos = pygame.mouse.get_pos()
            if voltar.collidepoint(mouse_pos):
                voltar = pygame.Rect(10, 520, 170, 80)
            else:
                voltar = pygame.Rect(20, 530, 150, 60)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    return  # Encerra a função e volta para a tela inicial
        
        # Desenha a tela de instruções
        tela.fill(branco)
        titulo = fonte_titulo.render('Desenvolvedores', True, preto)
        texto1 = fonte_texto.render('Arthur Meschede', True, preto)
        texto2 = fonte_texto.render('Ugo Mello De Alcantara', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto1, (230, 150))
        tela.blit(texto2, (230, 200))
       # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (75, 545))

        
        # Atualiza a tela
        pygame.display.update()

def desenha_interface_fases(tela):
    branco = (255, 255, 255)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    roxo = (147, 112, 219)
    preto = (0, 0, 0)
    alternativa_A = pygame.Rect(60, 250, 310, 80)
    alternativa_B = pygame.Rect(430, 250, 310, 80)
    alternativa_C = pygame.Rect(60, 390, 310, 80)
    alternativa_D = pygame.Rect(430, 390, 310, 80)
    retangulo = pygame.Rect(700, -10, 1000, 70)
    coin = pygame.image.load('MCoin.png')
    coin = pygame.transform.scale(coin, (60, 60))
    fonte = pygame.font.Font('Chendolle.otf', 40)
    xzinho = fonte.render('x', True, preto)
    tela.fill(branco)
    pygame.draw.rect(tela, laranja, alternativa_A)
    pygame.draw.rect(tela, laranja_escuro, alternativa_A, 5)
    pygame.draw.rect(tela, laranja_claro, alternativa_A.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, alternativa_B)
    pygame.draw.rect(tela, laranja_escuro, alternativa_B, 5)
    pygame.draw.rect(tela, laranja_claro, alternativa_B.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, alternativa_C)
    pygame.draw.rect(tela, laranja_escuro, alternativa_C, 5)
    pygame.draw.rect(tela, laranja_claro, alternativa_C.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, alternativa_D)
    pygame.draw.rect(tela, laranja_escuro, alternativa_D, 5)
    pygame.draw.rect(tela, laranja_claro, alternativa_D.inflate(-10, -10))
    pygame.draw.rect(tela, laranja, retangulo)
    pygame.draw.rect(tela, laranja_escuro, retangulo, 5)
    pygame.draw.rect(tela, laranja_claro, retangulo.inflate(-10, -10))
    pygame.draw.circle(tela, roxo, (50, 50), 40)
    pygame.draw.circle(tela, laranja_escuro, (50, 50), 42, 5)
    tela.blit(coin, (752, 8))
    tela.blit(xzinho,(745, 22))


def desenha_quantidade_moedas_0(tela):
    fonte = pygame.font.Font('Chendolle.otf', (60))
    moeda = fonte.render('0', True, (0, 0, 0))
    tela.blit(moeda, (708, 5))

def desenha_quantidade_moedas_1(tela):
    fonte = pygame.font.Font('Chendolle.otf', (60))
    moeda = fonte.render('1', True, (0, 0, 0))
    tela.blit(moeda, (718, 4))

def desenha_quantidade_moedas_2(tela):
    fonte = pygame.font.Font('Chendolle.otf', (60))
    moeda = fonte.render('2', True, (0, 0, 0))
    tela.blit(moeda, (710, 0))

def derrota_0(tela):
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 30)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    voltar = pygame.Rect(20, 530, 150, 60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    return
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Perdeu!!!!', True, preto)

        texto5 = fonte_texto.render('Tome seu premio: 0', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto5, (160, 350))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()


def derrota_1(tela):
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 30)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    voltar = pygame.Rect(20, 530, 150, 60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    return
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Perdeu!!!!', True, preto)

        texto5 = fonte_texto.render('Tome seu premio: 1', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto5, (160, 350))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()

def derrota_2(tela):
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    laranja = (230, 115, 0)
    laranja_escuro = (200, 100, 0)
    laranja_claro = (255, 140, 0)
    fonte_titulo = pygame.font.Font('Chendolle.otf', 90)
    fonte_texto = pygame.font.Font('Chendolle.otf', 30)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    voltar = pygame.Rect(20, 530, 150, 60)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if voltar.collidepoint(mouse_pos):
                    return
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Perdeu!!!!', True, preto)

        texto5 = fonte_texto.render('Tome seu premio: 2', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto5, (160, 350))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()


 



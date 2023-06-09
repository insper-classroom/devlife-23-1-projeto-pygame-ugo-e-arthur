import pygame, Main_Menu,pygame.mixer

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
    toshi = pygame.image.load('Andrew-Kurauchi-2 (1).png')
    toshi = pygame.transform.scale(toshi, (150, 150))
    toshi_descolado = pygame.image.load('toshi_cool.png')
    toshi_descolado = pygame.transform.scale(toshi_descolado, (150, 150))
    intervalos_animacao_toshi = 1000
    imagem_atual = 1  # variavel para controlar qual imagem sera exibida na animacao
    # -----------imagem--------------------------------------

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

        tela.fill(branco)
        titulo = fonte_titulo.render('Instruções', True, preto)
        texto1 = fonte_texto.render('Bem-vindos ao Show do Miranda!!!', True, preto)
        texto2 = fonte_texto.render('Você deve responder corretamente as perguntas para ganhar o prêmio', True, preto)
        texto3 = fonte_texto.render('Nosso jogo possui 15 perguntas! Com foco no cotidiano da Turma', True, preto)
        texto4 = fonte_texto.render('A cada 5 perguntas acertadas, o jogador ganha 1 Miranca Coin', True, preto)
        texto5 = fonte_texto.render('Clique no botão "Jogar" para começar o jogo', True, preto)
        texto6 = fonte_texto.render('Boa sorte!!!', True, preto)
        tela.blit(titulo, (230, 20))
        tela.blit(texto1, (230, 150))
        tela.blit(texto2, (25, 200))
        tela.blit(texto3, (45, 250))
        tela.blit(texto4, (60, 300))
        tela.blit(texto5, (160, 350))
        tela.blit(texto6, (450, 500))
        tela.blit(toshi, (610, 410))
        
        # Desenha a animação do personagem Toshi
        if imagem_atual == 1:
            tela.blit(toshi, (610, 410))
            imagem_atual = 2
        else:
            tela.blit(toshi_descolado, (610, 410))
            imagem_atual = 1
        
        # Interface Retângulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        # Atualiza a tela
        pygame.display.update()

        pygame.time.wait(intervalos_animacao_toshi)



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

        tela.blit(titulo, (155, 20))
        tela.blit(texto1, (310, 150))
        tela.blit(texto2, (280, 200))
       # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
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

    a_cor = laranja_claro
    if alternativa_A.collidepoint(pygame.mouse.get_pos()):
        a_cor = (0, 255, 0)

    b_cor = laranja_claro
    if alternativa_B.collidepoint(pygame.mouse.get_pos()):
        b_cor = (0, 255, 0)

    c_cor = laranja_claro
    if alternativa_C.collidepoint(pygame.mouse.get_pos()):
        c_cor = (0, 255, 0)

    d_cor = laranja_claro
    if alternativa_D.collidepoint(pygame.mouse.get_pos()):
        d_cor = (0, 255, 0)



    pygame.draw.rect(tela, laranja, alternativa_A)
    pygame.draw.rect(tela, laranja_escuro, alternativa_A, 5)
    pygame.draw.rect(tela, a_cor, alternativa_A.inflate(-10, -10))


    pygame.draw.rect(tela, laranja, alternativa_B)
    pygame.draw.rect(tela, laranja_escuro, alternativa_B, 5)
    pygame.draw.rect(tela, b_cor, alternativa_B.inflate(-10, -10))

    pygame.draw.rect(tela, laranja, alternativa_C)
    pygame.draw.rect(tela, laranja_escuro, alternativa_C, 5)
    pygame.draw.rect(tela, c_cor, alternativa_C.inflate(-10, -10))

    pygame.draw.rect(tela, laranja, alternativa_D)
    pygame.draw.rect(tela, laranja_escuro, alternativa_D, 5)
    pygame.draw.rect(tela, d_cor, alternativa_D.inflate(-10, -10))

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
    fonte_texto = pygame.font.Font('Chendolle.otf', 100)
    fonte_quantidade = pygame.font.Font('Chendolle.otf', 150)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    coin = pygame.image.load('MCoin.png')
    coin = pygame.transform.scale(coin, (200, 200))
    voltar = pygame.Rect(20, 530, 150, 60)
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
                    Main_Menu.jogo()
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Perdeu!!!!', True, preto)
        premio = fonte_texto.render('Tome seu premio:', True, preto)
        quantidade = fonte_quantidade.render('0x', True, preto)
        tela.blit(titulo, (170, 20))
        tela.blit(premio, (100, 150))
        tela.blit(quantidade, (300, 280))
        tela.blit(coin, (415, 255))
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
    fonte_texto = pygame.font.Font('Chendolle.otf', 100)
    fonte_quantidade = pygame.font.Font('Chendolle.otf', 150)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    coin = pygame.image.load('MCoin.png')
    coin = pygame.transform.scale(coin, (200, 200))
    voltar = pygame.Rect(20, 530, 150, 60)
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
                    Main_Menu.jogo()
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Perdeu!!!!', True, preto)
        premio = fonte_texto.render('Tome seu premio:', True, preto)
        quantidade = fonte_quantidade.render('1x', True, preto)
        tela.blit(titulo, (170, 20))
        tela.blit(premio, (100, 150))
        tela.blit(quantidade, (300, 280))
        tela.blit(coin, (390, 255))
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
    fonte_texto = pygame.font.Font('Chendolle.otf', 100)
    fonte_quantidade = pygame.font.Font('Chendolle.otf', 150)
    seta = pygame.image.load('seta-esquerda.png')
    seta = pygame.transform.scale(seta, (50, 50))
    coin = pygame.image.load('MCoin.png')
    coin = pygame.transform.scale(coin, (200, 200))
    voltar = pygame.Rect(20, 530, 150, 60)
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
                    Main_Menu.jogo()
        tela.fill(branco)
        titulo = fonte_titulo.render('Voce Perdeu!!!!', True, preto)
        premio = fonte_texto.render('Tome seu premio:', True, preto)
        quantidade = fonte_quantidade.render('2x', True, preto)
        tela.blit(titulo, (170, 20))
        tela.blit(premio, (100, 150))
        tela.blit(quantidade, (300, 280))
        tela.blit(coin, (395, 270))
        # interface Retangulo
        pygame.draw.rect(tela, laranja, voltar)
        pygame.draw.rect(tela, laranja_escuro, voltar, 5)
        pygame.draw.rect(tela, laranja_claro, voltar.inflate(-10, -10))
        tela.blit(seta, (65, 535))

        
        # Atualiza a tela
        pygame.display.update()